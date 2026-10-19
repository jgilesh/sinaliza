# SORRIR: L hand lying just under the chin, back of the hand to the viewer: the index runs along the
# line of the chin toward the other side, the thumb stands up beside the jaw. The hand taps up and
# down under the chin a few times, with a smile. (UFSC Signbank SORRIR and INES SORRIR agree.)
_sorrir_l = hs_L()


def _sorrir_pose(dy):
    return P((173, 108 + dy), _sorrir_l, 'thumb_tip', yaw=180, pitch=-10, roll=92, scale=1.0, depth=30,
             pole=(0.5, 1.0, 0.45))


_sorrir_up, _sorrir_down = _sorrir_pose(0), _sorrir_pose(7)
_sorrir_keys = [(0.0, [_sorrir_up]), (0.3, [_sorrir_up])]
for _sorrir_i in range(3):
    _sorrir_keys += [(0.3 + 0.36 * _sorrir_i + 0.18, [_sorrir_down]), (0.3 + 0.36 * _sorrir_i + 0.36, [_sorrir_up])]
_sorrir_keys.append((2.2, [_sorrir_up]))
SIGNS['sorrir'] = {
    'poster': 0.3, 'dur': 2.2, 'hands': ['right'], 'handshape': _sorrir_l,
    'keys': _sorrir_keys,
    'marks': [(228, 145, 80)],
    'arrows': [{'d': 'M 148 118 L 148 142', 'both': True}],
}
TITLES['sorrir'] = 'Sinal de sorrir em Libras'
