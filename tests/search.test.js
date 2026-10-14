// Run without Node (macOS JavaScriptCore):
//   /System/Library/Frameworks/JavaScriptCore.framework/Versions/Current/Helpers/jsc -m tests/search.test.js
import { normalize, editDistance, buildIndex, search, highlightRange } from '../js/search.js';

const SIGNS = [
  { word: 'água', aliases: ['agua'] },
  { word: 'família', aliases: [] },
  { word: 'mãe', aliases: ['mamãe'] },
  { word: 'obrigado', aliases: ['obrigada'] },
  { word: 'bom dia', aliases: [] },
  { word: 'coração', aliases: [] },
  { word: 'você', aliases: [] },
  { word: 'café', aliases: [] },
  { word: 'casa', aliases: [] },
];
const index = buildIndex(SIGNS);

let failures = 0;
let passed = 0;
function check(name, actual, expected) {
  const ok = JSON.stringify(actual) === JSON.stringify(expected);
  if (ok) passed++;
  else {
    failures++;
    print(`FAIL ${name}\n  expected ${JSON.stringify(expected)}\n  got      ${JSON.stringify(actual)}`);
  }
}
const top = q => search(index, q)[0]?.sign.word ?? null;
const words = q => search(index, q).map(r => r.sign.word);

// normalize
check('normalize accents', normalize('Água'), 'agua');
check('normalize cedilla + til', normalize('CORAÇÃO'), 'coracao');
check('normalize punctuation', normalize('  bom-dia! '), 'bom dia');
check('normalize empty', normalize(null), '');

// edit distance
check('distance equal', editDistance('agua', 'agua'), 0);
check('distance swap', editDistance('agau', 'agua'), 1);
check('distance insert', editDistance('famlia', 'familia'), 1);
check('distance cap', editDistance('xxxxxxx', 'agua', 1), 2);

// accents never required
check('agua -> água', top('agua'), 'água');
check('AGUA -> água', top('AGUA'), 'água');
check('familia -> família', top('familia'), 'família');
check('mae -> mãe', top('mae'), 'mãe');
check('coracao -> coração', top('coracao'), 'coração');
check('voce -> você', top('voce'), 'você');
check('cafe -> café', top('cafe'), 'café');
// accents typed are fine too, even the wrong ones
check('água typed with accent', top('água'), 'água');
check('wrong accent cáfe', top('cáfe'), 'café');

// as-you-type prefixes
check('prefix "ag"', top('ag'), 'água');
check('prefix "fam"', top('fam'), 'família');
check('prefix "c" lists café, casa, coração', words('c'), ['café', 'casa', 'coração']);
check('prefix "ca" only matches word starts', words('ca'), ['café', 'casa']);

// aliases
check('alias obrigada', top('obrigada'), 'obrigado');
check('alias mamae', top('mamae'), 'mãe');
check('alias result reports matched term', search(index, 'obrigada')[0].term.text, 'obrigada');

// multi-word
check('bom dia', top('bom dia'), 'bom dia');
check('second word "dia"', top('dia'), 'bom dia');
check('reversed words', top('dia bom'), 'bom dia');

// typos
check('typo famlia', top('famlia'), 'família');
check('typo obirgado (swap)', top('obirgado'), 'obrigado');
check('typo while typing "famli"', top('famli'), 'família');
check('typo coracap', top('coracap'), 'coração');
check('no result for nonsense', words('xyzw'), []);
check('empty query', words('   '), []);

// headword beats an alias that matches the same way
const OBR = buildIndex([{ word: 'obrigado', aliases: ['obrigada', 'obg'] }]);
check('"o" shows the headword, not the alias', search(OBR, 'o')[0].term.text, 'obrigado');
check('"obg" still reports the alias', search(OBR, 'obg')[0].term.text, 'obg');
check('typo with a dropped letter while typing', top('fmil'), 'família');
check('typo with an extra letter while typing', top('famiil'), 'família');

// highlight
check('highlight ag in Água', highlightRange('Água', 'ag'), [0, 2]);
check('highlight dia in bom dia', highlightRange('bom dia', 'dia'), [4, 7]);
check('highlight coracao', highlightRange('coração', 'coracao'), [0, 7]);
check('highlight none for typo', highlightRange('família', 'famlia'), null);

print(`${passed} passed, ${failures} failed`);
if (failures) throw new Error(`${failures} test(s) failed`);
