# DUVIDAR: both hands with the index straight (1), horizontal, pointing at each other, palms down, just
# below the chin. Alternately, each index brushes forward under the chin and drops away while the other
# comes up, three or four times. (UFSC Signbank DUVIDAR: 1/1, chin, continuous contact, forward,
# repeated, alternating. The INES DUVIDAR video shows a one-handed variant.)

_duv_one = HANDSHAPES['1']()


def _duv_pose(state):
    """Right hand (the left mirrors it). The index points across toward the midline, palm down, the back
    of the hand tipped toward the viewer so the index reads along the top of the fist."""
    at, scale, depth = {'low': ((186, 200), 1.05, 55), 'up': ((203, 143), 1.05, 45),
                        'fwd': ((198, 155), 1.16, 75), 'drop': ((189, 180), 1.12, 70)}[state]
    return P(at, _duv_one, 'index_tip', yaw=120, pitch=0, roll=90, scale=scale, depth=depth,
             pole=(0.35, 1.0, 0.4), ease='linear')


# One cycle = low, up under the chin (contact), forward, dropping; the left hand is half a cycle behind.
_duv_cycle = ['low', 'up', 'fwd', 'drop']
_duv_keys = []
_duv_step = 0.165
for _duv_i in range(13):   # ends where it starts, so the loop is seamless
    _duv_r = _duv_cycle[_duv_i % 4]
    _duv_l = _duv_cycle[(_duv_i + 2) % 4]
    _duv_keys.append((0.2 + _duv_step * _duv_i, [_duv_pose(_duv_r), mirrored(_duv_pose(_duv_l))]))
_duv_keys = [(0.0, _duv_keys[0][1])] + _duv_keys + [(2.4, _duv_keys[-1][1])]
SIGNS['duvidar'] = {
    'poster': 0.37, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _duv_one,
    'keys': _duv_keys,
    # Outside each hand: up to the chin, then forward and down, alternating.
    'arrows': [{'d': 'M 108 206 Q 98 166 124 146'}, {'d': 'M 292 206 Q 302 166 276 146'}],
    'marks': [(177, 137, -60)],
    'mirror_second': True,
}
TITLES['duvidar'] = 'Sinal de duvidar em Libras'
