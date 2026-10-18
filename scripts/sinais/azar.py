# AZAR: Y hand, palm toward the face, the little finger pointing to the other side and the thumb up;
# the hand moves back and the backs of the folded middle fingers touch the nose, once. (INES and UFSC
# Signbank agree.)
_azar_y = hs_Y()
_azar_on = P((164, 114), _azar_y, 'wrist', yaw=160, pitch=0, roll=80, scale=1.05, depth=30, pole=(0.5, 1.0, 0.45))
_azar_off = P((158, 131), _azar_y, 'wrist', yaw=160, pitch=-10, roll=75, scale=1.15, depth=70, pole=(0.5, 1.0, 0.45))
SIGNS['azar'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right'], 'handshape': _azar_y,
    'keys': [(0.0, [_azar_off]), (0.3, [_azar_off]), (0.7, [_azar_on]), (1.9, [_azar_on]), (2.4, [_azar_off])],
    'marks': [(234, 98, 60)],
}
TITLES['azar'] = 'Sinal de azar em Libras'
