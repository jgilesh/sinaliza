# VITÓRIA: both hands in V, palms forward, rise from shoulder height to beside the top of the head,
# with a small sway at the top, like a cheer. (UFSC Signbank VITÓRIA; the INES VITÓRIA1 video shows
# a different sign, V at the nose, likely the city's name.)
_vit_v = hs_V()
_vit_low = P((128, 176), _vit_v, 'wrist', yaw=8, roll=-6, scale=1.05, depth=55)
_vit_high = P((124, 124), _vit_v, 'wrist', yaw=4, roll=-12, scale=1.12, depth=55, ease='out')
_vit_sway = dict(_vit_high, at=(127, 122), roll=-3, ease='smooth')
SIGNS['vitoria'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _vit_v,
    'keys': [(0.0, [_vit_low, mirrored(_vit_low)]), (0.2, [_vit_low, mirrored(_vit_low)]),
             (0.7, [_vit_high, mirrored(_vit_high)]), (0.95, [_vit_sway, mirrored(_vit_sway)]),
             (1.2, [_vit_high, mirrored(_vit_high)]), (1.45, [_vit_sway, mirrored(_vit_sway)]),
             (1.7, [_vit_high, mirrored(_vit_high)]), (2.0, [_vit_high, mirrored(_vit_high)]),
             (2.4, [_vit_low, mirrored(_vit_low)])],
    # Up beside each hand, outside it.
    'arrows': [{'d': 'M 84 182 Q 80 150 86 122'}, {'d': 'M 316 182 Q 320 150 314 122'}],
    'mirror_second': True,
}
TITLES['vitoria'] = 'Sinal de vitória em Libras'
