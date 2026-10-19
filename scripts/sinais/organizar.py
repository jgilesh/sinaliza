# ORGANIZAR: both hands in F (thumb and index tips together in a ring, the other three fingers
# open), palms down, the fingers pointing forward and toward the middle, in front of the chest and
# belly. The hands go up and down in alternation, 3 to 4 times, like arranging things.
# (UFSC Signbank ORGANIZAR and INES ORGANIZAR agree.)
_org_f = hs_F()


def _org_pose(up):
    """Right hand; up = 1 at the top of its stroke, 0 at the bottom. Back of the hand up and a
    little toward the viewer, fingers pointing in toward the middle and away."""
    return P((128, 232 - 16 * up), _org_f, 'wrist', yaw=40, pitch=40, roll=95, scale=1.05, depth=70,
             pole=(0.4, 1.0, 0.4))


_org_up, _org_down = _org_pose(1.0), _org_pose(0.0)
_org_keys = [(0.0, [_org_up, mirrored(_org_down)]), (0.3, [_org_up, mirrored(_org_down)])]
_org_t = 0.3
for _org_k in range(6):                   # three full alternations
    _org_t += 0.3
    _org_r, _org_l = (_org_down, _org_up) if _org_k % 2 == 0 else (_org_up, _org_down)
    _org_keys.append((round(_org_t, 2), [_org_r, mirrored(_org_l)]))
_org_keys.append((round(_org_t + 0.5, 2), _org_keys[-1][1]))
SIGNS['organizar'] = {
    'poster': 0.3, 'dur': round(_org_t + 0.5, 2), 'hands': ['right', 'left'], 'handshape': _org_f,
    'handshape_view': {'yaw': 40}, 'mirror_second': True,
    'keys': _org_keys,
    # Up and down beside each hand, in alternation.
    'arrows': [{'d': 'M 88 206 L 88 238', 'both': True}, {'d': 'M 312 206 L 312 238', 'both': True}],
}
TITLES['organizar'] = 'Sinal de organizar em Libras'
