# COÇAR: the support forearm lies across in front of the body, fist closed (S), palm up; the fingers
# of the dominant hand, spread and bent like a claw, scratch the forearm near the wrist, back and
# forth several times. Face of mild discomfort (not drawn). (UFSC Signbank COÇAR: 5_claw + S, 2a,
# rubbing on the forearm.)


def hs_cocar_claw():
    """Claw: fingers spread, a little bent at the knuckles and strongly at the middle and end joints;
    the thumb out and bent the same way."""
    return {'index': fing(12, 22, 70, 45), 'middle': fing(3, 24, 72, 46), 'ring': fing(-6, 26, 72, 46),
            'pinky': fing(-15, 28, 70, 44), 'thumb': (34.0, 26.0, 20.0, 22.0, 30.0)}


_coc_claw, _coc_s = hs_cocar_claw(), hs_S()
# Support (left) arm, written as the right hand at the mirrored place: fist across the body, palm up.
_coc_sup = mirrored(P((240, 234), _coc_s, 'wrist', yaw=-60, pitch=0, roll=90, scale=1.0, depth=70, pole=(1.0, 0.25, 0.3)))
# Dominant hand: palm down on the forearm, fingertips toward the body, seen a little from above.
_coc_hand = lambda x, **kw: P((x, 224), _coc_claw, 'fingertips', yaw=170, pitch=-20, roll=165, scale=1.05, depth=90,
                             pole=(1.0, 0.3, 0.3), **kw)
_coc_a, _coc_b = _coc_hand(222), _coc_hand(240)
_coc_keys = [(0.0, [_coc_a, _coc_sup]), (0.3, [_coc_a, _coc_sup])]
for _coc_i in range(3):
    _coc_keys += [(0.3 + 0.4 * _coc_i + 0.2, [_coc_b, _coc_sup]), (0.3 + 0.4 * _coc_i + 0.4, [_coc_a, _coc_sup])]
_coc_keys.append((2.3, [_coc_a, _coc_sup]))
SIGNS['cocar'] = {
    'poster': 0.3, 'dur': 2.3, 'hands': ['right', 'left'], 'handshape': _coc_claw, 'handshape_view': {'yaw': 40},
    'keys': _coc_keys,
    'mirror_second': True,
    'marks': [(222, 238, 180)],
    'arrows': [{'d': 'M 214 182 L 250 182', 'both': True}],
}
TITLES['cocar'] = 'Sinal de coçar em Libras'
