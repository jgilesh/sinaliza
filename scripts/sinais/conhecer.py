# CONHECER: hand in 4 (four fingers straight and apart, thumb folded on the palm), fingers up, palm
# toward the face; the side of the index taps the chin on the signing side, 2 times. (UFSC Signbank
# CONHECER: 4, chin, double contact; INES CONHECER agrees.)


def hs_conhecer_4():
    """4: index, middle, ring and little fingers straight and spread; the thumb folded across the palm,
    its pad on the palm below the ring finger."""
    shape = {'index': fing(10, 0, 2, 1), 'middle': fing(2, 0, 2, 1), 'ring': fing(-7, 0, 2, 1),
             'pinky': fing(-16, 0, 3, 2)}
    target = (-3.0, -20.0, PALM_HALF_THICKNESS + seg_radius('thumb', 2) + 0.6)
    shape['thumb'] = solve_thumb(target, pad_to=(0.0, 0.0, -1.0), point=(-1.0, -0.6, 0.0),
                                 pref=(-15.0, 50.0, 60.0, 30.0, 30.0), w_point=120.0)
    return shape


_conhecer_4 = hs_conhecer_4()
# Beside the chin on the signing side, fingers up, the palm turned toward the chin and a little toward
# the viewer, so the four spread fingers read; the index's side rests on the chin.
_conhecer = lambda x, y: P((x, y), _conhecer_4, 'wrist', yaw=50, pitch=0, roll=-6, scale=0.95, depth=40,
                           pole=(0.6, 1.0, 0.45))
_conhecer_on, _conhecer_off = _conhecer(181, 188), _conhecer(167, 192)
_conhecer_keys = [(0.0, [_conhecer_off]), (0.3, [_conhecer_off])]
for _conhecer_k in range(2):
    _conhecer_t = 0.3 + 0.5 * _conhecer_k
    _conhecer_keys += [(_conhecer_t + 0.2, [dict(_conhecer_on, ease='in')]), (_conhecer_t + 0.5, [_conhecer_off])]
_conhecer_keys.append((2.0, [_conhecer_off]))
SIGNS['conhecer'] = {
    'poster': 0.5, 'dur': 2.0, 'hands': ['right'], 'handshape': _conhecer_4, 'handshape_view': {'yaw': 10},
    'keys': _conhecer_keys,
    'marks': [(196, 150, 60)],
    'arrows': [{'d': 'M 132 140 L 148 143', 'both': True}],
}
TITLES['conhecer'] = 'Sinal de conhecer em Libras'
