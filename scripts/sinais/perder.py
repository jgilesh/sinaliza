# PERDER: both hands open with the fingers together (B). The palm of the signing hand brushes up
# across the palm of the other hand to the front of the chin; then both hands open out to the sides
# at shoulder height and end with the palms up. Once. (UFSC Signbank PERDER.)


def hs_perder_b():
    """B with the thumb resting along the side of the index (fingers together and straight)."""
    shape = hs_B()
    shape['thumb'] = (8.0, 12.0, 6.0, 6.0, 4.0)
    return shape


_perder_b = hs_perder_b()
# The signing hand, back of the hand to the viewer, fingers up and leaning toward the other side; it
# starts low, over the other palm, and brushes up to the front of the chin.
_perder_front = lambda at, roll: P(at, _perder_b, 'wrist', yaw=180, pitch=0, roll=roll, scale=1.0, depth=46,
                                   pole=(0.4, 1.0, 0.45))
_perder_low, _perder_high = _perder_front((176, 226), 34), _perder_front((164, 202), 28)
# The other hand, lower and on its own side, palm to the viewer and turned up toward the signing hand,
# fingers leaning toward the midline (the palms face each other).
_perder_sup = mirrored(P((168, 226), _perder_b, 'wrist', yaw=-20, pitch=0, roll=38, scale=1.0, depth=36,
                         pole=(0.4, 1.0, 0.45)))
# Open: out at the sides, shoulder height, palm up and tipped toward the viewer, fingers out and up.
_perder_open = P((108, 182), _perder_b, 'wrist', yaw=40, pitch=24, roll=-70, scale=1.08, depth=60,
                 ease='out', pole=(0.4, 1.0, 0.45))
SIGNS['perder'] = {
    'poster': 0.6, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _perder_b,
    'keys': [(0.0, [_perder_low, _perder_sup]), (0.3, [_perder_low, _perder_sup]),
             (0.6, [_perder_high, _perder_sup]), (1.1, [_perder_open, mirrored(_perder_open)]),
             (2.0, [_perder_open, mirrored(_perder_open)]), (2.6, [_perder_low, _perder_sup])],
    # Above the open hands, from beside the face out to each side.
    'arrows': [{'d': 'M 148 128 Q 112 98 76 116'}, {'d': 'M 252 128 Q 288 98 324 116'}],
    'mirror_second': True,
}
TITLES['perder'] = 'Sinal de perder em Libras'
