# MÉDICO: both hands with the index up and its tip curled (1 curvo) in front of the neck. The
# support hand holds its hooked index up; the dominant index, lying across with the palm down,
# hooks over it and rubs it with small repeated movements. (INES MÉDICO and UFSC Signbank agree.)
_med_hs = hs_1_curved()
# Support hand (left), drawn as the right hand at the mirrored place: index up, the hook curling
# toward the midline.
_med_sup = mirrored(P((176, 168), _med_hs, 'index_tip', yaw=60, pitch=0, roll=0, scale=1.0, depth=55))
_med_on = P((230, 171), _med_hs, 'index_tip', yaw=130, pitch=0, roll=90, scale=1.0, depth=60, pole=(0.5, 1.0, 0.4))
_med_up = dict(_med_on, at=(229, 162), roll=78)
SIGNS['medico'] = {
    'poster': 0.4, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _med_hs, 'handshape_view': {'yaw': -30, 'pitch': -25},
    'keys': [(0.0, [_med_on, _med_sup]), (0.4, [_med_on, _med_sup]), (0.6, [_med_up, _med_sup]), (0.8, [_med_on, _med_sup]),
             (1.0, [_med_up, _med_sup]), (1.2, [_med_on, _med_sup]), (1.4, [_med_up, _med_sup]), (1.6, [_med_on, _med_sup]),
             (2.4, [_med_on, _med_sup])],
    'mirror_second': True,
    'marks': [(250, 170, 70)],
    'arrows': [{'d': 'M 238 136 L 238 152', 'both': True}],
}
TITLES['medico'] = 'Sinal de médico em Libras'
