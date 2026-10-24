# MULTIPLICAR: both hands with the index straight (1), palms toward the body; they come together in
# front of the chest and the two index fingers cross in an X (the "times" sign), holding it a moment.
# (UFSC Signbank VEZES "1" on the weak index; the INES MULTIPLICAR video shows another variant.)

_multiplicar_1 = hs_1()
_multiplicar_pole = (0.35, 1.0, 0.45)


def _multiplicar_pose(at, roll, yaw=150, **kw):
    # Back of the hand mostly to the viewer, turned a little toward the other hand; the index up.
    return P(at, _multiplicar_1, 'wrist', yaw=yaw, pitch=0, roll=roll, scale=1.1, depth=62, pole=_multiplicar_pole, **kw)


# Apart: the index fingers up, a hand's width on each side of the midline.
_multiplicar_apart = _multiplicar_pose((146, 232), 8)
# Crossed: each index leans in toward the other side, the two crossing halfway along their length.
_multiplicar_x = _multiplicar_pose((160, 232), 56, ease='out')
_multiplicar_keys = [(0.0, _multiplicar_apart), (0.3, _multiplicar_apart), (0.8, _multiplicar_x),
                     (1.8, _multiplicar_x), (2.3, dict(_multiplicar_apart, ease='smooth'))]
SIGNS['multiplicar'] = {
    'poster': 1.0, 'dur': 2.3, 'hands': ['right', 'left'], 'handshape': _multiplicar_1,
    'keys': [(t, [p, mirrored(p)]) for t, p in _multiplicar_keys],
    # Below the hands: each hand moves in toward the other.
    'arrows': [{'d': 'M 132 262 L 160 256'}, {'d': 'M 268 262 L 240 256'}],
    'mirror_second': True,
}
TITLES['multiplicar'] = 'Sinal de multiplicar em Libras'
