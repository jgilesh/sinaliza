# RECEBER: both hands open in claws (fingers spread and bent), palms up, in front of the body; they close
# into fists and are drawn in toward the chest, as if taking something, ending with the palms toward the
# body. Once. (UFSC Signbank RECEBER: 5_claw+S, both hands. The INES RECEBER video shows a one-handed
# variant.)


def hs_receber_claw():
    """5 claw: the fingers spread and bent at every joint, the thumb bent and apart."""
    return {'index': fing(13, 22, 58, 38), 'middle': fing(3, 22, 60, 40), 'ring': fing(-7, 22, 60, 40),
            'pinky': fing(-16, 24, 58, 38), 'thumb': (45.0, 20.0, 15.0, 25.0, 35.0)}


_receber_claw, _receber_fist = hs_receber_claw(), hs_S()
_receber_pole = (0.4, 1.0, 0.45)
# Open: claws in front of the body, palms up and toward the signer, the bent fingers rising toward the
# viewer; turned a little so the claws show from the side.
_receber_open = P((150, 240), _receber_claw, 'wrist', yaw=205, pitch=45, roll=14, scale=1.12, depth=85,
                  pole=_receber_pole)
# Closed: fists drawn in toward the chest, upright, palms toward the body (the thumb side turned a
# little toward the viewer).
_receber_shut = P((162, 216), _receber_fist, 'wrist', yaw=150, pitch=0, roll=8, scale=1.05, depth=50,
                  pole=_receber_pole, ease='in')
SIGNS['receber'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _receber_claw,
    'handshape_view': {'yaw': 30, 'pitch': -20},
    'keys': [(0.0, [_receber_open, mirrored(_receber_open)]), (0.35, [_receber_open, mirrored(_receber_open)]),
             (0.95, [_receber_shut, mirrored(_receber_shut)]), (1.8, [_receber_shut, mirrored(_receber_shut)]),
             (2.4, [dict(_receber_open, ease='smooth'), mirrored(dict(_receber_open, ease='smooth'))])],
    'arrows': [{'d': 'M 108 236 Q 104 210 124 194'}, {'d': 'M 292 236 Q 296 210 276 194'}],
    'mirror_second': True,
}
TITLES['receber'] = 'Sinal de receber em Libras'
