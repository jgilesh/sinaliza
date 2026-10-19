# CONCORDAR: both hands with the fingers together and bent 90 degrees at the knuckles (B bent),
# palms down, in front of the chin; the fingertips of the two hands touch. The hands move in small
# alternating steps toward the body, the tips meeting twice. (UFSC Signbank CONCORDAR: B_bent,
# double contact on the other hand's fingertips, proximal, alternating; INES CONCORDAR agrees.)


def hs_concordar_bent():
    """B bent at the base: the four fingers straight and together, folded 90 degrees at the
    knuckles; the thumb alongside the index."""
    return {'index': fing(2, 82, 6, 4), 'middle': fing(0, 84, 6, 4), 'ring': fing(-2, 84, 6, 4),
            'pinky': fing(-4, 82, 8, 5), 'thumb': (-10.0, 20.0, 20.0, 8.0, 6.0)}


_concordar_h = hs_concordar_bent()


def _concordar_pose(x, y, k=0.0):
    """Right hand; k = 1 drawn back toward the body (a little higher and smaller)."""
    return P((x - 9 * k, y - 6 * k), _concordar_h, 'fingertips', yaw=110, pitch=-30, roll=0, scale=1.05 - 0.06 * k,
             depth=60 - 18 * k, pole=(0.45, 1.0, 0.4))


_concordar_a, _concordar_b = _concordar_pose(197, 166), _concordar_pose(197, 166, 1.0)
_concordar_keys = [(0.0, [_concordar_a, mirrored(_concordar_a)]), (0.3, [_concordar_a, mirrored(_concordar_a)])]
# Alternating: the right hand draws back toward the body and its tips come in to touch again, then
# the left hand does the same (two touches).
for _concordar_t, (_concordar_r, _concordar_l) in ((0.55, (_concordar_b, _concordar_a)), (0.8, (_concordar_a, _concordar_a)),
                                                    (1.05, (_concordar_a, _concordar_b)), (1.3, (_concordar_a, _concordar_a))):
    _concordar_keys.append((_concordar_t, [_concordar_r, mirrored(_concordar_l)]))
_concordar_keys.append((2.0, [_concordar_a, mirrored(_concordar_a)]))
SIGNS['concordar'] = {
    'poster': 0.3, 'dur': 2.0, 'hands': ['right', 'left'], 'handshape': _concordar_h,
    'handshape_view': {'yaw': 75, 'pitch': -10},
    'keys': _concordar_keys,
    # Small two-headed arrows beside each hand: the hands step back toward the body and in again.
    'arrows': [{'d': 'M 138 172 Q 138 156 150 150', 'both': True}, {'d': 'M 262 172 Q 262 156 250 150', 'both': True}],
    'marks': [(200, 161, 0)],
    'mirror_second': True,
}
TITLES['concordar'] = 'Sinal de concordar em Libras'
