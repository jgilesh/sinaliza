# ESPIAR: both flat hands (B), upright and turned to the side, palms facing each other, in front of
# the face like a curtain. They slide sideways and cross in front of the face and open again, 3
# times, as if peeking through the gap. (UFSC Signbank ESPIAR; INES ESPIAR1 agrees.) Drawn with the
# fingertips just under the eyes, so the eyes stay visible.


def hs_espiar_b():
    """B with the thumb resting along the side of the index."""
    shape = hs_B()
    shape['thumb'] = (-14.0, 6.0, 10.0, 6.0, 4.0)
    return shape


_espiar_b = hs_espiar_b()


def _espiar_pose(x, depth):
    # Fingers up, palm turned toward the midline (and a little toward the viewer).
    return P((x, 108), _espiar_b, 'fingertips', yaw=52, pitch=0, roll=3, scale=1.0, depth=depth, pole=(0.45, 1.0, 0.45))


_espiar_open = [_espiar_pose(172, 42), mirrored(_espiar_pose(172, 36))]
_espiar_cross = [_espiar_pose(226, 46), mirrored(_espiar_pose(226, 34))]
_espiar_keys = [(0.0, _espiar_open), (0.3, _espiar_open)]
for _espiar_t in (0.55, 1.05, 1.55):
    _espiar_keys += [(_espiar_t, _espiar_cross), (_espiar_t + 0.25, _espiar_open)]
_espiar_keys.append((2.4, _espiar_open))
SIGNS['espiar'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _espiar_b,
    'keys': _espiar_keys,
    # Side to side under the hands (two heads: the hands cross and open again).
    'arrows': [{'d': 'M 172 214 L 228 214', 'both': True}],
    'mirror_second': True,
}
TITLES['espiar'] = 'Sinal de espiar em Libras'
