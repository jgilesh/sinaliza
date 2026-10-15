# Sinais · Dicionário de Libras

A Libras (Brazilian Sign Language) dictionary for an **interpreter** who needs a sign in the moment, on a phone or a computer. Type a Portuguese word (accents optional, typos tolerated) and the best match shows up big right away, with an animated drawing of the sign and its parameters. Personal project for John; not a Finances Demystified project, so the demystified brand does not apply.

Status (15 Oct 2026): 1,151 signs. **Básico** has 1,150 (17 topics); 5 of them have drawings (água, café, família, obrigado, você), the rest are text entries ("Desenho em breve") waiting for drawings in checked batches. **Tecnologia** has computador (drawn). Runs locally; not on GitHub yet.

## How the Básico words were made (15 Oct 2026)

John chose "words first, drawings later". Candidates = words in BOTH the UFSC Libras Signbank and the INES dictionary (1,363), ranked by Signbank corpus frequency. A workflow of 55 writer agents (25 words each: Signbank video frames + phonology fields + INES meaning → our own pt-BR entry) and 55 checker agents (≥8 entries per batch re-checked against the video; 570 fixes) produced the entries. Left out: non-basic/academic words, meaning mismatches, missing videos, and 27 low-confidence entries. Each entry has `refs` (`signbank` id, `ines` headword) and no `image`. Known gaps: some very common words (e.g. mãe, number words) are missing because one source lists them under another name; about 300 Signbank detail records didn't download.

## Categories

- John's plan: interpreters already know everyday signs, so the value is in advanced, specialised categories. **Básico** holds everyday signs; every other category is a specialised area (Tecnologia first; John will send more names and sections). Each category has its own color token (`--cat-<id>` in `css/app.css`), an icon (`ICONS` in `js/app.js`) and a one-line description in `data/sinais.json`.
- Home shows one section per category; Básico shows topic tiles (`categories[].topics`, sign `topic`) that open a word list. The chips filter browsing only: **search always covers every category** (John). Near-miss (typo) results only show when nothing real matches.

## Non-negotiables

- **Every sign picture is our own drawing**, made by `scripts/desenhar_sinais.py`. Never download or embed sign images or videos from the internet. Other dictionaries (INES) are only a reference for *how* the sign is made; descriptions are written in our own words.
- All drawings share one style: the same figure, hand model, colors and arrows. The signer is drawn to resemble the person the app is for: a woman in her fifties, dark brown hair pulled back, small gold hoop earrings, warm smile, plain blue top (plain on purpose, like interpreters wear, so hands stand out).
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
- `sw.js`: offline and weak signal. Drawings cache-first; JS/CSS/data stale-while-revalidate; the page network-first with a 2.5 s timeout. Install precaches the app, the data and every drawing listed in it (`allSettled`, so one missing file doesn't cancel the rest). `CACHE` comes from `scripts/versao.py`; the page reloads once when a new version takes over.
- `data/sinais.json`: categories, reference, signs. Sign fields: `id`, `word`, `aliases` (spelling variants, informal forms, abbreviations that use the same sign), `category`, `image`, `poster`, `how` (1–2 sentences), `params` (`handshape`, `location`, `movement`, `orientation`, `expression`), optional `regionalNote`.
- `scripts/desenhar_sinais.py`: the drawing engine. A 3D-ish hand (fingers as joint chains with `twist` for sideways curls, thumb solved to touch a target), projected with yaw (0 palm to viewer, 180 back of hand), pitch, roll; arms by 3D two-bone IK (elbow drops for low hands, opens sideways for raised hands; `pole=` overrides). Keyframes are interpolated and sampled at 20 fps into SMIL `values`; when the anchor changes between keys the wrist is interpolated, and `via` curves a moving segment only. Each sign = a few `P(...)` poses; `mirrored()` makes the left hand for two-handed signs. Each SVG is framed (`view_box`) on the face and hands so handshapes stay readable on a phone.
- Drawing symbols: orange arrows = movement; orange 3-tick burst = contact with the body (never use it for a sign without contact); orange ripples around a fingertip = pointing toward the viewer.
- `media/sinais/<id>.svg` (animated), `<id>-parado.svg` (still, the `poster` time in the spec) and `media/maos/<id>.svg` (the handshape alone, from the spec's `handshape`).
- Finger drawing: each phalanx is its own tapered stroke (`TAPER`), knuckle creases at the joints, a nail when the back of the fingertip faces the viewer (`distal_dorsal`), a shaded hole inside thumb-index rings (`ring=True` on the pose), and the palm has thickness so side views read as a slab.

## Adding a sign

1. Look at a reference (e.g. the INES video for the word) and note handshape, contact point, movement, palm orientation, expression, one or two hands.
2. Add a `SIGNS['<id>']` entry in `scripts/desenhar_sinais.py` (reuse or add a handshape function `hs_*`), run the script, check it in `tests/ilustracoes.html` at several times.
3. Add the entry to `data/sinais.json` in our own words (with `category`, `image`, `poster`, `handshapeImage`), and the id to the list in `tests/ilustracoes.html`.
4. Prefer signs that two independent sources agree on (INES, UFSC Libras Signbank, UFV dictionary). Signbank API: `https://api-signbank.levantelab.com.br/api/tabela_sinais/sinais/<id>` (needs a browser-like User-Agent).
