# ESTRANHO: closed fist (S) in front of the chest, palm toward the body; the hand rises in a straight
# line to beside the face and the index finger opens upward on the way (S to 1), once. Face: puzzled.
# (UFSC Signbank ESTRANHO: S+1, para cima.)
_estr_s, _estr_1 = hs_S(), hs_1()
# Back of the hand to the viewer (palm toward the body), turned a little toward the thumb side so the
# folded fingers and the thumb read; at the end the index stands up beside the cheek.
_estr_low = P((170, 236), _estr_s, 'wrist', yaw=215, pitch=0, roll=4, scale=1.05, depth=55, pole=(0.45, 1.0, 0.45))
_estr_mid = P((160, 196), lerp(_estr_s, _estr_1, 0.5), 'wrist', yaw=215, pitch=0, roll=0, scale=1.05, depth=50,
              pole=(0.45, 1.0, 0.45), ease='linear')
_estr_up = P((150, 160), _estr_1, 'wrist', yaw=215, pitch=0, roll=-4, scale=1.05, depth=45, pole=(0.45, 1.0, 0.45),
             ease='out')
SIGNS['estranho'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right'], 'handshape': _estr_1,
    'keys': [(0.0, [_estr_low]), (0.3, [_estr_low]), (0.65, [_estr_mid]), (0.95, [_estr_up]), (1.9, [_estr_up]),
             (2.4, [_estr_low])],
    'arrows': [{'d': 'M 126 240 L 118 176'}],
}
TITLES['estranho'] = 'Sinal de estranho em Libras'
