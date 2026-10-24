# ESTAR: both hands in A (fist, thumb straight up beside it) in front of the chest, the thumb tips
# meeting; the fists tip forward and go down and apart in an arc, ending at waist height with the
# thumbs pointing down. Once. (UFSC Signbank ESTAR: A, contact on the other thumb, arc down; INES
# ESTAR agrees.)


def hs_estar_a():
    """A: fist, the thumb straight up along the side of the index, its tip above the knuckles."""
    shape = fist()
    shape['thumb'] = solve_thumb((17.0, -44.0, -1.5), pad_to=(-1.0, 0.0, 0.0), point=(0.0, -1.0, 0.0),
                                 pref=(-5.0, 10.0, 20.0, 0.0, 0.0))
    return shape


_estar_a = hs_estar_a()
# Thumbs up, palm forward and turned a little outward so the thumb (on the inner side) reads against
# the fist; the thumb tips meet in front of the chest.
_estar_up = P((195, 198), _estar_a, 'thumb_tip', yaw=-30, pitch=0, roll=4, scale=1.1, depth=60, pole=(0.4, 1.0, 0.4))
# Tipped forward and down: the back of the fist to the viewer, thumbs down, apart at the waist.
_estar_down = P((160, 266), _estar_a, 'thumb_tip', yaw=-45, pitch=150, roll=-10, scale=1.1, depth=70,
                pole=(0.4, 1.0, 0.4), via=(168, 214))
_estar_k = lambda p: [p, mirrored(p)]
SIGNS['estar'] = {
    'poster': 0.2, 'dur': 2.0, 'hands': ['right', 'left'], 'handshape': _estar_a,
    'keys': [(0.0, _estar_k(_estar_up)), (0.3, _estar_k(_estar_up)), (0.9, _estar_k(_estar_down)),
             (1.5, _estar_k(_estar_down)), (2.0, _estar_k(dict(_estar_up, via=(150, 250))))],
    'marks': [(200, 190, 0)],
    'arrows': [{'d': 'M 156 202 Q 132 214 134 248'}, {'d': 'M 244 202 Q 268 214 266 248'}],
    'mirror_second': True,
}
TITLES['estar'] = 'Sinal de estar em Libras'
