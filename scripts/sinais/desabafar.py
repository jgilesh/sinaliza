# DESABAFAR: the fingertips gathered on the thumb (O) against the mouth; the hand moves out forward and
# the fingers open, ending palm up, as if letting out what one feels; back to the mouth and again, about
# three times. (UFSC Signbank DESABAFAR: O, boca, repeated; INES DESABAFAR agrees.)
_desabafar_o, _desabafar_5 = hs_O(), hs_5()
_desabafar_pole = (0.45, 1.0, 0.5)
# At the mouth: the hand below and beside the mouth on the signing side, the gathered fingertips on the
# corner of the lips; the palm turned toward the midline and the viewer, so the O reads from the side.
_desabafar_on = P((192, 131), _desabafar_o, 'index_tip', yaw=60, pitch=-20, roll=18, scale=0.98, depth=30,
                  pole=_desabafar_pole)
# Out: forward and down in front of the chest, fingers spread, palm up (tilted toward the viewer).
_desabafar_off = P((150, 204), _desabafar_5, 'wrist', yaw=0, pitch=-55, roll=-30, scale=1.12, depth=80,
                   pole=_desabafar_pole, ease='out')
_desabafar_keys = [(0.0, [_desabafar_on]), (0.3, [_desabafar_on])]
_desabafar_t = 0.3
for _desabafar_i in range(3):
    _desabafar_keys += [(_desabafar_t + 0.4, [_desabafar_off]), (_desabafar_t + 0.6, [_desabafar_off]),
                        (_desabafar_t + 0.95, [dict(_desabafar_on, ease='smooth')])]
    _desabafar_t += 0.95
_desabafar_keys.append((_desabafar_t + 0.3, [_desabafar_on]))
SIGNS['desabafar'] = {
    'poster': 0.3, 'dur': _desabafar_t + 0.3, 'hands': ['right'], 'handshape': _desabafar_o,
    'handshape_view': {'yaw': 60},
    'keys': _desabafar_keys,
    'marks': [(200, 131, 160)],
    'arrows': [{'d': 'M 176 160 Q 170 196 140 214', 'both': True}],
}
TITLES['desabafar'] = 'Sinal de desabafar em Libras'
