# ANGÚSTIA: both hands in a claw (fingers spread and curved), the fingertips on the chest, palms
# toward the body; the hands rub the chest in small circles, alternating (one goes up while the
# other goes down), repeated. (UFSC Signbank ANGÚSTIA; the INES video for MAGOAR shows another form.)


def hs_angustia_claw():
    """5 claw: fingers spread and curved, thumb out and bent."""
    return {'index': fing(14, 12, 50, 34), 'middle': fing(3, 8, 44, 30), 'ring': fing(-8, 14, 50, 34),
            'pinky': fing(-18, 18, 50, 34), 'thumb': (42.0, 12.0, 15.0, 15.0, 25.0)}


_angustia_hs = hs_angustia_claw()
_ANGUSTIA_C = (179.0, 214.0)   # right hand: fingertips' circle centre
_ANGUSTIA_R = 7.0


def _angustia_pose(angle):
    """Right hand on the circle (angle 0 = toward the midline). Back of the hand to the viewer,
    fingers leaning in toward the middle of the chest."""
    a = math.radians(angle)
    at = (_ANGUSTIA_C[0] + _ANGUSTIA_R * math.cos(a), _ANGUSTIA_C[1] + _ANGUSTIA_R * math.sin(a))
    return P(at, _angustia_hs, 'middle_tip', yaw=160, pitch=-10, roll=16, scale=1.05, depth=40,
             pole=(0.5, 1.0, -0.6), ease='linear')


# Counter-clockwise on screen for the right hand (out at the top, down the outer side), the left
# hand mirrors it half a turn later: when one is up, the other is down.
_angustia_keys = [(0.0, [_angustia_pose(-90), mirrored(_angustia_pose(90))])]
_angustia_steps = 16                  # two full circles, 8 steps each
for _angustia_k in range(1, _angustia_steps + 1):
    _angustia_a = -90 - 45 * _angustia_k
    _angustia_keys.append((0.3 + 1.6 * _angustia_k / _angustia_steps,
                           [_angustia_pose(_angustia_a), mirrored(_angustia_pose(_angustia_a + 180))]))
_angustia_keys.append((2.4, _angustia_keys[-1][1]))
SIGNS['angustia'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _angustia_hs,
    'handshape_view': {'yaw': -45},
    'keys': _angustia_keys,
    'marks': [(190, 205, -25), (210, 205, 25)],
    # A small circle above each hand: counter-clockwise for the right hand, clockwise for the left.
    'arrows': [{'d': circle_arrow(150, 186, 11, 0, 90, False)},
               {'d': circle_arrow(250, 186, 11, 180, 90, True)}],
}
TITLES['angustia'] = 'Sinal de angústia em Libras'
