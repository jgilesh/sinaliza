# PALESTRAR: the open hand (5), fingers spread and a little bent, beside the head on its own side,
# palm forward; it moves forward and down from the head and back, 3 times, as if sending ideas out to
# an audience. (UFSC Signbank PALESTRAR: 5 at the side of the head; INES PALESTRAR.)


def hs_palestrar_5():
    """5 with the fingers spread and a little bent at every joint."""
    return {'index': fing(14, 10, 22, 14), 'middle': fing(3, 10, 22, 14), 'ring': fing(-8, 12, 22, 14),
            'pinky': fing(-18, 14, 22, 14), 'thumb': (40.0, 18.0, 10.0, 10.0, 10.0)}


_pal_h = hs_palestrar_5()
_pal_up = P((118, 108), _pal_h, 'wrist', yaw=20, pitch=0, roll=-18, scale=1.0, depth=40, pole=(0.7, 1.0, 0.45))
_pal_out = P((114, 142), _pal_h, 'wrist', yaw=20, pitch=28, roll=-16, scale=1.2, depth=100, pole=(0.7, 1.0, 0.45))
_pal_keys = [(0.0, [_pal_up]), (0.3, [_pal_up])]
for _pal_i in range(3):
    _pal_keys += [(0.3 + 0.5 * _pal_i + 0.25, [_pal_out]), (0.3 + 0.5 * _pal_i + 0.5, [_pal_up])]
_pal_keys.append((2.3, [_pal_up]))
SIGNS['palestrar'] = {
    'poster': 0.0, 'dur': 2.3, 'hands': ['right'], 'handshape': _pal_h,
    'keys': _pal_keys,
    'arrows': [{'d': 'M 78 70 Q 70 98 82 122', 'both': True}],
}
TITLES['palestrar'] = 'Sinal de palestrar em Libras'
