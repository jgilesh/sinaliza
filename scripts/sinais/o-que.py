# O QUE: small beak (thumb and index pinched pad to pad, the other fingers closed) beside the chin, a
# little in front of the face, the pinch up and the palm turned toward the face; the wrist rocks
# side to side a few times. Question face (UFSC Signbank O-QUE).


def hs_o_que_beak():
    """Baby beak: the index bends forward and its pad meets the thumb's pad above the fist."""
    shape = fist({'index': fing(2, 20, 60, 40)})
    shape['thumb'] = pinch_thumb(shape)
    return shape


oq_beak = hs_o_que_beak()
oq_pose = lambda roll: P((172, 142), oq_beak, 'pinch', yaw=42, pitch=0, roll=roll, scale=1.1, depth=40,
                         pole=(0.5, 1.0, 0.45))
oq_mid, oq_in, oq_out = oq_pose(-4), oq_pose(10), oq_pose(-18)
oq_keys = [(0.0, [oq_mid]), (0.2, [oq_mid])]
for k in range(4):
    oq_keys += [(0.3 + 0.3 * k, [oq_out]), (0.45 + 0.3 * k, [oq_in])]
oq_keys += [(1.6, [oq_mid]), (2.2, [oq_mid])]
SIGNS['o-que'] = {
    'poster': 0.0, 'dur': 2.2, 'hands': ['right'], 'handshape': oq_beak, 'handshape_ring': True,
    'handshape_view': {'yaw': 40},
    'keys': oq_keys,
    'arrows': [{'d': 'M 122 136 Q 131 123 146 123', 'both': True}],
}
TITLES['o-que'] = 'Sinal de o que em Libras'
