# TORCER (tomara): both hands with the index and middle fingers crossed (R), the other fingers folded
# under the thumb, raised beside the face at cheek height, palms forward; they shake a little in
# place, several times. (UFSC Signbank TORCER: R+R, plano paralelo; INES TOMARA shows the same sign.)


def hs_torcer_r():
    """R: index and middle up and crossed. The index bends a little at the knuckle (toward the palm),
    so it lies in front of the middle finger, which leans over toward the thumb side behind it and
    shows above it; ring and little finger folded under the thumb."""
    shape = fist({'index': fing(-17, 18, 6, 4), 'middle': fing(20, -6, 4, 2)})
    shape['thumb'] = thumb_over(shape, ['ring', 'pinky'])
    return shape


_torcer_r = hs_torcer_r()


def _torcer_pose(dx, roll):
    return P((134 + dx, 140), _torcer_r, 'wrist', yaw=8, pitch=0, roll=-6 + roll, scale=1.0, depth=55,
             pole=(0.6, 1.0, 0.4), ease='smooth')


_torcer_a, _torcer_b = _torcer_pose(-2, -5), _torcer_pose(2, 5)
_torcer_keys = [(0.0, [_torcer_pose(0, 0), mirrored(_torcer_pose(0, 0))])]
for _torcer_i in range(3):
    _torcer_t = 0.35 + 0.3 * _torcer_i
    _torcer_keys += [(_torcer_t, [_torcer_a, mirrored(_torcer_a)]), (_torcer_t + 0.15, [_torcer_b, mirrored(_torcer_b)])]
_torcer_keys += [(1.5, [_torcer_pose(0, 0), mirrored(_torcer_pose(0, 0))]),
                 (2.0, [_torcer_pose(0, 0), mirrored(_torcer_pose(0, 0))])]
SIGNS['torcer'] = {
    'poster': 0.0, 'dur': 2.0, 'hands': ['right', 'left'], 'handshape': _torcer_r, 'handshape_view': {'yaw': 0},
    'keys': _torcer_keys,
    # Short two-headed arcs above the fingertips: a small shake.
    'arrows': [{'d': 'M 122 56 Q 134 50 146 56', 'both': True}, {'d': 'M 254 56 Q 266 50 278 56', 'both': True}],
    'mirror_second': True,
}
TITLES['torcer'] = 'Sinal de torcer em Libras'
