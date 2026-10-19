# VÁRIOS: the support hand lies open in front of the chest, palm up. The signing hand, with the thumb,
# index and middle finger out and the palm down, comes in over the support palm near its wrist and
# slides toward its fingertips and on out to its own side, the fingers wiggling; once.
# (UFSC Signbank VÁRIOS: L2 on B, mão fraca palma; INES VÁRIOS1.)


def hs_varios_L2(lift=(0.0, 0.0)):
    """L2: thumb out sideways, index and middle straight and a little apart, the other two folded.
    `lift` bends the index and the middle a little at the knuckle (for the wiggle)."""
    return fist({'index': fing(6, lift[0], lift[0] * 0.4, 0), 'middle': fing(-5, lift[1], lift[1] * 0.4, 0),
                 'thumb': (48.0, 8.0, 0.0, 4.0, 2.0)})


def hs_varios_flat():
    """Support hand: open, fingers together and nearly straight, thumb a little apart."""
    return {'index': fing(2, 6, 8, 4), 'middle': fing(0, 6, 8, 4), 'ring': fing(-2, 6, 8, 4),
            'pinky': fing(-4, 8, 8, 4), 'thumb': (26.0, 16.0, 8.0, 6.0, 4.0)}


_var_l2, _var_flat = hs_varios_L2(), hs_varios_flat()
_var_wa, _var_wb = hs_varios_L2((28.0, 0.0)), hs_varios_L2((0.0, 28.0))
# Support hand (defined as a right hand, then mirrored): palm up, tipped a little toward the viewer,
# fingers pointing across toward the midline.
_var_base = mirrored(P((160, 250), _var_flat, 'wrist', yaw=-50, pitch=0, roll=92, scale=1.1, depth=70))
# Signing hand: palm down, the fingers pointing across toward the support hand's wrist, the palm turned
# a little away from the viewer so the thumb stands up and the index and middle finger read side by side.
_var_pose = lambda at, shape, **kw: P(at, shape, 'fingertips', yaw=140, pitch=0, roll=90, scale=1.05, depth=80,
                                      pole=(0.4, 1.0, 0.4), **kw)
# In over the support wrist, along the palm to the fingertips and out beyond them; the index and middle
# finger wiggle (bend a little in turn) on the way.
_var_path = [(236, 226), (220, 227), (204, 228), (188, 229), (172, 230), (156, 232), (140, 234), (126, 236)]
_var_shapes = [_var_wa, _var_wb]
_var_keys = [(0.0, [_var_pose(_var_path[0], _var_l2), _var_base]), (0.35, [_var_pose(_var_path[0], _var_l2), _var_base])]
for _var_i, _var_at in enumerate(_var_path[1:], 1):
    _var_keys.append((round(0.35 + 0.13 * _var_i, 2), [_var_pose(_var_at, _var_shapes[_var_i % 2], ease='linear'), _var_base]))
_var_end = _var_pose(_var_path[-1], _var_l2)
_var_keys += [(1.45, [_var_end, _var_base]), (2.0, [_var_end, _var_base]),
              (2.5, [dict(_var_pose(_var_path[0], _var_l2), via=(180, 200)), _var_base])]
SIGNS['varios'] = {
    'poster': 0.35, 'dur': 2.5, 'hands': ['right', 'left'], 'handshape': _var_l2, 'handshape_view': {'yaw': 0},
    'keys': _var_keys,
    'arrows': [{'d': 'M 236 188 Q 186 178 132 192'}],
    'mirror_second': True,
}
TITLES['varios'] = 'Sinal de vários em Libras'
