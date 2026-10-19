# IMPRIMIR: the support hand open (B), upright on its own side, palm turned toward the dominant hand.
# In front of that palm the dominant index, straight with its tip curled, palm down and pointing at
# the support palm, makes small side-to-side moves while it steps down, like a printer head.
# (UFSC Signbank IMPRIMIR: 1_curved + B, 2a; INES IMPRIMIR1.)
_imp_b, _imp_1 = hs_B(), hs_1_curved()
# Support (left) hand at its screen place, orientation written as a right hand (mirrored when drawn).
_imp_base = P((262, 252), _imp_b, 'wrist', yaw=70, pitch=-4, roll=2, scale=1.1, depth=70, pole=(0.3, 1.0, 0.4))
_imp_dom = lambda x, y, **kw: P((x, y), _imp_1, 'index_tip', yaw=150, pitch=0, roll=90, scale=1.1, depth=80,
                                pole=(0.45, 1.0, 0.45), ease='linear', **kw)
_imp_keys = [(0.0, [_imp_dom(240, 196), _imp_base]), (0.3, [_imp_dom(240, 196), _imp_base])]
_imp_t = 0.3
for _imp_k in range(1, 7):
    _imp_t += 0.18
    _imp_keys.append((_imp_t, [_imp_dom(240 - 8 * (_imp_k % 2), 196 + 6 * _imp_k), _imp_base]))
_imp_keys += [(2.0, [_imp_dom(240, 232), _imp_base]), (2.5, [_imp_dom(240, 196), _imp_base])]
SIGNS['imprimir'] = {
    'poster': 0.3, 'dur': 2.5, 'hands': ['right', 'left'], 'handshape': _imp_1, 'handshape_view': {'yaw': -30, 'pitch': -25},
    'keys': _imp_keys,
    'mirror_second': True,
    'arrows': [{'d': 'M 292 196 L 300 202 L 292 208 L 300 214 L 292 220 L 300 226 L 294 236'}],
}
TITLES['imprimir'] = 'Sinal de imprimir em Libras'
