# APRESENTAR: both hands flat (B), palms up, start crossed in front of the body (the dominant hand on
# top); they open out to the sides, palms still up, fingers pointing out and forward, like showing
# something. Once. (UFSC Signbank APRESENTAR: B, palms up, crossed then out; the INES video shows
# another variant.)



def hs_apresentar_b():
    """B: flat hand, fingers together, the thumb resting along the side of the index (so it never
    points straight at the viewer while the palm faces up)."""
    shape = hs_B()
    shape['thumb'] = (-18.0, 8.0, 10.0, 6.0, 4.0)
    return shape


_apr_b = hs_apresentar_b()
# Crossed: palm up, fingers pointing across the body toward the other side.
_apr_cross = P((176, 226), _apr_b, 'wrist', yaw=-50, pitch=15, roll=-265, scale=1.05, depth=70, pole=(0.4, 1.0, 0.4))
# Open: out on each side, palm up and a little toward the viewer, fingers out and forward. (The angles
# are chosen so that, on the way, the palm stays up and the fingers sweep round through "forward".)
_apr_open = P((124, 214), _apr_b, 'wrist', yaw=-130, pitch=150, roll=-270, scale=1.1, depth=80, pole=(0.5, 1.0, 0.4),
              via=(150, 236), ease='out')
_apr_cross_l = mirrored(dict(_apr_cross, at=(178, 238)))
_apr_open_l = mirrored(_apr_open)
SIGNS['apresentar'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _apr_b,
    'handshape_view': {'yaw': 0},
    'keys': [(0.0, [_apr_cross, _apr_cross_l]), (0.4, [_apr_cross, _apr_cross_l]), (1.0, [_apr_open, _apr_open_l]),
             (1.8, [_apr_open, _apr_open_l]),
             (2.4, [dict(_apr_cross, via=(150, 250)), dict(_apr_cross_l, via=(250, 262))])],
    'arrows': [{'d': 'M 172 262 Q 130 262 110 240'}, {'d': 'M 228 262 Q 270 262 290 240'}],
    'mirror_second': True,
}
TITLES['apresentar'] = 'Sinal de apresentar em Libras'
