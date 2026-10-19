# ECONOMIZAR: both hands make the "money" shape (the thumb rubbing the tips of the bent fingers), one
# above the other in front of the chest; they circle vertically in alternation, passing each other,
# several times. (UFSC Signbank ECONOMIZAR.)


def hs_economizar_money(on='index'):
    """Money: fingers bent at the knuckles and middle joints, their tips close together; the thumb's
    pad presses on the tip of the index (or the middle finger: the thumb rubs along the tips)."""
    shape = {'index': fing(2, 52, 58, 34), 'middle': fing(0, 55, 58, 36), 'ring': fing(-1, 58, 56, 36),
             'pinky': fing(-2, 62, 54, 36)}
    shape['thumb'] = pinch_thumb(shape, fingers=(on,))
    return shape


_eco_m, _eco_m2 = hs_economizar_money('index'), hs_economizar_money('middle')
_ECO_C, _ECO_R = (160.0, 212.0), 16.0


def _eco_pose(angle, shape):
    """Right hand on its vertical circle (angle 0 = top, clockwise on screen), turned so its thumb side
    faces the viewer: the thumb on the fingertips reads. A little nearer the viewer at the bottom."""
    a = math.radians(angle)
    at = (_ECO_C[0] + 5 * math.sin(a), _ECO_C[1] - _ECO_R * math.cos(a))
    near = (1 - math.cos(a)) / 2
    return P(at, shape, 'wrist', yaw=-55, pitch=0, roll=-5, scale=1.08 + 0.06 * near, depth=60 + 25 * near,
             pole=(0.4, 1.0, 0.4), ease='linear')


_eco_keys = []
_eco_steps = 24                      # three turns, 8 steps each
for _eco_k in range(_eco_steps + 1):
    _eco_ang = 45 * _eco_k
    _eco_sh = _eco_m if _eco_k % 2 == 0 else _eco_m2      # the thumb slides along the fingertips
    # The left hand runs half a turn behind: one hand is up while the other is down.
    _eco_keys.append((round(0.2 + 2.0 * _eco_k / _eco_steps, 3),
                      [_eco_pose(_eco_ang, _eco_sh), mirrored(_eco_pose(_eco_ang + 180, _eco_sh))]))
_eco_keys = [(0.0, _eco_keys[0][1])] + _eco_keys + [(2.6, _eco_keys[-1][1])]
SIGNS['economizar'] = {
    'poster': 0.2, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _eco_m,
    'handshape_view': {'yaw': -85},
    'keys': _eco_keys,
    # On the outer side of each hand: vertical circles, in alternation.
    'arrows': [{'d': circle_arrow(_ECO_C[0] - 2, _ECO_C[1] - 22, 52, 128, 232, True)},
               {'d': circle_arrow(400 - _ECO_C[0] + 2, _ECO_C[1] - 22, 52, 52, -52, False)}],
    'mirror_second': True,
}
TITLES['economizar'] = 'Sinal de economizar em Libras'
