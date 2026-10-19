# FALTAR: the support hand lies open in front of the chest, palm up. The signing hand, fingertips
# gathered on the thumb (beak), touches the support palm with the fingertips and rises opening the
# fingers, twice. (UFSC Signbank FALTAR: Flower, mão fraca palma; INES FALTAR1.)


def hs_faltar_beak():
    """Beak: the four fingers together and bent mostly at the knuckles, their tips gathered on the
    thumb's pad."""
    shape = {'index': fing(2, 52, 34, 22), 'middle': fing(0, 56, 32, 22), 'ring': fing(-2, 60, 30, 20),
             'pinky': fing(-4, 64, 28, 20)}
    shape['thumb'] = pinch_thumb(shape)
    return shape


def hs_faltar_open():
    """Opened beak (flower): fingers apart and a little curved, the thumb away from them."""
    return {'index': fing(12, 18, 16, 10), 'middle': fing(3, 18, 16, 10), 'ring': fing(-6, 20, 16, 10),
            'pinky': fing(-15, 22, 16, 10), 'thumb': (30.0, 30.0, 20.0, 8.0, 6.0)}


def hs_faltar_flat():
    """Support hand: open, fingers together and nearly straight, thumb a little apart."""
    return {'index': fing(2, 6, 8, 4), 'middle': fing(0, 6, 8, 4), 'ring': fing(-2, 6, 8, 4),
            'pinky': fing(-4, 8, 8, 4), 'thumb': (26.0, 16.0, 8.0, 6.0, 4.0)}


_faltar_beak, _faltar_open, _faltar_flat = hs_faltar_beak(), hs_faltar_open(), hs_faltar_flat()
# Support hand (defined as a right hand, then mirrored): palm up, tipped a little toward the viewer,
# fingers pointing across toward the midline.
_faltar_base = mirrored(P((160, 248), _faltar_flat, 'wrist', yaw=-50, pitch=0, roll=92, scale=1.1, depth=70))
# Signing hand: fingertips down onto the palm, seen from the thumb side so the gathered fingertips read.
_faltar_pose = lambda at, shape, **kw: P(at, shape, 'fingertips', yaw=kw.pop('yaw', 60), pitch=kw.pop('pitch', 0), roll=180, scale=1.05,
                                         depth=kw.pop('depth', 72), pole=(0.9, 0.6, 0.5), **kw)
_faltar_above = _faltar_pose((196, 220), _faltar_beak)
_faltar_touch = _faltar_pose((196, 233), _faltar_beak, ease='in')
# Opened: the palm turns toward the viewer and the fingers tip forward a little, so the spread fingers
# read and the hand stays below the chin.
_faltar_up = _faltar_pose((194, 218), _faltar_open, yaw=20, pitch=25, depth=85, ease='out')
SIGNS['faltar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _faltar_beak, 'handshape_view': {'yaw': 60},
    'keys': [(0.0, [_faltar_above, _faltar_base]), (0.3, [_faltar_touch, _faltar_base]), (0.65, [_faltar_up, _faltar_base]),
             (0.95, [_faltar_touch, _faltar_base]), (1.3, [_faltar_up, _faltar_base]), (1.9, [_faltar_up, _faltar_base]),
             (2.4, [_faltar_above, _faltar_base])],
    'marks': [(189, 233, -70)],
    # Up from the palm (opening) and down again, twice.
    'arrows': [{'d': 'M 252 226 L 252 200', 'both': True}],
    'mirror_second': True,
}
TITLES['faltar'] = 'Sinal de faltar em Libras'
