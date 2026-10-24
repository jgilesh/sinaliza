# DESAFIO: both hands in 1 (index straight, the others closed). The index tips touch the cheeks; then
# the hands come away from the face, turn the index fingers down and end in front of the chest with the
# index fingers level, pointing at each other, palms toward the body. Once. Raised brows, firm look.
# (UFSC Signbank DESAFIO: 1/1, double contact, arc, pronation. The INES DESAFIO video shows only the
# last part: the two index fingers pointing at each other low in front of the body.)
_desafio_one = hs_1()
# On the cheek: the index points up and in at the cheek from below and outside, the palm to the
# viewer, so the closed fingers and the thumb over them read.
_desafio_on = P((174, 116), _desafio_one, 'index_tip', yaw=10, pitch=0, roll=30, scale=0.95, depth=40,
                pole=(0.5, 1.0, 0.45))
# Turning: away from the face and down, the index pointing down, the back of the hand coming forward.
_desafio_mid = P((158, 214), _desafio_one, 'index_tip', yaw=130, pitch=0, roll=170, scale=1.0, depth=60,
                 pole=(0.5, 1.0, 0.45), via=(154, 172))
# End: in front of the chest, the index level and pointing at the other one, back of the hand to the
# viewer, thumb up.
_desafio_end = P((186, 206), _desafio_one, 'index_tip', yaw=180, pitch=0, roll=92, scale=1.05, depth=70,
                 pole=(0.4, 1.0, 0.4), ease='out')
_desafio_keys = [(0.0, [_desafio_on, mirrored(_desafio_on)]), (0.45, [_desafio_on, mirrored(_desafio_on)]),
                 (0.95, [_desafio_mid, mirrored(_desafio_mid)]), (1.35, [_desafio_end, mirrored(_desafio_end)]),
                 (2.2, [_desafio_end, mirrored(_desafio_end)]),
                 (2.8, [dict(_desafio_on, via=(140, 170), ease='smooth'), mirrored(dict(_desafio_on, via=(140, 170), ease='smooth'))])]
SIGNS['desafio'] = {
    'poster': 0.0, 'dur': 2.8, 'hands': ['right', 'left'], 'handshape': _desafio_one,
    'keys': _desafio_keys,
    'marks': [(168, 126, -110), (232, 126, 110)],
    'arrows': [{'d': 'M 104 112 Q 48 160 94 204'}, {'d': 'M 296 112 Q 352 160 306 204'}],
    'mirror_second': True,
}
TITLES['desafio'] = 'Sinal de desafio em Libras'
