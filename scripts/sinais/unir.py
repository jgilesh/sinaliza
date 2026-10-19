# UNIR: both hands in F (thumb and index joined in a ring, the other three fingers straight). The hands
# come together in front of the chest and the two rings hook into each other like the links of a
# chain, and stay joined: the dominant hand upright, palm toward the other hand and the viewer; the
# other hand lying across, palm down. (UFSC Signbank UNIR: F+F, dedos. INES UNIR shows both hands
# upright, palms forward, mirrored.)
_unir_f = hs_F()
# Dominant hand: upright, palm turned toward the midline and the viewer, so its ring shows at a slant.
_unir_r_on = P((194, 206), _unir_f, 'pinch', yaw=58, pitch=0, roll=-6, scale=1.1, depth=70, pole=(0.45, 1.0, 0.4))
_unir_r_off = dict(_unir_r_on, at=(158, 214))
# Other hand (defined as a right hand, then mirrored): palm down, fingers pointing across toward the
# dominant hand, seen from the little-finger side, so its ring stands in the picture plane: its straight
# fingers pass behind the dominant thumb tip and its ring loops around the dominant ring (a chain link).
_unir_l_on = mirrored(P((188, 222), _unir_f, 'pinch', yaw=95, pitch=0, roll=90, scale=1.1, depth=68,
                        pole=(0.45, 1.0, 0.4)))
_unir_l_off = dict(_unir_l_on, at=(246, 228))
SIGNS['unir'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _unir_f, 'handshape_view': {'yaw': 40},
    'keys': [(0.0, [_unir_r_off, _unir_l_off]), (0.3, [_unir_r_off, _unir_l_off]), (0.8, [_unir_r_on, _unir_l_on]),
             (1.9, [_unir_r_on, _unir_l_on]), (2.4, [_unir_r_off, _unir_l_off])],
    # Below the hands: they come together.
    'arrows': [{'d': 'M 150 262 L 176 252'}, {'d': 'M 262 262 L 236 252'}],
    'mirror_second': True,
    'contact': ['index', 'thumb'],
}
TITLES['unir'] = 'Sinal de unir em Libras'
