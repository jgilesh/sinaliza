# AGRADECER: flat hands. The fingertips of the dominant hand touch the forehead (palm to the side)
# while the other hand rests flat against the chest; the dominant hand leaves the forehead in an arc,
# forward and down, once. (UFSC Signbank AGRADECER; INES AGRADECER.)
_agr_b = hs_B()
_agr_on = P((176, 76), _agr_b, 'fingertips', yaw=140, pitch=0, roll=40, scale=1.0, depth=40, pole=(0.25, 1.0, 0.6))
# Out in front at shoulder height, the palm turned up and toward the face, fingers up and forward.
_agr_off = P((126, 140), _agr_b, 'fingertips', yaw=52, pitch=-45, roll=-16, scale=1.12, depth=85, via=(130, 86),
             ease='out', pole=(0.25, 1.0, 0.5))
_agr_back = dict(_agr_on, ease='smooth')
# The other hand: flat against the chest, back of the hand to the viewer, fingers toward the midline.
_agr_rest = P((214, 232), _agr_b, 'fingertips', yaw=180, pitch=0, roll=84, scale=1.0, depth=25)
SIGNS['agradecer'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _agr_b,
    'keys': [(0.0, [_agr_on, _agr_rest]), (0.5, [_agr_on, _agr_rest]), (1.1, [_agr_off, _agr_rest]),
             (1.9, [_agr_off, _agr_rest]), (2.4, [_agr_back, _agr_rest])],
    'marks': [(181, 64, -30)],
    'arrows': [{'d': 'M 160 56 Q 120 56 112 96'}],
    'mirror_second': True,
}
TITLES['agradecer'] = 'Sinal de agradecer em Libras'
