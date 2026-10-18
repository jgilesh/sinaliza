# DESCULPAR: Y hand (thumb and little finger out), palm toward the body, the little finger pointing to
# the other side and the thumb up beside the cheek; the hand rises and the folded fingers touch under
# the chin, once. (INES and UFSC Signbank agree.)
_desc_y = hs_Y()
_desc_on = P((180, 169), _desc_y, 'wrist', yaw=160, pitch=0, roll=80, scale=1.05, depth=40, pole=(0.5, 1.0, 0.45))
_desc_low = P((172, 205), _desc_y, 'wrist', yaw=160, pitch=-10, roll=70, scale=1.05, depth=55, pole=(0.5, 1.0, 0.45))
SIGNS['desculpar'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right'], 'handshape': _desc_y,
    'keys': [(0.0, [_desc_low]), (0.25, [_desc_low]), (0.75, [_desc_on]), (1.9, [_desc_on]), (2.4, [_desc_low])],
    'marks': [(222, 143, 60)],
}
TITLES['desculpar'] = 'Sinal de desculpar em Libras'
