# CAMINHAR: index and middle fingers straight and pointing down like two legs, thumb out, the other
# fingers closed; the back of the hand toward the viewer, in front of the shoulder at chest height. The
# two fingers swing back and forth in turn, like steps, while the hand moves a little forward and in.
# No contact. (UFSC Signbank CAMINHAR, INES CAMINHAR.)


def hs_caminhar_legs(swing=0.0):
    """Index and middle straight and a little apart (two legs), ring and little finger folded, thumb
    out to the side. `swing` > 0 bends the index forward at the knuckle and lets the middle finger
    hang straight; < 0 the other way round (a step)."""
    shape = fist({'index': fing(8, max(swing, 0.0) * 30 + 2, 4, 2), 'middle': fing(-6, max(-swing, 0.0) * 30 + 2, 4, 2)})
    shape['thumb'] = (44.0, 14.0, 6.0, 6.0, 4.0)
    return shape


_caminhar_mid, _caminhar_a, _caminhar_b = hs_caminhar_legs(0.0), hs_caminhar_legs(1.0), hs_caminhar_legs(-1.0)


def _caminhar_at(shape, k, ease='smooth'):
    # Back of the hand to the viewer, turned a little so the fingers swing sideways on screen (toward
    # the palm); fingers down, the thumb pointing in toward the midline.
    x, y = 140 + 22 * k, 156 + 8 * k
    return P((x, y), shape, 'wrist', yaw=212, pitch=0, roll=180, scale=1.1 + 0.1 * k, depth=55 + 30 * k, ease=ease,
             pole=(0.45, 1.0, 0.4))


_caminhar_keys = [(0.0, [_caminhar_at(_caminhar_mid, 0.0)]), (0.3, [_caminhar_at(_caminhar_mid, 0.0)])]
_caminhar_n = 4
for _caminhar_i in range(_caminhar_n):
    _caminhar_k = (_caminhar_i + 1) / _caminhar_n
    _caminhar_shape = _caminhar_a if _caminhar_i % 2 == 0 else _caminhar_b
    _caminhar_keys.append((0.3 + 0.32 * (_caminhar_i + 1), [_caminhar_at(_caminhar_shape, _caminhar_k, 'linear')]))
_caminhar_keys += [(0.3 + 0.32 * _caminhar_n + 0.2, [_caminhar_at(_caminhar_mid, 1.0)]),
                   (0.3 + 0.32 * _caminhar_n + 0.7, [_caminhar_at(_caminhar_mid, 1.0)]),
                   (0.3 + 0.32 * _caminhar_n + 1.2, [_caminhar_at(_caminhar_mid, 0.0)])]
SIGNS['caminhar'] = {
    'poster': 0.62, 'dur': 0.3 + 0.32 * _caminhar_n + 1.2, 'hands': ['right'], 'handshape': _caminhar_mid,
    'handshape_view': {'yaw': 0},
    'keys': _caminhar_keys,
    # Below the fingertips (clear of them): the hand moves forward and in while the fingers step.
    'arrows': [{'d': 'M 136 266 L 172 278'}],
}
TITLES['caminhar'] = 'Sinal de caminhar em Libras'
