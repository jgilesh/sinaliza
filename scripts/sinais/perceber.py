# PERCEBER: both hands in V come up to the sides of the face, palms toward the face, and the index
# and middle fingers bend into hooks and straighten again, two times, both hands at once. No contact.
# (UFSC Signbank PERCEBER "V+V_curved"; INES PERCEBER1 shows it with the dominant hand at the chin.)


def hs_perceber_v(hook=0.0):
    """V (index and middle up and apart, the others folded under the thumb); `hook` 0..1 bends the two
    fingers at the middle and end joints into hooks."""
    shape = fist({'index': fing(12, 6 * hook, 85 * hook, 60 * hook), 'middle': fing(-8, 6 * hook, 85 * hook, 60 * hook)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


_perceber_v, _perceber_hook = hs_perceber_v(0.0), hs_perceber_v(1.0)
_perceber_pole = (0.6, 1.0, 0.45)


def _perceber_up(shape, ease='smooth'):
    # Beside the face on the dominant side, in front of the shoulder: fingers up, the palm turned toward
    # the face and a little toward the viewer, so the two fingers stand apart and their hooks show in
    # profile.
    return P((132, 200), shape, 'wrist', yaw=64, pitch=0, roll=-6, scale=1.0, depth=42, pole=_perceber_pole, ease=ease)


_perceber_low = P((150, 250), _perceber_v, 'wrist', yaw=40, pitch=0, roll=-10, scale=1.05, depth=60, pole=_perceber_pole)
_perceber_a, _perceber_b = _perceber_up(_perceber_v), _perceber_up(_perceber_hook)
_perceber_keys = [(0.0, _perceber_low), (0.25, _perceber_low), (0.7, _perceber_a), (0.9, _perceber_b),
                  (1.1, _perceber_a), (1.3, _perceber_b), (1.5, _perceber_a), (2.1, _perceber_a),
                  (2.6, _perceber_low)]
SIGNS['perceber'] = {
    'poster': 0.9, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _perceber_v,
    'keys': [(t, [p, mirrored(p)]) for t, p in _perceber_keys],
    # Outside each hand, at the fingertips: the fingers bend and straighten.
    'arrows': [{'d': 'M 110 116 Q 104 132 114 144', 'both': True}, {'d': 'M 290 116 Q 296 132 286 144', 'both': True}],
    'mirror_second': True,
}
TITLES['perceber'] = 'Sinal de perceber em Libras'
