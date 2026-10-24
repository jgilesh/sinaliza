# CAIR: the support hand open and a little curved, palm up. The signing hand, index and middle finger
# bent and apart like legs (V curved), comes down in an arc onto it: the fingertips land on the palm and
# the hand turns over (palm up), the bent fingers lying on the support palm, like a person falling. Once.
# (UFSC Signbank CAIR: V curved on the palm of B curved, final contact, supination; INES CAIR1 agrees.)


def hs_cair_v():
    """V curved: index and middle apart, bent at the knuckles and middle joints; the others folded under
    the thumb."""
    shape = fist({'index': fing(14, 30, 50, 30), 'middle': fing(-10, 30, 50, 30)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


def hs_cair_open():
    """Support hand: open, fingers together and a little curved, thumb a little apart."""
    return {'index': fing(2, 10, 16, 10), 'middle': fing(0, 10, 16, 10), 'ring': fing(-2, 10, 16, 10),
            'pinky': fing(-4, 12, 16, 10), 'thumb': (24.0, 18.0, 10.0, 8.0, 6.0)}


_cair_v, _cair_open = hs_cair_v(), hs_cair_open()
# Support hand, defined as a right hand (palm up, fingers toward the midline) and mirrored.
_cair_base = mirrored(P((140, 258), _cair_open, 'wrist', yaw=-50, pitch=0, roll=90, scale=1.1, depth=70))
# Standing: high above the support side, back of the hand to the viewer, the bent legs pointing down.
_cair_up = P((200, 208), _cair_v, 'fingertips', yaw=200, pitch=0, roll=180, scale=1.05, depth=72, pole=(0.35, 1.0, 0.45))
# Landing: the fingertips on the support palm.
_cair_touch = P((236, 240), _cair_v, 'fingertips', yaw=200, pitch=0, roll=150, scale=1.05, depth=74,
                pole=(0.35, 1.0, 0.45), via=(226, 210))
# Fallen: turned over, palm up, the bent fingers lying across the support palm toward the little-finger side.
_cair_down = P((252, 242), _cair_v, 'fingertips', yaw=-40, pitch=0, roll=70, scale=1.05, depth=78,
               pole=(0.35, 1.0, 0.45), ease='out')
SIGNS['cair'] = {
    'poster': 1.2, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _cair_v, 'handshape_view': {'yaw': 25, 'pitch': 25},
    'keys': [(0.0, [_cair_up, _cair_base]), (0.3, [_cair_up, _cair_base]), (0.75, [_cair_touch, _cair_base]),
             (1.2, [_cair_down, _cair_base]), (2.0, [_cair_down, _cair_base]),
             (2.6, [dict(_cair_up, via=(190, 230)), _cair_base])],
    # Down in an arc onto the palm, then the turn over.
    'arrows': [{'d': 'M 180 196 Q 222 176 250 210'}],
    'marks': [(268, 230, 60)],
    'mirror_second': True,
}
TITLES['cair'] = 'Sinal de cair em Libras'
