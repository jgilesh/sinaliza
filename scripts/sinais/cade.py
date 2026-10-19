# CADÊ: both open hands (5) start in front of the chest, close together, palms down; they move
# apart to the sides and turn the palms up, once, as if looking for something that is not there.
# Question face. (INES CADÊ and UFSC Signbank CADÊ agree.)
_cade_5 = hs_5()
# Start: back of the hand to the viewer, fingers toward the other hand, a little tipped so the palm
# faces down.
_cade_in = P((150, 226), _cade_5, 'wrist', yaw=105, pitch=50, roll=70, scale=1.08, depth=60, pole=(0.4, 1.0, 0.4))
# End: out to the side, palm up and tilted toward the viewer, fingers pointing outward and forward.
_cade_out = P((112, 214), _cade_5, 'wrist', yaw=45, pitch=20, roll=-85, scale=1.12, depth=70, pole=(0.5, 1.0, 0.4),
              via=(150, 232))
# Halfway: the fingers swing forward (toward the viewer) while the forearms turn.
_cade_mid = P((130, 226), _cade_5, 'wrist', yaw=80, pitch=65, roll=-10, scale=1.1, depth=66, pole=(0.45, 1.0, 0.4),
              via=(146, 232), ease='linear')
_cade_out['via'] = (118, 222)
_cade_back = dict(_cade_in, via=(150, 240))
SIGNS['cade'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _cade_5,
    'keys': [(0.0, [_cade_in, mirrored(_cade_in)]), (0.3, [_cade_in, mirrored(_cade_in)]),
             (0.6, [_cade_mid, mirrored(_cade_mid)]), (0.9, [_cade_out, mirrored(_cade_out)]), (1.8, [_cade_out, mirrored(_cade_out)]),
             (2.4, [_cade_back, mirrored(_cade_back)])],
    'arrows': [{'trail': 0, 'from': 0.3, 'to': 0.9, 'offset': (0, 30)},
               {'trail': 1, 'from': 0.3, 'to': 0.9, 'offset': (0, 30)}],
    'mirror_second': True,
}
TITLES['cade'] = 'Sinal de cadê em Libras'
