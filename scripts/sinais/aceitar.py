# ACEITAR: both hands open in claws (fingers spread and bent), palms toward the signer, in front of
# the upper chest; they come down to in front of the waist and close into fists, ending with the
# palms up, as if receiving something. Once. (UFSC Signbank ACEITAR: 5_claw+S; INES ACEITAR agrees.)


def hs_aceitar_claw():
    """5 claw: the fingers spread and bent at every joint, the thumb bent and apart."""
    return {'index': fing(13, 22, 58, 38), 'middle': fing(3, 22, 60, 40), 'ring': fing(-7, 22, 60, 40),
            'pinky': fing(-16, 24, 58, 38), 'thumb': (45.0, 20.0, 15.0, 25.0, 35.0)}


_aceitar_claw, _aceitar_fist = hs_aceitar_claw(), hs_S()
_aceitar_pole = (0.4, 1.0, 0.45)
# Claws in front of the upper chest: the backs of the hands toward the viewer, turned a little so
# the bent fingers show from the side, fingertips up and leaning in.
_aceitar_open = P((148, 228), _aceitar_claw, "wrist", yaw=222, pitch=10, roll=8, scale=1.12, depth=55,
                  pole=_aceitar_pole)
# Fists in front of the waist, palms up, the folded fingers toward the viewer.
_aceitar_shut = P((150, 268), _aceitar_fist, 'wrist', yaw=180, pitch=45, roll=70, scale=1.12, depth=75,
                  pole=_aceitar_pole, ease='in')
_aceitar_back = dict(_aceitar_open, ease='smooth')
SIGNS['aceitar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _aceitar_claw,
    'handshape_view': {'yaw': 30, 'pitch': -20},
    'keys': [(0.0, [_aceitar_open, mirrored(_aceitar_open)]), (0.35, [_aceitar_open, mirrored(_aceitar_open)]),
             (0.95, [_aceitar_shut, mirrored(_aceitar_shut)]), (1.8, [_aceitar_shut, mirrored(_aceitar_shut)]),
             (2.4, [_aceitar_back, mirrored(_aceitar_back)])],
    # Outside each hand: down to the waist.
    'arrows': [{'d': 'M 94 220 Q 90 250 112 270'}, {'d': 'M 306 220 Q 310 250 288 270'}],
    'mirror_second': True,
}
TITLES['aceitar'] = 'Sinal de aceitar em Libras'
