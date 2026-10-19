# PREOCUPADO: both hands with the index up and its tip curled (1 curvo), the other fingers closed,
# beside the temples, palms turned toward the head; the index fingers make small circles there in
# alternation (one hand at the top of its circle while the other is at the bottom), several times.
# (UFSC Signbank PREOCUPAR and INES PREOCUPAR agree.)
_preoc_1c = hs_1_curved()
_PREOC_C, _PREOC_R = (157.0, 82.0), 6.0


def _preoc_pose(angle):
    """Right hand on its circle (screen angle, clockwise); the curled index tip by the temple."""
    a = math.radians(angle)
    at = (_PREOC_C[0] + _PREOC_R * math.cos(a), _PREOC_C[1] + _PREOC_R * math.sin(a))
    return P(at, _preoc_1c, 'index_tip', yaw=30, pitch=-20, roll=6, scale=1.05, depth=36,
             pole=(0.8, 1.0, 0.45), ease='linear')


_preoc_keys = []
_preoc_n = 16                            # two full circles, 8 steps each
for _preoc_k in range(_preoc_n + 1):
    _preoc_a = -90 + 45 * _preoc_k
    _preoc_keys.append((0.15 + 1.6 * _preoc_k / _preoc_n,
                        [_preoc_pose(_preoc_a), mirrored(_preoc_pose(_preoc_a + 180))]))
_preoc_keys = [(0.0, _preoc_keys[0][1])] + _preoc_keys + [(2.0, _preoc_keys[-1][1])]
SIGNS['preocupado'] = {
    'poster': 0.15, 'dur': 2.0, 'hands': ['right', 'left'], 'handshape': _preoc_1c, 'mirror_second': True,
    'handshape_view': {'yaw': -30, 'pitch': -25},
    'keys': _preoc_keys,
    # Small circles above the fingertips, the right one clockwise, the left mirrored.
    'arrows': [{'d': circle_arrow(_PREOC_C[0], _PREOC_C[1], 14, 200, 340, True)},
               {'d': circle_arrow(400 - _PREOC_C[0], _PREOC_C[1], 14, 340, 200, False)}],
}
TITLES['preocupado'] = 'Sinal de preocupado em Libras'
