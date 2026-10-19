# APAIXONAR: one hand in a claw (fingers spread and bent), palm toward the face. It starts beside the
# face on the signing side, draws a circle in front of the face (across, down, back out) and goes up
# to the side of the head, while the gaze goes up, dreamy. Once. (UFSC Signbank APAIXONAR: 5_claw,
# front of the head, circular; the INES APAIXONAR video shows a variant: the hand closes on the chest.)


def hs_apaixonar_claw():
    """5 claw: the fingers spread and bent at every joint, the thumb bent and apart."""
    return {'index': fing(13, 22, 58, 38), 'middle': fing(3, 22, 60, 40), 'ring': fing(-7, 22, 60, 40),
            'pinky': fing(-16, 24, 58, 38), 'thumb': (45.0, 20.0, 15.0, 25.0, 35.0)}


_apaixonar_claw = hs_apaixonar_claw()
_apaixonar_pole = (0.6, 1.0, 0.45)
_apaixonar_hand = lambda at, yaw, roll, **kw: P(at, _apaixonar_claw, 'wrist', yaw=yaw, pitch=5, roll=roll, scale=1.05,
                                                depth=45, pole=_apaixonar_pole, **kw)
_apaixonar_a = _apaixonar_hand((138, 168), 150, 6)                       # beside the face, palm toward it
_apaixonar_b = _apaixonar_hand((186, 176), 150, 14, via=(160, 160))      # across, in front of the face
_apaixonar_c = _apaixonar_hand((164, 196), 150, 8, via=(190, 196))       # down
_apaixonar_d = _apaixonar_hand((128, 176), 150, 0, via=(138, 200))       # back out
_apaixonar_e = _apaixonar_hand((118, 112), 150, 30, via=(112, 150), ease='out')   # up beside the head
SIGNS['apaixonar'] = {
    'poster': 1.5, 'dur': 2.6, 'hands': ['right'], 'handshape': _apaixonar_claw,
    'handshape_view': {'yaw': 30, 'pitch': -20},
    'keys': [(0.0, [_apaixonar_a]), (0.3, [_apaixonar_a]), (0.6, [_apaixonar_b]), (0.85, [_apaixonar_c]),
             (1.1, [_apaixonar_d]), (1.45, [_apaixonar_e]), (2.1, [_apaixonar_e]),
             (2.6, [dict(_apaixonar_a, via=(104, 150))])],
    # The circle low in front of the face, then up the outside to beside the head.
    'arrows': [{'d': 'M 150 156 Q 202 156 198 178 Q 186 198 138 186 Q 100 170 98 110'}],
}
TITLES['apaixonar'] = 'Sinal de apaixonar em Libras'
