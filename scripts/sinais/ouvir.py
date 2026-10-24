# OUVIR: the hand open in a claw (fingers apart and bent) beside the ear closes into a fist next to
# it, once. (UFSC Signbank OUVIR: 5_claw+S; INES OUVIR agrees.)


def hs_ouvir_claw():
    """5 claw: the fingers spread and bent at every joint, the thumb bent and apart."""
    return {'index': fing(13, 22, 58, 38), 'middle': fing(3, 22, 60, 40), 'ring': fing(-7, 22, 60, 40),
            'pinky': fing(-16, 24, 58, 38), 'thumb': (45.0, 20.0, 15.0, 25.0, 35.0)}


_ouvir_claw, _ouvir_fist = hs_ouvir_claw(), hs_S()
_ouvir_pole = (0.6, 0.9, 0.45)
# Beside the ear on the dominant side, fingers up, the palm turned toward the ear and a little to the
# viewer, so the bent fingers show from the side.
_ouvir = lambda shape, **kw: P((126, 152), shape, 'wrist', yaw=35, pitch=-15, roll=-4, scale=1.05, depth=40,
                               pole=_ouvir_pole, **kw)
_ouvir_open, _ouvir_shut = _ouvir(_ouvir_claw), _ouvir(_ouvir_fist, ease='in')
SIGNS['ouvir'] = {
    'poster': 0.4, 'dur': 2.2, 'hands': ['right'], 'handshape': _ouvir_claw, 'handshape_view': {'yaw': 30, 'pitch': -20},
    'keys': [(0.0, [_ouvir_open]), (0.4, [_ouvir_open]), (0.8, [_ouvir_shut]), (1.7, [_ouvir_shut]),
             (2.2, [dict(_ouvir_open, ease='smooth')])],
    # The fingers close down into the palm.
    'arrows': [{'d': 'M 98 86 Q 86 100 94 118'}],
}
TITLES['ouvir'] = 'Sinal de ouvir em Libras'
