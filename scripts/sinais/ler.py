# LER: the support hand stands open (B), fingers up, palm toward the signing hand. The signing hand in V
# points the two fingers at that palm and goes down in small steps, like the eyes running along the
# lines of a page. No contact. (UFSC Signbank LER "V" with "B"; INES LER1 agrees.)

_ler_v, _ler_b = hs_V(), hs_B()
_ler_pole = (0.4, 1.0, 0.4)
# Support hand (defined as a right hand, then mirrored): fingers up, palm turned toward the signing hand
# and a little toward the viewer.
_ler_base = mirrored(P((152, 236), _ler_b, 'wrist', yaw=58, pitch=0, roll=-4, scale=1.05, depth=60))


def _ler_pose(step, ease='smooth'):
    # Back of the hand to the viewer, the two fingers level and pointing at the support palm: the V opens
    # up and down, both fingers in view.
    return P((226, 182 + 12 * step), _ler_v, 'fingertips', yaw=160, pitch=0, roll=90, scale=1.05, depth=60,
             pole=_ler_pole, ease=ease)


_ler_keys = [(0.0, _ler_pose(0)), (0.35, _ler_pose(0))]
for _ler_i in range(1, 4):   # three small steps down, each with a short stop
    _ler_keys += [(0.35 + 0.4 * _ler_i - 0.15, _ler_pose(_ler_i)), (0.35 + 0.4 * _ler_i, _ler_pose(_ler_i))]
_ler_keys += [(2.0, _ler_pose(3)), (2.5, _ler_pose(0))]
SIGNS['ler'] = {
    'poster': 0.35, 'dur': 2.5, 'hands': ['right', 'left'], 'handshape': _ler_v,
    'keys': [(t, [p, _ler_base]) for t, p in _ler_keys],
    # Beside the signing hand, on the outer side: down in steps.
    'arrows': [{'d': 'M 124 172 L 124 214'}],
    'mirror_second': True,
}
TITLES['ler'] = 'Sinal de ler em Libras'
