# DEFENDER: both hands closed in fists (S), in front of the chest, palms down; they move forward
# firmly, once, turning the wrists until the thumbs are up and the palms face each other, like a
# guard. (UFSC Signbank DEFENDER. INES DEFENDER1 shows a variant: a flat hand upright in front of
# the other forearm, like a wall.)
_defender_s = hs_S()
_defender_pole = (0.4, 1.0, 0.4)
# Near: fists close together in front of the chest, the knuckles forward, palms down (the front of
# the fist, the folded fingers, toward the viewer).
_defender_near = P((170, 214), _defender_s, 'wrist', yaw=0, pitch=62, roll=8, scale=1.05, depth=50, pole=_defender_pole)
# Far: forward and a little apart, the wrists turned: thumbs up, palms facing each other.
_defender_far = P((146, 222), _defender_s, 'wrist', yaw=80, pitch=62, roll=4, scale=1.25, depth=95, ease='out',
                  pole=_defender_pole)
_defender_back = dict(_defender_near, ease='smooth')
_defender_k = lambda p: [p, mirrored(p)]
SIGNS['defender'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _defender_s,
    'keys': [(0.0, _defender_k(_defender_near)), (0.4, _defender_k(_defender_near)),
             (0.9, _defender_k(_defender_far)), (1.8, _defender_k(_defender_far)),
             (2.4, _defender_k(_defender_back))],
    # Above each fist, the turn (the thumb comes up); below, forward (toward the viewer: down and out on
    # the picture).
    'arrows': [{'d': 'M 178 176 Q 166 164 150 170'}, {'d': 'M 222 176 Q 234 164 250 170'},
               {'d': 'M 150 246 L 138 270'}, {'d': 'M 250 246 L 262 270'}],
    'mirror_second': True,
}
TITLES['defender'] = 'Sinal de defender em Libras'
