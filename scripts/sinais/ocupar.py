# OCUPAR: both hands in a claw (fingers spread and curved), palms down, in front of the chest; they move
# down and forward together and close into fists, as if taking hold of a space. Once. (UFSC Signbank
# OCUPAR: 5_claw+S, neutral space. The INES OCUPAR video shows a one-handed variant: one claw sweeps
# across in front of the body.)


def hs_ocupar_claw():
    """5 in a claw: fingers spread and bent at the middle and end joints, thumb out and bent."""
    return {'index': fing(20, 14, 52, 38), 'middle': fing(5, 14, 54, 40), 'ring': fing(-10, 16, 54, 40),
            'pinky': fing(-20, 18, 52, 38), 'thumb': (30.0, 26.0, 26.0, 16.0, 26.0)}


_ocupar_claw, _ocupar_s = hs_ocupar_claw(), hs_S()
# Up: in front of the chest, the back of the hand toward the viewer and tipped up (palm down), the
# clawed fingers hanging forward and down.
_ocupar_up = P((150, 196), _ocupar_claw, 'wrist', yaw=-15, pitch=52, roll=-8, scale=1.1, depth=55, pole=(0.45, 1.0, 0.4))
# Down: lower and forward, closed into fists, palm down, knuckles forward.
_ocupar_down = P((140, 226), _ocupar_s, 'wrist', yaw=-10, pitch=78, roll=-6, scale=1.18, depth=95, pole=(0.45, 1.0, 0.4),
                 ease='in')
_ocupar_k = lambda p: [p, mirrored(p)]
SIGNS['ocupar'] = {
    'poster': 0.2, 'dur': 1.9, 'hands': ['right', 'left'], 'handshape': _ocupar_claw,
    'handshape_view': {'yaw': 25, 'pitch': -20},
    'keys': [(0.0, _ocupar_k(_ocupar_up)), (0.35, _ocupar_k(_ocupar_up)), (0.8, _ocupar_k(_ocupar_down)),
             (1.4, _ocupar_k(_ocupar_down)), (1.9, _ocupar_k(dict(_ocupar_up, ease='smooth')))],
    # Down and forward, outside each hand.
    'arrows': [{'trail': 0, 'from': 0.35, 'to': 0.8, 'offset': (-34, 0), 'trim': 0.05},
               {'trail': 1, 'from': 0.35, 'to': 0.8, 'offset': (34, 0), 'trim': 0.05}],
    'mirror_second': True,
}
TITLES['ocupar'] = 'Sinal de ocupar em Libras'
