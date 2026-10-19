# ESFORÇAR: both hands closed (S) in front of the chest, palms forward; with force and tension the
# fists turn (palms down, knuckles toward each other) and rise together to shoulder height, ending
# with the palms facing each other. Once. (UFSC Signbank ESFORÇAR; INES ESFORÇAR also pulls the
# fists up to the shoulders.)
_esf_s = hs_S()
_esf_start = P((160, 236), _esf_s, 'wrist', yaw=0, pitch=0, roll=-8, scale=1.08, depth=60, pole=(0.4, 1.0, 0.4))
_esf_mid = P((146, 222), _esf_s, 'wrist', yaw=120, pitch=5, roll=90, scale=1.08, depth=64, pole=(0.4, 1.0, 0.4))
_esf_end = P((146, 192), _esf_s, 'wrist', yaw=60, pitch=-10, roll=4, scale=1.1, depth=58, pole=(0.45, 1.0, 0.4),
             ease='out')
_esf_back = dict(_esf_start, ease='smooth')
SIGNS['esforcar'] = {
    'poster': 1.0, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _esf_s,
    'keys': [(0.0, [_esf_start, mirrored(_esf_start)]), (0.3, [_esf_start, mirrored(_esf_start)]),
             (0.55, [_esf_mid, mirrored(_esf_mid)]), (0.8, [_esf_end, mirrored(_esf_end)]),
             (1.85, [_esf_end, mirrored(_esf_end)]), (2.2, [_esf_back, mirrored(_esf_back)])],
    # Up, beside each fist (outer side).
    'arrows': [{'d': 'M 112 236 Q 104 210 110 182'}, {'d': 'M 288 236 Q 296 210 290 182'}],
    'mirror_second': True,
}
TITLES['esforcar'] = 'Sinal de esforçar em Libras'
