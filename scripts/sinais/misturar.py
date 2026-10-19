# MISTURAR: both hands in a loose bico (fingers together and curved toward the thumb, a little open),
# one above the other in front of the chest, the upper palm down and the lower palm up; the hands turn
# around each other in vertical circles, swapping places, 2 to 3 times, as if stirring ingredients.
# (UFSC Signbank MISTURAR: Flower, 2s; INES MISTURAR1 agrees.)


def hs_misturar_beak():
    """Loose bico: the four fingers together, bent at the knuckles and curved, the thumb opposite them
    with a small gap between the thumb tip and the fingertips."""
    shape = {'index': fing(2, 40, 46, 28), 'middle': fing(0, 42, 48, 30), 'ring': fing(-2, 44, 48, 30),
             'pinky': fing(-4, 46, 48, 30)}
    tip = finger_chain('index', shape['index'])[0][3]
    target = vadd(tip, (2.0, 10.0, 4.0))
    shape['thumb'] = solve_thumb(target, pad_to=(0.0, -0.6, 0.8), pref=(10.0, 45.0, 50.0, 12.0, 14.0))
    return shape


_mist_h = hs_misturar_beak()
_MIST_C, _MIST_RX, _MIST_RY = (200, 212), 6, 20


def _mist_pose(angle):
    """Right hand, its bunched fingertips on a tall ellipse (angle on screen, clockwise; 180 = outer
    side, 270 = top). The fingers point to the middle; the forearm turns so the palm faces down at the
    top and up at the bottom."""
    a = math.radians(angle)
    at = (_MIST_C[0] + _MIST_RX * math.cos(a) - 32, _MIST_C[1] + _MIST_RY * math.sin(a))
    s = -math.sin(a)      # 1 at the top, -1 at the bottom
    return P(at, _mist_h, 'pinch', yaw=15 + 95 * s, pitch=0, roll=90 + 15 * s, scale=1.0, depth=70 + 8 * math.cos(a),
             pole=(0.4, 1.0, 0.4), ease='linear')


_mist_keys = []
_mist_n = 16
for _mist_i in range(_mist_n + 1):
    _mist_a = 270 + 720.0 * _mist_i / _mist_n
    # The left hand is opposite on the ellipse: its right-hand twin sits at the mirrored angle.
    _mist_keys.append((0.2 + 2.0 * _mist_i / _mist_n, [_mist_pose(_mist_a), mirrored(_mist_pose(-_mist_a))]))
_mist_keys = [(0.0, _mist_keys[0][1])] + _mist_keys + [(2.6, _mist_keys[-1][1])]
SIGNS['misturar'] = {
    'poster': 0.2, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _mist_h, 'handshape_view': {'yaw': -60},
    'keys': _mist_keys,
    # Both hands turn clockwise on screen (opposite phases): up on the outer side for the right hand, down
    # on the outer side for the left.
    'arrows': [{'d': circle_arrow(_MIST_C[0] - 86, _MIST_C[1] + 6, 16, 150, 290, True)},
               {'d': circle_arrow(_MIST_C[0] + 86, _MIST_C[1] + 6, 16, 250, 30, True)}],
    'mirror_second': True,
}
TITLES['misturar'] = 'Sinal de misturar em Libras'
