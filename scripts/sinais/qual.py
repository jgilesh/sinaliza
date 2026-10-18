# QUAL: both hands with the index up (1) in front of the chest, palms toward the body and a little toward
# each other; the hands go up and down alternately, two or three times, as if weighing the options.
# Question face, cheeks puffing (UFSC Signbank QUAL-2; the INES QUAL1 video shows another variant).
ql_one = hs_1()
ql_pose = lambda y: P((152, y), ql_one, 'index_tip', yaw=150, pitch=-5, roll=4, scale=1.12, depth=60,
                      pole=(0.25, 1.0, 0.45))
QL_Y, QL_D = 176, 11
ql_keys = [(0.0, [ql_pose(QL_Y), mirrored(ql_pose(QL_Y))]), (0.2, [ql_pose(QL_Y), mirrored(ql_pose(QL_Y))])]
for k in range(3):
    t = 0.2 + 0.5 * k
    ql_keys += [(t + 0.25, [ql_pose(QL_Y - QL_D), mirrored(ql_pose(QL_Y + QL_D))]),
                (t + 0.5, [ql_pose(QL_Y + QL_D), mirrored(ql_pose(QL_Y - QL_D))])]
ql_keys += [(2.2, [ql_pose(QL_Y), mirrored(ql_pose(QL_Y))])]
SIGNS['qual'] = {
    'poster': 0.45, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': ql_one,
    'keys': ql_keys,
    'arrows': [{'d': 'M 114 166 L 114 204', 'both': True}, {'d': 'M 286 166 L 286 204', 'both': True}],
    'mirror_second': True,
}
TITLES['qual'] = 'Sinal de qual em Libras'
