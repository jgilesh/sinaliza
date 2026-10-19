# RELACIONAR: both hands with the index and middle fingers straight and crossed (the middle finger
# over the index), the thumb open and the other fingers closed, palms toward the body. In
# alternation each hand brings its fingertips to the lips while the other drops a little, so the
# hands cross in front of the mouth, 2 to 3 times. (UFSC Signbank RELACIONAR. INES RELACIONAR shows
# another variant: L-like hands side by side in front of the neck, moving sideways.)


def hs_relacionar_r():
    """R with the thumb open: index and middle straight and crossed, the middle on the back of the
    index (the index bends a little more at the knuckle, so it lies on the palm side); thumb out to
    the side in the palm plane; ring and little finger folded."""
    return fist({'index': fing(-19, 10, 2, 1), 'middle': fing(19, 0, 2, 1), 'thumb': (46.0, 8.0, 0.0, 4.0, 2.0)})


_rel_r = hs_relacionar_r()


def _rel_pose(up):
    """Right hand; up = 1: fingertips on the lips, 0: lower and out to the side. Back of the hand
    to the viewer, fingers up and leaning in toward the middle."""
    tip = (176 + 20 * up, 168 - 42 * up)
    return P(tip, _rel_r, 'fingertips', yaw=172, pitch=-8, roll=10 + 14 * up, scale=1.0, depth=44 - 6 * up,
             pole=(0.4, 1.0, 0.45))


_rel_up, _rel_down = _rel_pose(1.0), _rel_pose(0.0)
_rel_keys = [(0.0, [_rel_up, mirrored(_rel_down)]), (0.3, [_rel_up, mirrored(_rel_down)])]
_rel_t = 0.3
for _rel_k in range(4):                   # two touches for each hand
    _rel_t += 0.45
    _rel_a, _rel_b = (_rel_down, _rel_up) if _rel_k % 2 == 0 else (_rel_up, _rel_down)
    _rel_keys.append((round(_rel_t, 2), [_rel_a, mirrored(_rel_b)]))
    _rel_keys.append((round(_rel_t + 0.12, 2), [_rel_a, mirrored(_rel_b)]))
    _rel_t += 0.12
_rel_keys.append((round(_rel_t + 0.5, 2), _rel_keys[-1][1]))
SIGNS['relacionar'] = {
    'poster': 0.3, 'dur': round(_rel_t + 0.5, 2), 'hands': ['right', 'left'], 'handshape': _rel_r,
    'handshape_view': {'yaw': 0},
    'keys': _rel_keys,
    # The fingertips touch the lips, one hand and then the other.
    'marks': [(184, 122, -70), (216, 122, 70)],
    'arrows': [{'d': 'M 116 156 Q 128 126 152 116', 'both': True}, {'d': 'M 284 156 Q 272 126 248 116', 'both': True}],
    'mirror_second': True,
}
TITLES['relacionar'] = 'Sinal de relacionar em Libras'
