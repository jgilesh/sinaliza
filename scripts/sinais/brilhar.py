# BRILHAR: both hands start closed (S) in front of the upper chest, below the chin, and open into 5
# (fingers straight and spread) as they rise to the sides of the head, palms forward, the fingers
# fluttering. Once. (UFSC Signbank BRILHAR; the INES video shows another form.)


def hs_brilhar_flutter(odd=None):
    """5 (fingers straight and spread, thumb out), or with every other finger a little bent for the
    flutter (odd=True: index and ring; odd=False: middle and little finger)."""
    bend, flat = (0, 28, 18), (0, 3, 2)
    a, b = (flat, flat) if odd is None else (bend, flat) if odd else (flat, bend)
    return {'index': fing(14, *a), 'middle': fing(3, *b), 'ring': fing(-8, *a), 'pinky': fing(-18, *b),
            'thumb': (32.0, 18.0, 6.0, 6.0, 4.0)}


_brilhar_s, _brilhar_5 = hs_S(), hs_brilhar_flutter()
_brilhar_fa, _brilhar_fb = hs_brilhar_flutter(True), hs_brilhar_flutter(False)
_brilhar_fist = P((160, 204), _brilhar_s, 'wrist', yaw=30, pitch=0, roll=4, scale=1.05, depth=60, pole=(0.4, 1.0, 0.4))
_brilhar_open = lambda shape, **kw: P((104, 132), shape, 'wrist', yaw=8, pitch=0, roll=-22, scale=1.08, depth=70,
                                      pole=(0.7, 1.0, 0.4), **kw)
_brilhar_up = _brilhar_open(_brilhar_5, via=(146, 178), ease='out')
_brilhar_keys = [(0.0, [_brilhar_fist, mirrored(_brilhar_fist)]), (0.4, [_brilhar_fist, mirrored(_brilhar_fist)]),
                 (1.0, [_brilhar_up, mirrored(_brilhar_up)])]
for _brilhar_k in range(3):
    _brilhar_p = _brilhar_open(_brilhar_fa if _brilhar_k % 2 == 0 else _brilhar_fb)
    _brilhar_keys.append((round(1.12 + 0.12 * _brilhar_k, 2), [_brilhar_p, mirrored(_brilhar_p)]))
_brilhar_rest = _brilhar_open(_brilhar_5)
_brilhar_keys += [(1.5, [_brilhar_rest, mirrored(_brilhar_rest)]), (1.7, [_brilhar_rest, mirrored(_brilhar_rest)]),
                  (2.2, [dict(_brilhar_fist, via=(150, 190)), mirrored(dict(_brilhar_fist, via=(150, 190)))])]
SIGNS['brilhar'] = {
    'poster': 1.6, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _brilhar_5,
    'keys': _brilhar_keys,
    'arrows': [{'d': 'M 158 232 Q 112 222 92 182'}, {'d': 'M 242 232 Q 288 222 308 182'}],
    'mirror_second': True,
}
TITLES['brilhar'] = 'Sinal de brilhar em Libras'
