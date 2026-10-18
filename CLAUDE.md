# Sinaliza · Dicionário de Libras

A Libras (Brazilian Sign Language) dictionary for an **interpreter** who needs a sign in the moment, on a phone or a computer. Type a Portuguese word (accents optional, typos tolerated) and the best match shows up big right away, with an animated drawing of the sign and its parameters. Personal project for John; not a Finances Demystified project, so the demystified brand does not apply.

Status (18 Oct 2026): 1,151 signs. Repo: https://github.com/jgilesh/Sinaliza (John renamed the app from "Sinais" to **Sinaliza** on 18 Oct; it is for interpreters to look up and pass on signs, and for Deaf people to learn). **Básico** has 1,150 (17 topics); 72 signs have drawings (all of Cumprimentos e expressões and every word used on the Frases page), the rest are text entries ("Desenho em breve") waiting for drawings in checked batches. **Tecnologia** has computador (drawn). Look (John, 18 Oct): calm palette with few colours, ameixa (plum) for almost everything and terracota only for accents (tokens at the top of `css/app.css`, light and dark); logo/favicon = two interlocking rings, terracota and white on plum (`icons/`), meaning hearing and Deaf people connected. Planned: open the app with a choice between "ouvinte" and "surdo" (two audiences: hearing people learning signs, e.g. parents and interpreters in training, and Deaf people learning Libras).

## How the Básico words were made (15 Oct 2026)

John chose "words first, drawings later". Candidates = words in BOTH the UFSC Libras Signbank and the INES dictionary (1,363), ranked by Signbank corpus frequency. A workflow of 55 writer agents (25 words each: Signbank video frames + phonology fields + INES meaning → our own pt-BR entry) and 55 checker agents (≥8 entries per batch re-checked against the video; 570 fixes) produced the entries. Left out: non-basic/academic words, meaning mismatches, missing videos, and 27 low-confidence entries. Each entry has `refs` (`signbank` id, `ines` headword) and no `image`. Known gaps: some very common words (e.g. mãe, number words) are missing because one source lists them under another name; about 300 Signbank detail records didn't download.

## Word classes and sentences (expert's idea, 15 Oct 2026)

The expert (the Libras interpreter the app is for) wants people to *use* signs in sentences, not just know nouns. So:
- Every sign has `class` (substantivo, verbo, adjetivo, adverbio, pronome, numeral, ligacao, expressao), mostly from the INES class labels; `data.classes` lists them and a "Classe" chip row filters browsing.
- Tabs: **Sinais** (dictionary), **Frases** (`#/frases`: everyday sentences from `data/frases.json`, each in Portuguese + Libras gloss order + linked sign strip + grammar tips; grammar notes as closed single-open accordions) and **Monte uma frase** (`#/montar`: builder: QUANDO QUEM VERBO COMPLEMENTO + NÃO / question word at the end, with face cues). Code in `js/frases.js`; gloss tokens resolve to signs by word/alias, `A-N-A` = datilologia.
- The expert reviews section by section later; for now this is the first version showing the idea. Videos/designs from her are on hold.

## Categories

- John's plan: interpreters already know everyday signs, so the value is in advanced, specialised categories. **Básico** holds everyday signs; every other category is a specialised area (Tecnologia first; John will send more names and sections). Each category has its own color token (`--cat-<id>` in `css/app.css`; keep them inside the ameixa/terracota palette), an icon (`ICONS` in `js/app.js`) and a one-line description in `data/sinais.json`.
- Home shows one section per category; Básico shows topic tiles (`categories[].topics`, sign `topic`) that open a word list. The chips filter browsing only: **search always covers every category** (John). Near-miss (typo) results only show when nothing real matches.

## Non-negotiables

- **Every sign picture is our own drawing**, made by `scripts/desenhar_sinais.py`. Never download or embed sign images or videos from the internet. Other dictionaries (INES) are only a reference for *how* the sign is made; descriptions are written in our own words.
- All drawings share one style: the same figure, hand model, colors and arrows. The signer is the "Warm character" John chose on 18 Oct, drawn to resemble the expert (Regina) as a younger version: few face lines, long dark hair, small gold hoop earrings, warm smile, plain chambray shirt (plain on purpose, like interpreters wear, so hands stand out).
- **Fingers must be unmistakable** (John, 13 Oct). Prefer views where the handshape reads head-on (palm to the viewer for L, F, 1, B, OK); every sign also gets a large handshape picture (`media/maos/<id>.svg`, palm forward) shown next to "Mão". Signs with movement are animated SVG (SMIL, works inside `<img>`); each also has a still `-parado.svg` for lists and reduced motion.
- Built for speed, not for teaching: no lessons, example sentences or step lists. Show the sign first.
- Everything the user sees is Brazilian Portuguese. Code and comments stay in English.
- Static site: plain HTML, CSS, ES modules. No npm, no build step (Node is not installed on John's Mac).
- Check desktop and phone width (375 px), light and dark mode, before every push.
- Claude's job ends at `git push`; Vercel deploys on its own. Don't touch Vercel.

## Run

- Local server: `python3 -m http.server 4210 --directory .` (preview config `libras-dicionario` in `~/Claude/.claude/launch.json`), then http://127.0.0.1:4210
- Search tests: `/System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc -m tests/search.test.js`
- Redraw signs: `python3 scripts/desenhar_sinais.py` (all) or `python3 scripts/desenhar_sinais.py agua cafe`
- Review drawings frame by frame: http://127.0.0.1:4210/tests/ilustracoes.html (`?t=0.55` freezes all at that second; `freeze(t)` in the console)
- **Before every commit:** `python3 scripts/versao.py` (stamps `sw.js` with a hash of the site, so installed copies update; `--check` fails if it is stale). While testing locally, the service worker serves the previous copy of JS/CSS on the first reload; reload twice, or unregister it in DevTools.

## Layout

- `index.html`: header with the search box (sticky), `#status` (count, or an amber warning when only near-misses match: "doce" is not "você"), `#alts` (other matches as chips, above the drawing), `#feature` (the sign shown big), `#results` (recents + all signs when the search is empty).
- `js/search.js`: pure search (no DOM). `normalize` strips accents/case/punctuation; `search` ranks exact > prefix > word start > all words > contains (3+ letters) > typo (edit distance with swaps; 1 typo up to 5 letters, 2 after). Aliases count as matches.
- `js/app.js`: rendering and state. Typing features the best match; `#/sinal/<id>` holds a sign the user picked (cards, recents, arrow keys). Recents live in `localStorage` (`sinais.recentes`), every access in try/catch.
- `sw.js`: offline and weak signal. Drawings cache-first; JS/CSS/data stale-while-revalidate; the page network-first with a 2.5 s timeout. Install precaches the app, the data, and every sign's still drawing and handshape picture (`allSettled`, so one missing file doesn't cancel the rest); animated drawings are cached the first time they are opened. `CACHE` comes from `scripts/versao.py`; the page reloads once when a new version takes over.
- `data/sinais.json`: categories, reference, signs. Sign fields: `id`, `word`, `aliases` (spelling variants, informal forms, abbreviations that use the same sign), `category`, `image`, `poster`, `how` (1–2 sentences), `params` (`handshape`, `location`, `movement`, `orientation`, `expression`), optional `regionalNote`.
- `scripts/desenhar_sinais.py`: the drawing engine. An anatomical 3D-ish hand (fingers as joint chains with real limits and no sideways twist: they only bend toward the palm; the thumb has its own frame at the base of the palm and `pinch_thumb` puts its pad on the fingertip pad), projected with yaw (0 palm to viewer, 180 back of hand), pitch, roll; arms by 3D two-bone IK (elbow drops for low hands, opens sideways for raised hands; `pole=` overrides). Keyframes are interpolated and sampled at 20 fps into SMIL `values`; when the anchor changes between keys the wrist is interpolated, and `via` curves a moving segment only. Each sign = a few `P(...)` poses; `mirrored()` makes the left hand for two-handed signs. Each SVG is framed (`view_box`) on the face and hands so handshapes stay readable on a phone.
- Drawing symbols: orange arrows = movement; orange 3-tick burst = contact with the body (never use it for a sign without contact); orange ripples around a fingertip = pointing toward the viewer.
- `media/sinais/<id>.svg` (animated), `<id>-parado.svg` (still, the `poster` time in the spec) and `media/maos/<id>.svg` (the handshape alone, from the spec's `handshape`).
- Hand drawing rules (John, 18 Oct): joints bend only toward the palm; a nail only on the back of the fingertip and only when that side faces the viewer; creases only on palm-facing segments, knuckle wrinkles on the back; every finger visibly grows out of the hand with its whole length from the knuckle (the palm outline is left out at each finger's root), and a digit mostly hidden in a view is hidden cleanly, never shown as a loose piece or sliver. The rig and its checks were built in the session scratchpad (checker with raster checks for detached pieces, SMIL check); they are not in the repo.

## Adding a sign

New signs go one per file in `scripts/sinais/<id>.py` (the engine loads them; each file gets its own copy of the namespace, sets `SIGNS['<id>']` and `TITLES['<id>']`, and prefixes its own handshapes `hs_<id>_*`). 66 signs were added this way on 18 Oct (all of Cumprimentos + every word on the Frases page) from the brief in the session scratchpad.

1. Look at a reference (e.g. the INES video for the word) and note handshape, contact point, movement, palm orientation, expression, one or two hands.
2. Add `scripts/sinais/<id>.py` (reuse or add a handshape function `hs_*`), run the script, check it in `tests/ilustracoes.html` at several times.
3. Add the entry to `data/sinais.json` in our own words (with `category`, `image`, `poster`, `handshapeImage`), and the id to the list in `tests/ilustracoes.html`.
4. Prefer signs that two independent sources agree on (INES, UFSC Libras Signbank, UFV dictionary). Signbank API: `https://api-signbank.levantelab.com.br/api/tabela_sinais/sinais/<id>` (needs a browser-like User-Agent).
