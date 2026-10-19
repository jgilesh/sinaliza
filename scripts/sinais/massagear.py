# MASSAGEAR: both hands in an open beak (fingers together, thumb apart below them), at shoulder
# height in front of the body, palms down; the fingers squeeze down onto the thumb and open again,
# several times, both hands at once, as if kneading someone's shoulders. (UFSC Signbank MASSAGEAR:
# Beak_open, neutral space. The INES MASSAGEAR video shows a one-handed variant kneading the back
# of the other hand.)


def hs_massagear_open():
    """Open beak: the four fingers together and a little bent, the opposed thumb well apart below them."""
    return {'index': fing(2, 26, 12, 8), 'middle': fing(0, 28, 12, 8), 'ring': fing(-2, 30, 12, 8),
            'pinky': fing(-4, 32, 12, 8), 'thumb': (24.0, 60.0, 50.0, 4.0, 6.0)}


def hs_massagear_closed():
    """Closed beak: the fingers bend further and their pads press on the thumb's pad."""
    shape = {'index': fing(2, 56, 40, 24), 'middle': fing(0, 58, 40, 24), 'ring': fing(-1, 60, 40, 24),
             'pinky': fing(-2, 62, 40, 24)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


_massagear_o, _massagear_c = hs_massagear_open(), hs_massagear_closed()


def _massagear_pose(shape):
    return P((118, 192), shape, 'wrist', yaw=70, pitch=25, roll=86, scale=1.05, depth=70, pole=(0.5, 1.0, 0.4))


_massagear_a, _massagear_b = _massagear_pose(_massagear_o), _massagear_pose(_massagear_c)
_massagear_keys = [(0.0, [_massagear_a, mirrored(_massagear_a)]), (0.3, [_massagear_a, mirrored(_massagear_a)])]
for _massagear_i in range(3):
    _massagear_t = 0.3 + 0.4 * _massagear_i
    _massagear_keys += [(_massagear_t + 0.2, [_massagear_b, mirrored(_massagear_b)]),
                        (_massagear_t + 0.4, [_massagear_a, mirrored(_massagear_a)])]
_massagear_keys.append((1.9, [_massagear_a, mirrored(_massagear_a)]))
SIGNS['massagear'] = {
    'poster': 0.3, 'dur': 1.9, 'hands': ['right', 'left'], 'handshape': _massagear_o,
    'handshape_view': {'yaw': 70},
    'keys': _massagear_keys,
    # Beside the fingertips: the fingers squeeze down onto the thumb and open again.
    'arrows': [{'d': 'M 172 182 Q 182 198 170 214', 'both': True}, {'d': 'M 228 182 Q 218 198 230 214', 'both': True}],
    'mirror_second': True,
}
TITLES['massagear'] = 'Sinal de massagear em Libras'
