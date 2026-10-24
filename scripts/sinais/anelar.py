# ANELAR (dedo anelar): the support hand stands open with the fingers spread (5), palm toward the body,
# fingers up, just below the chin (lowered a little so the face stays clear). The dominant index (1) touches the tip of the support hand's ring finger,
# two times. (UFSC Signbank BOIA-ANELAR "anelar, anular": 1 on 5, mão fraca dedo anelar, contato duplo.
# The INES headword ANULAR1 is the other word, "anular" = to cancel.)
_anel_1, _anel_5 = hs_1(), hs_5()
# Support hand (written as a right hand, then mirrored): back of the hand to the viewer, fingers up,
# spread, beside the chin on the support side (the face stays clear).
_anel_base = mirrored(P((168, 232), _anel_5, 'wrist', yaw=180, pitch=0, roll=4, scale=1.1, depth=55))
# Dominant index: from below on its own side, pointing up and across at the ring fingertip; palm
# turned toward the viewer's right, so the index reads from its knuckle.
_anel_tip = (213, 157)   # the ring fingertip (the support hand's little finger is nearest the midline)
_anel_on = P(_anel_tip, _anel_1, 'index_tip', yaw=-20, pitch=0, roll=72, scale=1.05, depth=70, pole=(0.35, 1.0, 0.4))
_anel_off = dict(_anel_on, at=(_anel_tip[0] - 22, _anel_tip[1] + 7))
SIGNS['anelar'] = {
    'poster': 0.5, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _anel_1, 'handshape_view': {'yaw': 0},
    'keys': [(0.0, [_anel_off, _anel_base]), (0.3, [_anel_off, _anel_base]), (0.5, [_anel_on, _anel_base]),
             (0.7, [_anel_off, _anel_base]), (0.9, [_anel_on, _anel_base]), (1.1, [_anel_off, _anel_base]),
             (2.2, [_anel_off, _anel_base])],
    'marks': [(_anel_tip[0] + 3, _anel_tip[1] - 4, 8)],
    'mirror_second': True,
}
TITLES['anelar'] = 'Sinal de anelar em Libras'
