# ASSUSTAR: both hands open with the fingers spread (5) start against the chest, palms in, fingertips
# toward each other; in one quick arc they fly up, back and out to beside the head, the palms turning
# forward, like a start of fright. Once. (UFSC Signbank ASSUSTAR: 5, 2s, peito, arco para trás + para
# cima + ipsilateral, palms brushing the chest; INES ASSUSTAR agrees.)
_assu_5 = hs_5()
_assu_pole = (0.6, 1.0, 0.4)
# On the chest: back of the hand to the viewer, fingers toward the midline and a little up.
_assu_in = P((150, 246), _assu_5, 'wrist', yaw=172, pitch=0, roll=34, scale=1.0, depth=30, pole=_assu_pole)
# Beside the head: palm forward, fingers up and leaning out a little.
_assu_out = P((113, 142), _assu_5, 'wrist', yaw=-6, pitch=0, roll=-14, scale=1.1, depth=40, pole=_assu_pole,
              via=(120, 220), ease='out')
_assu_back = dict(_assu_in, via=(150, 200), ease='smooth')
SIGNS['assustar'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _assu_5,
    'keys': [(0.0, [_assu_in, mirrored(_assu_in)]), (0.35, [_assu_in, mirrored(_assu_in)]),
             (0.7, [_assu_out, mirrored(_assu_out)]), (1.8, [_assu_out, mirrored(_assu_out)]),
             (2.4, [_assu_back, mirrored(_assu_back)])],
    # From the chest, up and out to beside the head, one for each hand.
    'arrows': [{'d': 'M 150 246 Q 96 236 92 158'}, {'d': 'M 250 246 Q 304 236 308 158'}],
    'mirror_second': True,
}
TITLES['assustar'] = 'Sinal de assustar em Libras'
