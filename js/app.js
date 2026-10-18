// UI. Typing shows the best match right away, big, with no extra tap (built for interpreters
// who need a sign in the moment). The hash (#/sinal/<id>) holds a sign the user picked.
import { buildIndex, search, highlightRange, normalize, sortSigns } from './search.js';
import * as Frases from './frases.js';

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
  laptop: '<rect x="4" y="5" width="16" height="11" rx="1.5"/><path d="M2 19h20"/>',
  heart: '<path d="M12 20s-7.5-4.6-9.3-9.4A4.9 4.9 0 0 1 12 6.4a4.9 4.9 0 0 1 9.3 4.2C19.5 15.4 12 20 12 20z"/>',
  home: '<path d="M3 11l9-7 9 7M5 10v10h14V10M10 20v-6h4v6"/>',
  shirt: '<path d="M8 3 3 6l2 5 3-1v11h8V10l3 1 2-5-5-3a4 4 0 0 1-8 0z"/>',
  palette: '<path d="M12 3a9 9 0 1 0 0 18c1.5 0 2-1 2-2s-1-1.5-1-2.5 1-1.5 2-1.5h2a4 4 0 0 0 4-4c0-4.4-4-8-9-8z"/><circle cx="7.5" cy="11" r="1"/><circle cx="10" cy="7" r="1"/><circle cx="15" cy="7" r="1"/>',
  hash: '<path d="M5 9h14M5 15h14M10 4 8 20M16 4l-2 16"/>',
  leaf: '<path d="M5 19c0-9 6-14 15-14 0 9-5 15-14 15"/><path d="M5 19 13 11"/>',
  car: '<path d="M5 16V11l2-5h10l2 5v5M3 16h18v3H3zM7 19v1M17 19v1M5 11h14"/>',
  book: '<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2zM4 19V5"/>',
  smile: '<circle cx="12" cy="12" r="9"/><path d="M8.5 14.5a4.5 4.5 0 0 0 7 0M9 9.5h.01M15 9.5h.01"/>',
  run: '<circle cx="14" cy="4.5" r="2"/><path d="M6 21l4-6 3 2v5M8 11l3-4 4 3 3 1M11 7l-1 6"/>',
  close: '<path d="M6 6l12 12M18 6 6 18"/>',
  star: '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
  question: '<circle cx="12" cy="12" r="9"/><path d="M9.5 9.5a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .9-1 1.6V14M12 17h.01"/>',
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
const FAV_KEY = 'sinaliza.favoritos';
const ALTS_MAX = 8;
const DEFAULT_TITLE = 'Sinaliza · Dicionário de Libras';
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
  category: null,     // category filter (id), null = all
  wordClass: null,    // word-class filter (substantivo, verbo…), null = all
  pageView: null,     // which page (frases / montar) is currently in #page
  topic: null,        // open topic inside a category
  openCat: null,      // category whose accordion is open on the home screen
};

const els = {
  q: $('#q'),
  clear: $('#clear'),
  status: $('#status'),
  announce: $('#announce'),
  alts: $('#alts'),
  cats: $('#cats'),
  classes: $('#classes'),
  page: $('#page'),
  feature: $('#feature'),
  results: $('#results'),
  foot: $('#foot-note'),
  searchbox: $('.searchbox'),
};

// ---------- Storage (per device; the app works without it) ----------

// Favorites: signs the user saved to practise until they know them (newest first).
function readFavs() {
  try {
    const ids = JSON.parse(localStorage.getItem(FAV_KEY) ?? '[]');
    return Array.isArray(ids) ? ids.filter(id => state.byId.has(id)) : [];
  } catch {
    return [];
  }
}

const isFav = sign => readFavs().includes(sign.id);

function toggleFav(sign) {
  const ids = readFavs();
  const next = ids.includes(sign.id) ? ids.filter(id => id !== sign.id) : [sign.id, ...ids];
  try { localStorage.setItem(FAV_KEY, JSON.stringify(next)); } catch { /* private mode: skip */ }
  return next.includes(sign.id);
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
  buildCats();
  buildClasses();
  try {
    const frases = await (await fetch('data/frases.json')).json();
    Frases.setup({ esc, icon, thumb, signHref, signs: data.signs, classes: data.classes }, frases);
    state.frasesReady = true;
  } catch (err) {
    console.warn('frases', err);
  }
  render();
  if (matchMedia('(hover: hover)').matches) els.q.focus();
}

function footerHtml(data) {
  const refs = (data.references ?? []).map(r => `<a href="${esc(r.url)}" target="_blank" rel="noopener">${esc(r.name)}</a>`);
  return `${plural(data.signs.length, 'sinal', 'sinais')} · Desenhos e descrições próprios`
    + (refs.length ? `, com base em ${refs.join(' e ')}` : '');
}

const categoryOf = sign => state.categories.get(sign.category) ?? { id: 'outros', name: 'Outros', icon: 'tag', color: 'outros' };
const catVar = color => `var(--cat-${esc(color)}, var(--cat-outros))`;
const catStyle = sign => `--cat: ${catVar(categoryOf(sign).color ?? sign.category)}`;

// ---------- Rendering ----------

function viewFromHash() {
  if (location.hash.startsWith('#/frases')) return 'frases';
  if (location.hash.startsWith('#/montar')) return 'montar';
  if (location.hash.startsWith('#/favoritos')) return 'favoritos';
  return 'sinais';
}

function render() {
  if (!state.data) return;
  const query = els.q.value;
  const hasQuery = normalize(query).length > 0;
  els.clear.hidden = !query;
  els.searchbox.classList.toggle('has-text', Boolean(query));

  const view = hasQuery ? 'sinais' : viewFromHash();
  document.querySelectorAll('.tab').forEach(t => t.toggleAttribute('aria-current', t.dataset.view === view));
  if (view === 'favoritos') {
    for (const el of [els.cats, els.classes, els.alts, els.results]) el.hidden = true;
    els.status.textContent = '';
    els.feature.innerHTML = '';
    state.shownMedia = null;
    els.page.hidden = false;
    els.page.innerHTML = favsHtml();   // always rebuilt: the list changes as signs are saved
    state.pageView = view;
    document.title = 'Favoritos · Sinaliza';
    return;
  }
  if (view !== 'sinais' && state.frasesReady) {
    // Sentence pages replace the dictionary view.
    for (const el of [els.cats, els.classes, els.alts, els.results]) el.hidden = true;
    els.status.textContent = '';
    els.feature.innerHTML = '';
    state.shownMedia = null;
    els.page.hidden = false;
    if (state.pageView !== view) {
      els.page.innerHTML = view === 'frases' ? Frases.frasesHtml() : Frases.montarHtml();
      if (view === 'montar') Frases.wireMontar(els.page);
      state.pageView = view;
    }
    document.title = `${view === 'frases' ? 'Frases' : 'Monte uma frase'} · Sinaliza`;
    return;
  }
  els.page.hidden = true;
  state.pageView = null;
  els.results.hidden = false;

  // Search always covers every category; the chips only filter what is browsed.
  state.results = hasQuery ? search(state.index, query) : [];
  // With a big dictionary, near-misses ("cama" for "casa") only help when nothing real matches.
  if (state.results.some(r => r.kind !== 'typo')) state.results = state.results.filter(r => r.kind !== 'typo');
  const picked = pickedFromHash();
  // The picked sign wins while it is still a match; otherwise the best match is shown.
  state.featured = hasQuery
    ? state.results.find(r => r.sign === picked)?.sign ?? state.results[0]?.sign ?? null
    : picked;

  updateCats(hasQuery);
  updateClasses(hasQuery);
  renderStatus(query, hasQuery);
  const alts = altsHtml(query);
  els.alts.innerHTML = alts;
  els.alts.hidden = !alts;
  renderFeature(query);
  els.results.setAttribute('aria-busy', 'false');
  els.results.innerHTML = hasQuery ? (state.results.length ? '' : emptyHtml(query)) : browseHtml();
  document.title = state.featured ? `${state.featured.word} em Libras · Sinaliza` : DEFAULT_TITLE;
}

const inCategory = sign => !state.category || sign.category === state.category;

// The chips are built once (so a click keeps keyboard focus) and only updated afterwards.
function buildCats() {
  const counts = new Map();
  for (const s of state.data.signs) counts.set(s.category, (counts.get(s.category) ?? 0) + 1);
  const chip = (id, name, iconName, color, count) => `
    <button class="cat-chip" type="button" data-cat="${esc(id ?? '')}" data-name="${esc(name)}" data-count="${count}"
      aria-pressed="false" style="${color ? `--cat: ${catVar(color)}` : '--cat: var(--brand); --cat-ink: var(--brand-ink)'}">
      ${icon(iconName)}${esc(name)} <span class="count">${count}<span class="sr-only"> ${count === 1 ? 'sinal' : 'sinais'}</span></span></button>`;
  els.cats.innerHTML = chip(null, 'Todas', 'grid', null, state.data.signs.length)
    + state.data.categories.map(c => chip(c.id, c.name, c.icon, c.color ?? c.id, counts.get(c.id) ?? 0)).join('');
}

function buildClasses() {
  const counts = new Map();
  for (const s of state.data.signs) counts.set(s.class, (counts.get(s.class) ?? 0) + 1);
  els.classes.innerHTML = `<span class="classes-label">Classe:</span>`
    + (state.data.classes ?? []).filter(c => counts.get(c.id)).map(c => `
      <button class="cat-chip class-chip" type="button" data-class="${esc(c.id)}" aria-pressed="false" title="${esc(c.hint ?? '')}">
        ${esc(c.name)} <span class="count">${counts.get(c.id)}<span class="sr-only"> sinais</span></span></button>`).join('');
}

function updateClasses(hasQuery) {
  els.classes.querySelectorAll('.class-chip').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.class === state.wordClass)));
  els.classes.hidden = hasQuery;
}

function updateCats(hasQuery) {
  els.cats.querySelectorAll('.cat-chip').forEach(b => b.setAttribute('aria-pressed', String((b.dataset.cat || null) === state.category)));
  // While typing, the chips step aside so the sign stays above the keyboard (search is global).
  els.cats.hidden = hasQuery;
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
        ${thumb(r.sign)}<span>${highlighted(r.sign.word, query)}</span></a></li>`).join('')}
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
  if (!sign.image) {
    return `<div class="no-drawing">${icon('hand')}<p><strong>Desenho em breve</strong>
      <span>Veja abaixo como fazer o sinal.</span></p></div>`;
  }
  const still = reducedMotion.matches && !state.playMotion && sign.poster;
  return `
    <img src="${esc(still ? sign.poster : sign.image)}" decoding="async"
      alt="${still ? 'Ilustração' : 'Ilustração animada'} do sinal de ${esc(sign.word)} em Libras. ${esc(sign.how)}">
    ${still ? `<button class="play" type="button" data-action="play">${icon('play')}Ver movimento</button>` : ''}`;
}

function refLine(sign) {
  const r = sign.refs;
  if (!r) return '';
  const names = [];
  if (r.signbank || /signbank/i.test(r.source ?? '')) names.push('Libras Signbank (UFSC)');
  if (r.ines || /INES/.test(r.source ?? '')) names.push('INES');
  return names.length ? `<p class="sign-ref">Referências: ${names.join(' · ')}</p>` : '';
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
      <span class="cat-pill">${icon(topicOf(sign)?.icon ?? cat.icon)}${esc(topicOf(sign) ? `${cat.name} · ${topicOf(sign).name}` : cat.name)}</span>
      ${favButton(sign)}
    </div>
    ${sign.class ? `<p class="class-line">${esc(state.data.classes?.find(c => c.id === sign.class)?.name.replace(/s$/, '').replace(/õe$/, 'ão') ?? sign.class)}</p>` : ''}
    ${viaAlias ? `<p class="sign-alias">Você buscou <b>${highlighted(match.term.text, query)}</b></p>`
      : aliases.length ? `<p class="sign-alias">Também: ${aliases.map(esc).join(', ')}</p>` : ''}
    <p class="sign-how">${esc(sign.how)}</p>
    ${params.length ? `
    <dl class="params">
      ${params.map(([key, label, ic]) => `
        <div class="param${key === 'handshape' && sign.handshapeImage ? ' param-hs' : ''}"><dt>${icon(ic)}${esc(label)}</dt><dd>${key === 'handshape' && sign.handshapeImage
          ? `<span class="hs"><img src="${esc(sign.handshapeImage)}" alt="" loading="lazy"><span>${esc(sign.params[key])}</span></span>`
          : esc(sign.params[key])}</dd></div>`).join('')}
    </dl>` : ''}
    ${sign.regionalNote ? `<p class="sign-note">${icon('info')}<span><b>Variação regional.</b> ${esc(sign.regionalNote)}</span></p>` : ''}
    ${refLine(sign)}`;
}

function favButton(sign) {
  const on = isFav(sign);
  return `<button class="fav${on ? ' is-on' : ''}" type="button" data-action="fav" aria-pressed="${on}"
    title="${on ? 'Tirar dos favoritos' : 'Guardar nos favoritos para praticar'}">${icon('star')}<span>${on ? 'Nos favoritos' : 'Favoritar'}</span></button>`;
}

function favsHtml() {
  const favs = readFavs().map(id => state.byId.get(id));
  return `
    <div class="page-intro">
      <h1>Favoritos</h1>
      <p>Guarde aqui os sinais que você ainda está aprendendo. Toque na estrela de um sinal para guardar ou tirar.</p>
    </div>
    ${favs.length ? `
    <p class="fav-count">${plural(favs.length, 'sinal guardado', 'sinais guardados')}</p>
    <ul class="words fav-list">${favs.map(s => `<li class="fav-row">${wordRow(s).replace(/^<li>|<\/li>$/g, '')}
      <button class="fav-remove" type="button" data-action="unfav" data-id="${esc(s.id)}" aria-label="Tirar ${esc(s.word)} dos favoritos" title="Tirar dos favoritos">${icon('close')}</button></li>`).join('')}</ul>`
    : `<div class="empty">
        <div class="empty-art">${icon('star')}</div>
        <h2>Nenhum favorito ainda</h2>
        <p>Abra um sinal e toque em <b>Favoritar</b>. Ele fica guardado aqui até você tirar.</p>
        <a class="btn" href="#/">${icon('search')}Buscar sinais</a>
      </div>`}`;
}

// Small picture of a sign: its still drawing, or a hand icon while the drawing is pending.
function thumb(sign, cls = '') {
  const src = sign.poster ?? sign.image;
  return src
    ? `<img class="${cls}" src="${esc(src)}" alt="" loading="lazy" decoding="async">`
    : `<span class="thumb-none ${cls}" aria-hidden="true">${icon('hand')}</span>`;
}

const topicOf = sign => state.categories.get(sign.category)?.topics?.find(t => t.id === sign.topic);

function wordRow(sign) {
  return `<li><a class="word-row" href="${signHref(sign)}" style="${catStyle(sign)}">
    ${thumb(sign)}<span class="wr-word">${esc(sign.word)}</span>
    ${sign.image ? '' : '<span class="wr-note">desenho em breve</span>'}</a></li>`;
}

function cardHtml(sign, active) {
  const cat = categoryOf(sign);
  return `
    <a class="card${active ? ' is-active' : ''}" href="${signHref(sign)}" style="${catStyle(sign)}"
      ${active ? 'aria-current="true"' : ''}>
      <div class="card-media">${thumb(sign, 'card-img')}</div>
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
      <p>O dicionário tem ${plural(state.data.signs.length, 'sinal', 'sinais')} por enquanto. Confira a palavra ou veja todos.</p>
      <button class="btn" type="button" data-action="show-all">${icon('grid')}Ver todos os sinais</button>
    </div>`;
}

function classListHtml() {
  const cls = state.data.classes.find(c => c.id === state.wordClass);
  const signs = state.sorted.filter(s => s.class === state.wordClass && inCategory(s));
  return `<section class="cat-section">
    <header class="cat-head" style="--cat: var(--brand)">
      <span class="cat-ico">${icon('book')}</span>
      <div><h2>${esc(cls?.name ?? '')}</h2>${cls?.hint ? `<p>${esc(cls.hint)}</p>` : ''}</div>
      <span class="count">${plural(signs.length, 'sinal', 'sinais')}</span>
    </header>
    <ul class="words">${signs.map(wordRow).join('')}</ul>
  </section>`;
}

function browseHtml() {
  if (state.wordClass) return classListHtml();
  // One closed accordion per category (one open at a time); its topics show only when it is opened.
  return state.data.categories
    .filter(c => !state.category || c.id === state.category)
    .map(c => {
      const signs = state.sorted.filter(s => s.category === c.id);
      const topics = (c.topics ?? []).map(t => ({ ...t, signs: signs.filter(s => s.topic === t.id) })).filter(t => t.signs.length);
      const open = topics.find(t => t.id === state.topic);
      const isOpen = state.openCat === c.id || state.category === c.id;
      const body = !topics.length
        ? (signs.length ? `<div class="grid">${signs.map(s => cardHtml(s, s === state.featured)).join('')}</div>`
          : '<p class="section-empty">Em breve.</p>')
        : `<div class="topics">${topics.map(t => `
            <button class="topic${t === open ? ' is-open' : ''}" type="button" data-topic="${esc(t.id)}" aria-expanded="${t === open}"
              style="--cat: ${catVar(c.color ?? c.id)}">
              <span class="topic-ico">${icon(t.icon)}</span><span class="topic-name">${esc(t.name)}</span>
              <span class="topic-count">${t.signs.length}</span></button>`).join('')}</div>
          ${open ? `<div class="topic-list" id="tema-${esc(open.id)}">
            <h3>${icon(open.icon)}${esc(open.name)} <span class="count">${plural(open.signs.length, 'sinal', 'sinais')}</span></h3>
            <ul class="words">${open.signs.map(wordRow).join('')}</ul></div>` : ''}`;
      return `
      <details class="cat-section" name="categorias" data-cat-acc="${esc(c.id)}"${isOpen ? ' open' : ''}>
        <summary class="cat-head" style="--cat: var(--cat-${esc(c.color ?? c.id)})">
          <span class="cat-ico">${icon(c.icon)}</span>
          <div><h2>${esc(c.name)}</h2>${c.description ? `<p>${esc(c.description)}</p>` : ''}</div>
          <span class="count">${plural(signs.length, 'sinal', 'sinais')}</span>
          <span class="acc-tri" aria-hidden="true"></span>
        </summary>
        <div class="cat-body">${body}</div>
      </details>`;
    }).join('');
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
  if (picked && !inCategory(picked)) state.category = null;
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

// Clears the typed word but keeps the category filter (X button, Escape).
function clearSearch() {
  els.q.value = '';
  if (location.hash && location.hash !== '#/') history.replaceState(null, '', '#/');
  render();
}

// Full reset: no word, no filter (logo, "Ver todos os sinais").
function goHome() {
  els.q.value = '';
  state.category = null;
  state.topic = null;
  state.openCat = null;
  state.wordClass = null;
  if (location.hash && location.hash !== '#/') history.replaceState(null, '', '#/');
  render();
  window.scrollTo({ top: 0 });
}

// ---------- Events ----------

els.q.addEventListener('input', () => {
  if (viewFromHash() !== 'sinais') history.replaceState(null, '', '#/');
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
    els.q.blur(); // closes the phone keyboard so the whole sign is visible
  }
  if (e.key === 'Escape' && els.q.value) clearSearch();
});
els.clear.addEventListener('click', () => {
  clearSearch();
  els.q.focus();
});
$('.brand').addEventListener('click', e => {
  e.preventDefault();
  goHome();
});
els.classes.addEventListener('click', e => {
  const chip = e.target.closest('.class-chip');
  if (!chip) return;
  state.wordClass = state.wordClass === chip.dataset.class ? null : chip.dataset.class;   // tap again to turn off
  announce(state.wordClass ? chip.textContent.trim() : 'Todas as classes');
  render();
});
els.cats.addEventListener('click', e => {
  const chip = e.target.closest('.cat-chip');
  if (!chip) return;
  const id = chip.dataset.cat || null;
  state.category = id && id === state.category ? null : id;   // tapping the active chip turns it off
  announce(state.category ? `${chip.dataset.name}: ${plural(Number(chip.dataset.count), 'sinal', 'sinais')}` : 'Todas as categorias');
  // A picked sign from another category no longer applies.
  const picked = pickedFromHash();
  if (picked && !inCategory(picked)) history.replaceState(null, '', '#/');
  render();
});
document.addEventListener('click', e => {
  // A tab always opens its page, even with a word still in the search box.
  if (e.target.closest('.tab')) {
    els.q.value = '';
    if (e.target.closest('.tab').getAttribute('href') === location.hash) render();
    return;
  }
  const topic = e.target.closest('[data-topic]');
  if (topic) {
    state.topic = state.topic === topic.dataset.topic ? null : topic.dataset.topic;   // one open at a time
    render();
    if (state.topic) document.getElementById(`tema-${state.topic}`)?.scrollIntoView({ block: 'start', behavior: reducedMotion.matches ? 'auto' : 'smooth' });
    return;
  }
  const actionEl = e.target.closest('[data-action]');
  const action = actionEl?.dataset.action;
  if (action === 'show-all') goHome();
  if (action === 'fav' && state.featured) {
    const on = toggleFav(state.featured);
    actionEl.outerHTML = favButton(state.featured);
    announce(on ? `${state.featured.word} guardado nos favoritos` : `${state.featured.word} tirado dos favoritos`);
    $('.fav', els.feature)?.focus();
  }
  if (action === 'unfav') {
    const sign = state.byId.get(actionEl.dataset.id);
    if (sign && isFav(sign)) toggleFav(sign);
    render();
    announce(`${sign?.word ?? 'Sinal'} tirado dos favoritos`);
  }
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
// Remember which category accordion is open, so re-rendering keeps it (toggle doesn't bubble).
document.addEventListener('toggle', e => {
  const acc = e.target.closest?.('[data-cat-acc]');
  if (!acc || e.target !== acc) return;
  if (acc.open) state.openCat = acc.dataset.catAcc;
  else if (state.openCat === acc.dataset.catAcc) { state.openCat = null; state.topic = null; }
}, true);
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
