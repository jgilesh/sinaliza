# DESTRUIR: both hands open with the fingers spread (5), crossed palm against palm on the side of the
# support hand (the dominant on top, palm down; the support hand under it, palm up). Together they go
# down and forward on a diagonal to the dominant side, turning one against the other, once. Tense face
# (not drawn). (UFSC Signbank DESTRUIR: 5, 2s, para a frente, rotação. The INES DESTRUIR1 video shows
# another variant: one closed hand rising across the body.)
_des_5 = hs_5()
_des_pole = (0.45, 1.0, 0.4)
# Start, on the support side: the dominant hand palm down, fingers toward the support side, the back
# tipped up toward the viewer; the support hand (written as a right hand, then mirrored) palm up and
# tipped toward the viewer, fingers toward the dominant side, under it.
_des_r0 = P((206, 216), _des_5, 'wrist', yaw=128, pitch=0, roll=72, scale=1.0, depth=70, pole=_des_pole)
_des_l0 = mirrored(P((122, 210), _des_5, 'wrist', yaw=-52, pitch=0, roll=58, scale=1.0, depth=62))
# End, low and forward on the dominant side (nearer the viewer: bigger): the pair has turned together
# a quarter of the way (clockwise on screen), the palms still together.
_des_r1 = P((131, 232), _des_5, 'wrist', yaw=135, pitch=0, roll=97, scale=1.12, depth=100, pole=_des_pole,
            ease='in')
_des_l1 = mirrored(P((201, 257), _des_5, 'wrist', yaw=-58, pitch=0, roll=33, scale=1.1, depth=92, ease='in'))
SIGNS['destruir'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _des_5,
    'keys': [(0.0, [_des_r0, _des_l0]), (0.3, [_des_r0, _des_l0]), (0.85, [_des_r1, _des_l1]),
             (1.8, [_des_r1, _des_l1]), (2.4, [dict(_des_r0, ease='smooth'), dict(_des_l0, ease='smooth')])],
    'arrows': [{'d': 'M 274 246 Q 236 276 160 282'}],
    'mirror_second': True,
}
TITLES['destruir'] = 'Sinal de destruir em Libras'
