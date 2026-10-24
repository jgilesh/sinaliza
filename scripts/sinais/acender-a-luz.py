# ACENDER A LUZ: the hand, closed with the fingertips gathered on the thumb, is held above the head on the
# dominant side; it opens at once into a loose 5, fingers apart and pointing down toward the head, and
# comes down a little, like the light of a lamp spreading. Once. No contact. (UFSC Signbank ACENDER-LUZ
# "O+5_lax"; the INES video under ACENDER LUZ shows another sign.)


def hs_acender_a_luz_bunch():
    """Fingers bent at the knuckles and middle joints, their tips gathered on the thumb's pad."""
    shape = {'index': fing(2, 52, 58, 34), 'middle': fing(0, 55, 58, 36), 'ring': fing(-1, 58, 56, 36),
             'pinky': fing(-2, 62, 54, 36)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


def hs_acender_a_luz_lax():
    """Open hand, fingers loose: spread and a little curved, thumb open."""
    return {'index': fing(12, 12, 20, 12), 'middle': fing(3, 12, 22, 14), 'ring': fing(-7, 14, 24, 15),
            'pinky': fing(-15, 16, 26, 16), 'thumb': (36.0, 18.0, 8.0, 8.0, 6.0)}


_acender_a_luz_bunch, _acender_a_luz_lax = hs_acender_a_luz_bunch(), hs_acender_a_luz_lax()
_acender_a_luz_pole = (0.7, 1.0, 0.45)
# Above the head on the dominant side, fingers pointing down: closed, the thumb side turned to the viewer
# so the gathered fingertips show in profile...
_acender_a_luz_closed = P((106, 28), _acender_a_luz_bunch, 'wrist', yaw=-70, pitch=0, roll=168, scale=1.05, depth=50,
                          pole=_acender_a_luz_pole)
# ...then open, the back of the hand to the viewer, the loose fingers fanning down toward the head.
_acender_a_luz_open = P((108, 40), _acender_a_luz_lax, 'wrist', yaw=170, pitch=0, roll=162, scale=1.1, depth=50,
                        ease='out', pole=_acender_a_luz_pole)
SIGNS['acender-a-luz'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right'], 'handshape': _acender_a_luz_lax, 'handshape_view': {'yaw': 0},
    'keys': [(0.0, [_acender_a_luz_closed]), (0.4, [_acender_a_luz_closed]), (0.75, [_acender_a_luz_open]),
             (1.9, [_acender_a_luz_open]), (2.4, [dict(_acender_a_luz_closed, ease='smooth')])],
    # Outside the hand: it opens and comes down a little.
    'arrows': [{'d': 'M 76 50 L 76 82'}],
}
TITLES['acender-a-luz'] = 'Sinal de acender a luz em Libras'
