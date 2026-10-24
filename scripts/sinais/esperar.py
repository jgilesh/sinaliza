# ESPERAR: both hands closed in fists (S). The support fist lies across in front of the chest, palm
# down; the signing fist stands upright on it, its wrist resting on the back of the support hand, and
# taps it lightly a few times. (UFSC Signbank ESPERAR. INES ESPERAR1 shows a variant: the index and
# middle finger up, the elbow resting on the back of the other hand.)
_esperar_s = hs_S()
# Support fist (defined as a right hand, then mirrored): palm down, the knuckles toward the midline,
# the back of the hand turned a little up toward the viewer.
_esperar_base = mirrored(P((136, 236), _esperar_s, 'wrist', yaw=115, pitch=0, roll=90, scale=1.1, depth=65))
# Signing fist upright over the support hand, palm toward the midline, the thumb side turned a little
# to the viewer; its wrist rests on the back of the support hand.
_esperar_top = lambda dy: P((240, 218 - dy), _esperar_s, 'wrist', yaw=55, pitch=0, roll=6, scale=1.1, depth=80,
                            pole=(0.2, 1.0, 0.5))
_esperar_on, _esperar_off = _esperar_top(0), _esperar_top(8)
_esperar_keys = [(0.0, [_esperar_on, _esperar_base]), (0.4, [_esperar_on, _esperar_base])]
for _esperar_i in range(3):   # three light taps
    _esperar_t = 0.4 + 0.36 * _esperar_i
    _esperar_keys += [(_esperar_t + 0.18, [_esperar_off, _esperar_base]), (_esperar_t + 0.36, [_esperar_on, _esperar_base])]
_esperar_keys += [(2.2, [_esperar_on, _esperar_base])]
SIGNS['esperar'] = {
    'poster': 0.4, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _esperar_s,
    'keys': _esperar_keys,
    'arrows': [{'d': 'M 214 174 L 214 196', 'both': True}],
    'marks': [(262, 226, 70)],
    'mirror_second': True,
}
TITLES['esperar'] = 'Sinal de esperar em Libras'
