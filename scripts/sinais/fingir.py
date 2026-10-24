# FINGIR: the support hand open with the fingers spread and up, palm toward the signing hand, in front
# of the shoulder on its own side. The signing hand open with the middle finger bent forward touches
# the support palm with the tip of the middle finger and rubs it with small movements, repeated.
# (UFSC Signbank FINGIR: 5m on B, weak hand; INES FINGIR agrees.)


def hs_fingir_5m():
    """Open hand, fingers spread, the middle finger bent forward at the knuckle."""
    shape = hs_5()
    shape['middle'] = fing(2, 62, 45, 25)
    return shape


_fingir_dom, _fingir_sup = hs_fingir_5m(), hs_5()
# Support hand, defined as a right hand and mirrored: fingers up, palm turned toward the midline and
# partly toward the viewer.
_fingir_base = mirrored(P((154, 228), _fingir_sup, 'wrist', yaw=55, pitch=0, roll=-8, scale=1.1, depth=50))
_fingir_base_low = mirrored(P((152, 236), _fingir_sup, 'wrist', yaw=55, pitch=10, roll=-8, scale=1.08, depth=55))
# Signing hand: palm toward the support hand, fingers up; the bent middle finger reaches across and its
# tip rests on the support palm.
_fingir_hand = lambda at, **kw: P(at, _fingir_dom, 'middle_tip', yaw=110, pitch=0, roll=10, scale=1.1, depth=58,
                                  pole=(0.4, 1.0, 0.4), **kw)
_fingir_a, _fingir_b = _fingir_hand((236, 203)), _fingir_hand((236, 195))
_fingir_low = _fingir_hand((212, 216))
_fingir_keys = [(0.0, [_fingir_low, _fingir_base_low]), (0.25, [_fingir_low, _fingir_base_low]),
                (0.6, [_fingir_a, _fingir_base])]
for _fingir_i in range(4):
    _fingir_keys += [(0.75 + 0.3 * _fingir_i, [_fingir_b, _fingir_base]), (0.9 + 0.3 * _fingir_i, [_fingir_a, _fingir_base])]
_fingir_keys += [(2.1, [_fingir_a, _fingir_base]), (2.6, [_fingir_low, _fingir_base_low])]
SIGNS['fingir'] = {
    'poster': 0.6, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _fingir_dom, 'handshape_view': {'yaw': -40},
    'keys': _fingir_keys,
    'marks': [(262, 210, 70)],
    # Small two-headed arrow beside the fingers: the middle fingertip rubs up and down on the palm.
    'arrows': [{'d': 'M 178 166 Q 172 178 178 190', 'both': True}],
    'mirror_second': True,
}
TITLES['fingir'] = 'Sinal de fingir em Libras'
