# CANTAR: both hands curved in C, palms turned toward each other, in front of the mouth and chin; they
# alternate: one comes back toward the mouth while the other moves forward and out, in arcs, several
# times. (UFSC Signbank CANTAR: C+C, para trás e para a frente, arco, alternado, repetido. The INES
# CANTAR video shows another variant, with one hand.)
_cantar_c = hs_C()


def _cantar_pose(k):
    """Right hand; k = 0 back by the mouth, 1 forward (nearer the viewer, a little lower and out)."""
    at = (156 - 10 * k, 168 + 30 * k)
    return P(at, _cantar_c, 'wrist', yaw=62 - 6 * k, pitch=-8 + 10 * k, roll=6 - 4 * k, scale=0.94 + 0.26 * k,
             depth=30 + 45 * k, pole=(0.45, 1.0, 0.45))


_cantar_back, _cantar_fwd = _cantar_pose(0.0), _cantar_pose(1.0)
_cantar_keys = [(0.0, [_cantar_back, mirrored(_cantar_fwd)]), (0.25, [_cantar_back, mirrored(_cantar_fwd)])]
_cantar_t = 0.25
for _cantar_i in range(2):
    _cantar_keys += [(_cantar_t + 0.4, [_cantar_fwd, mirrored(_cantar_back)]),
                     (_cantar_t + 0.8, [_cantar_back, mirrored(_cantar_fwd)])]
    _cantar_t += 0.8
_cantar_keys.append((_cantar_t + 0.5, [_cantar_back, mirrored(_cantar_fwd)]))
SIGNS['cantar'] = {
    'poster': 0.0, 'dur': _cantar_t + 0.5, 'hands': ['right', 'left'], 'handshape': _cantar_c,
    'handshape_view': {'yaw': 60},
    'keys': _cantar_keys,
    # Outside each hand: back to the mouth and forward again, alternating.
    'arrows': [{'d': 'M 130 132 Q 118 150 132 172', 'both': True},
               {'d': 'M 270 132 Q 282 150 268 172', 'both': True}],
    'mirror_second': True,
}
TITLES['cantar'] = 'Sinal de cantar em Libras'
