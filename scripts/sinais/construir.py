# CONSTRUIR: both hands flat (B), palms down, fingers pointing across toward the other side, one above
# the other in front of the body. The lower hand goes up over the other one, then the other, rising
# from the waist to the height of the chin, like bricks being laid. (UFSC Signbank CONSTRUIR-TIJOLO:
# B+B, para cima, alternado; the INES video agrees.)
_construir_b = hs_B()


def _construir_r(y, depth=72, **kw):
    # Right hand: palm down and a little toward the body (the back of the hand seen from a little above),
    # fingers across toward the other side, the thumb up behind.
    return P((166, y), _construir_b, 'wrist', yaw=114, pitch=0, roll=90, scale=1.0, depth=depth,
             pole=(0.45, 1.0, 0.4), **kw)


def _construir_l(y, depth=72, **kw):
    return mirrored(P((166, y), _construir_b, 'wrist', yaw=114, pitch=0, roll=90, scale=1.0, depth=depth,
                      pole=(0.45, 1.0, 0.4), **kw))


# Levels from the waist up. The right hand (drawn in front) rises in front of the left; the left hand
# rises behind the right (closer to the body), so the hands never pass through each other.
_construir_y = [252, 230, 208, 186, 164]
_construir_keys = [(0.0, [_construir_r(_construir_y[1]), _construir_l(_construir_y[0])]),
                   (0.3, [_construir_r(_construir_y[1]), _construir_l(_construir_y[0])])]
_construir_t = 0.3
_construir_rl = [_construir_y[1], _construir_y[0]]   # current y of right, left
for _construir_k in range(3):
    _construir_mover = 1 if _construir_k % 2 == 0 else 0     # left first, then right, then left
    _construir_new = min(_construir_rl) - 22
    _construir_rl[_construir_mover] = _construir_new
    _construir_t += 0.45
    if _construir_mover == 1:
        _construir_keys.append((_construir_t, [_construir_r(_construir_rl[0]),
                                               _construir_l(_construir_new, via=(166, _construir_new + 30), depth=60)]))
    else:
        _construir_keys.append((_construir_t, [_construir_r(_construir_new, via=(166, _construir_new + 30), depth=80),
                                               _construir_l(_construir_rl[1])]))
_construir_keys += [(2.4, _construir_keys[-1][1]),
                    (3.0, [_construir_r(_construir_y[1], via=(120, 230)), _construir_l(_construir_y[0], via=(280, 230))])]
SIGNS['construir'] = {
    'poster': 1.2, 'dur': 3.0, 'hands': ['right', 'left'], 'handshape': _construir_b, 'handshape_view': {'yaw': 0},
    'keys': _construir_keys,
    'arrows': [{'d': 'M 288 250 L 288 176'}],
    'mirror_second': True,
}
TITLES['construir'] = 'Sinal de construir em Libras'
