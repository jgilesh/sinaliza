# PREJUDICAR: both hands in a beak (fingertips gathered on the thumb) meet tip to tip in front of the
# chin; they then move down and apart, opening into spread hands, palms down, once.
# (UFSC Signbank PREJUDICAR: Beak+Beak_open_spread, both hands; INES PREJUDICAR shows another variant.)


def hs_prejudicar_beak():
    """Beak: the four fingers together and bent mostly at the knuckles, their tips gathered on the
    thumb's pad."""
    shape = {'index': fing(2, 52, 34, 22), 'middle': fing(0, 56, 32, 22), 'ring': fing(-2, 60, 30, 20),
             'pinky': fing(-4, 64, 28, 20)}
    shape['thumb'] = pinch_thumb(shape)
    return shape


def hs_prejudicar_open():
    """Opened beak: fingers spread and a little curved, the thumb apart."""
    return {'index': fing(14, 10, 14, 8), 'middle': fing(3, 10, 14, 8), 'ring': fing(-8, 12, 14, 8),
            'pinky': fing(-18, 14, 14, 8), 'thumb': (36.0, 22.0, 12.0, 8.0, 6.0)}


_prej_beak, _prej_open = hs_prejudicar_beak(), hs_prejudicar_open()
# Start: fingertips meeting at the midline below the chin, the fingers pointing up and in at each other;
# the palms turned toward each other and partly toward the viewer, so the fingertips gathered on each
# thumb read.
_prej_meet = P((197, 174), _prej_beak, 'pinch', yaw=60, roll=55, scale=1.0, depth=55, pole=(0.4, 1.0, 0.45))
# End: low and apart, open with the fingers spread, palms down, the backs of the hands to the viewer.
_prej_end = P((148, 222), _prej_open, 'wrist', yaw=160, pitch=40, roll=170, scale=1.05, depth=72,
              via=(170, 196), ease='out', pole=(0.4, 1.0, 0.45))
_prej_back = dict(_prej_meet, via=(160, 200), ease='smooth')
_prej_keys = [(0.0, _prej_meet), (0.4, _prej_meet), (1.05, _prej_end), (1.9, _prej_end), (2.5, _prej_back)]
SIGNS['prejudicar'] = {
    'poster': 0.2, 'dur': 2.5, 'hands': ['right', 'left'], 'handshape': _prej_beak, 'handshape_view': {'yaw': 60},
    'keys': [(t, [k, mirrored(k)]) for t, k in _prej_keys],
    'arrows': [{'trail': 0, 'from': 0.4, 'to': 1.05, 'offset': (-22, -4), 'trim': 0.12},
               {'trail': 1, 'from': 0.4, 'to': 1.05, 'offset': (22, -4), 'trim': 0.12}],
    'mirror_second': True,
}
TITLES['prejudicar'] = 'Sinal de prejudicar em Libras'
