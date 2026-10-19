# ATACAR: both hands open in a claw (fingers spread and bent), palms forward, up beside the face;
# they swing forward and down in an arc and close into fists, palms down, once. Fierce face.
# (UFSC Signbank ATACAR: 5+S, face, arc forward and down. The INES ATACAR1 video shows a one-handed
# variant: one claw beside the head strikes down across the body.)


def hs_atacar_claw():
    """5 in a claw: fingers spread and bent at the middle and end joints, thumb out and bent."""
    return {'index': fing(16, 12, 48, 34), 'middle': fing(4, 12, 50, 36), 'ring': fing(-8, 14, 50, 36),
            'pinky': fing(-19, 16, 48, 34), 'thumb': (22.0, 30.0, 30.0, 16.0, 30.0)}


_atacar_claw, _atacar_s = hs_atacar_claw(), hs_S()
_atacar_up = P((123, 130), _atacar_claw, 'wrist', yaw=22, pitch=-15, roll=-10, scale=1.05, depth=45, pole=(0.7, 1.0, 0.3))
_atacar_down = P((150, 206), _atacar_s, 'wrist', yaw=10, pitch=75, roll=-10, scale=1.25, depth=110,
                 pole=(0.4, 1.0, 0.4), via=(118, 168), ease='in')
_atacar_back = dict(_atacar_up, via=(110, 180), ease='smooth')
SIGNS['atacar'] = {
    'poster': 0.3, 'dur': 2.0, 'hands': ['right', 'left'], 'handshape': _atacar_claw,
    'handshape_view': {'yaw': 25, 'pitch': -20},
    'keys': [(0.0, [_atacar_up, mirrored(_atacar_up)]), (0.3, [_atacar_up, mirrored(_atacar_up)]),
             (0.75, [_atacar_down, mirrored(_atacar_down)]), (1.4, [_atacar_down, mirrored(_atacar_down)]),
             (2.0, [_atacar_back, mirrored(_atacar_back)])],
    'arrows': [{'trail': 0, 'from': 0.3, 'to': 0.75, 'offset': (-26, 0)},
               {'trail': 1, 'from': 0.3, 'to': 0.75, 'offset': (26, 0)}],
    'mirror_second': True,
}
TITLES['atacar'] = 'Sinal de atacar em Libras'
