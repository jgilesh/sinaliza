# FELIZ: both hands in F, palms forward, start beside the head and come down together in an arc
# to the front of the waist, closer to the middle, once. (UFSC Signbank FELIZ; INES FELIZ1.)
fel_f = hs_F()
fel_top = P((128, 150), fel_f, 'wrist', yaw=20, pitch=0, roll=-8, scale=1.0, depth=45, pole=(0.35, 1.0, 0.3))
fel_low = P((156, 268), fel_f, 'wrist', yaw=30, pitch=-20, roll=6, scale=1.0, depth=80, via=(104, 222), pole=(0.35, 1.0, 0.3))
fel_back = dict(fel_top, via=(150, 200))
SIGNS['feliz'] = {
    'poster': 0.0, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': fel_f, 'handshape_view': {'yaw': 40},
    'keys': [(0.0, [fel_top, mirrored(fel_top)]), (0.35, [fel_top, mirrored(fel_top)]),
             (1.15, [fel_low, mirrored(fel_low)]), (1.9, [fel_low, mirrored(fel_low)]),
             (2.6, [fel_back, mirrored(fel_back)])],
    'arrows': [{'trail': 0, 'from': 0.35, 'to': 1.15, 'offset': (-16, 0), 'trim': 0.12},
               {'trail': 1, 'from': 0.35, 'to': 1.15, 'offset': (16, 0), 'trim': 0.12}],
    'mirror_second': True,
}
TITLES['feliz'] = 'Sinal de feliz em Libras'
