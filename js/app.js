// UI. Typing shows the best match right away, big, with no extra tap (built for interpreters
// who need a sign in the moment). The hash (#/sinal/<id>) holds a sign the user picked.
import { buildIndex, search, highlightRange, normalize, sortSigns } from './search.js';

const ICONS = {
  hand: '<path d="M7 12V5.5a1.5 1.5 0 0 1 3 0V11M10 10.5V4a1.5 1.5 0 0 1 3 0v6.5M13 10.5V5a1.5 1.5 0 0 1 3 0v6M16 11V8a1.5 1.5 0 0 1 3 0v5.5a7.5 7.5 0 0 1-7.5 7.5h-.7a6 6 0 0 1-4.7-2.3L3.6 15.4a1.6 1.6 0 0 1 2.5-2L7 14.5"/>',
  pin: '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.6"/>',
  move: '<path d="M12 3v18M3 12h18M9 6l3-3 3 3M9 18l3 3 3-3M6 9l-3 3 3 3M18 9l3 3-3 3"/>',
  palm: '<path d="M12 3v4M12 17v4M3 12h4M17 12h4"/><circle cx="12" cy="12" r="4"/>',
  face: '<circle cx="12" cy="12" r="9"/><path d="M8.5 14.5a4.5 4.5 0 0 0 7 0M9 9.5h.01M15 9.5h.01"/>',
  info: '<circle cx="12" cy="12" r="9"/><path d="M12 16v-5M12 8h.01"/>',
  alert: '<path d="M12 3 2 20h20z"/><path d="M12 10v4M12 17h.01"/>',
  search: '<circle cx="11" cy="11" r="7"/><path d="M16.5 16.5 21 21"/>',
  clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
  grid: '<rect x="4" y="4" width="7" height="7" rx="1.5"/><rect x="13" y="4" width="7" height="7" rx="1.5"/><rect x="4" y="13" width="7" height="7" rx="1.5"/><rect x="13" y="13" width="7" height="7" rx="1.5"/>',
  play: '<path d="M8 5.5v13l10.5-6.5z"/>',
  // Category icons
  chat: '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1.1-4.6A8 8 0 1 1 21 12z"/>',
  people: '<circle cx="9" cy="8" r="3"/><path d="M3.5 20a5.5 5.5 0 0 1 11 0"/><circle cx="17" cy="9.5" r="2.4"/><path d="M15.6 14.4A4.6 4.6 0 0 1 21 19"/>',
  cup: '<path d="M5 9h12v4a6 6 0 0 1-12 0z"/><path d="M17 10h1.5a2.5 2.5 0 0 1 0 5H17M8 3v3M11 3v3M14 3v3"/>',
  person: '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
  tag: '<path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8.5" r="1.5"/>',
};

// Sign parameters, in the order interpreters read them.
const PARAMS = [
  ['handshape', 'Mão', 'hand'],
  ['location', 'Local', 'pin'],
  ['movement', 'Movimento', 'move'],
  ['orientation', 'Palma', 'palm'],
  ['expression', 'Expressão', 'face'],
];
const RECENT_KEY = 'sinais.recentes';
const RECENT_MAX = 8;
const ALTS_MAX = 8;
const DEFAULT_TITLE = 'Sinais · Dicionário de Libras';
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

const $ = (sel, root = document) => root.querySelector(sel);
const esc = s => String(s ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const icon = (name, cls = '') => `<svg class="icon ${cls}" viewBox="0 0 24 24" aria-hidden="true">${ICONS[name] ?? ICONS.tag}</svg>`;
const plural = (n, one, many) => `${n} ${n === 1 ? one : many}`;
const signHref = sign => `#/sinal/${encodeURIComponent(sign.id)}`;

const state = {
  data: null,
  index: [],
  sorted: [],
  byId: new Map(),
  categories: new Map(),
  results: [],        // current search results
  featured: null,     // sign shown big
  shownMedia: null,   // id of the sign whose drawing is in the page (so typing doesn't restart it)
  playMotion: false,  // reduced-motion users asked to see the movement
  recentTimer: 0,
};

const els = {
  q: $('#q'),
  clear: $('#clear'),
  status: $('#status'),
  announce: $('#announce'),
  alts: $('#alts'),
  feature: $('#feature'),
  results: $('#results'),
  foot: $('#foot-note'),
  searchbox: $('.searchbox'),
};

// ---------- Storage (per device; the app works without it) ----------

function readRecent() {
  try {
    const ids = JSON.parse(localStorage.getItem(RECENT_KEY) ?? '[]');
    return Array.isArray(ids) ? ids.filter(id => state.byId.has(id)) : [];
  } catch {
    return [];
  }
}

function remember(sign) {
  if (!sign) return;
  const ids = [sign.id, ...readRecent().filter(id => id !== sign.id)].slice(0, RECENT_MAX);
  try { localStorage.setItem(RECENT_KEY, JSON.stringify(ids)); } catch { /* private mode: skip */ }
}

// ---------- Data ----------

async function load() {
  let data;
  try {
    const res = await fetch('data/sinais.json');
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    data = await res.json();
  } catch (err) {
    console.error(err);
    els.results.setAttribute('aria-busy', 'false');
    els.results.innerHTML = `
      <div class="empty">
        <div class="empty-art">${icon('info')}</div>
        <h2>Não deu para carregar os sinais</h2>
        <p>Confira a conexão e tente de novo.</p>
        <button class="btn" type="button" onclick="location.reload()">Tentar de novo</button>
      </div>`;
    return;
  }
  state.data = data;
  state.index = buildIndex(data.signs);
  state.sorted = sortSigns(data.signs);
  state.byId = new Map(data.signs.map(s => [s.id, s]));
  state.categories = new Map(data.categories.map(c => [c.id, c]));
  els.foot.innerHTML = footerHtml(data);
  const picked = pickedFromHash();
  if (picked) remember(picked);
  render();
  if (matchMedia('(hover: hover)').matches) els.q.focus();
}

function footerHtml(data) {
  const ref = data.reference;
  return `${esc(data.title ?? 'Demo')} · ${plural(data.signs.length, 'sinal', 'sinais')} · Desenhos próprios`
    + (ref ? `, com base no <a href="${esc(ref.url)}" target="_blank" rel="noopener">${esc(ref.name)}</a>` : '');
}

const categoryOf = sign => state.categories.get(sign.category) ?? { id: 'outros', name: 'Outros', icon: 'tag', color: 'outros' };
const catStyle = sign => `--cat: var(--cat-${esc(categoryOf(sign).color ?? sign.category)})`;

// ---------- Rendering ----------

function render() {
  if (!state.data) return;
  const query = els.q.value;
  const hasQuery = normalize(query).length > 0;
  els.clear.hidden = !query;
  els.searchbox.classList.toggle('has-text', Boolean(query));

  state.results = hasQuery ? search(state.index, query) : [];
  const picked = pickedFromHash();
  // The picked sign wins while it is still a match; otherwise the best match is shown.
  state.featured = hasQuery
    ? state.results.find(r => r.sign === picked)?.sign ?? state.results[0]?.sign ?? null
    : picked;

  renderStatus(query, hasQuery);
  const alts = altsHtml(query);
  els.alts.innerHTML = alts;
  els.alts.hidden = !alts;
  renderFeature(query);
  els.results.setAttribute('aria-busy', 'false');
  els.results.innerHTML = hasQuery ? (state.results.length ? '' : emptyHtml(query)) : browseHtml();
  document.title = state.featured ? `${state.featured.word} em Libras · Sinais` : DEFAULT_TITLE;

  clearTimeout(state.recentTimer);
  if (hasQuery && state.featured) {
    // Count a sign as "looked up" once the user stops typing on it for a moment.
    const sign = state.featured;
    state.recentTimer = setTimeout(() => remember(sign), 2500);
  }
}

function renderStatus(query, hasQuery) {
  els.status.classList.remove('is-fuzzy');
  if (!hasQuery) {
    els.status.textContent = '';
    return;
  }
  const q = `“<strong>${esc(query.trim())}</strong>”`;
  const n = state.results.length;
  if (!n) {
    els.status.innerHTML = `Nenhum sinal para ${q}`;
  } else if (state.results.every(r => r.kind === 'typo')) {
    // Only near-misses: say clearly that this is not the word typed ("doce" is not "você").
    els.status.classList.add('is-fuzzy');
    els.status.innerHTML = `${icon('alert')}<span>Nenhum sinal para ${q}. ${n === 1 ? 'O mais parecido:' : 'Os mais parecidos:'}</span>`;
  } else {
    els.status.innerHTML = `${plural(n, 'sinal', 'sinais')} para ${q}`;
  }
}

function highlighted(text, query) {
  const range = query ? highlightRange(text, query) : null;
  if (!range) return esc(text);
  const [a, b] = range;
  return `${esc(text.slice(0, a))}<mark>${esc(text.slice(a, b))}</mark>${esc(text.slice(b))}`;
}

// Aliases worth showing: skip the ones that only drop accents ("agua" for "água").
function visibleAliases(sign) {
  const base = normalize(sign.word);
  return (sign.aliases ?? []).filter(a => normalize(a) !== base);
}

// Other matches sit above the drawing, so variants are one tap away on a phone.
function altsHtml(query) {
  if (state.results.length < 2) return '';
  const shown = state.results.slice(0, ALTS_MAX);
  const more = state.results.length - shown.length;
  return `<ul class="alts">
    ${shown.map(r => `
      <li><a class="alt" href="${signHref(r.sign)}" style="${catStyle(r.sign)}"
        ${r.sign === state.featured ? 'aria-current="true"' : ''}>
        <img src="${esc(r.sign.poster ?? r.sign.image)}" alt="" loading="lazy">${highlighted(r.sign.word, query)}</a></li>`).join('')}
  </ul>
  ${more > 0 ? `<p class="alt-more">+${more}: digite mais letras</p>` : ''}`;
}

function renderFeature(query) {
  const sign = state.featured;
  if (!sign) {
    els.feature.innerHTML = '';
    state.shownMedia = null;
    return;
  }
  const article = $('.sign', els.feature);
  if (article && state.shownMedia === sign.id) {
    // Same sign while typing: refresh the text only, so the animation keeps playing.
    $('.sign-info', article).innerHTML = featureInfoHtml(sign, query);
    return;
  }
  state.shownMedia = sign.id;
  state.playMotion = false;
  els.feature.innerHTML = `
    <article class="sign" style="${catStyle(sign)}">
      <div class="sign-media" tabindex="-1">${featureMediaHtml(sign)}</div>
      <div class="sign-info">${featureInfoHtml(sign, query)}</div>
    </article>`;
}

function featureMediaHtml(sign) {
  const still = reducedMotion.matches && !state.playMotion && sign.poster;
  return `
    <img src="${esc(still ? sign.poster : sign.image)}" decoding="async"
      alt="${still ? 'Ilustração' : 'Ilustração animada'} do sinal de ${esc(sign.word)} em Libras. ${esc(sign.how)}">
    ${still ? `<button class="play" type="button" data-action="play">${icon('play')}Ver movimento</button>` : ''}`;
}

function featureInfoHtml(sign, query) {
  const cat = categoryOf(sign);
  const match = state.results.find(r => r.sign === sign);
  const viaAlias = match && !match.term.primary && normalize(match.term.text) !== normalize(sign.word);
  const aliases = visibleAliases(sign);
  const params = PARAMS.filter(([key]) => sign.params?.[key]);
  return `
    <div class="sign-head">
      <h2 class="sign-word" tabindex="-1">${esc(sign.word)}</h2>
      <span class="cat-pill">${icon(cat.icon)}${esc(cat.name)}</span>
    </div>
    ${viaAlias ? `<p class="sign-alias">Você buscou <b>${highlighted(match.term.text, query)}</b></p>`
      : aliases.length ? `<p class="sign-alias">Também: ${aliases.map(esc).join(', ')}</p>` : ''}
    <p class="sign-how">${esc(sign.how)}</p>
    ${params.length ? `
    <dl class="params">
      ${params.map(([key, label, ic]) => `
        <div class="param"><dt>${icon(ic)}${esc(label)}</dt><dd>${esc(sign.params[key])}</dd></div>`).join('')}
    </dl>` : ''}
    ${sign.regionalNote ? `<p class="sign-note">${icon('info')}<span><b>Variação regional.</b> ${esc(sign.regionalNote)}</span></p>` : ''}`;
}

function cardHtml(sign, active) {
  const cat = categoryOf(sign);
  return `
    <a class="card${active ? ' is-active' : ''}" href="${signHref(sign)}" style="${catStyle(sign)}"
      ${active ? 'aria-current="true"' : ''}>
      <div class="card-media"><img src="${esc(sign.poster ?? sign.image)}" alt="" loading="lazy" decoding="async"></div>
      <div class="card-body">
        <h3 class="card-word">${esc(sign.word)}</h3>
        <span class="card-cat">${icon(cat.icon)}${esc(cat.name)}</span>
      </div>
    </a>`;
}

function emptyHtml(query) {
  return `
    <div class="empty">
      <div class="empty-art">${icon('search')}</div>
      <h2>Ainda não temos “${esc(query.trim())}”</h2>
      <p>Este demo tem só ${plural(state.data.signs.length, 'sinal', 'sinais')}. Confira a palavra ou veja todos.</p>
      <button class="btn" type="button" data-action="show-all">${icon('grid')}Ver todos os sinais</button>
    </div>`;
}

function browseHtml() {
  const recent = readRecent().map(id => state.byId.get(id));
  return `
    ${recent.length ? `
    <h2 class="section-title">${icon('clock')}Recentes</h2>
    <div class="recent">
      ${recent.map(s => `<a class="recent-chip" href="${signHref(s)}" style="${catStyle(s)}">
        <img src="${esc(s.poster ?? s.image)}" alt="" loading="lazy">${esc(s.word)}</a>`).join('')}
    </div>` : ''}
    <h2 class="section-title">${icon('grid')}Todos os sinais <span class="count">${state.sorted.length}</span></h2>
    <div class="grid">${state.sorted.map(s => cardHtml(s, s === state.featured)).join('')}</div>`;
}

// ---------- Selection (hash) ----------

function pickedFromHash() {
  const m = location.hash.match(/^#\/sinal\/(.+)$/);
  if (!m) return null;
  try {
    return state.byId.get(decodeURIComponent(m[1])) ?? null;
  } catch {
    return null; // malformed link: ignore it
  }
}

function announce(text) {
  els.announce.textContent = '';
  // A fresh text node makes screen readers read it even when the text repeats.
  requestAnimationFrame(() => { els.announce.textContent = text; });
}

function onHashChange() {
  const picked = pickedFromHash();
  if (picked) remember(picked);
  // A link to a sign that the current search doesn't include: show the sign, drop the search.
  if (picked && normalize(els.q.value) && !search(state.index, els.q.value).some(r => r.sign === picked)) {
    els.q.value = '';
  }
  render();
  if (!picked) return;
  announce(`${picked.word} em Libras`);
  window.scrollTo({ top: 0, behavior: reducedMotion.matches ? 'auto' : 'smooth' });
  // Keep focus in the search box while the user is typing; otherwise move it to the sign.
  if (document.activeElement !== els.q) $('.sign-word', els.feature)?.focus({ preventScroll: true });
}

// Moves the featured sign within the current results (arrow keys).
function step(delta) {
  if (!state.results.length) return;
  const at = state.results.findIndex(r => r.sign === state.featured);
  const next = state.results[(at + delta + state.results.length) % state.results.length].sign;
  history.replaceState(null, '', signHref(next));
  render();
  announce(`${next.word}, ${at + delta < 0 ? state.results.length : ((at + delta) % state.results.length) + 1} de ${state.results.length}`);
}

function goHome() {
  els.q.value = '';
  if (location.hash && location.hash !== '#/') history.replaceState(null, '', '#/');
  render();
  window.scrollTo({ top: 0 });
}

// ---------- Events ----------

els.q.addEventListener('input', () => {
  // A new search starts from its best match, not from a sign picked earlier.
  if (pickedFromHash()) history.replaceState(null, '', '#/');
  render();
  window.scrollTo({ top: 0 });
});
els.q.addEventListener('keydown', e => {
  if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
    e.preventDefault();
    step(e.key === 'ArrowDown' ? 1 : -1);
  }
  if (e.key === 'Enter') {
    e.preventDefault();
    remember(state.featured);
    els.q.blur(); // closes the phone keyboard so the whole sign is visible
  }
  if (e.key === 'Escape' && els.q.value) goHome();
});
els.clear.addEventListener('click', () => {
  goHome();
  els.q.focus();
});
$('.brand').addEventListener('click', e => {
  e.preventDefault();
  goHome();
});
document.addEventListener('click', e => {
  const action = e.target.closest('[data-action]')?.dataset.action;
  if (action === 'show-all') goHome();
  if (action === 'play') {
    state.playMotion = true;
    const media = $('.sign-media', els.feature);
    media.innerHTML = featureMediaHtml(state.featured);
    media.focus({ preventScroll: true }); // the button is gone; keep focus on the drawing
  }
});
document.addEventListener('keydown', e => {
  if (e.key === '/' && document.activeElement !== els.q) {
    e.preventDefault();
    els.q.focus();
    els.q.select();
  }
});
window.addEventListener('hashchange', onHashChange);
reducedMotion.addEventListener?.('change', () => { state.shownMedia = null; render(); });

if ('serviceWorker' in navigator) {
  // Offline use: the service worker keeps the app, data and drawings on the device.
  // When a new version takes over, reload once so the page matches it.
  // When a new version takes over, reload so the page matches it, but never in the middle of
  // a lookup: right away if the search is idle, otherwise when the user leaves the page.
  const hadController = Boolean(navigator.serviceWorker.controller);
  navigator.serviceWorker.addEventListener('controllerchange', () => {
    if (!hadController) return;
    if (!els.q.value && document.activeElement !== els.q) location.reload();
    else document.addEventListener('visibilitychange', () => document.hidden && location.reload(), { once: true });
  });
  window.addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(err => console.warn('SW', err)));
}

load();
