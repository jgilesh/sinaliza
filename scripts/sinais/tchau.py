# TCHAU: open hand (5), palm forward, raised beside the head on the signer's right; it waves from
# side to side (the wrist turns on screen), three times. No contact. (INES and UFSC Signbank agree.)
_tchau_5 = hs_5()


def _tchau_pose(roll):
    return P((114, 166), _tchau_5, 'wrist', yaw=-8, pitch=0, roll=roll, scale=1.1, depth=55, pole=(0.5, 1.0, 0.4))


_tchau_keys = [(0.0, [_tchau_pose(-4)]), (0.25, [_tchau_pose(-4)])]
for _k in range(3):
    _tchau_keys += [(0.25 + 0.5 * _k + 0.25, [_tchau_pose(-22)]), (0.25 + 0.5 * _k + 0.5, [_tchau_pose(6)])]
_tchau_keys += [(2.1, [_tchau_pose(-4)]), (2.6, [_tchau_pose(-4)])]
SIGNS['tchau'] = {
    'poster': 0.0, 'dur': 2.6, 'hands': ['right'], 'handshape': _tchau_5,
    'keys': _tchau_keys,
    # A two-headed arc above the fingertips: the hand swings from side to side.
    'arrows': [{'d': 'M 84 70 Q 112 54 140 68', 'both': True}],
}
TITLES['tchau'] = 'Sinal de tchau em Libras'
