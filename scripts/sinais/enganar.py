# ENGANAR: the support hand, closed (S), in front of the chest; the signing hand in Y (thumb and little
# finger out) starts on its back. The Y rises to the chin and rests the tip of the thumb on it, the little
# finger pointing to the other side; at the same time the support hand drops to the waist. Once.
# (UFSC Signbank ENGANAR: Y over S, final contact; the INES ENGANAR1 video shows another variant.)

_eng_y, _eng_s = HANDSHAPES['Y'](), hs_S()


def _eng_base(at, ease='smooth'):
    """Support fist, defined as a right hand and mirrored: palm down, knuckles toward the midline."""
    return mirrored(P(at, _eng_s, 'wrist', yaw=125, pitch=0, roll=88, scale=1.08, depth=66, ease=ease))


# On the chin: back of the hand mostly to the viewer, the thumb up with its tip on the chin and the little
# finger out toward the other side; palm turned down and away.
_eng_chin = P((194, 146), _eng_y, 'thumb_tip', yaw=140, pitch=0, roll=92, scale=1.05, depth=40,
              pole=(0.5, 1.0, 0.45), ease='out')
# Start: lying on the back of the support fist, the little finger toward the support side.
_eng_start = P((214, 214), _eng_y, 'thumb_tip', yaw=150, pitch=30, roll=100, scale=1.08, depth=70,
               pole=(0.4, 1.0, 0.4))
_eng_b_hi, _eng_b_lo = _eng_base((172, 230)), _eng_base((166, 282))
SIGNS['enganar'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _eng_y,
    'keys': [(0.0, [_eng_start, _eng_b_hi]), (0.3, [_eng_start, _eng_b_hi]), (0.9, [_eng_chin, _eng_b_lo]),
             (1.8, [_eng_chin, _eng_b_lo]), (2.4, [dict(_eng_start, ease='smooth'), _eng_b_hi])],
    'marks': [(184, 150, -60)],
    # The Y up to the chin; the support fist down to the waist.
    'arrows': [{'d': 'M 172 214 Q 156 186 168 160'}, {'d': 'M 268 222 L 268 262'}],
    'mirror_second': True,
}
TITLES['enganar'] = 'Sinal de enganar em Libras'
