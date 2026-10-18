# PRECISAR: both hands with the fingertips bunched on the thumb ("Money"), in front of the chest and
# apart, palms down; the wrists bend down together, three times.


def hs_precisar_bunch():
    """Fingers bent at the knuckles and middle joints, their tips gathered on the thumb's pad (a
    flattened O); the thumb's pad presses on the index and middle fingertips."""
    shape = {'index': fing(2, 52, 58, 34), 'middle': fing(0, 55, 58, 36), 'ring': fing(-1, 58, 56, 36),
             'pinky': fing(-2, 62, 54, 36)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


_prec_h = hs_precisar_bunch()
_prec_up = P((132, 200), _prec_h, 'wrist', yaw=-165, pitch=45, roll=140, scale=1.1, depth=75, pole=(0.6, 1.0, 0.4))
_prec_down = P((132, 203), _prec_h, 'wrist', yaw=-130, pitch=5, roll=165, scale=1.1, depth=75, pole=(0.6, 1.0, 0.4))
_prec_keys = [(0.0, [_prec_up, mirrored(_prec_up)]), (0.3, [_prec_up, mirrored(_prec_up)])]
for _prec_i in range(3):
    _prec_keys += [(0.3 + 0.44 * _prec_i + 0.2, [_prec_down, mirrored(_prec_down)]),
                   (0.3 + 0.44 * _prec_i + 0.44, [_prec_up, mirrored(_prec_up)])]
_prec_keys.append((2.3, [_prec_up, mirrored(_prec_up)]))
SIGNS['precisar'] = {
    'poster': 0.5, 'dur': 2.3, 'hands': ['right', 'left'], 'handshape': _prec_h,
    'handshape_view': {'yaw': -85},
    'keys': _prec_keys,
    # Beside the fingertips, between the hands: the hands flick down (the wrists bend).
    'arrows': [{'d': 'M 184 204 Q 192 216 186 232'}, {'d': 'M 216 204 Q 208 216 214 232'}],
    'mirror_second': True,
}
TITLES['precisar'] = 'Sinal de precisar em Libras'
