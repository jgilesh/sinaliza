# PREFERIR: the hand comes up beside the head, palm forward, the thumb and index open and apart and
# the other three fingers straight; the thumb and index then close into a ring (like the ASL F).
# Once. (UFSC Signbank PREFERIR: T_open + T [ASL F].)


def hs_preferir_open():
    """Thumb and index open and apart (the index a little curved toward the thumb), the other three
    fingers straight and a little spread."""
    return {'index': fing(6, 30, 18, 10), 'middle': fing(3, 0, 0, 0), 'ring': fing(-6, 0, 0, 0),
            'pinky': fing(-15, 0, 0, 0), 'thumb': (40.0, 14.0, 6.0, 6.0, 4.0)}


_pre_open, _pre_ring = hs_preferir_open(), hs_F()
_pre = lambda at, shape, **kw: P(at, shape, 'wrist', yaw=28, pitch=0, roll=-6, scale=1.08, depth=55,
                                 pole=(0.4, 1.0, 0.5), **kw)
_pre_low = _pre((124, 228), _pre_open)
_pre_head = _pre((110, 142), _pre_open, ease='out')
_pre_shut = _pre((110, 142), _pre_ring)
SIGNS['preferir'] = {
    'poster': 1.0, 'dur': 2.6, 'hands': ['right'], 'handshape': _pre_ring, 'handshape_view': {'yaw': 40},
    'keys': [(0.0, [_pre_low]), (0.2, [_pre_low]), (0.65, [_pre_head]), (0.85, [_pre_head]), (1.1, [_pre_shut]),
             (1.9, [_pre_shut]), (2.6, [dict(_pre_low, ease='smooth')])],
    'arrows': [{'d': 'M 138 68 Q 154 74 152 96'}],
}
TITLES['preferir'] = 'Sinal de preferir em Libras'
