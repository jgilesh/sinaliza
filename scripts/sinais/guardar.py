# GUARDAR: both hands flat (B). The signing hand starts in front of the mouth, palm toward the face;
# it comes down and lies crossed on the back of the support hand (palm down, in front of the chest),
# and the two crossed hands go down together a little. Once. (UFSC Signbank GUARDAR; INES GUARDAR.)


def hs_guardar_flat():
    """B: flat hand, fingers together, the thumb along the side of the index."""
    return {'index': fing(2, 0, 0, 0), 'middle': fing(0, 0, 0, 0), 'ring': fing(-2, 0, 0, 0),
            'pinky': fing(-4, 0, 0, 0), 'thumb': (-12.0, 6.0, 10.0, 6.0, 6.0)}


_gua_b = hs_guardar_flat()
# Start: in front of the mouth, palm toward the face (back of the hand to the viewer), fingers across.
_gua_mouth = P((160, 144), _gua_b, 'wrist', yaw=170, pitch=0, roll=84, scale=1.0, depth=40, pole=(0.7, 1.0, 0.4))


def _gua_pair(dy, via=None):
    # Both palms down, seen a little from above (backs toward the viewer); the hands cross.
    top = P((156, 212 + dy), _gua_b, 'wrist', yaw=125, pitch=0, roll=122, scale=1.1, depth=75, pole=(0.5, 1.0, 0.4),
            via=via)
    base = mirrored(P((146, 238 + dy), _gua_b, 'wrist', yaw=125, pitch=0, roll=62, scale=1.1, depth=70))
    return top, base


_gua_on, _gua_sup = _gua_pair(0, via=(150, 186))
_gua_low, _gua_sup_low = _gua_pair(14)
SIGNS['guardar'] = {
    'poster': 1.0, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _gua_b,
    'keys': [(0.0, [_gua_mouth, _gua_sup]), (0.3, [_gua_mouth, _gua_sup]), (0.85, [_gua_on, _gua_sup]),
             (1.0, [dict(_gua_on, via=None), _gua_sup]), (1.45, [_gua_low, _gua_sup_low]),
             (2.1, [_gua_low, _gua_sup_low]), (2.6, [dict(_gua_mouth, via=(140, 200)), _gua_sup])],
    'marks': [(232, 206, 25)],
    'arrows': [{'d': 'M 128 132 Q 104 176 126 206'}, {'d': 'M 284 222 L 284 246'}],
    'mirror_second': True,
}
TITLES['guardar'] = 'Sinal de guardar em Libras'
