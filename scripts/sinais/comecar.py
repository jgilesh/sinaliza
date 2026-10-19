# COMEÇAR: the support hand lies open, palm up, in front of the body, fingers toward the signing side.
# The signing hand, flat with the thumb up (palm toward the body, fingers toward the other side), rests
# its little-finger edge on the support palm and slides along it from the heel to the fingertips,
# once. (UFSC Signbank COMEÇAR; the INES COMEÇAR1 video shows another form.)

_comecar_b = hs_B()


def hs_comecar_thumb_up():
    """B with the thumb raised: fingers together and straight, the thumb up and apart from the index."""
    shape = hs_B()
    shape['thumb'] = (30.0, 6.0, 0.0, 4.0, 2.0)
    return shape


_comecar_t = hs_comecar_thumb_up()
# Support hand (a right-hand pose, mirrored): palm up, tipped toward the viewer, fingers toward the
# signing side.
_comecar_base = mirrored(P((150, 238), _comecar_b, 'wrist', yaw=-38, pitch=0, roll=96, scale=1.05, depth=55))
# Signing hand on its edge: back of the hand to the viewer, fingers toward the other side, thumb up.
_comecar_pole = (0.35, 1.0, 0.4)
_comecar_on = P((198, 220), _comecar_t, 'wrist', yaw=200, pitch=0, roll=88, scale=1.0, depth=62, pole=_comecar_pole)
_comecar_off = dict(_comecar_on, at=(146, 220), ease='linear')
SIGNS['comecar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _comecar_t, 'handshape_view': {'yaw': 15},
    'keys': [(0.0, [_comecar_on, _comecar_base]), (0.35, [_comecar_on, _comecar_base]),
             (1.05, [_comecar_off, _comecar_base]), (1.8, [_comecar_off, _comecar_base]),
             (2.4, [dict(_comecar_on, ease='smooth'), _comecar_base])],
    'arrows': [{'d': 'M 236 274 L 176 274'}],
    'marks': [(254, 238, 160)],
    'mirror_second': True,
}
TITLES['comecar'] = 'Sinal de começar em Libras'
