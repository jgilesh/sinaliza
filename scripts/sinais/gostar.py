# GOSTAR: open hand, fingers together and the thumb apart, the palm flat on the middle of the
# chest; it rubs the chest in small circles, repeated. Back of the hand to the viewer, fingers
# pointing across the body (toward the signer's left), thumb up. (UFSC Signbank GOSTAR, INES.)


def hs_gostar_open():
    """Open hand: four fingers straight and close together, the thumb well apart from them."""
    return {'index': fing(3, 0, 2, 1), 'middle': fing(0, 0, 2, 1), 'ring': fing(-3, 0, 2, 1),
            'pinky': fing(-6, 0, 3, 2), 'thumb': (44.0, 14.0, 6.0, 6.0, 4.0)}


_gostar_hs = hs_gostar_open()
_GOSTAR_C = (170.0, 224.0)   # wrist at the circle's centre
_GOSTAR_R = 6.0


def _gostar_pose(angle):
    a = math.radians(angle)
    at = (_GOSTAR_C[0] + _GOSTAR_R * math.cos(a), _GOSTAR_C[1] + _GOSTAR_R * math.sin(a))
    return P(at, _gostar_hs, 'wrist', yaw=180, pitch=8, roll=82, scale=1.2, depth=22,
             pole=(0.6, 1.0, 0.2), ease='linear')


_gostar_keys = [(0.0, [_gostar_pose(-90)])]
_gostar_steps = 16                     # two full circles, 8 steps each
for _gostar_k in range(1, _gostar_steps + 1):
    _gostar_keys.append((0.3 + 1.6 * _gostar_k / _gostar_steps, [_gostar_pose(-90 + 45 * _gostar_k)]))
_gostar_keys.append((2.4, [dict(_gostar_pose(-90), ease='smooth')]))

SIGNS['gostar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right'], 'handshape': _gostar_hs,
    'keys': _gostar_keys,
    # The palm rests on the chest the whole time: one contact burst below the hand.
    'marks': [(206, 246, 180)],
    # A small circle just above the fingers: the rubbing.
    'arrows': [{'d': circle_arrow(222, 175, 9, 150, 80, True)}],
}
TITLES['gostar'] = 'Sinal de gostar em Libras'
