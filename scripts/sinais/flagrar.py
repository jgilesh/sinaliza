# FLAGRAR: the tip of the index (1) touches just below the eye, beside the nose; then the hand moves
# out firmly to the front, the index pointing at the person who was caught. Once.
# (UFSC Signbank FLAGRAR, INES FLAGRAR1.)

_flagrar_one = hs_1()
# Below the eye: the index points up and in at the face, the hand below and beside the cheek,
# turned so the index and the folded fingers show from the side.
_flagrar_on = P((191, 105), _flagrar_one, 'index_tip', yaw=120, pitch=-3, roll=42, scale=1.05, depth=30,
                pole=(0.5, 1.0, 0.4))
# Out to the front on the signing side: the index points at the viewer.
_flagrar_out = P((114, 150), _flagrar_one, 'index_tip', yaw=-35, pitch=68, roll=-20, scale=1.15, depth=95,
                 via=(150, 104), ease='out', pole=(0.6, 1.0, 0.4))
SIGNS['flagrar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right'], 'handshape': _flagrar_one,
    'keys': [(0.0, [_flagrar_on]), (0.5, [_flagrar_on]), (0.8, [_flagrar_out]), (1.8, [_flagrar_out]),
             (2.4, [dict(_flagrar_on, via=(150, 150))])],
    'marks': [(189, 106, -105)],
    'arrows': [{'d': 'M 166 70 Q 128 62 108 106'}, {'ripples': (114, 150)}],
}
TITLES['flagrar'] = 'Sinal de flagrar em Libras'
