# COMPENSAR: both hands flat (B), fingers together. They start up in front of the face, palms toward
# it and fingers up, and come down together in an arc, forward, to in front of the waist, ending
# with the palms down and the fingers forward. Once. (UFSC Signbank COMPENSAR.)

_comp_b = hs_B()
_comp_pole = (0.4, 1.0, 0.45)
# Beside the face (eyes clear), palms turned toward it, fingers up and leaning in a little.
_comp_up = P((150, 152), _comp_b, 'wrist', yaw=135, pitch=0, roll=8, scale=1.05, depth=40, pole=_comp_pole)
# Down and forward in front of the waist: palms down, the fingers forward and in.
_comp_down = P((134, 238), _comp_b, 'wrist', yaw=0, pitch=130, roll=-12, scale=1.2, depth=90, pole=_comp_pole,
               via=(112, 210))
_comp_back = dict(_comp_up, via=(120, 214))
SIGNS['compensar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _comp_b,
    'keys': [(0.0, [_comp_up, mirrored(_comp_up)]), (0.4, [_comp_up, mirrored(_comp_up)]),
             (1.05, [_comp_down, mirrored(_comp_down)]), (1.8, [_comp_down, mirrored(_comp_down)]),
             (2.4, [_comp_back, mirrored(_comp_back)])],
    # Outside each hand: down in an arc, forward.
    'arrows': [{'d': 'M 108 150 Q 80 200 106 240'}, {'d': 'M 292 150 Q 320 200 294 240'}],
    'mirror_second': True,
}
TITLES['compensar'] = 'Sinal de compensar em Libras'
