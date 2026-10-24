# VAZAR: the fingertips gathered on the thumb (O), in front of the face on the signing side at mouth
# height, fingers up; the hand moves a little forward and the fingers spring open into 5 at once; twice.
# (UFSC Signbank VAZAR: O+5, espaço neutro. The INES VAZAR1 video shows a two-handed variant.)
_vazar_o, _vazar_5 = hs_O(), hs_5()
_vazar_pole = (0.6, 1.0, 0.45)
# Closed: the O beside the face, palm turned toward the midline and the viewer, so the round opening
# between the fingertips and the thumb shows from the side.
_vazar_shut = P((140, 160), _vazar_o, 'wrist', yaw=50, pitch=-6, roll=-6, scale=1.0, depth=50, pole=_vazar_pole)
# Open: a little forward (nearer the viewer), fingers spread, palm forward.
_vazar_open = P((134, 162), _vazar_5, 'wrist', yaw=20, pitch=8, roll=-8, scale=1.1, depth=72, pole=_vazar_pole,
                ease='out')
_vazar_keys = [(0.0, [_vazar_shut]), (0.35, [_vazar_shut])]
_vazar_t = 0.35
for _vazar_i in range(2):
    _vazar_keys += [(_vazar_t + 0.22, [_vazar_open]), (_vazar_t + 0.6, [_vazar_open]),
                    (_vazar_t + 0.95, [dict(_vazar_shut, ease='smooth')])]
    _vazar_t += 0.95
_vazar_keys.append((_vazar_t + 0.35, [_vazar_shut]))
SIGNS['vazar'] = {
    'poster': 0.35, 'dur': _vazar_t + 0.35, 'hands': ['right'], 'handshape': _vazar_o, 'handshape_view': {'yaw': 60},
    'keys': _vazar_keys,
    # Out from the fingertips: the fingers spring open.
    'arrows': [{'d': 'M 114 106 L 100 92'}, {'d': 'M 134 100 L 136 82'}],
}
TITLES['vazar'] = 'Sinal de vazar em Libras'
