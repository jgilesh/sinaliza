# VENDER: both hands open in front of the chest, apart, palms forward, the middle finger bent and held
# by the thumb; the middle finger flicks out straight (a fillip), three times, both hands together.
# (UFSC Signbank VENDER: 5m_closed+5m, neutral space; INES VENDER shows a similar flick.)


def hs_vender_hold():
    """Spread hand with the middle finger bent forward and its tip held by the thumb's pad."""
    shape = {'index': fing(12, 0, 4, 2), 'middle': fing(0, 60, 65, 40), 'ring': fing(-8, 0, 4, 2),
             'pinky': fing(-18, 0, 5, 3)}
    shape['thumb'] = pinch_thumb(shape, ('middle',))
    return shape


def hs_vender_open():
    """After the flick: all fingers straight and spread, the thumb out."""
    return {'index': fing(12, 0, 4, 2), 'middle': fing(0, 0, 3, 2), 'ring': fing(-8, 0, 4, 2),
            'pinky': fing(-18, 0, 5, 3), 'thumb': (40.0, 16.0, 6.0, 6.0, 4.0)}


_vender_hold, _vender_open = hs_vender_hold(), hs_vender_open()


def _vender_pose(shape, ease='smooth'):
    """Right hand in front of the chest, out to the side: palm forward, turned a little toward the
    midline so the held middle finger and the thumb on it read."""
    return P((134, 214), shape, 'wrist', yaw=42, pitch=-18, roll=-8, scale=1.12, depth=60, pole=(0.5, 1.0, 0.4),
             ease=ease)


_vender_a, _vender_b = _vender_pose(_vender_hold), _vender_pose(_vender_open, 'out')
_vender_k = lambda p: [p, mirrored(p)]
_vender_keys = [(0.0, _vender_k(_vender_a)), (0.35, _vender_k(_vender_a))]
for _vender_i in range(3):   # flick (fast), then the thumb catches the middle finger again
    _vender_t = 0.35 + 0.5 * _vender_i
    _vender_keys += [(_vender_t + 0.12, _vender_k(_vender_b)), (_vender_t + 0.5, _vender_k(_vender_a))]
_vender_keys.append((2.4, _vender_k(_vender_a)))
SIGNS['vender'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _vender_hold,
    'handshape_view': {'yaw': 60, 'pitch': -25, 'roll': -10},
    'keys': _vender_keys,
    # The middle finger springs up and out: a short arrow above each middle finger.
    'arrows': [{'d': 'M 119 123 Q 122 110 134 104'}, {'d': 'M 281 123 Q 278 110 266 104'}],
    'mirror_second': True,
}
TITLES['vender'] = 'Sinal de vender em Libras'
