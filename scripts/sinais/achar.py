# ACHAR (opinião): open hand with the fingers spread and the middle finger bent forward (5m); the tip of
# the middle finger touches the side of the forehead and slides a short way down to the temple. Once.
# (UFSC Signbank ACHAR: 5m, head; INES ACHAR2 agrees. INES ACHAR1 is "achar = encontrar", another sign.)


def hs_achar_5m():
    """Open hand, fingers spread and almost straight; the middle finger bends forward (toward the palm)
    at the knuckle and middle joint, so its tip sticks out in front of the others."""
    return {'index': fing(14, 0, 4, 2), 'middle': fing(2, 55, 40, 20), 'ring': fing(-8, 0, 4, 2),
            'pinky': fing(-18, 0, 5, 3), 'thumb': (40.0, 16.0, 6.0, 6.0, 4.0)}


_achar_5m = hs_achar_5m()


def _achar_pose(at, roll=18, ease='smooth', anchor='middle_tip', **kw):
    # Beside the head, palm turned toward the face and partly to the viewer: the open fingers fan up and
    # the bent middle finger reaches in to the side of the forehead; the hand stays out at the side.
    return P(at, _achar_5m, anchor, yaw=55, pitch=0, roll=roll, scale=1.0, depth=36,
             pole=(0.7, 1.0, 0.45), ease=ease, **kw)


_achar_low = _achar_pose((128, 172), roll=8, anchor='wrist')
_achar_on = _achar_pose((164, 72))
_achar_down = _achar_pose((162, 90), roll=12)
SIGNS['achar'] = {
    'poster': 0.6, 'dur': 2.2, 'hands': ['right'], 'handshape': _achar_5m,
    'handshape_view': {'yaw': 55, 'roll': -5},
    'keys': [(0.0, [_achar_low]), (0.4, [_achar_on]), (0.6, [_achar_on]), (1.1, [_achar_down]),
             (1.7, [_achar_down]), (2.2, [dict(_achar_low, via=(150, 120))])],
    'marks': [(168, 66, 40)],
    'arrows': [{'d': 'M 180 70 Q 184 79 181 88'}],
}
TITLES['achar'] = 'Sinal de achar em Libras'
