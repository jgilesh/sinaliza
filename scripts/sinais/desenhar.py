# DESENHAR: the support hand stands open (B), fingers up, palm toward the signing hand. The signing hand
# in U (index and middle straight and together) rubs the tips of the two fingers on the support palm in
# short wavy strokes, several times, the eyes on the hands. (UFSC Signbank DESENHAR: U on B, rubbing;
# INES DESENHAR agrees.)


def hs_desenhar_U():
    """U of Libras: index and middle fingers straight and side by side, ring and little fingers folded
    under the thumb."""
    shape = fist({'index': fing(-1, 0, 0, 0), 'middle': fing(1, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


_des_u, _des_b = hs_desenhar_U(), hs_B()
# Support hand (defined as a right hand, then mirrored): fingers up, palm turned toward the signing hand
# and a little toward the viewer, so the fingertips can be seen on it.
_des_base = mirrored(P((150, 238), _des_b, 'wrist', yaw=55, pitch=0, roll=-4, scale=1.05, depth=60))


def _des_pose(x, y, roll):
    # The two fingers level, pointing at the support palm, back of the hand to the viewer: the index and
    # the middle finger lie one above the other, both in view.
    return P((x, y), _des_u, 'fingertips', yaw=150, pitch=0, roll=roll, scale=1.05, depth=58,
             pole=(0.4, 1.0, 0.4), ease='smooth')


_des_strokes = [(240, 194, 86), (243, 202, 96), (240, 210, 86), (243, 218, 96)]   # a wavy line down the palm
_des_off = P((200, 214), _des_u, 'fingertips', yaw=150, pitch=0, roll=92, scale=1.05, depth=58, pole=(0.4, 1.0, 0.4))
_des_keys = [(0.0, [_des_off, _des_base]), (0.25, [_des_off, _des_base])]
_des_t = 0.55
for _des_rep in range(2):
    for _des_i, _des_s in enumerate(_des_strokes if _des_rep == 0 else _des_strokes[::-1]):
        _des_keys.append((round(_des_t, 2), [_des_pose(*_des_s), _des_base]))
        _des_t += 0.17
_des_keys += [(2.05, [_des_pose(*_des_strokes[0]), _des_base]), (2.5, [_des_off, _des_base])]
SIGNS['desenhar'] = {
    'poster': 0.72, 'dur': 2.5, 'hands': ['right', 'left'], 'handshape': _des_u,
    'keys': _des_keys,
    'marks': [(240, 184, 0)],
    # Beside the support hand: the wavy stroke up and down the palm.
    'arrows': [{'d': 'M 288 180 Q 280 192 288 204 Q 296 216 288 228', 'both': True}],
    'mirror_second': True,
}
TITLES['desenhar'] = 'Sinal de desenhar em Libras'
