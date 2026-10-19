# INCLUIR: the support hand is open with the fingers spread, in front of the belly, palm toward the
# body and down, fingers pointing across toward the dominant side. The dominant hand, also open and
# spread, comes from the side with the fingers pointing down and goes down, fitting its fingers
# between the fingers of the support hand, then stops. (UFSC Signbank INCLUIR-2; INES INCLUIR is
# similar, both hands spread.)
_incluir_5 = hs_5()
# Support (defined as a right hand, then mirrored): the back of the hand toward the viewer and up,
# the spread fingers pointing across toward the midline.
_incluir_sup = mirrored(P((116, 254), _incluir_5, 'wrist', yaw=150, pitch=0, roll=90, scale=1.05, depth=60))


def _incluir_dom(at, ease='smooth', via=None):
    # Back of the hand to the viewer, the spread fingers pointing down.
    pose = P(at, _incluir_5, 'fingertips', yaw=172, pitch=0, roll=176, scale=1.05, depth=70, pole=(0.35, 1.0, 0.4),
             ease=ease)
    if via:
        pose['via'] = via
    return pose


_incluir_start = _incluir_dom((168, 214))
_incluir_end = _incluir_dom((216, 270), 'out', via=(208, 214))
SIGNS['incluir'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _incluir_5,
    'keys': [(0.0, [_incluir_start, _incluir_sup]), (0.4, [_incluir_start, _incluir_sup]),
             (1.0, [_incluir_end, _incluir_sup]), (1.9, [_incluir_end, _incluir_sup]),
             (2.4, [dict(_incluir_start), _incluir_sup])],
    # Across and down into the support hand, above the moving hand.
    'arrows': [{'d': 'M 150 150 Q 226 140 250 192'}],
    'mirror_second': True,
}
TITLES['incluir'] = 'Sinal de incluir em Libras'
