// Accent-insensitive, typo-tolerant search over the sign list.
// Pure module (no DOM), so it runs in the browser and in tests/search.test.js.

const MARKS = /\p{M}/gu;
const NON_ALNUM = /[^a-z0-9]+/g;
const collator = new Intl.Collator('pt-BR', { sensitivity: 'base' });

// "Água-Viva!" -> "agua viva"
export function normalize(text) {
  return String(text ?? '')
    .normalize('NFD')
    .replace(MARKS, '')
    .toLowerCase()
    .replace(NON_ALNUM, ' ')
    .trim();
}

// Optimal string alignment distance (Damerau-Levenshtein with adjacent swaps),
// so "agau" -> "agua" costs 1. Stops early once every path exceeds `max`.
export function editDistance(a, b, max = Infinity) {
  if (a === b) return 0;
  if (Math.abs(a.length - b.length) > max) return max + 1;
  let prev2 = null;
  let prev = Array.from({ length: b.length + 1 }, (_, j) => j);
  for (let i = 1; i <= a.length; i++) {
    const cur = [i];
    let rowMin = i;
    for (let j = 1; j <= b.length; j++) {
      const cost = a[i - 1] === b[j - 1] ? 0 : 1;
      let d = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + cost);
      if (prev2 && i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) {
        d = Math.min(d, prev2[j - 2] + 1);
      }
      cur.push(d);
      if (d < rowMin) rowMin = d;
    }
    if (rowMin > max) return max + 1;
    prev2 = prev;
    prev = cur;
  }
  return prev[b.length];
}

// How many typos we forgive for a query of this length.
function typoBudget(length) {
  if (length < 3) return 0;
  if (length < 6) return 1;
  return 2;
}

// Scores one normalized term against a normalized query. Higher is better; null = no match.
function scoreTerm(term, query) {
  if (term === query) return { score: 100, kind: 'exact' };
  if (term.startsWith(query)) return { score: 90 - Math.min(term.length - query.length, 9), kind: 'prefix' };

  const words = term.split(' ');
  const queryWords = query.split(' ');
  if (words.some(w => w.startsWith(query))) return { score: 75, kind: 'word' };
  // "dia bom" or "bom d" still finds "bom dia": every typed word starts some word of the term.
  if (queryWords.length > 1 && queryWords.every(q => words.some(w => w.startsWith(q)))) {
    return { score: 70, kind: 'words' };
  }
  if (query.length >= 3 && term.includes(query)) return { score: 55, kind: 'contains' };

  const budget = typoBudget(query.length);
  if (!budget) return null;
  // Whole-term typo ("famlia", "obirgado").
  const whole = editDistance(query, term, budget);
  if (whole <= budget) return { score: 45 - whole * 5, kind: 'typo' };
  // Typo while still typing ("famli", "fmil" -> "familia"): compare with the start of the
  // term, allowing for a dropped or an extra letter.
  const lengths = [];
  for (let d = -budget; d <= budget; d++) if (query.length + d > 0) lengths.push(query.length + d);
  const candidates = [term, ...words].flatMap(t => lengths.map(n => t.slice(0, n)));
  const partial = Math.min(...candidates.map(t => editDistance(query, t, budget)));
  if (partial <= budget && query.length >= 4) return { score: 35 - partial * 5, kind: 'typo' };
  return null;
}

// Builds the searchable index once. Each sign is found by its word and every alias.
export function buildIndex(signs) {
  return signs.map(sign => ({
    sign,
    terms: [sign.word, ...(sign.aliases ?? [])].map((text, i) => ({
      text,
      norm: normalize(text),
      primary: i === 0,
    })),
  }));
}

// Returns [{ sign, term, kind, score }] best first. `term` is the word or alias that matched.
export function search(index, query, limit = 50) {
  const q = normalize(query);
  if (!q) return [];
  const results = [];
  for (const entry of index) {
    let best = null;
    let primary = null;
    for (const term of entry.terms) {
      const match = scoreTerm(term.norm, q);
      if (!match) continue;
      const score = match.score + (term.primary ? 2 : 0);
      const hit = { sign: entry.sign, term, kind: match.kind, score };
      if (term.primary) primary = hit;
      if (!best || score > best.score) best = hit;
    }
    // When the headword matches the same way as the winning alias, show the headword
    // ("o" -> obrigado, not "obg").
    if (best && primary && primary.kind === best.kind) best = { ...primary, score: best.score };
    if (best) results.push(best);
  }
  results.sort((a, b) => b.score - a.score || collator.compare(a.sign.word, b.sign.word));
  return results.slice(0, limit);
}

// Where the query appears inside `text`, in original-string indexes: [start, end] or null.
// Lets the UI bold "Ág" in "Água" when the user typed "ag".
export function highlightRange(text, query) {
  const q = normalize(query);
  if (!q) return null;
  let folded = '';
  const origin = [];
  let i = 0;
  for (const ch of text) {
    const f = ch.normalize('NFD').replace(MARKS, '').toLowerCase().replace(/[^a-z0-9]/g, ' ');
    for (const c of f) {
      folded += c;
      origin.push(i);
    }
    i += ch.length;
  }
  origin.push(text.length);
  // Prefer a match at the start of a word over one in the middle.
  let at = folded.startsWith(q) ? 0 : -1;
  if (at < 0) {
    const wordStart = folded.indexOf(' ' + q);
    if (wordStart >= 0) at = wordStart + 1;
  }
  if (at < 0) at = folded.indexOf(q);
  if (at < 0) return null;
  return [origin[at], origin[at + q.length]];
}

export function sortSigns(signs) {
  return [...signs].sort((a, b) => collator.compare(a.word, b.word));
}
