# AUMENTAR: both hands in a claw (fingers spread and curved), palms toward each other in front of the
# chest; they move apart, out and up to shoulder height, once, like something growing.
# (UFSC Signbank AUMENTAR; INES AUMENTAR1.)


def hs_aumentar_claw():
    """5 in a claw: fingers spread and bent at the middle and end joints, thumb out and bent."""
    return {'index': fing(16, 12, 48, 34), 'middle': fing(4, 12, 50, 36), 'ring': fing(-8, 14, 50, 36),
            'pinky': fing(-19, 16, 48, 34), 'thumb': (22.0, 30.0, 30.0, 16.0, 30.0)}


_aum_claw = hs_aumentar_claw()
# Palm turned toward the other hand and partly to the viewer, so the curved, spread fingers read.
_aum_in = P((154, 222), _aum_claw, "wrist", yaw=65, pitch=-10, roll=4, scale=1.05, depth=60, pole=(0.3, 1.0, 0.4))
_aum_out = P((118, 178), _aum_claw, 'wrist', yaw=50, pitch=-10, roll=-12, scale=1.1, depth=70, pole=(0.5, 1.0, 0.4),
             via=(140, 222), ease='out')
_aum_back = dict(_aum_in, via=(132, 236), ease='smooth')
SIGNS['aumentar'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _aum_claw, 'handshape_view': {'yaw': 30, 'pitch': -20},
    'keys': [(0.0, [_aum_in, mirrored(_aum_in)]), (0.35, [_aum_in, mirrored(_aum_in)]),
             (1.0, [_aum_out, mirrored(_aum_out)]), (1.8, [_aum_out, mirrored(_aum_out)]),
             (2.4, [_aum_back, mirrored(_aum_back)])],
    'arrows': [{'trail': 0, 'from': 0.35, 'to': 1.0, 'offset': (-26, 6), 'trim': 0.1},
               {'trail': 1, 'from': 0.35, 'to': 1.0, 'offset': (26, 6), 'trim': 0.1}],
    'mirror_second': True,
}
TITLES['aumentar'] = 'Sinal de aumentar em Libras'
