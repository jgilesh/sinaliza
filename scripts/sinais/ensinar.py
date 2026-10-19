# ENSINAR: both hands in front of the chest with the fingertips gathered on the thumb (O / beak), palms
# forward and down; they move forward and open into curved fingers, then come back closed, three
# times, both hands together. (UFSC Signbank ENSINAR: O then 5_claw, neutral space, forward; INES
# ENSINAR agrees.)


def hs_ensinar_beak():
    """Beak / O: fingers together, bent at the knuckles and middle joints, their tips gathered on the
    thumb's pad."""
    shape = {'index': fing(2, 52, 58, 34), 'middle': fing(0, 55, 58, 36), 'ring': fing(-1, 58, 56, 36),
             'pinky': fing(-2, 62, 54, 36)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


def hs_ensinar_open():
    """Opened: fingers spread and curved, the thumb apart from them."""
    return {'index': fing(14, 22, 30, 20), 'middle': fing(3, 22, 30, 20), 'ring': fing(-8, 24, 30, 20),
            'pinky': fing(-18, 26, 30, 20), 'thumb': (42.0, 14.0, 10.0, 8.0, 10.0)}


_ensinar_beak, _ensinar_open = hs_ensinar_beak(), hs_ensinar_open()


def _ensinar_pose(shape, fwd=0.0, ease='smooth'):
    """Right hand in front of the chest, the thumb side toward the viewer a little so the gathered
    fingertips on the thumb read; fwd (0..1) carries it forward (bigger, a little lower and out)."""
    return P((156 - 12 * fwd, 214 + 6 * fwd), shape, 'wrist', yaw=-75 + 45 * fwd, pitch=-15 + 20 * fwd, roll=15 - 5 * fwd,
             scale=1.08 + 0.1 * fwd,
             depth=50 + 40 * fwd, pole=(0.45, 1.0, 0.4), ease=ease)


_ensinar_a, _ensinar_b = _ensinar_pose(_ensinar_beak), _ensinar_pose(_ensinar_open, 1.0, 'out')
_ensinar_k = lambda p: [p, mirrored(p)]
_ensinar_keys = [(0.0, _ensinar_k(_ensinar_a)), (0.3, _ensinar_k(_ensinar_a))]
for _ensinar_i in range(3):
    _ensinar_t = 0.3 + 0.56 * _ensinar_i
    _ensinar_keys += [(_ensinar_t + 0.3, _ensinar_k(_ensinar_b)), (_ensinar_t + 0.56, _ensinar_k(_ensinar_a))]
_ensinar_keys.append((2.4, _ensinar_k(_ensinar_a)))
SIGNS['ensinar'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _ensinar_beak,
    'handshape_view': {'yaw': -60, 'pitch': -10},
    'keys': _ensinar_keys,
    # Forward and a little out and down, beside each hand.
    'arrows': [{'d': 'M 112 196 Q 104 214 112 232'}, {'d': 'M 288 196 Q 296 214 288 232'}],
    'mirror_second': True,
}
TITLES['ensinar'] = 'Sinal de ensinar em Libras'
