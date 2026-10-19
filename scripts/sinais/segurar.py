# SEGURAR: both hands closed (S), one above the other in front of the chest on the signing side, as if
# holding a stick upright: the dominant hand on top, its little-finger side resting on the thumb side of
# the lower hand. The hands come together and tighten the grip with a small squeeze. (UFSC Signbank
# SEGURAR: S/S, on the thumb side of the weak hand. The INES SEGURAR video shows another variant: the two
# fists apart at shoulder height, holding something in front of the body.)
_seg_s = hs_S()


def _seg_upper(y, ease='smooth'):
    # Knuckles toward the viewer and a little toward the midline, thumb on top: the folded fingers and the
    # thumb across them read. The elbow is raised a little, so the forearm passes beside the lower fist.
    return P((166, y), _seg_s, 'wrist', yaw=10, pitch=55, roll=-90, scale=1.1, depth=90,
             pole=(0.8, 0.6, 0.6), ease=ease)


def _seg_lower(y, ease='smooth'):
    # The support hand reaches across and holds just under it, the same way round (thumb up).
    return mirrored(P((236, y), _seg_s, 'wrist', yaw=-10, pitch=55, roll=-90, scale=1.1, depth=70,
                      pole=(0.3, 1.0, 0.4), ease=ease))


_seg_open = [_seg_upper(184), _seg_lower(238)]
_seg_held = [_seg_upper(194, 'out'), _seg_lower(228, 'out')]
_seg_squeeze = [_seg_upper(197), _seg_lower(225)]
SIGNS['segurar'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _seg_s,
    'keys': [(0.0, _seg_open), (0.3, _seg_open), (0.75, _seg_held), (0.95, _seg_squeeze), (1.15, _seg_held),
             (1.9, _seg_held), (2.4, _seg_open)],
    # Beside the fists: the upper one comes down, the lower one up, to meet.
    'arrows': [{'d': 'M 224 172 L 224 188'}, {'d': 'M 224 262 L 224 246'}],
    'mirror_second': True,
}
TITLES['segurar'] = 'Sinal de segurar em Libras'
