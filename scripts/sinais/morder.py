# MORDER: clawed hand (fingers spread and bent, the thumb apart below them, like an open jaw) in front
# of the chest, palm down; the fingers close all at once onto the thumb with a small push forward, like
# a mouth biting. Once. (UFSC Signbank MORDER: 5_claw closing; INES MORDER agrees.)


def hs_morder_claw():
    """Open jaw: the four fingers a little apart, bent at every joint; the thumb opposite them, bent."""
    return {'index': fing(8, 25, 55, 35), 'middle': fing(2, 25, 58, 38), 'ring': fing(-5, 27, 58, 38),
            'pinky': fing(-12, 30, 56, 36), 'thumb': (30.0, 45.0, 40.0, 25.0, 30.0)}


def hs_morder_shut():
    """Closed jaw: the fingers bent further, their tips pressed on the thumb's pad."""
    shape = {'index': fing(4, 50, 75, 45), 'middle': fing(1, 52, 75, 45), 'ring': fing(-2, 54, 74, 45),
             'pinky': fing(-5, 58, 72, 44)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


_morder_open, _morder_shut = hs_morder_claw(), hs_morder_shut()
# Palm down and fingers forward, seen a little from below and from the thumb side: the fingers on top,
# the thumb under them, the opening between them like a jaw.
_morder_pose = lambda at, shape, scale, depth, **kw: P(at, shape, 'wrist', yaw=60, pitch=20, roll=60, scale=scale,
                                                        depth=depth, pole=(0.4, 1.0, 0.4), **kw)
_morder_a = _morder_pose((138, 204), _morder_open, 1.1, 50)
_morder_b = _morder_pose((146, 212), _morder_shut, 1.18, 75, ease='in')
SIGNS['morder'] = {
    'poster': 0.4, 'dur': 2.2, 'hands': ['right'], 'handshape': _morder_open, 'handshape_view': {'yaw': -60, 'pitch': -10},
    'keys': [(0.0, [_morder_a]), (0.4, [_morder_a]), (0.62, [_morder_b]), (1.5, [_morder_b]),
             (2.2, [dict(_morder_a, ease='smooth')])],
    # Over the fingertips, curving down onto the thumb: the jaw shuts.
    'arrows': [{'d': 'M 174 158 Q 206 158 214 186'}],
}
TITLES['morder'] = 'Sinal de morder em Libras'
