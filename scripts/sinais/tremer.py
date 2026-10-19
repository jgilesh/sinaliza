# TREMER: both hands open in 5 (fingers straight and spread), palms down, in front of the chest and
# belly; the hands shake with short, quick jolts while they drift a little out to the sides.
# (UFSC Signbank TREMER: 5/5. The INES TREMER1 video shows a variant: fists shaking beside the
# shoulders, as with cold.)

_tremer_5 = hs_5()
_tremer_pole = (0.4, 1.0, 0.4)


def _tremer_pose(k, n):
    """Palm down, fingers forward and toward the midline, the back of the hand tilted up toward the
    viewer so the spread fingers read; k = step of the shake (alternating), drifting outward."""
    s = 1 if k % 2 == 0 else -1
    drift = 10 * k / n
    return P((120 - drift, 222 + 2 * s), _tremer_5, 'wrist', yaw=135, pitch=40, roll=108 + 7 * s, scale=1.08,
             depth=62, pole=_tremer_pole, ease='linear')


_tremer_still = P((120, 222), _tremer_5, 'wrist', yaw=135, pitch=40, roll=108, scale=1.08, depth=62, pole=_tremer_pole)
_tremer_keys = [(0.0, [_tremer_still, mirrored(_tremer_still)]), (0.3, [_tremer_still, mirrored(_tremer_still)])]
_TREMER_N = 14
for _tremer_k in range(_TREMER_N + 1):
    _tremer_p = _tremer_pose(_tremer_k, _TREMER_N)
    _tremer_keys.append((round(0.35 + 0.08 * _tremer_k, 2), [_tremer_p, mirrored(_tremer_p)]))
_tremer_end = dict(_tremer_pose(_TREMER_N, _TREMER_N), roll=100, at=(110, 222), ease='smooth')
_tremer_keys += [(1.7, [_tremer_end, mirrored(_tremer_end)]), (2.0, [_tremer_end, mirrored(_tremer_end)]),
                 (2.4, [_tremer_still, mirrored(_tremer_still)])]
SIGNS['tremer'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _tremer_5,
    'keys': _tremer_keys,
    # Zigzag under each hand, out to the side: a quick shake.
    'arrows': [{'d': 'M 156 268 L 148 262 L 140 270 L 132 262 L 124 270 L 114 264'},
               {'d': 'M 244 268 L 252 262 L 260 270 L 268 262 L 276 270 L 286 264'}],
    'mirror_second': True,
}
TITLES['tremer'] = 'Sinal de tremer em Libras'
