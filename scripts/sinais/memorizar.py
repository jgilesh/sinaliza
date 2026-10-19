# MEMORIZAR: the hand comes in open and closes on the forehead, the fingertips gathered on the thumb
# (a beak) against the side of the forehead, the fingertips pointing down onto it; it holds there a
# moment, as if keeping something in the head, then moves away. Once. (UFSC Signbank MEMORIZAR.)


def hs_memorizar_open():
    """Relaxed open hand: fingers a little spread and a little curved, thumb out."""
    return {'index': fing(10, 8, 14, 9), 'middle': fing(2, 8, 14, 9), 'ring': fing(-6, 10, 14, 9),
            'pinky': fing(-13, 12, 15, 10), 'thumb': (34.0, 22.0, 10.0, 8.0, 8.0)}


def hs_memorizar_beak():
    """Beak: fingers bent at the knuckles and middle joints, their tips gathered on the thumb's pad."""
    shape = {'index': fing(2, 52, 58, 34), 'middle': fing(0, 55, 58, 36), 'ring': fing(-1, 58, 56, 36),
             'pinky': fing(-2, 62, 54, 36)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


_mem_open, _mem_beak = hs_memorizar_open(), hs_memorizar_beak()
_mem = lambda at, shape, anchor='fingertips', **kw: P(at, shape, anchor, yaw=20, pitch=0, roll=96, scale=1.0, depth=40,
                                                      pole=(0.25, 1.0, 0.8), **kw)
_mem_side = P((114, 150), _mem_open, 'wrist', yaw=20, pitch=0, roll=-8, scale=1.0, depth=45, pole=(0.25, 1.0, 0.8))
_mem_near = _mem((152, 64), _mem_open, ease='out', via=(110, 100))
_mem_on = _mem((176, 70), _mem_beak)
_mem_off = _mem((104, 84), _mem_beak, 'wrist', ease='smooth')
SIGNS['memorizar'] = {
    'poster': 1.0, 'dur': 2.6, 'hands': ['right'], 'handshape': _mem_beak, 'handshape_view': {'yaw': 20, 'pitch': -30},
    'keys': [(0.0, [_mem_side]), (0.2, [_mem_side]), (0.6, [_mem_near]), (0.85, [_mem_on]), (1.6, [_mem_on]),
             (2.0, [_mem_off]), (2.6, [dict(_mem_side, ease='smooth', via=(96, 120))])],
    'marks': [(194, 66, 60)],
    'arrows': [{'d': 'M 92 62 Q 112 34 146 40'}],
}
TITLES['memorizar'] = 'Sinal de memorizar em Libras'
