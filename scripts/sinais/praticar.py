# PRATICAR: the support hand lies flat in front of the chest, palm down, fingers pointing across. The
# dominant hand, also palm down and pointing the other way, turns in vertical circles above it: it
# rises toward the chin bending at the knuckles and comes down flat onto the back of the support
# hand, 2 times. (UFSC Signbank PRATICAR: B+B_curved+B_bent, weak hand's back. The INES PRATICAR
# video brushes the side of the hand along the support forearm instead.)


def hs_praticar_flat():
    """Flat hand, fingers together, the thumb resting alongside the index."""
    return {'index': fing(2, 0, 2, 1), 'middle': fing(0, 0, 2, 1), 'ring': fing(-2, 0, 2, 1),
            'pinky': fing(-4, 0, 3, 2), 'thumb': (6.0, 14.0, 10.0, 6.0, 4.0)}


def hs_praticar_bent():
    """The same hand bent at the knuckles (fingers straight, about a right angle to the palm)."""
    return {'index': fing(2, 62, 8, 5), 'middle': fing(0, 64, 8, 5), 'ring': fing(-2, 64, 8, 5),
            'pinky': fing(-4, 66, 8, 5), 'thumb': (10.0, 18.0, 12.0, 8.0, 6.0)}


_praticar_flat, _praticar_bent = hs_praticar_flat(), hs_praticar_bent()
# Support hand (defined as a right hand, then mirrored): palm down, back of the hand up and a little
# toward the viewer, fingers pointing across toward the signing side.
_praticar_base = mirrored(P((150, 244), _praticar_flat, 'wrist', yaw=115, pitch=0, roll=90, scale=1.05, depth=70))
_PRATICAR_C, _PRATICAR_R = (166.0, 196.0), (10.0, 42.0)


def _praticar_pose(angle):
    """Angle 90 = bottom (flat on the support), 270 = top (by the chin, bent); counter-clockwise on
    screen: up on the inner side, down on the outer side."""
    a = math.radians(angle)
    at = (_PRATICAR_C[0] + _PRATICAR_R[0] * math.cos(a), _PRATICAR_C[1] + _PRATICAR_R[1] * math.sin(a))
    k = (1 - math.sin(a)) / 2                       # 0 at the bottom, 1 at the top
    shape = lerp(_praticar_flat, _praticar_bent, k)
    return P(at, shape, 'wrist', yaw=115, pitch=0, roll=90 - 12 * k, scale=1.05, depth=72, pole=(0.4, 1.0, 0.4),
             ease='linear')


_praticar_keys = [(0.0, [_praticar_pose(90), _praticar_base]), (0.3, [_praticar_pose(90), _praticar_base])]
_praticar_steps = 12                     # two circles, 6 steps each
for _praticar_k in range(1, _praticar_steps + 1):
    _praticar_keys.append((round(0.3 + 1.6 * _praticar_k / _praticar_steps, 3),
                           [_praticar_pose(90 - 60 * _praticar_k), _praticar_base]))
_praticar_keys.append((2.4, [_praticar_pose(90), _praticar_base]))
SIGNS['praticar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _praticar_flat,
    'keys': _praticar_keys,
    'marks': [(252, 226, 40)],
    'arrows': [{'d': circle_arrow(130, 194, 26, 250, 110, False)}],
    'mirror_second': True,
}
TITLES['praticar'] = 'Sinal de praticar em Libras'
