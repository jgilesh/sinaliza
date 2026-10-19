# MEXER: both hands in an open beak (fingers together and curved, the thumb apart from them), palms down
# and fingers pointing down, make small alternating circles in front of the stomach, as if rummaging.
# Several times. (UFSC Signbank MEXER: Beak_open, 2s; INES MEXER agrees.)


def hs_mexer_beak():
    """Open beak: the four fingers together, bent at the knuckles and curved, the thumb opposite them
    with a gap between the thumb tip and the fingertips."""
    shape = {'index': fing(2, 40, 46, 28), 'middle': fing(0, 42, 48, 30), 'ring': fing(-2, 44, 48, 30),
             'pinky': fing(-4, 46, 48, 30)}
    tip = finger_chain('index', shape['index'])[0][3]
    target = vadd(tip, (2.0, 13.0, 4.0))     # below the index tip, toward the wrist: the beak stays open
    shape['thumb'] = solve_thumb(target, pad_to=(0.0, -0.6, 0.8), pref=(10.0, 45.0, 50.0, 12.0, 14.0))
    return shape


_mex_h = hs_mexer_beak()
_MEX_C, _MEX_RX, _MEX_RY = (150, 232), 9, 5


def _mex_pose(angle):
    """Right hand on its circle (angle 0 = outer point, clockwise on screen); palm down, the fingers
    hanging forward and down, the hand turned a little so the curve of the beak shows from the thumb side."""
    a = math.radians(angle)
    at = (_MEX_C[0] - _MEX_RX * math.cos(a), _MEX_C[1] + _MEX_RY * math.sin(a))
    near = math.sin(a)
    return P(at, _mex_h, 'wrist', yaw=-125, pitch=20, roll=-175, scale=1.1 + 0.03 * near, depth=70 + 10 * near,
             pole=(0.4, 1.0, 0.4), ease='linear')


_mex_keys = []
_mex_n = 12
for _mex_k in range(_mex_n + 1):
    _mex_a = 360.0 * 2 * _mex_k / _mex_n
    _mex_keys.append((0.2 + 1.8 * _mex_k / _mex_n, [_mex_pose(_mex_a), mirrored(_mex_pose(_mex_a + 180))]))
_mex_keys = [(0.0, _mex_keys[0][1])] + _mex_keys + [(2.4, _mex_keys[-1][1])]
SIGNS['mexer'] = {
    'poster': 0.2, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _mex_h, 'handshape_view': {'yaw': -80},
    'keys': _mex_keys,
    'arrows': [{'d': circle_arrow(_MEX_C[0], _MEX_C[1] - 30, 14, 200, 340, True)},
               {'d': circle_arrow(400 - _MEX_C[0], _MEX_C[1] - 30, 14, 340, 200, False)}],
    'mirror_second': True,
}
TITLES['mexer'] = 'Sinal de mexer em Libras'
