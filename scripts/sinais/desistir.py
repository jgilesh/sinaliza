# DESISTIR: the fingertips, bunched together on the thumb, touch the side of the forehead; the hand
# then comes down in an arc to the front of the chest, opening on the way, and ends palm down with the
# fingers hanging loose. Once. (UFSC Signbank DESISTIR "Flower", INES DESISTIR.)


def hs_desistir_bunch():
    """Fingers bent at the knuckles and middle joints, their tips gathered on the thumb's pad."""
    shape = {'index': fing(2, 52, 58, 34), 'middle': fing(0, 55, 58, 36), 'ring': fing(-1, 58, 56, 36),
             'pinky': fing(-2, 62, 54, 36)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


def hs_desistir_open():
    """Open hand, fingers loose and a little apart, slightly curved, thumb open."""
    return {'index': fing(10, 10, 16, 10), 'middle': fing(2, 10, 16, 10), 'ring': fing(-6, 12, 18, 11),
            'pinky': fing(-14, 14, 20, 12), 'thumb': (14.0, 16.0, 8.0, 8.0, 6.0)}


_desistir_bunch, _desistir_open = hs_desistir_bunch(), hs_desistir_open()
# Bunched fingertips on the side of the forehead, the hand beside the head pointing at it, the palm
# turned to the viewer and a little down: the fingertips gathered on the thumb read.
_desistir_on = P((170, 84), _desistir_bunch, 'index_tip', yaw=0, pitch=0, roll=90, scale=0.95, depth=40,
                 pole=(0.6, 1.0, 0.45))
# In front of the chest, palm down, fingers hanging: the back of the hand to the viewer.
_desistir_off = P((150, 196), _desistir_open, 'wrist', yaw=-168, pitch=3, roll=177, scale=1.05, depth=70,
                  via=(104, 120), ease='out', pole=(0.5, 1.0, 0.45))
_desistir_back = dict(_desistir_on, via=(110, 130), ease='smooth')
SIGNS['desistir'] = {
    'poster': 0.4, 'dur': 2.6, 'hands': ['right'], 'handshape': _desistir_bunch, 'handshape_view': {'yaw': -85},
    'keys': [(0.0, [_desistir_on]), (0.45, [_desistir_on]), (1.15, [_desistir_off]), (2.0, [_desistir_off]),
             (2.6, [_desistir_back])],
    'marks': [(187, 74, 80)],
    'arrows': [{'d': 'M 128 70 Q 84 100 104 168'}],
}
TITLES['desistir'] = 'Sinal de desistir em Libras'
