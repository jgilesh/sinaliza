# DECEPCIONAR: both hands in a claw (fingers spread and curved). The other hand waits palm up in front of
# the chest; the signing hand covers the face, palm toward it, then comes straight down to the front of the
# chest, turning its palm up, and ends beside the other hand. Once. (UFSC Signbank DECEPCIONAR; the INES
# DECEPCIONAR video shows another variant, one hand closing in front of the neck and chest.)


def hs_decepcionar_claw():
    """5 claw: fingers spread and curved, thumb out and bent."""
    return {'index': fing(14, 12, 50, 34), 'middle': fing(3, 8, 44, 30), 'ring': fing(-8, 14, 50, 34),
            'pinky': fing(-18, 18, 50, 34), 'thumb': (42.0, 12.0, 15.0, 15.0, 25.0)}


_decepcionar_claw = hs_decepcionar_claw()
_decepcionar_pole = (0.45, 1.0, 0.45)
# Palm up and a little toward the viewer, the curved fingers pointing in toward the middle (right-hand
# pose; the other hand uses its mirror image).
_decepcionar_up = P((140, 230), _decepcionar_claw, 'wrist', yaw=-30, pitch=5, roll=52, scale=1.1, depth=60,
                    pole=_decepcionar_pole)
_decepcionar_base = mirrored(_decepcionar_up)
# Over the face: palm toward it, fingers up and curved toward it, turned a little so the curve shows.
_decepcionar_face = P((204, 66), _decepcionar_claw, 'middle_tip', yaw=155, pitch=0, roll=10, scale=1.0, depth=38,
                      pole=_decepcionar_pole)
_decepcionar_side = P((128, 176), _decepcionar_claw, 'wrist', yaw=150, pitch=0, roll=0, scale=1.05, depth=50,
                      pole=_decepcionar_pole)
SIGNS['decepcionar'] = {
    'poster': 0.7, 'dur': 2.8, 'hands': ['right', 'left'], 'handshape': _decepcionar_claw,
    'handshape_view': {'yaw': -30},
    'keys': [(0.0, [_decepcionar_side, _decepcionar_base]), (0.15, [_decepcionar_side, _decepcionar_base]),
             (0.55, [_decepcionar_face, _decepcionar_base]), (0.9, [_decepcionar_face, _decepcionar_base]),
             (1.45, [dict(_decepcionar_up, ease='smooth'), _decepcionar_base]),
             (2.2, [_decepcionar_up, _decepcionar_base]),
             (2.8, [dict(_decepcionar_side, via=(118, 230)), _decepcionar_base])],
    # Straight down from the face to the chest, on the outer side.
    'arrows': [{'d': 'M 142 92 Q 128 150 146 200'}],
    'mirror_second': True,
}
TITLES['decepcionar'] = 'Sinal de decepcionar em Libras'
