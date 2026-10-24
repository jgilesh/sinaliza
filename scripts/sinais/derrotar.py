# DERROTAR: the support forearm lies across in front of the waist, hand flat, palm down. The dominant
# hand, flat (B), starts up beside the head, palm forward; it comes down in an arc across the body,
# lies flat for a moment over the support arm, then stands up on the elbow: the forearm upright, the
# elbow resting on the support hand, the palm toward the face. Once. (UFSC Signbank DERROTAR: B, both
# hands, final contact on the arm; the INES video shows another variant.)

_der_b = hs_B()
# Support (defined as a right hand, then mirrored): palm down, fingers across toward the other side.
_der_sup = mirrored(P((214, 262), _der_b, 'wrist', yaw=115, pitch=-20, roll=88, scale=1.05, depth=75))
# Dominant: up beside the head, palm forward, fingers up.
_der_up = P((112, 132), _der_b, 'wrist', yaw=10, pitch=0, roll=-12, scale=1.05, depth=55, pole=(0.7, 1.0, 0.45))
# Lying flat over the support arm, palm down, fingers across.
_der_flat = P((150, 232), _der_b, 'wrist', yaw=110, pitch=-20, roll=88, scale=1.08, depth=95, pole=(0.3, 1.0, 0.5),
              via=(108, 200))
# Standing up on the elbow: the forearm upright, back of the hand to the viewer, palm toward the face,
# the hand below the eyes.
_der_stand = P((158, 186), _der_b, 'wrist', yaw=170, pitch=0, roll=2, scale=1.05, depth=150, pole=(-0.25, 1.0, 0.2))
SIGNS['derrotar'] = {
    'poster': 1.5, 'dur': 2.8, 'hands': ['right', 'left'], 'handshape': _der_b,
    'keys': [(0.0, [_der_up, _der_sup]), (0.3, [_der_up, _der_sup]), (0.9, [_der_flat, _der_sup]),
             (1.3, [_der_stand, _der_sup]), (2.2, [_der_stand, _der_sup]),
             (2.8, [dict(_der_up, via=(110, 190)), _der_sup])],
    'marks': [(144, 270, -90)],
    'arrows': [{'d': 'M 96 104 Q 84 190 140 220'}],
    'mirror_second': True,   # the dominant arm in front: its elbow rests on the support hand
}
TITLES['derrotar'] = 'Sinal de derrotar em Libras'
