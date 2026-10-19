# ENGORDAR: both hands closed (S), one above the other in front of the chest, palms toward the body
# (like holding a pole); they move apart at the same time, the dominant hand out and up, the other out
# and down, opening the arms. Cheeks puffed. No contact. (UFSC Signbank ENGORDAR: S+S; INES ENGORDAR
# moves the fists apart side by side.)
_engordar_s = hs_S()


def _engordar_pose(at, yaw=228, roll=84, scale=1.1, depth=60, ease='smooth'):
    # Back of the hand to the viewer, knuckles toward the midline, turned a little on the forearm so the
    # thumb shows on top of the fist.
    return P(at, _engordar_s, 'wrist', yaw=yaw, pitch=0, roll=roll, scale=scale, depth=depth, ease=ease,
             pole=(0.5, 1.0, 0.4))


_engordar_r0 = _engordar_pose((166, 202))
_engordar_l0 = mirrored(_engordar_pose((166, 238)))
_engordar_r1 = _engordar_pose((104, 176), yaw=210, roll=40, depth=55, ease='out')
_engordar_l1 = mirrored(_engordar_pose((112, 266), yaw=210, roll=70, depth=55, ease='out'))
SIGNS['engordar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _engordar_s,
    'keys': [(0.0, [_engordar_r0, _engordar_l0]), (0.4, [_engordar_r0, _engordar_l0]),
             (1.0, [_engordar_r1, _engordar_l1]), (1.8, [_engordar_r1, _engordar_l1]),
             (2.4, [dict(_engordar_r0, ease='smooth'), dict(_engordar_l0, ease='smooth')])],
    # Outward from each fist: the dominant hand out and up, the other out and down.
    'arrows': [{'d': 'M 150 186 Q 128 176 112 160'}, {'d': 'M 252 252 Q 272 262 290 262'}],
    'mirror_second': True,
}
TITLES['engordar'] = 'Sinal de engordar em Libras'
