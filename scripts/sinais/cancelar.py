# CANCELAR: with the index straight (1), the hand draws a big X in the air in front of the body: one
# stroke from high up on the signing side down to low on the other side, then a second stroke from high
# up on the other side down to low on the signing side; the index ends each stroke pointing down. Once.
# No contact. (UFSC Signbank CANCELAR; the INES CANCELAR video shows another, quicker variant.)
_cancelar_1 = hs_1()
_cancelar_pole = (0.4, 1.0, 0.5)
_cancelar = lambda at, yaw, pitch, roll, **kw: P(at, _cancelar_1, 'index_tip', yaw=yaw, pitch=pitch, roll=roll, scale=1.1,
                                                 depth=kw.pop('depth', 60), pole=_cancelar_pole, **kw)
# Stroke 1: high on the signing side (index up, palm forward) -> low on the other side (index down).
_cancelar_a = _cancelar((120, 112), -20, 0, -14)
_cancelar_b = _cancelar((232, 246), 25, 0, 160, ease='linear', depth=70)
# Stroke 2: high on the other side (index up and out) -> low on the signing side (index down).
_cancelar_c = _cancelar((276, 116), -10, 0, 30, via=(276, 190))
_cancelar_d = _cancelar((140, 250), 10, 0, 195, ease='linear', depth=70)
SIGNS['cancelar'] = {
    'poster': 0.3, 'dur': 3.0, 'hands': ['right'], 'handshape': _cancelar_1,
    'keys': [(0.0, [_cancelar_a]), (0.3, [_cancelar_a]), (0.9, [_cancelar_b]), (1.0, [_cancelar_b]),
             (1.45, [_cancelar_c]), (1.55, [_cancelar_c]), (2.15, [_cancelar_d]), (2.5, [_cancelar_d]),
             (3.0, [dict(_cancelar_a, via=(104, 190))])],
    # The X: two crossing strokes, each beside the fingertip's path (above it), so the hand stays clear.
    'arrows': [{'d': 'M 150 134 L 238 230'}, {'d': 'M 250 134 L 156 236'}],
}
TITLES['cancelar'] = 'Sinal de cancelar em Libras'
