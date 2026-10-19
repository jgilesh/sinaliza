# APITAR: a pinch (thumb pad on the curled index, the other fingers closed) held at the lips like a
# whistle, palm toward the mouth; the hand makes a small movement down and stays. Cheeks puffed (not
# drawn). (UFSC Signbank APITAR: Baby_beak at the mouth, no contact, down; INES APITAR.)


def hs_apitar_pinch():
    """Baby beak: the index curls toward the palm and the thumb's pad meets its pad; the other three
    fingers folded into the palm."""
    shape = fist({'index': fing(2, 42, 62, 40)})
    shape['thumb'] = pinch_thumb(shape)
    return shape


_api_h = hs_apitar_pinch()


def _api_pose(at, **kw):
    return P(at, _api_h, 'pinch', yaw=200, pitch=-10, roll=40, scale=1.0, depth=30, pole=(0.5, 1.0, 0.45), **kw)


_api_on, _api_down = _api_pose((197, 129)), _api_pose((197, 137))
SIGNS['apitar'] = {
    'poster': 0.0, 'dur': 2.2, 'hands': ['right'], 'handshape': _api_h, 'handshape_view': {'yaw': -50},
    'keys': [(0.0, [_api_on]), (0.4, [_api_on]), (0.7, [_api_down]), (1.7, [_api_down]), (2.2, [_api_on])],
    'arrows': [{'d': 'M 168 136 L 168 158'}],
}
TITLES['apitar'] = 'Sinal de apitar em Libras'
