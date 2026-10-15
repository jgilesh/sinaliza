// "Frases" (everyday sentences in Libras order) and "Monte uma frase" (a simple sentence
// builder). Both link every word to its sign in the dictionary.
import { normalize } from './search.js';

let ctx;          // helpers from app.js: esc, icon, thumb, signHref, signs
let lookup;       // normalized word or alias -> sign
const builder = { when: '', who: 'eu', verb: 'querer', obj: 'água', type: 'afirmacao', qword: 'o que' };

export function setup(helpers, frases) {
  ctx = { ...helpers, frases };
  lookup = new Map();
  for (const s of helpers.signs) {
    for (const w of [s.word, ...(s.aliases ?? [])]) {
      const k = normalize(w);
      if (k && !lookup.has(k)) lookup.set(k, s);
    }
  }
}

const isSpelled = token => /^[A-ZÀ-Ú](-[A-ZÀ-Ú])+$/.test(token);
const signFor = token => lookup.get(normalize(token));

// One gloss token: a link to its sign with a small picture, or plain letters for spelled names.
function tokenHtml(token) {
  const { esc, thumb, signHref, icon } = ctx;
  if (isSpelled(token)) {
    return `<span class="tok tok-spelled" title="Datilologia (soletrado)"><span class="tok-pic">${icon('hand')}</span>
      <span class="tok-word">${esc(token)}</span><span class="tok-note">soletrado</span></span>`;
  }
  const sign = signFor(token);
  if (!sign) return `<span class="tok tok-missing"><span class="tok-word">${esc(token)}</span></span>`;
  return `<a class="tok" href="${signHref(sign)}">${thumb(sign, 'tok-pic')}<span class="tok-word">${esc(token)}</span>
    ${sign.class ? `<span class="tok-note">${esc(classShort(sign.class))}</span>` : ''}</a>`;
}

function classShort(id) {
  return ctx.classes?.find(c => c.id === id)?.short ?? id;
}

function glossLine(tokens, question) {
  return `<div class="gloss" role="list">${tokens.map(t => `<span role="listitem">${tokenHtml(t)}</span>`).join('<span class="gloss-sep" aria-hidden="true">›</span>')}
    ${question ? `<span class="gloss-q" title="Expressão interrogativa">?</span>` : ''}</div>`;
}

function tipsHtml(ids) {
  const tips = ctx.frases.tips.filter(t => ids.includes(t.id));
  return tips.length ? `<ul class="tips">${tips.map(t => `<li><b>${ctx.esc(t.title)}.</b> ${ctx.esc(t.text)}</li>`).join('')}</ul>` : '';
}

// ---------- Frases ----------

export function frasesHtml() {
  const { esc, icon, frases } = ctx;
  const groups = frases.groups.map(g => {
    const list = frases.sentences.filter(s => s.group === g.id);
    return `<section class="fr-group">
      <h2 class="section-title">${icon(g.icon)}${esc(g.name)} <span class="count">${list.length}</span></h2>
      ${list.map(s => `
        <article class="sentence">
          <p class="sentence-pt">${esc(s.pt)}</p>
          <p class="sentence-label">Em Libras</p>
          ${glossLine(s.gloss, s.question)}
          ${tipsHtml(s.tips ?? [])}
        </article>`).join('')}
    </section>`;
  }).join('');
  return `
    <div class="page-intro">
      <h1>Frases do dia a dia</h1>
      <p>Cada frase aparece em português e na ordem da Libras. Toque numa palavra para ver o sinal.</p>
    </div>
    ${grammarHtml()}
    ${groups}`;
}

// Short grammar notes: closed by default, one open at a time.
function grammarHtml() {
  const { esc, icon } = ctx;
  return `<section class="grammar">
    <h2 class="section-title">${icon('book')}Como a Libras monta frases</h2>
    ${ctx.frases.tips.map(t => `
      <details name="gramatica" class="acc">
        <summary><span class="acc-tri" aria-hidden="true"></span>${esc(t.title)}</summary>
        <p>${esc(t.text)}</p>
      </details>`).join('')}
  </section>`;
}

// ---------- Monte uma frase ----------

const WHEN = [['', '—'], ['hoje', 'Hoje'], ['amanhã', 'Amanhã'], ['ontem', 'Ontem'], ['agora', 'Agora'], ['depois', 'Depois']];
const WHO = [['eu', 'Eu'], ['você', 'Você'], ['ele', 'Ele / ela'], ['nós', 'Nós'], ['eles', 'Eles / elas']];
const VERBS = ['querer', 'gostar', 'precisar', 'ir', 'comer', 'beber', 'trabalhar', 'estudar', 'morar', 'ter', 'ver',
  'entender', 'saber', 'aprender', 'ajudar', 'comprar', 'chegar', 'sair', 'dormir', 'falar', 'pagar', 'conhecer'];
const OBJECTS = ['', 'água', 'café', 'comida', 'casa', 'escola', 'trabalho', 'família', 'mãe', 'pai', 'amigo', 'médico',
  'hospital', 'dinheiro', 'carro', 'livro', 'Libras', 'computador'];
const QWORDS = [['o que', 'O que'], ['onde', 'Onde'], ['quando', 'Quando'], ['quem', 'Quem'], ['por que', 'Por que']];

export function montarHtml() {
  const { esc } = ctx;
  const opt = (list, value) => list.map(([v, label]) => `<option value="${esc(v)}"${v === value ? ' selected' : ''}>${esc(label)}</option>`).join('');
  const known = list => list.filter(w => !w || signFor(w));
  const verbs = known(VERBS).map(v => [v, v]);
  const objs = known(OBJECTS).map(o => [o, o || '—']);
  return `
    <div class="page-intro">
      <h1>Monte uma frase</h1>
      <p>Escolha as partes e veja a frase na ordem da Libras, com o sinal de cada palavra.</p>
    </div>
    <form class="builder" id="builder" onsubmit="return false">
      <label><span>Quando</span><select name="when">${opt(WHEN, builder.when)}</select></label>
      <label><span>Quem</span><select name="who">${opt(WHO, builder.who)}</select></label>
      <label><span>Verbo</span><select name="verb">${opt(verbs, builder.verb)}</select></label>
      <label><span>Complemento</span><select name="obj">${opt(objs, builder.obj)}</select></label>
      <fieldset class="types">
        <legend>Tipo de frase</legend>
        ${[['afirmacao', 'Afirmação'], ['negacao', 'Negação'], ['sim-nao', 'Pergunta (sim/não)'], ['pergunta', 'Pergunta com…']]
          .map(([v, l]) => `<label class="type"><input type="radio" name="type" value="${v}"${builder.type === v ? ' checked' : ''}><span>${l}</span></label>`).join('')}
        <select name="qword" aria-label="Palavra da pergunta"${builder.type === 'pergunta' ? '' : ' hidden'}>${opt(QWORDS, builder.qword)}</select>
      </fieldset>
    </form>
    <section class="built" id="built" aria-live="polite">${builtHtml()}</section>`;
}

function builtHtml() {
  const b = builder;
  const tokens = [];
  const tips = [];
  if (b.when) { tokens.push(b.when.toUpperCase()); tips.push('tempo'); }
  tokens.push(b.who.toUpperCase(), b.verb.toUpperCase());
  // O QUE / QUEM ask about the complement, so they take its place.
  const asksObject = b.type === 'pergunta' && (b.qword === 'o que' || b.qword === 'quem');
  if (b.obj && !asksObject) tokens.push(b.obj.toUpperCase());
  if (b.type === 'negacao') { tokens.push('NÃO'); tips.push('negacao'); }
  if (b.type === 'pergunta') { tokens.push(b.qword.toUpperCase()); tips.push('pergunta'); }
  if (b.type === 'sim-nao') tips.push('pergunta');
  tips.push('sem-ligacao');
  const question = b.type === 'sim-nao' || b.type === 'pergunta';
  return `<article class="sentence">
      <p class="sentence-label">Em Libras</p>
      ${glossLine(tokens, question)}
      ${question ? `<p class="face-note">${ctx.icon('face')}${b.type === 'sim-nao' ? 'Sobrancelhas levantadas durante a frase.' : 'Sobrancelhas franzidas, principalmente na palavra da pergunta.'}</p>` : ''}
      ${b.type === 'negacao' ? `<p class="face-note">${ctx.icon('face')}Balance a cabeça para os lados no NÃO.</p>` : ''}
      ${tipsHtml(tips)}
    </article>`;
}

export function wireMontar(root) {
  const form = root.querySelector('#builder');
  if (!form) return;
  form.addEventListener('input', () => {
    const f = new FormData(form);
    for (const k of ['when', 'who', 'verb', 'obj', 'type', 'qword']) builder[k] = f.get(k) ?? builder[k];
    form.querySelector('[name=qword]').hidden = builder.type !== 'pergunta';
    root.querySelector('#built').innerHTML = builtHtml();
  });
}
