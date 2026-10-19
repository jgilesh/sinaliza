# ACABAR: both hands flat (B). The signing hand starts raised beside the head and comes down onto
# the palm of the support hand (palm up, in front of the body), sliding firmly across it as if
# cutting or wiping; then both hands open out to the sides at shoulder height, palms forward,
# fingers a little apart. Once. (UFSC Signbank ACABAR-2; the INES video shows only the slide.)


def hs_acabar_open():
    """B with the fingers a little apart (the end of the sign)."""
    return {'index': fing(8, 0, 2, 1), 'middle': fing(1, 0, 2, 1), 'ring': fing(-6, 0, 2, 1),
            'pinky': fing(-12, 0, 3, 2), 'thumb': (36.0, 14.0, 6.0, 6.0, 4.0)}


_acabar_b, _acabar_open = hs_B(), hs_acabar_open()
# Support hand (defined as a right hand, then mirrored): palm up and tilted toward the viewer,
# fingers pointing across toward the midline.
_acabar_base = mirrored(P((162, 252), _acabar_b, 'wrist', yaw=-50, pitch=0, roll=92, scale=1.1, depth=70))
# Signing hand beside the head, palm turned toward it, fingers up.
_acabar_up = P((128, 140), _acabar_b, 'wrist', yaw=50, pitch=0, roll=-4, scale=1.05, depth=45, pole=(0.1, 1.0, 0.2))
# On the support palm: palm down, back of the hand to the viewer, fingers across toward the other side.
_acabar_on = P((232, 236), _acabar_b, 'fingertips', yaw=150, pitch=5, roll=96, scale=1.08, depth=78,
               via=(150, 214), pole=(0.4, 1.0, 0.4))
_acabar_slid = P((206, 244), _acabar_b, 'fingertips', yaw=150, pitch=5, roll=98, scale=1.08, depth=80,
                 ease='linear', pole=(0.4, 1.0, 0.4))
# Both hands out to the sides, palms forward, fingers a little apart.
_acabar_end = P((126, 190), _acabar_open, 'wrist', yaw=0, pitch=0, roll=-14, scale=1.1, depth=75, ease='out')
_acabar_back = dict(_acabar_up, ease='smooth')
SIGNS['acabar'] = {
    'poster': 1.0, 'dur': 2.8, 'hands': ['right', 'left'], 'handshape': _acabar_b,
    'keys': [(0.0, [_acabar_up, _acabar_base]), (0.3, [_acabar_up, _acabar_base]),
             (0.8, [_acabar_on, _acabar_base]), (1.15, [_acabar_slid, _acabar_base]),
             (1.6, [_acabar_end, mirrored(_acabar_end)]), (2.2, [_acabar_end, mirrored(_acabar_end)]),
             (2.8, [_acabar_back, _acabar_base])],
    'marks': [(226, 226, 20)],
    # Down from beside the head onto the support palm; then both hands out to the sides.
    'arrows': [{'d': 'M 104 124 Q 104 214 156 230'},
               {'d': 'M 88 214 L 64 214'}, {'d': 'M 312 214 L 336 214'}],
    'mirror_second': True,
}
TITLES['acabar'] = 'Sinal de acabar em Libras'
