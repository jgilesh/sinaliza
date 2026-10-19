# SEPARAR: both hands flat (B), palms down, the fingertips touching in front of the chest; the hands
# move apart to the sides while the wrists turn down, ending with the fingers pointing down and the
# backs of the hands to the viewer. Once. (UFSC Signbank SEPARAR, INES SEPARAR1.)


def hs_separar_b():
    """B with the thumb resting along the side of the hand (not sticking out when the hand hangs)."""
    shape = hs_B()
    shape['thumb'] = (6.0, 12.0, 6.0, 6.0, 4.0)
    return shape


_separar_b = hs_separar_b()
# Palm down and turned a little toward the body, fingers pointing at the other hand: the back of the
# hand shows from above.
_separar_in = P((198, 204), _separar_b, 'fingertips', yaw=128, pitch=0, roll=92, scale=1.1, depth=70,
                pole=(0.45, 1.0, 0.4))
# Out at the side, waist height, fingers hanging down, back of the hand to the viewer.
_separar_out = P((96, 204), _separar_b, 'wrist', yaw=196, pitch=0, roll=172, scale=1.1, depth=70,
                 ease='out', pole=(0.45, 1.0, 0.4))
_separar_back = dict(_separar_in, ease='smooth')
SIGNS['separar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _separar_b,
    'keys': [(0.0, [_separar_in, mirrored(_separar_in)]), (0.4, [_separar_in, mirrored(_separar_in)]),
             (1.1, [_separar_out, mirrored(_separar_out)]), (1.9, [_separar_out, mirrored(_separar_out)]),
             (2.4, [_separar_back, mirrored(_separar_back)])],
    # Above the hands, from the middle out to each side and down: the hands part and turn down.
    'arrows': [{'d': 'M 186 186 Q 128 168 96 194'}, {'d': 'M 214 186 Q 272 168 304 194'}],
    'mirror_second': True,
}
TITLES['separar'] = 'Sinal de separar em Libras'
