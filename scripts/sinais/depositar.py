# DEPOSITAR: index and thumb pinched (as if holding a coin), the other fingers closed, beside the face;
# the hand goes forward and down in an arc and opens, the fingers spread and a little curved, palm
# down, letting the coin go. Once. (UFSC Signbank DEPOSITAR: Baby_beak+5; INES DEPOSITAR.)


def hs_depositar_pinch():
    """Baby beak: the index, bent mostly at the knuckle, meets the thumb pad to pad (a beak); the other three
    fingers folded into the palm."""
    shape = fist({'index': fing(2, 58, 26, 16)})
    shape['thumb'] = pinch_thumb(shape)
    return shape


def hs_depositar_open():
    """Open hand, fingers spread and a little curved, the thumb apart."""
    return {'index': fing(13, 10, 26, 16), 'middle': fing(3, 10, 28, 18), 'ring': fing(-7, 12, 28, 18),
            'pinky': fing(-16, 14, 26, 16), 'thumb': (22.0, 30.0, 20.0, 14.0, 18.0)}


_dep_pinch, _dep_open = hs_depositar_pinch(), hs_depositar_open()
# Beside the face, palm forward and turned so the thumb side faces the viewer: the pinch reads as a ring.
_dep_start = P((130, 122), _dep_pinch, 'pinch', yaw=-70, pitch=0, roll=-10, scale=1.05, depth=45, pole=(0.6, 1.0, 0.45))
# Forward and down, open, palm down: the fingers come toward the viewer and hang down a little.
_dep_end = P((136, 204), _dep_open, 'wrist', yaw=-20, pitch=70, roll=-10, scale=1.12, depth=85, pole=(0.45, 1.0, 0.4),
             via=(104, 168), ease='out')
SIGNS['depositar'] = {
    'poster': 0.2, 'dur': 2.4, 'hands': ['right'], 'handshape': _dep_pinch, 'handshape_view': {'yaw': -70},
    'keys': [(0.0, [_dep_start]), (0.35, [_dep_start]), (1.0, [_dep_end]), (1.9, [_dep_end]),
             (2.4, [dict(_dep_start, via=(120, 190))])],
    'arrows': [{'d': 'M 100 112 Q 82 146 98 186'}],
}
TITLES['depositar'] = 'Sinal de depositar em Libras'
