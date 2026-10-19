# MORRER: the hand with the fingers together and curved, thumb apart, starts beside the neck on the
# opposite side, palm toward the body, and moves away in an arc to the signing side at shoulder
# height, ending with the fingers up, curved toward the body, and the thumb pointing out. Once.
# (UFSC Signbank MORRER, INES MORRER.)


def hs_morrer_bc():
    """B curved: the four fingers together and bent at every joint, thumb apart."""
    return {'index': fing(2, 32, 42, 28), 'middle': fing(0, 32, 44, 30), 'ring': fing(-2, 32, 44, 30),
            'pinky': fing(-4, 34, 44, 30), 'thumb': (40.0, 16.0, 6.0, 6.0, 4.0)}


_morrer_hs = hs_morrer_bc()
_morrer_neck = P((226, 186), _morrer_hs, 'fingertips', yaw=163, pitch=0, roll=90, scale=1.05, depth=35,
                 pole=(0.5, 1.0, 0.4))
_morrer_out = P((112, 178), _morrer_hs, 'wrist', yaw=150, pitch=-10, roll=-4, scale=1.1, depth=70,
                via=(160, 160), ease='out', pole=(0.6, 1.0, 0.4))
SIGNS['morrer'] = {
    'poster': 1.1, 'dur': 2.4, 'hands': ['right'], 'handshape': _morrer_hs, 'handshape_view': {'yaw': 30, 'pitch': -30},
    'keys': [(0.0, [_morrer_neck]), (0.35, [_morrer_neck]), (0.95, [_morrer_out]), (1.8, [_morrer_out]),
             (2.4, [dict(_morrer_neck, via=(170, 205))])],
    'arrows': [{'d': 'M 214 222 Q 160 232 108 210'}],
}
TITLES['morrer'] = 'Sinal de morrer em Libras'
