# TRABALHAR: both hands in L in front of the chest, the index fingers pointing at each other. The
# wrists turn in alternation, about three times: while one hand comes up with the thumb up (back
# of the hand to the viewer), the other goes down with the thumb down (palm to the viewer).
_trab_l = hs_L()


def _trab_pose(up):
    """Right hand; up=1: thumb up, a little higher; up=0: thumb down, a little lower. In between
    the wrist turns on the forearm's axis, the thumb passing back toward the body."""
    yaw = 15 + 150 * up
    return P((180, 214 - 18 * up), _trab_l, 'index_tip', yaw=yaw, pitch=0, roll=92, scale=1.12, depth=70,
             pole=(0.5, 1.0, 0.4))


_trab_up, _trab_down = _trab_pose(1.0), _trab_pose(0.0)
_trab_keys = [(0.0, [_trab_up, mirrored(_trab_down)]), (0.3, [_trab_up, mirrored(_trab_down)])]
_trab_t = 0.3
for _trab_k in range(6):            # three full alternations
    _trab_t += 0.36
    _trab_r, _trab_l2 = (_trab_down, _trab_up) if _trab_k % 2 == 0 else (_trab_up, _trab_down)
    _trab_keys.append((round(_trab_t, 2), [_trab_r, mirrored(_trab_l2)]))
_trab_keys.append((round(_trab_t + 0.6, 2), _trab_keys[-1][1]))

SIGNS['trabalhar'] = {
    'poster': 0.3, 'dur': round(_trab_t + 0.6, 2), 'hands': ['right', 'left'], 'handshape': _trab_l,
    'handshape_view': {'yaw': 0},
    'keys': _trab_keys,
    # Curved two-headed arrows around each wrist: the hands turn on the forearm's axis.
    'arrows': [{'twist': 0, 'at': 0.3, 'r': (15, 6), 'drop': 12}, {'twist': 1, 'at': 0.3, 'r': (15, 6), 'drop': 12}],
    'mirror_second': True,
}
TITLES['trabalhar'] = 'Sinal de trabalhar em Libras'
