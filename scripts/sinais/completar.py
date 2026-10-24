# COMPLETAR: both hands in C start apart at chest height, palms toward each other, and meet in front of
# the chest; then they cross toward the body, rubbing by the thumb side: the support hand ends lying on
# the dominant side, palm down, and the signing hand upright on the other side, the forearms in an X.
# Once. (UFSC Signbank COMPLETAR "C" on "C", rubbing at the thumb side; INES COMPLETAR agrees.)

_completar_c = hs_C()
_completar_pole = (0.4, 1.0, 0.45)


def _completar_pose(at, yaw, roll, depth, pitch=0, **kw):
    return P(at, _completar_c, 'wrist', yaw=yaw, pitch=pitch, roll=roll, scale=1.05, depth=depth, pole=_completar_pole, **kw)


# Signing hand: apart (palm toward the midline, the C seen nearly side-on) -> meeting the other hand in
# front of the chest -> upright on the other side, palm toward the midline, nearer the viewer.
_completar_r_apart = _completar_pose((128, 228), 62, -4, 55)
_completar_r_meet = _completar_pose((176, 228), 70, 0, 66)
_completar_r_end = _completar_pose((228, 232), -80, 10, 82, ease='smooth')
# Support hand (defined as a right hand, then mirrored): apart and meeting like the signing hand, then it
# goes over to the dominant side and lies palm down, the fingers curved down and pointing outward.
_completar_l_apart = mirrored(_completar_pose((128, 228), 62, -4, 55))
_completar_l_meet = mirrored(_completar_pose((176, 232), 70, 0, 60))
_completar_l_end = mirrored(_completar_pose((210, 226), 95, 92, 58, ease='smooth'))
_completar_keys = [(0.0, [_completar_r_apart, _completar_l_apart]), (0.3, [_completar_r_apart, _completar_l_apart]),
                   (0.75, [_completar_r_meet, _completar_l_meet]), (0.85, [_completar_r_meet, _completar_l_meet]),
                   (1.4, [_completar_r_end, _completar_l_end]), (2.1, [_completar_r_end, _completar_l_end]),
                   (2.7, [dict(_completar_r_apart, ease='smooth'), dict(_completar_l_apart, ease='smooth')])]
SIGNS['completar'] = {
    'poster': 1.6, 'dur': 2.7, 'hands': ['right', 'left'], 'handshape': _completar_c, 'handshape_view': {'yaw': 60},
    'keys': _completar_keys,
    'marks': [(200, 192, 0)],
    'arrows': [{'trail': 0, 'from': 0.85, 'to': 1.4, 'offset': (0, 54), 'trim': 0.1},
               {'trail': 1, 'from': 0.85, 'to': 1.4, 'offset': (0, 42), 'trim': 0.1}],
    'mirror_second': False,   # the support hand, lying on the dominant side at the end, is drawn over the signing arm
}
TITLES['completar'] = 'Sinal de completar em Libras'
