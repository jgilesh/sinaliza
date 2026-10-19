# AMASSAR: both hands open in claws (fingers spread and bent), apart in front of the face and chest,
# come in toward the body and close into fists with force, ending in front of the chin with the
# backs of the bent fingers touching, palms toward the signer, once (like crumpling a sheet of
# paper). (UFSC Signbank AMASSAR. INES AMASSAR1 shows a variant: claws one in front of the other,
# squeezing.)


def hs_amassar_claw():
    """5 claw: the fingers spread and bent at every joint, the thumb bent and apart."""
    return {'index': fing(13, 22, 58, 38), 'middle': fing(3, 22, 60, 40), 'ring': fing(-7, 22, 60, 40),
            'pinky': fing(-16, 24, 58, 38), 'thumb': (45.0, 20.0, 15.0, 25.0, 35.0)}


_ama_claw = hs_amassar_claw()
_ama_fist = hs_S()
# Open: claws apart at shoulder/face height, palms forward and a little in.
_ama_open = P((124, 204), _ama_claw, 'wrist', yaw=40, pitch=-20, roll=-4, scale=1.08, depth=70, pole=(0.45, 1.0, 0.45))
# Closed: fists in front of the chin, palms toward the signer, the knuckles toward each other, the
# backs of the bent fingers touching at the midline.
_ama_shut = P((151, 172), _ama_fist, 'wrist', yaw=180, pitch=30, roll=80, scale=1.08, depth=48,
              pole=(0.4, 1.0, 0.45), ease='in')
_ama_back = dict(_ama_open, ease='smooth')
SIGNS['amassar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _ama_claw, 'handshape_view': {'yaw': 30, 'pitch': -20},
    'keys': [(0.0, [_ama_open, mirrored(_ama_open)]), (0.4, [_ama_open, mirrored(_ama_open)]),
             (0.85, [_ama_shut, mirrored(_ama_shut)]), (1.8, [_ama_shut, mirrored(_ama_shut)]),
             (2.4, [_ama_back, mirrored(_ama_back)])],
    # In toward the middle and the body, from each claw.
    'arrows': [{'d': 'M 150 244 Q 170 236 180 214'}, {'d': 'M 250 244 Q 230 236 220 214'}],
    'marks': [(200, 150, 0)],
    'mirror_second': True,
}
TITLES['amassar'] = 'Sinal de amassar em Libras'
