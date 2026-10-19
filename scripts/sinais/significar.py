# SIGNIFICAR: the support hand stands open and upright in front of the chest, palm toward the
# signing hand. The signing hand, in V lying level (index and middle pointing at the support palm),
# comes in until both fingertips touch that palm, and turns a little there. (UFSC Signbank
# SIGNIFICAR: V on the weak hand's palm (B); INES SIGNIFICAR.)
_sig_v, _sig_b = hs_V(), hs_B()
# Support hand, defined as a right hand (palm toward the midline, turned a little to the viewer) and
# mirrored.
_sig_sup = mirrored(P((180, 240), _sig_b, 'wrist', yaw=62, pitch=0, roll=4, scale=1.05, depth=55))
# Signing hand: back of the hand mostly to the viewer, the two fingers level and apart, one above the
# other, pointing at the support palm.
_sig = lambda at, yaw, anchor='fingertips', **kw: P(at, _sig_v, anchor, yaw=yaw, pitch=0, roll=92, scale=1.05, depth=60,
                                                    pole=(0.3, 1.0, 0.4), **kw)
_sig_far = _sig((96, 228), 140, 'wrist')
_sig_on = _sig((206, 208), 140, ease='out')
_sig_turn = _sig((206, 208), 168)
SIGNS['significar'] = {
    'poster': 0.9, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _sig_v,
    'keys': [(0.0, [_sig_far, _sig_sup]), (0.25, [_sig_far, _sig_sup]), (0.7, [_sig_on, _sig_sup]),
             (0.95, [_sig_turn, _sig_sup]), (1.2, [_sig_on, _sig_sup]), (1.9, [_sig_on, _sig_sup]),
             (2.6, [dict(_sig_far, ease='smooth'), _sig_sup])],
    'arrows': [{'d': 'M 112 186 L 156 186'}],
    'mirror_second': True,
}
TITLES['significar'] = 'Sinal de significar em Libras'
