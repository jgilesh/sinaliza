# ENROLAR: both index fingers (1), lying horizontal and pointing across toward each other, one above the
# other in front of the body; they circle around each other, as when rolling something up, two or three
# turns, moving a little forward. No contact. (UFSC Signbank ENROLAR; the INES ENROLAR1 video shows the
# same rolling movement done to the side.)
_enrolar_1 = hs_1()
_enrolar_C = (135.0, 214.0)   # right hand: wrist's circle centre
_enrolar_R = 13.0


def _enrolar_pose(angle, k):
    """Right hand on its circle (angle 0 = nearest the viewer, 90 = bottom). The back of the hand to the
    viewer, the index pointing across toward the other hand; k (0..1) moves the circle forward."""
    a = math.radians(angle)
    at = (_enrolar_C[0] + 4 * math.cos(a), _enrolar_C[1] + _enrolar_R * math.sin(a))
    return P(at, _enrolar_1, 'wrist', yaw=180, pitch=-20, roll=90, scale=1.05 + 0.03 * math.cos(a) + 0.06 * k,
             depth=60 + 12 * math.cos(a) + 15 * k, pole=(0.35, 1.0, 0.45), ease='linear')


# The right hand turns one way (over the top toward the viewer), the left half a turn behind it: when one
# is up, the other is down.
_enrolar_steps = 20                 # two and a half turns, 8 steps each
_enrolar_keys = [(0.0, [_enrolar_pose(-90, 0), mirrored(_enrolar_pose(90, 0))]),
                 (0.25, [_enrolar_pose(-90, 0), mirrored(_enrolar_pose(90, 0))])]
for _enrolar_k in range(1, _enrolar_steps + 1):
    _enrolar_a = -90 + 45 * _enrolar_k
    _enrolar_f = _enrolar_k / _enrolar_steps
    _enrolar_keys.append((0.25 + 1.75 * _enrolar_f,
                          [_enrolar_pose(_enrolar_a, _enrolar_f), mirrored(_enrolar_pose(_enrolar_a + 180, _enrolar_f))]))
_enrolar_keys.append((2.4, _enrolar_keys[-1][1]))
SIGNS['enrolar'] = {
    'poster': 0.25, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _enrolar_1,
    'keys': _enrolar_keys,
    # A turning arrow on the outer side of each hand.
    'arrows': [{'d': circle_arrow(100, 214, 16, 120, 300, True)},
               {'d': circle_arrow(300, 214, 16, 60, 240, False)}],
    'mirror_second': True,
}
TITLES['enrolar'] = 'Sinal de enrolar em Libras'
