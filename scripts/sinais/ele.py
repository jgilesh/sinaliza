# ELE / ELA: index hand (1) out to the signer's right side, a little forward, between shoulder and face
# height; the index points at the place of the person being talked about with a short push, once.
# Palm toward the viewer, thumb up, so the index reads full length beside the folded fingers (INES: ELE).
ele_one = hs_1()
ele_pose = lambda at, scale, pitch: P(at, ele_one, 'index_tip', yaw=0, pitch=pitch, roll=-84, scale=scale, depth=70,
                                      pole=(1.0, 0.7, 0.0))
ele_back = ele_pose((60, 172), 1.1, 15)
ele_out = ele_pose((44, 168), 1.16, 22)
SIGNS['ele'] = {
    'poster': 0.8, 'dur': 2.0, 'hands': ['right'], 'handshape': ele_one,
    'keys': [(0.0, [ele_back]), (0.25, [ele_back]), (0.5, [dict(ele_out, ease='out')]), (1.5, [ele_out]),
             (2.0, [ele_back])],
    'arrows': [{'d': 'M 62 150 L 38 148'}],
}
TITLES['ele'] = 'Sinal de ele em Libras'
