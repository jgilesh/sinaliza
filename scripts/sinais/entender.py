# ENTENDER: flat hand (B), the fingertips on the temple on the signing side, palm turned down and
# toward the face; the hand stays there and turns a little on the wrist, back and forth.
# (UFSC Signbank ENTENDER, INES ENTENDER.)

_entender_b = hs_B()


def _entender_pose(yaw, roll):
    return P((161, 77), _entender_b, 'fingertips', yaw=yaw, pitch=-10, roll=roll, scale=1.05, depth=40,
             pole=(0.75, 1.0, 0.45))


_entender_a, _entender_b2 = _entender_pose(150, 70), _entender_pose(122, 62)
SIGNS['entender'] = {
    'poster': 0.4, 'dur': 2.4, 'hands': ['right'], 'handshape': _entender_b,
    'keys': [(0.0, [_entender_a]), (0.4, [_entender_a]), (0.7, [_entender_b2]), (1.0, [_entender_a]),
             (1.3, [_entender_b2]), (1.6, [_entender_a]), (2.4, [_entender_a])],
    'marks': [(170, 70, -50)],
    'arrows': [{'twist': 0, 'at': 0.4, 'r': (15, 6), 'drop': 6}],
}
TITLES['entender'] = 'Sinal de entender em Libras'
