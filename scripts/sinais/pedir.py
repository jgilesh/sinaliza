# PEDIR: both hands open (B), fingertips almost touching in front of the chest, palms toward the body;
# the hands close into A (fist, thumb up) while they move a little apart and forward, ending with the
# thumbs up, palms facing forward and toward each other. Once. (UFSC Signbank PEDIR: B+A, both hands;
# INES PEDIR1 shows a one-handed variant.)


def hs_pedir_a():
    """A: fist, the thumb straight up along the side of the index, its tip above the knuckles."""
    shape = fist()
    shape['thumb'] = solve_thumb((17.0, -44.0, -1.5), pad_to=(-1.0, 0.0, 0.0), point=(0.0, -1.0, 0.0),
                                 pref=(-5.0, 10.0, 20.0, 0.0, 0.0))
    return shape


_pedir_b, _pedir_a = hs_B(), hs_pedir_a()
# Open: back of the hand to the viewer, fingers pointing across toward the other hand, thumb up.
_pedir_open = P((190, 206), _pedir_b, 'fingertips', yaw=-155, pitch=-5, roll=60, scale=1.05, depth=55,
                pole=(0.4, 1.0, 0.4))
# Closed: thumbs up, palm forward (the thumb on the inner side reads against the fist), a little apart
# and forward.
_pedir_closed = P((162, 222), _pedir_a, 'wrist', yaw=-15, pitch=0, roll=2, scale=1.12, depth=80,
                  pole=(0.4, 1.0, 0.4))
_pedir_k = lambda p: [p, mirrored(p)]
SIGNS['pedir'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _pedir_a,
    'keys': [(0.0, _pedir_k(_pedir_open)), (0.35, _pedir_k(_pedir_open)), (0.95, _pedir_k(_pedir_closed)),
             (1.9, _pedir_k(_pedir_closed)), (2.4, _pedir_k(_pedir_open))],
    # Apart and forward, below the hands.
    'arrows': [{'d': 'M 186 258 Q 170 266 150 262'}, {'d': 'M 214 258 Q 230 266 250 262'}],
    'mirror_second': True,
}
TITLES['pedir'] = 'Sinal de pedir em Libras'
