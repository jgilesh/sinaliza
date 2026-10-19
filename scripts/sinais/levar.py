# LEVAR: the fingertips start bunched together on the thumb, near the chest on the dominant side,
# pointing down; the hand goes out and up in an arc to above the shoulder, opening on the way, and ends
# with the fingers spread and the palm forward. Once. (UFSC Signbank LEVAR "Flower"; the INES LEVAR1
# video shows another variant.)


def hs_levar_bunch():
    """Fingers bent at the knuckles and middle joints, their tips gathered on the thumb's pad."""
    shape = {'index': fing(2, 52, 58, 34), 'middle': fing(0, 55, 58, 36), 'ring': fing(-1, 58, 56, 36),
             'pinky': fing(-2, 62, 54, 36)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


_levar_bunch, _levar_5 = hs_levar_bunch(), hs_5()
# Fingers pointing down, the thumb side to the viewer: the fingertips gathered on the thumb show in
# profile.
_levar_start = P((162, 196), _levar_bunch, 'wrist', yaw=-60, pitch=20, roll=170, scale=1.05, depth=55,
                 pole=(0.4, 1.0, 0.45))
# Above the shoulder, fingers spread and up, palm forward.
_levar_end = P((106, 126), _levar_5, 'wrist', yaw=-6, pitch=0, roll=-14, scale=1.1, depth=60, via=(112, 196),
               ease='out', pole=(0.5, 1.0, 0.45))
_levar_back = dict(_levar_start, via=(104, 206), ease='smooth')   # back down on the outer side, clear of the face
SIGNS['levar'] = {
    'poster': 1.1, 'dur': 2.4, 'hands': ['right'], 'handshape': _levar_bunch, 'handshape_view': {'yaw': -85},
    'keys': [(0.0, [_levar_start]), (0.35, [_levar_start]), (1.05, [_levar_end]), (1.85, [_levar_end]),
             (2.4, [_levar_back])],
    # Out and up from the chest, on the inner side of the hand's path (the arm lies on the outer side).
    'arrows': [{'d': 'M 186 176 Q 140 184 136 140'}],
}
TITLES['levar'] = 'Sinal de levar em Libras'
