# CRIAR: the support hand stands in a C, palm toward the signing hand. The signing hand, in an O (fingertips
# on the thumb), rubs the backs of its fingers up the support palm and then rises in an arc to the front of
# the chin, opening into a 5 (fingers spread). Once. (UFSC Signbank CRIAR; the INES CRIAR1 video shows
# another variant.)
_criar_o, _criar_5, _criar_c = hs_O(), hs_5(), hs_C()
_criar_pole = (0.4, 1.0, 0.45)
# Support (right-hand pose, mirrored): the C seen from the side, fingers up, palm toward the signing hand.
_criar_base = mirrored(P((162, 214), _criar_c, 'wrist', yaw=90, pitch=0, roll=-6, scale=1.1, depth=60))
# The O seen from the thumb side (its round opening shows), the backs of its fingers toward the support palm.
_criar_o_pose = lambda at, **kw: P(at, _criar_o, 'wrist', yaw=-100, pitch=0, roll=4, scale=1.05, depth=60,
                                   pole=_criar_pole, **kw)
_criar_low = _criar_o_pose((198, 226))
_criar_rub = _criar_o_pose((200, 204), ease='linear')
# Open in front of the chin, palm forward and a little to the side, fingers spread.
_criar_open = P((164, 196), _criar_5, 'wrist', yaw=-30, pitch=0, roll=-4, scale=1.05, depth=50, pole=_criar_pole,
                via=(160, 200), ease='out')
SIGNS['criar'] = {
    'poster': 0.45, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _criar_o, 'handshape_view': {'yaw': -115},
    'keys': [(0.0, [_criar_low, _criar_base]), (0.25, [_criar_low, _criar_base]), (0.6, [_criar_rub, _criar_base]),
             (1.05, [_criar_open, _criar_base]), (1.9, [_criar_open, _criar_base]),
             (2.6, [dict(_criar_low, via=(160, 220), ease='smooth'), _criar_base])],
    'marks': [(206, 238, 180)],
    # Up along the support palm, then out in an arc to the chin.
    'arrows': [{'d': 'M 162 240 Q 134 216 128 176'}],
    'mirror_second': True,
}
TITLES['criar'] = 'Sinal de criar em Libras'
