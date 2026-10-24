# BRIGAR: both hands open with the fingers bent into claws, palms facing each other, at the height of
# the chin and chest; they move alternately forward and back, the fingers bending further, as if the
# two were grabbing at each other. (UFSC Signbank BRIGAR: 5_claw on both hands, alternating; the INES
# BRIGAR1 video shows a one-handed variant beside the face.)


def hs_brigar_claw():
    """5 claw: the fingers spread and bent at every joint, the thumb bent and apart."""
    return {'index': fing(13, 18, 50, 34), 'middle': fing(3, 18, 52, 36), 'ring': fing(-7, 18, 52, 36),
            'pinky': fing(-16, 20, 50, 34), 'thumb': (42.0, 20.0, 15.0, 20.0, 28.0)}


def hs_brigar_grab():
    """The claw closing: the fingers bent further, still apart."""
    return {'index': fing(12, 32, 66, 44), 'middle': fing(3, 32, 68, 46), 'ring': fing(-6, 32, 68, 46),
            'pinky': fing(-14, 34, 66, 44), 'thumb': (38.0, 28.0, 25.0, 28.0, 36.0)}


_brigar_claw, _brigar_grab = hs_brigar_claw(), hs_brigar_grab()


def _brigar_hand(fwd):
    """Right hand, palm turned toward the midline but mostly to the viewer (the claw reads), fingers up and curled; fwd = 1
    reaching forward (nearer, a little in and down, the fingers grabbing), 0 drawn back."""
    shape = _brigar_grab if fwd else _brigar_claw
    at = (138 + 10 * fwd, 194 + 6 * fwd)
    return P(at, shape, 'wrist', yaw=30, pitch=-10 + 6 * fwd, roll=-8, scale=1.02 + 0.16 * fwd, depth=40 + 45 * fwd,
             pole=(0.45, 1.0, 0.4))


_brigar_r1, _brigar_r0 = _brigar_hand(1), _brigar_hand(0)
_brigar_keys = [(0.0, [_brigar_r0, mirrored(_brigar_r0)]), (0.3, [_brigar_r0, mirrored(_brigar_r0)])]
for _brigar_i in range(3):
    _t = 0.6 + 0.6 * _brigar_i
    _brigar_keys += [(_t, [_brigar_r1, mirrored(_brigar_r0)]), (_t + 0.3, [_brigar_r0, mirrored(_brigar_r1)])]
_brigar_keys += [(2.4, [_brigar_r0, mirrored(_brigar_r0)]), (2.8, [_brigar_r0, mirrored(_brigar_r0)])]
SIGNS['brigar'] = {
    'poster': 0.6, 'dur': 2.8, 'hands': ['right', 'left'], 'handshape': _brigar_claw,
    'handshape_view': {'yaw': 30, 'pitch': -20},
    'keys': _brigar_keys,
    # Beside each hand a short two-headed arrow, slanting toward the viewer: forward and back, in turn.
    'arrows': [{'d': 'M 96 176 L 112 196', 'both': True}, {'d': 'M 304 176 L 288 196', 'both': True}],
    'mirror_second': True,
}
TITLES['brigar'] = 'Sinal de brigar em Libras'
