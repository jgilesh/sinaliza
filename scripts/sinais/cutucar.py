# CUTUCAR: the hand with the fingers together and bent 90 degrees at the knuckles (bent B), palm down and
# the bent fingers pointing down, raised in front of the shoulder at face height; it gives short little
# pushes forward, as when poking someone. (UFSC Signbank CUTUCAR: B_bent, neutral space, forward, straight.
# There is no INES video for CUTUCAR.)


def hs_cutucar_bent():
    """B bent at the base: the four fingers straight and together, folded 90 degrees at the knuckles;
    the thumb alongside the index."""
    return {'index': fing(2, 82, 6, 4), 'middle': fing(0, 84, 6, 4), 'ring': fing(-2, 84, 6, 4),
            'pinky': fing(-4, 82, 8, 5), 'thumb': (-18.0, 18.0, 20.0, 8.0, 6.0)}


_cutucar_b = hs_cutucar_bent()
_cutucar_pole = (0.6, 1.0, 0.45)
# Palm down, the knuckles toward the midline (and forward), seen from the little-finger side: the
# 90-degree bend at the knuckles reads in profile.
_cutucar_pose = lambda at, scale, depth, **kw: P(at, _cutucar_b, 'wrist', yaw=110, pitch=-10, roll=90, scale=scale,
                                                 depth=depth, pole=_cutucar_pole, **kw)
_cutucar_back = _cutucar_pose((112, 122), 1.0, 45)
_cutucar_poke = _cutucar_pose((122, 126), 1.08, 65, ease='out')
_cutucar_keys = [(0.0, [_cutucar_back]), (0.3, [_cutucar_back])]
for _cutucar_k in range(3):
    _cutucar_t = 0.3 + 0.4 * _cutucar_k
    _cutucar_keys += [(round(_cutucar_t + 0.15, 2), [_cutucar_poke]),
                      (round(_cutucar_t + 0.4, 2), [dict(_cutucar_back, ease='smooth')])]
_cutucar_keys.append((2.2, [_cutucar_back]))
SIGNS['cutucar'] = {
    'poster': 0.45, 'dur': 2.2, 'hands': ['right'], 'handshape': _cutucar_b, 'handshape_view': {'yaw': -60, 'pitch': -20},
    'keys': _cutucar_keys,
    # Short pushes forward, toward the person poked.
    'arrows': [{'d': 'M 96 96 L 122 102'}],
}
TITLES['cutucar'] = 'Sinal de cutucar em Libras'
