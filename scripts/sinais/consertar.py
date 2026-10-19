# CONSERTAR: the support hand holds the index out sideways (1), in front of the chest. The signing hand
# in V fits over it, the support index between its two fingers, and turns the wrist one way and the
# other, rubbing it, a few times, like turning a screw. (UFSC Signbank CONFIGURAR/consertar: V on 1,
# esfregar + contínuo, supinação; INES CONSERTAR.)


def hs_consertar_V():
    """V: index and middle straight and apart, the others folded under the thumb."""
    shape = fist({'index': fing(12, 0, 0, 0), 'middle': fing(-10, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


_con_v, _con_one = hs_consertar_V(), hs_1()
# Support hand (defined as a right hand, then mirrored): the index pointing across toward the midline,
# the back of the hand to the viewer.
_con_base = mirrored(P((150, 240), _con_one, 'wrist', yaw=-150, pitch=0, roll=90, scale=1.05, depth=65))
# Signing hand: the V hanging over the support index, the back of the hand to the viewer and the
# fingertips tipped a little toward the viewer; the wrist turns (yaw about the forearm) one way and back.
_con_pose = lambda yaw: P((206, 236), _con_v, 'fingertips', yaw=yaw, pitch=25, roll=158, scale=1.05, depth=72,
                          pole=(0.9, 0.6, 0.5))
_con_mid, _con_a, _con_b = _con_pose(180), _con_pose(148), _con_pose(212)
_con_keys = [(0.0, [_con_mid, _con_base]), (0.3, [_con_mid, _con_base])]
for _con_k in range(2):                    # two turns each way
    _con_t = 0.3 + 0.6 * _con_k
    _con_keys += [(round(_con_t + 0.15, 2), [_con_a, _con_base]), (round(_con_t + 0.45, 2), [_con_b, _con_base]),
                  (round(_con_t + 0.6, 2), [_con_mid, _con_base])]
_con_keys.append((2.1, [_con_mid, _con_base]))
SIGNS['consertar'] = {
    'poster': 0.3, 'dur': 2.1, 'hands': ['right', 'left'], 'handshape': _con_v,
    'keys': _con_keys,
    'arrows': [{'d': 'M 170 161 Q 186 149 203 158', 'both': True}],   # the wrist turns one way and the other
    'mirror_second': True,
}
TITLES['consertar'] = 'Sinal de consertar em Libras'
