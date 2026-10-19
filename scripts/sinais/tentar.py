# TENTAR: the hand in a beak (fingers together, their tips on the thumb tip) touches the cheek on its
# own side with the fingertips, palm toward the face, and taps it lightly a few times.
# (UFSC Signbank TENTAR: Beak, bochecha; INES TENTAR.)


def hs_tentar_beak():
    """Beak: the four fingers together and bent mostly at the knuckles, their tips gathered on the
    thumb's pad."""
    shape = {'index': fing(2, 52, 34, 22), 'middle': fing(0, 56, 32, 22), 'ring': fing(-2, 60, 30, 20),
             'pinky': fing(-4, 64, 28, 20)}
    shape['thumb'] = pinch_thumb(shape)
    return shape


_tentar_beak = hs_tentar_beak()
# Beside the cheek, the fingertips pointing up and in at it; the palm turned toward the face and a
# little toward the viewer, so the fingertips gathered on the thumb read.
_tentar_pose = lambda at, **kw: P(at, _tentar_beak, 'pinch', yaw=70, pitch=0, roll=45, scale=0.9, depth=35,
                                  pole=(0.6, 1.0, 0.45), **kw)
_tentar_on = _tentar_pose((175, 113))
_tentar_off = _tentar_pose((168, 115))
_tentar_keys = [(0.0, [_tentar_off]), (0.3, [_tentar_off])]
for _tentar_k in range(3):                 # three light taps
    _tentar_t = 0.3 + 0.36 * _tentar_k
    _tentar_keys += [(round(_tentar_t + 0.16, 2), [_tentar_on]), (round(_tentar_t + 0.36, 2), [_tentar_off])]
_tentar_keys.append((2.2, [_tentar_off]))
SIGNS['tentar'] = {
    'poster': 0.46, 'dur': 2.2, 'hands': ['right'], 'handshape': _tentar_beak, 'handshape_view': {'yaw': 60},
    'keys': _tentar_keys,
    'marks': [(179, 115, 75)],
    'arrows': [{'d': 'M 139 77 L 154 82', 'both': True}],
}
TITLES['tentar'] = 'Sinal de tentar em Libras'
