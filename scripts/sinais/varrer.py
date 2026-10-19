# VARRER: both hands closed (S), one above the other as if holding a broom handle: the signing hand at
# chest height, the other lower down; the palms toward the body. Both hands swing together from side to
# side, as when sweeping, a few times. No contact. (UFSC Signbank VARRER; INES VARRER agrees.)
_varrer_s = hs_S()


def _varrer_pose(x, y, roll, depth):
    """A fist around a vertical handle: palm toward the body, knuckles toward the other side; turned a
    little so the thumb wrapped on top and the curled fingers show."""
    return P((x, y), _varrer_s, 'wrist', yaw=-110, pitch=20, roll=roll, scale=1.05, depth=depth, pole=(0.35, 1.0, 0.45),
             ease='smooth')


def _varrer_pair(dx):
    """Both hands, shifted sideways by dx (the lower hand, near the broom's head, swings more)."""
    upper = _varrer_pose(156 + dx * 0.5, 196, 80 - dx * 0.4, 50)
    lower = mirrored(_varrer_pose(400 - (196 + dx), 248, 80 + dx * 0.4, 60))
    return [upper, lower]


_varrer_keys = [(0.0, _varrer_pair(0)), (0.25, _varrer_pair(0))]
for _varrer_k, _varrer_dx in enumerate((-20, 20, -20, 20)):
    _varrer_keys.append((0.5 + 0.35 * _varrer_k, _varrer_pair(_varrer_dx)))
_varrer_keys += [(1.85, _varrer_pair(0)), (2.2, _varrer_pair(0))]
SIGNS['varrer'] = {
    'poster': 0.5, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _varrer_s, 'handshape_view': {'yaw': -20},
    'keys': _varrer_keys,
    # Side to side, below the lower hand.
    'arrows': [{'d': 'M 150 276 Q 180 286 212 276', 'both': True}],
    'mirror_second': True,
}
TITLES['varrer'] = 'Sinal de varrer em Libras'
