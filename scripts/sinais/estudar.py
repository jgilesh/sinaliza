# ESTUDAR: both hands open with the fingers together and a little curved, palms up, in front of
# the chest. The back of the signing hand comes down onto the palm of the support hand and taps
# it, 3 times; the support hand stays still. (UFSC Signbank ESTUDAR, INES ESTUDAR.)


def hs_estudar_b():
    """B with the fingers together and slightly curved, thumb a little apart."""
    return {'index': fing(2, 10, 14, 8), 'middle': fing(0, 10, 14, 8), 'ring': fing(-2, 10, 14, 8),
            'pinky': fing(-4, 12, 14, 8), 'thumb': (22.0, 18.0, 10.0, 8.0, 6.0)}


_estudar_hs = hs_estudar_b()
# Support hand (defined as a right hand, then mirrored): palm up, tilted a little toward the viewer
# so the palm shows, fingers pointing across toward the midline and a little up.
_estudar_base = mirrored(P((142, 246), _estudar_hs, 'wrist', yaw=-50, pitch=0, roll=92, scale=1.1, depth=70))


def _estudar_top(lift):
    # The signing hand, palm up, fingers pointing across and up; its back lands on the support palm.
    return P((172, 234 - lift), _estudar_hs, 'wrist', yaw=-50, pitch=0, roll=68, scale=1.1, depth=74,
             pole=(0.4, 1.0, 0.4))


_estudar_up, _estudar_down = _estudar_top(16), _estudar_top(0)
_estudar_keys = [(0.0, [_estudar_up, _estudar_base])]
for _estudar_t in (0.3, 0.6, 0.9):
    _estudar_keys += [(_estudar_t + 0.15, [_estudar_down, _estudar_base]), (_estudar_t + 0.3, [_estudar_up, _estudar_base])]
_estudar_keys.append((2.4, [_estudar_up, _estudar_base]))
SIGNS['estudar'] = {
    'poster': 0.45, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _estudar_hs,
    'keys': _estudar_keys,
    'marks': [(250, 222, 80)],
    'arrows': [{'d': 'M 140 190 L 140 214', 'both': True}],
    'mirror_second': True,
}
TITLES['estudar'] = 'Sinal de estudar em Libras'
