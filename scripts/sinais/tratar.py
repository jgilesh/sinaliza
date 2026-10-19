# TRATAR: both hands open with the fingers together and a little curved (B), palms up, in front of the
# chest; they turn in alternating forward circles, one going up while the other goes down, 2 to 3
# times. (UFSC Signbank TRATAR: B, 2s; INES TRATAR agrees.)


def hs_tratar_b():
    """B, the fingers together and a little curved, thumb open beside them."""
    return {'index': fing(2, 8, 12, 8), 'middle': fing(0, 8, 12, 8), 'ring': fing(-2, 9, 12, 8),
            'pinky': fing(-4, 10, 12, 8), 'thumb': (26.0, 16.0, 8.0, 6.0, 4.0)}


_trat_b = hs_tratar_b()
_TRAT_C = (120, 228)


def _trat_pose(phase):
    """Right hand on its circle. Phase 0 = farthest forward (toward the viewer), 90 = lowest, 180 = back
    near the body, 270 = highest: up near the body, forward at the top, down, back at the bottom."""
    a = math.radians(phase)
    at = (_TRAT_C[0] + 3 * math.sin(a), _TRAT_C[1] + 11 * math.sin(a))
    near = math.cos(a)
    # Palm up and tipped toward the viewer (so the palm shows), fingers toward the middle and a little up.
    return P(at, _trat_b, 'wrist', yaw=-45, pitch=10, roll=72, scale=1.1 + 0.05 * near, depth=68 + 14 * near,
             pole=(0.4, 1.0, 0.4), ease='linear')


_trat_keys = []
_trat_n = 16
for _trat_i in range(_trat_n + 1):
    _trat_p = 270 + 720.0 * _trat_i / _trat_n
    _trat_keys.append((0.2 + 2.0 * _trat_i / _trat_n, [_trat_pose(_trat_p), mirrored(_trat_pose(_trat_p + 180))]))
_trat_keys = [(0.0, _trat_keys[0][1])] + _trat_keys + [(2.6, _trat_keys[-1][1])]
SIGNS['tratar'] = {
    'poster': 0.2, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _trat_b, 'handshape_view': {'yaw': 0},
    'keys': _trat_keys,
    'arrows': [{'d': circle_arrow(_TRAT_C[0] - 26, _TRAT_C[1] - 6, 14, 120, 300, True)},
               {'d': circle_arrow(400 - _TRAT_C[0] + 26, _TRAT_C[1] - 6, 14, 60, 240, False)}],
    'mirror_second': True,
}
TITLES['tratar'] = 'Sinal de tratar em Libras'
