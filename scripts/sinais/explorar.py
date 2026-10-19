# EXPLORAR: both hands in a hooked V (index and middle apart and bent like claws), in front of the
# chest, palms forward and fingers up; the wrists bend down and in together, so the hooked fingers
# end level, pointing at each other, palms down, like claws pulling something in. Twice.
# (UFSC Signbank EXPLORAR: V_curved, neutral space, ulnar flexion; INES EXPLORAR similar.)


def hs_explorar_v():
    """Hooked V: index and middle spread and bent at the middle and end joints, ring and little
    finger folded under the thumb."""
    shape = fist({'index': fing(17, 10, 52, 36), 'middle': fing(-12, 10, 52, 36)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


_explorar_v = hs_explorar_v()
_explorar_up = P((148, 212), _explorar_v, 'wrist', yaw=-30, pitch=-35, roll=-6, scale=1.1, depth=65, pole=(0.45, 1.0, 0.4))
_explorar_down = P((124, 222), _explorar_v, 'wrist', yaw=35, pitch=0, roll=88, scale=1.1, depth=65, pole=(0.45, 1.0, 0.4))
_explorar_keys = [(0.0, [_explorar_up, mirrored(_explorar_up)]), (0.3, [_explorar_up, mirrored(_explorar_up)])]
for _explorar_i in range(2):
    _explorar_t = 0.3 + 0.44 * _explorar_i
    _explorar_keys += [(_explorar_t + 0.22, [_explorar_down, mirrored(_explorar_down)]),
                       (_explorar_t + 0.44, [_explorar_up, mirrored(_explorar_up)])]
_explorar_keys.append((1.7, [_explorar_up, mirrored(_explorar_up)]))
SIGNS['explorar'] = {
    'poster': 0.3, 'dur': 1.7, 'hands': ['right', 'left'], 'handshape': _explorar_v,
    'handshape_view': {'yaw': -30, 'pitch': -40},
    'keys': _explorar_keys,
    'arrows': [{'d': 'M 150 150 Q 182 152 186 182'}, {'d': 'M 250 150 Q 218 152 214 182'}],
    'mirror_second': True,
}
TITLES['explorar'] = 'Sinal de explorar em Libras'
