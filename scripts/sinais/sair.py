# SAIR: the dominant hand, fingers bent, starts in front of the chest with the palm toward the body;
# it goes out and up in an arc to beside the head, closing on the way into A (fist, thumb up). Once.
# (UFSC Signbank SAIR "P+A", chest; the INES video agrees.)


def hs_sair_bent():
    """Fingers bent at the knuckles and middle joints, a little apart, the thumb bent beside the index."""
    return {'index': fing(3, 45, 60, 35), 'middle': fing(0, 48, 62, 36), 'ring': fing(-3, 50, 60, 35),
            'pinky': fing(-6, 54, 58, 34), 'thumb': (20.0, 30.0, 30.0, 12.0, 18.0)}


def hs_sair_a():
    """A: fist, the thumb straight up along the side of the index, its tip above the knuckles."""
    shape = fist()
    shape['thumb'] = solve_thumb((17.0, -44.0, -1.5), pad_to=(-1.0, 0.0, 0.0), point=(0.0, -1.0, 0.0),
                                 pref=(-5.0, 10.0, 20.0, 0.0, 0.0))
    return shape


_sair_bent, _sair_a = hs_sair_bent(), hs_sair_a()
# In front of the chest: back of the hand turned to the viewer, the bent fingers toward the midline.
_sair_start = P((176, 236), _sair_bent, 'wrist', yaw=145, pitch=0, roll=35, scale=1.05, depth=50, pole=(0.4, 1.0, 0.4))
# Beside the head: thumbs up, palm forward (the thumb on the inner side reads against the fist).
_sair_end = P((124, 146), _sair_a, 'wrist', yaw=-10, pitch=0, roll=-6, scale=1.08, depth=60, pole=(0.25, 1.0, 0.5),
              via=(118, 210), ease='out')
SIGNS['sair'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right'], 'handshape': _sair_a,
    'keys': [(0.0, [_sair_start]), (0.35, [_sair_start]), (1.0, [_sair_end]), (1.9, [_sair_end]),
             (2.4, [dict(_sair_start, via=(150, 200))])],
    'arrows': [{'d': 'M 176 206 Q 148 194 146 152'}],
}
TITLES['sair'] = 'Sinal de sair em Libras'
