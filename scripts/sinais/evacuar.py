# EVACUAR: A hand (fist, thumb straight up), in front of the upper chest, palm toward the body; it
# moves straight down to the belly, once (cheeks puffed, lips pressed: not drawn).
# (UFSC Signbank EVACUAR: A, para baixo, reto; INES EVACUAR.)


def hs_evacuar_A():
    """A: fist, the thumb straight up along the side of the index, its tip a little above the knuckles."""
    shape = fist()
    shape['thumb'] = solve_thumb((17.0, -44.0, -1.5), pad_to=(-1.0, 0.0, 0.0), point=(0.0, -1.0, 0.0),
                                 pref=(-5.0, 10.0, 20.0, 0.0, 0.0))
    return shape


_evacuar_a = hs_evacuar_A()
# Thumb up, the palm toward the chest, turned a little toward the viewer so the folded fingers and the
# thumb standing beside them read.
_evacuar_pose = lambda at, **kw: P(at, _evacuar_a, 'wrist', yaw=135, pitch=0, roll=0, scale=1.1, depth=kw.pop("depth", 45),
                                   pole=(0.4, 1.0, 0.45), **kw)
_evacuar_top = _evacuar_pose((172, 210))
_evacuar_low = _evacuar_pose((172, 256), depth=60, ease='in')
SIGNS['evacuar'] = {
    'poster': 0.3, 'dur': 2.2, 'hands': ['right'], 'handshape': _evacuar_a, 'handshape_view': {'yaw': -30},
    'keys': [(0.0, [_evacuar_top]), (0.4, [_evacuar_top]), (1.0, [_evacuar_low]), (1.7, [_evacuar_low]),
             (2.2, [_evacuar_top])],
    'arrows': [{'d': 'M 204 206 L 204 256'}],
}
TITLES['evacuar'] = 'Sinal de evacuar em Libras'
