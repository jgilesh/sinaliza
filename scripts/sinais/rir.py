# RIR: L hand under the chin, back of the hand to the viewer: the index lies under the chin pointing to
# the other side, the thumb up along the cheek. The index bends a little and straightens, 3 times,
# with a big smile. (UFSC Signbank RIR: L at the chin; INES RIR.)
_rir_l, _rir_bent = hs_L(), hs_L((30, 65, 40))


def _rir_pose(shape):
    return P((173, 108), shape, 'thumb_tip', yaw=180, pitch=-10, roll=92, scale=1.0, depth=30, pole=(0.5, 1.0, 0.45))


_rir_up, _rir_down = _rir_pose(_rir_l), _rir_pose(_rir_bent)
_rir_keys = [(0.0, [_rir_up]), (0.3, [_rir_up])]
for _rir_i in range(3):
    _rir_keys += [(0.3 + 0.36 * _rir_i + 0.18, [_rir_down]), (0.3 + 0.36 * _rir_i + 0.36, [_rir_up])]
_rir_keys.append((2.2, [_rir_up]))
SIGNS['rir'] = {
    'poster': 0.3, 'dur': 2.2, 'hands': ['right'], 'handshape': _rir_l,
    'keys': _rir_keys,
    'marks': [(214, 138, 0)],
    'arrows': [{'d': 'M 222 164 Q 236 172 248 160', 'both': True}],
}
TITLES['rir'] = 'Sinal de rir em Libras'
