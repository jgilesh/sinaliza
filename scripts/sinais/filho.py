# FILHO: open hand, fingers spread, palm on the chest with the fingers pointing across the body;
# then the hand leaves the chest forward and up to in front of the shoulder, the fingers curving.
# (UFSC Signbank FILHO; INES FILHO closes the hand on the chest instead.)


def hs_filho_claw():
    """Open hand with the fingers spread and curved (the end of FILHO): every finger bends a
    little at the knuckle and more at the middle and end joints, the thumb out, a little bent."""
    return {'index': fing(12, 25, 45, 30), 'middle': fing(3, 25, 48, 30), 'ring': fing(-7, 27, 48, 30),
            'pinky': fing(-16, 30, 45, 28), 'thumb': (34.0, 30.0, 20.0, 15.0, 20.0)}


_filho_5, _filho_claw = hs_5(), hs_filho_claw()
_filho_chest = P((206, 214), _filho_5, 'middle_tip', yaw=180, pitch=0, roll=95, scale=1.1, depth=20, pole=(0.5, 1.0, 0.3))
_filho_out = P((150, 182), _filho_claw, 'wrist', yaw=40, pitch=-30, roll=-10, scale=1.15, depth=80, via=(160, 215))
_filho_back = dict(_filho_chest, via=(150, 230))
SIGNS['filho'] = {
    'poster': 0.3, 'dur': 2.6, 'hands': ['right'], 'handshape': _filho_5,
    'keys': [(0.0, [_filho_chest]), (0.5, [_filho_chest]), (1.1, [_filho_out]), (2.0, [_filho_out]), (2.6, [_filho_back])],
    'marks': [(196, 246, 180)],
    'arrows': [{'d': 'M 212 206 Q 210 188 198 180', 'cap': True}],
}
TITLES['filho'] = 'Sinal de filho em Libras'
