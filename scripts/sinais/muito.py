# MUITO: both hands open and relaxed in front of the chest, palms toward the body, fingers up; the
# fingers bend and straighten several times with the hands almost still. (INES MUITO1; Signbank 1942.)
def hs_muito_open():
    """Relaxed 5: fingers spread and a little curved."""
    return {'index': fing(13, 6, 12, 8), 'middle': fing(3, 6, 12, 8), 'ring': fing(-7, 8, 12, 8),
            'pinky': fing(-16, 10, 14, 9), 'thumb': (36.0, 18.0, 8.0, 8.0, 8.0)}


def hs_muito_bent():
    """The same hand with the fingers bent toward the palm (a loose claw)."""
    return {'index': fing(11, 35, 65, 40), 'middle': fing(2, 38, 68, 42), 'ring': fing(-6, 40, 66, 42),
            'pinky': fing(-13, 42, 64, 40), 'thumb': (30.0, 24.0, 14.0, 14.0, 16.0)}


muito_open, muito_bent = hs_muito_open(), hs_muito_bent()
# Back of the hand toward the viewer, turned a little toward the thumb side, so the bending fingers
# are seen half in profile.
muito_at = lambda shape: P((140, 226), shape, 'wrist', yaw=148, pitch=-8, roll=10, scale=1.05, depth=70,
                           pole=(0.3, 1.0, 0.4))
muito_o, muito_b = muito_at(muito_open), muito_at(muito_bent)
muito_keys = [(0.0, [muito_o, mirrored(muito_o)]), (0.25, [muito_o, mirrored(muito_o)])]
for k in range(4):
    muito_keys += [(0.45 + 0.4 * k, [muito_b, mirrored(muito_b)]), (0.65 + 0.4 * k, [muito_o, mirrored(muito_o)])]
muito_keys.append((2.4, [muito_o, mirrored(muito_o)]))
SIGNS['muito'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': muito_open,
    'keys': muito_keys,
    # Beside the inner fingers: they fold down and come back up (both ways).
    'arrows': [{'d': 'M 186 150 Q 195 167 187 186', 'both': True}, {'d': 'M 214 150 Q 205 167 213 186', 'both': True}],
    'mirror_second': True,
}
TITLES['muito'] = 'Sinal de muito em Libras'
