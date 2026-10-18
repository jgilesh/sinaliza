# SORTE: both hands in L at shoulder height, palms toward the body, the index fingers pointing in and
# up toward the neck, the thumbs up; the wrists rock a little, two or three times. No contact.
# (INES and UFSC Signbank agree.)
_sorte_l = hs_L()


def _sorte_pose(roll, dy=0):
    return P((128, 210 + dy), _sorte_l, 'wrist', yaw=160, pitch=0, roll=roll, scale=1.1, depth=55, pole=(0.5, 1.0, 0.4))


_sorte_keys = [(0.0, [_sorte_pose(56), mirrored(_sorte_pose(56))]), (0.3, [_sorte_pose(56), mirrored(_sorte_pose(56))])]
for _k in range(3):
    _a, _b = _sorte_pose(46, 4), _sorte_pose(64, -2)
    _sorte_keys += [(0.3 + 0.4 * _k + 0.2, [_a, mirrored(_a)]), (0.3 + 0.4 * _k + 0.4, [_b, mirrored(_b)])]
_sorte_keys += [(2.2, [_sorte_pose(56), mirrored(_sorte_pose(56))])]
SIGNS['sorte'] = {
    'poster': 0.0, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _sorte_l, 'mirror_second': True,
    'keys': _sorte_keys,
    'arrows': [{'d': 'M 96 154 Q 88 174 96 194', 'both': True}, {'d': 'M 304 154 Q 312 174 304 194', 'both': True}],
}
TITLES['sorte'] = 'Sinal de sorte em Libras'
