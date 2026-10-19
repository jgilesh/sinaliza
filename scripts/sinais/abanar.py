# ABANAR: hand in 4 (four fingers straight and apart, thumb folded on the palm) beside the neck on the
# signing side, palm toward the face; the wrist bends back and forth, fanning the face, several times.
# (UFSC Signbank ABANAR: 4, flexion/extension, repeated. The INES ABANAR video shows a closed hand, as
# if holding a fan.)


def hs_abanar_4():
    """4: index, middle, ring and little fingers straight and spread; the thumb folded across the palm,
    its pad on the palm below the ring finger."""
    shape = {'index': fing(10, 0, 2, 1), 'middle': fing(2, 0, 2, 1), 'ring': fing(-7, 0, 2, 1),
             'pinky': fing(-16, 0, 3, 2)}
    target = (-3.0, -20.0, PALM_HALF_THICKNESS + seg_radius('thumb', 2) + 0.6)
    shape['thumb'] = solve_thumb(target, pad_to=(0.0, 0.0, -1.0), point=(-1.0, -0.6, 0.0),
                                 pref=(-15.0, 50.0, 60.0, 30.0, 30.0), w_point=120.0)
    return shape


_aba_4 = hs_abanar_4()
# Palm turned toward the face and a little toward the viewer, so the four spread fingers read; the
# wrist stays beside the neck while the hand swings (yaw and roll) toward the face and back.
_aba = lambda yaw, roll: P((126, 170), _aba_4, 'wrist', yaw=yaw, pitch=0, roll=roll, scale=1.0, depth=40,
                           pole=(0.6, 1.0, 0.45))
_aba_out, _aba_in = _aba(28, -22), _aba(62, 4)
_aba_keys = [(0.0, [_aba_out]), (0.25, [_aba_out])]
for _aba_k in range(3):
    _aba_keys += [(0.25 + 0.36 * _aba_k + 0.18, [_aba_in]), (0.25 + 0.36 * _aba_k + 0.36, [_aba_out])]
_aba_keys.append((2.0, [_aba_out]))
SIGNS['abanar'] = {
    'poster': 0.0, 'dur': 2.0, 'hands': ['right'], 'handshape': _aba_4, 'handshape_view': {'yaw': 10},
    'keys': _aba_keys,
    # Above the fingertips: the hand swings toward the face and back.
    'arrows': [{'d': 'M 96 92 Q 118 76 142 86', 'both': True}],
}
TITLES['abanar'] = 'Sinal de abanar em Libras'
