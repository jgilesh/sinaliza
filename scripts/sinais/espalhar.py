# ESPALHAR: both fists closed (S), one over the other, palms down, just below the chin; they open into
# 5 (fingers spread, palms down) and move apart to the sides, once. Lips pressed (not drawn). (UFSC
# Signbank ESPALHAR: S+5, 2s; INES ESPALHAR.)
_esp_s, _esp_5 = hs_S(), hs_5()
# Right fist on top, the left fist under it (both written as right hands; the left one is mirrored).
_esp_r0 = P((176, 202), _esp_s, 'wrist', yaw=130, pitch=0, roll=90, scale=1.0, depth=60, pole=(0.6, 1.0, 0.4))
_esp_l0 = P((176, 228), _esp_s, 'wrist', yaw=130, pitch=0, roll=90, scale=1.0, depth=55, pole=(0.6, 1.0, 0.4))
_esp_r1 = P((128, 160), _esp_5, 'wrist', yaw=230, pitch=0, roll=-60, scale=1.1, depth=80, pole=(0.6, 1.0, 0.4))
_esp_l1 = dict(_esp_r1)
_esp_L = lambda p: mirrored(p)
SIGNS['espalhar'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _esp_s,
    'keys': [(0.0, [_esp_r0, _esp_L(_esp_l0)]), (0.4, [_esp_r0, _esp_L(_esp_l0)]),
             (1.0, [_esp_r1, _esp_L(_esp_l1)]), (1.9, [_esp_r1, _esp_L(_esp_l1)]),
             (2.4, [_esp_r0, _esp_L(_esp_l0)])],
    'mirror_second': True,
    'arrows': [{'d': 'M 172 196 L 128 196'}, {'d': 'M 228 196 L 272 196'}],
}
TITLES['espalhar'] = 'Sinal de espalhar em Libras'
