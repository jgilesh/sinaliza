# HOSPITAL: the index (hand 1) draws a cross on the forehead: first a line from top to bottom,
# then a line from side to side. The hand comes from the side, so the face stays clear.
# (INES HOSPITAL and UFSC Signbank agree.)
_hos_hs = hs_1()
_hos_pose = lambda at, roll=72, **kw: P(at, _hos_hs, 'index_tip', yaw=-10, pitch=0, roll=roll, scale=0.95, depth=40,
                                          pole=(0.7, 1.0, 0.45), **kw)
_hos_top, _hos_low = _hos_pose((199, 54), 62), _hos_pose((199, 82), 80)
_hos_left, _hos_right = _hos_pose((185, 69), 74), _hos_pose((215, 69), 74)
SIGNS['hospital'] = {
    'poster': 0.85, 'dur': 2.6, 'hands': ['right'], 'handshape': _hos_hs,
    'keys': [(0.0, [_hos_top]), (0.3, [_hos_top]), (0.7, [_hos_low]), (0.95, [_hos_left]), (1.35, [_hos_right]),
             (2.0, [_hos_right]), (2.6, [_hos_top])],
    'marks': [(190, 50, -35)],
    'arrows': [{'d': 'M 202 50 L 202 88', 'cap': True}, {'d': 'M 187 68 L 220 68', 'cap': True}],
}
TITLES['hospital'] = 'Sinal de hospital em Libras'
