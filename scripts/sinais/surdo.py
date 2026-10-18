# SURDO: the index (hand 1) touches the ear, then moves down and touches the chin, beside the
# mouth. (INES SURDO1 and UFSC Signbank agree.)
surdo_hs = hs_1()
surdo_ear = P((157, 104), surdo_hs, 'index_tip', yaw=-25, pitch=0, roll=18, scale=1.0, depth=35, pole=(0.6, 1.0, 0.45))
surdo_chin = P((191, 141), surdo_hs, 'index_tip', yaw=160, pitch=-10, roll=82, scale=1.0, depth=40, via=(150, 132),
               pole=(0.6, 1.0, 0.45))
surdo_back = dict(surdo_ear, via=(140, 150))
SIGNS['surdo'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right'], 'handshape': surdo_hs,
    'keys': [(0.0, [surdo_ear]), (0.45, [surdo_ear]), (0.95, [surdo_chin]), (1.8, [surdo_chin]), (2.4, [surdo_back])],
    'marks': [(152, 100, -60), (194, 148, 160)],
    'arrows': [{'d': 'M 167 113 Q 166 131 181 136', 'cap': True}],
}
TITLES['surdo'] = 'Sinal de surdo em Libras'
