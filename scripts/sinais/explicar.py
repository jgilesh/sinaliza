# EXPLICAR: both fists raised beside the head, palms forward; the hands drop forward and down to the
# front of the shoulders, opening, the fingers left hanging loose (back of the hands to the viewer).
# Twice. (UFSC Signbank EXPLICAR: S/S, both hands, downward with a flexion of the wrist.)


def hs_explicar_loose():
    """Open hand, fingers loose and a little apart, slightly curved, thumb open."""
    return {'index': fing(10, 10, 16, 10), 'middle': fing(2, 10, 16, 10), 'ring': fing(-6, 12, 18, 11),
            'pinky': fing(-14, 14, 20, 12), 'thumb': (14.0, 16.0, 8.0, 8.0, 6.0)}


_explicar_s, _explicar_open = hs_S(), hs_explicar_loose()
# Fist beside the head, palm forward.
_explicar_up = P((126, 128), _explicar_s, 'wrist', yaw=0, pitch=0, roll=-6, scale=1.05, depth=50,
                 pole=(0.6, 1.0, 0.45))
# Dropped: the wrist bent forward, fingers hanging down and toward the viewer, back of the hand seen.
_explicar_down = P((130, 196), _explicar_open, 'wrist', yaw=0, pitch=150, roll=4, scale=1.1, depth=80,
                   pole=(0.5, 1.0, 0.45), ease='out')
_explicar_keys = [(0.0, _explicar_up), (0.15, _explicar_up), (0.45, _explicar_down), (0.7, dict(_explicar_up, ease='smooth')),
                  (1.0, _explicar_down), (1.45, _explicar_down), (1.7, dict(_explicar_up, ease='smooth'))]
SIGNS['explicar'] = {
    'poster': 0.45, 'dur': 1.7, 'hands': ['right', 'left'], 'handshape': _explicar_s,
    'keys': [(t, [p, mirrored(p)]) for t, p in _explicar_keys],
    'arrows': [{'d': 'M 100 112 Q 90 150 102 186'}, {'d': 'M 300 112 Q 310 150 298 186'}],
    'mirror_second': True,
}
TITLES['explicar'] = 'Sinal de explicar em Libras'
