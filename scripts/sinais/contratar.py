# CONTRATAR: the support hand lies open (B) in front of the chest, palm up. The signing hand, closed in a
# fist (S) with the thumb side up, touches the mouth and then comes down in an arc and strikes the support
# palm, like a stamp. Twice. (UFSC Signbank CONTRATAR; the INES CONTRATAR1 video shows another variant.)


def hs_contratar_flat():
    """Support hand: open, fingers together and a little curved, thumb a little apart."""
    return {'index': fing(2, 8, 12, 8), 'middle': fing(0, 8, 12, 8), 'ring': fing(-2, 8, 12, 8),
            'pinky': fing(-4, 10, 12, 8), 'thumb': (22.0, 18.0, 10.0, 8.0, 6.0)}


_contratar_s, _contratar_flat = hs_S(), hs_contratar_flat()
# Support hand (defined as a right hand, then mirrored): palm up, tipped a little toward the viewer,
# fingers pointing across toward the midline.
_contratar_base = mirrored(P((140, 242), _contratar_flat, 'wrist', yaw=-50, pitch=0, roll=92, scale=1.1, depth=70))
# At the mouth: knuckles up, turned so the thumb side touches the corner of the mouth and the curled
# fingers with the thumb across them face the viewer.
_contratar_mouth = P((182, 158), _contratar_s, 'wrist', yaw=-45, pitch=0, roll=6, scale=1.0, depth=40,
                     pole=(0.4, 1.0, 0.4), ease='out')
# On the palm: the little-finger side down on it, knuckles forward and toward the other hand, thumb on top.
_contratar_on = P((214, 214), _contratar_s, 'wrist', yaw=-132, pitch=63, roll=135, scale=1.08, depth=74,
                  pole=(0.4, 1.0, 0.4), ease='in', via=(170, 190))
_contratar_up = P((180, 176), _contratar_s, 'wrist', yaw=-132, pitch=63, roll=135, scale=1.05, depth=60,
                  pole=(0.4, 1.0, 0.4))
SIGNS['contratar'] = {
    'poster': 1.0, 'dur': 3.0, 'hands': ['right', 'left'], 'handshape': _contratar_s, 'handshape_view': {'yaw': -20},
    'keys': [(0.0, [_contratar_up, _contratar_base]), (0.2, [_contratar_up, _contratar_base]),
             (0.5, [_contratar_mouth, _contratar_base]), (0.6, [_contratar_mouth, _contratar_base]),
             (0.95, [_contratar_on, _contratar_base]), (1.1, [_contratar_on, _contratar_base]),
             (1.45, [_contratar_mouth, _contratar_base]), (1.55, [_contratar_mouth, _contratar_base]),
             (1.9, [_contratar_on, _contratar_base]), (2.4, [_contratar_on, _contratar_base]),
             (3.0, [_contratar_up, _contratar_base])],
    'marks': [(184, 116, -35), (204, 232, -125)],
    # From the mouth down onto the palm, in an arc on the outer side.
    'arrows': [{'d': 'M 140 140 Q 132 196 186 226'}],
    'mirror_second': True,
}
TITLES['contratar'] = 'Sinal de contratar em Libras'
