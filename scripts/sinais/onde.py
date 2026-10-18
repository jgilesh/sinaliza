# ONDE: both hands in a small L (thumb up, index out and a little curved, the other fingers closed) in
# front of the chest, the index fingers pointing forward and in toward each other, palms facing in;
# the hands go down a little in small shakes, two or three times. Question face (INES ONDE and UFSC
# Signbank agree; drawn with the index fingers turned a little inward so they read full length).
onde_l = hs_L((6, 22, 14))
onde_pose = lambda y: P((176, y), onde_l, 'index_tip', yaw=-180, pitch=38, roll=86, scale=1.18, depth=75,
                        pole=(0.3, 1.0, 0.4))
onde_keys = [(0.0, [onde_pose(196), mirrored(onde_pose(196))]), (0.25, [onde_pose(196), mirrored(onde_pose(196))])]
y, t = 196, 0.25
for k in range(3):
    y += 9
    t += 0.14
    onde_keys.append((t, [dict(onde_pose(y), ease='out'), dict(mirrored(onde_pose(y)), ease='out')]))
    t += 0.12
    onde_keys.append((t, [onde_pose(y - 3), mirrored(onde_pose(y - 3))]))
onde_keys += [(1.6, [onde_pose(y - 3), mirrored(onde_pose(y - 3))]), (2.2, [onde_pose(196), mirrored(onde_pose(196))])]
SIGNS['onde'] = {
    'poster': 0.4, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': onde_l, 'handshape_view': {'yaw': -20},
    'keys': onde_keys,
    'arrows': [{'d': 'M 90 186 L 90 220'}, {'d': 'M 310 186 L 310 220'}],
    'mirror_second': True,
}
TITLES['onde'] = 'Sinal de onde em Libras'
