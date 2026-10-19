# COMPRAR: the support hand lies open in front of the chest, palm up. The signing hand, rubbing the
# thumb on the fingertips (the "money" gesture), passes over the support palm and goes out in an arc
# to the dominant side and forward, ending as a fist with the thumb up. Once. (UFSC Signbank COMPRAR
# "Money+L"; the INES video shows another variant.)


def hs_comprar_money(k=0.0):
    """Fingers bent at the knuckles and middle joints, their tips gathered on the thumb's pad; k (0..1)
    rolls the fingertips a little over the thumb (the rubbing)."""
    shape = {'index': fing(2, 52 + 6 * k, 58 - 6 * k, 34), 'middle': fing(0, 55 + 5 * k, 58 - 5 * k, 36),
             'ring': fing(-1, 58 + 4 * k, 56 - 4 * k, 36), 'pinky': fing(-2, 62 + 3 * k, 54 - 3 * k, 36)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


def hs_comprar_a():
    """Fist with the thumb straight up beside it (thumbs up): the thumb along the side of the index,
    its tip above the knuckles."""
    shape = fist()
    shape['thumb'] = solve_thumb((17.0, -44.0, -1.5), pad_to=(-1.0, 0.0, 0.0), point=(0.0, -1.0, 0.0),
                                 pref=(-5.0, 10.0, 20.0, 0.0, 0.0))
    return shape


def hs_comprar_flat():
    """Support hand: open, fingers together and a little curved, thumb a little apart."""
    return {'index': fing(2, 8, 12, 8), 'middle': fing(0, 8, 12, 8), 'ring': fing(-2, 8, 12, 8),
            'pinky': fing(-4, 10, 12, 8), 'thumb': (22.0, 18.0, 10.0, 8.0, 6.0)}


_comprar_m0, _comprar_m1 = hs_comprar_money(0.0), hs_comprar_money(1.0)
_comprar_a, _comprar_flat = hs_comprar_a(), hs_comprar_flat()
# Support hand (defined as a right hand, then mirrored): palm up, tipped a little toward the viewer,
# fingers pointing across toward the midline.
_comprar_base = mirrored(P((140, 242), _comprar_flat, 'wrist', yaw=-50, pitch=0, roll=92, scale=1.1, depth=70))
# Above the support palm, the gathered fingertips pointing down at it, the thumb side turned to the
# viewer: the fingertips on the thumb read, and the support palm shows below.
_comprar_over = lambda shape, at: P(at, shape, 'wrist', yaw=-60, pitch=20, roll=170, scale=1.05, depth=72,
                                    pole=(0.45, 1.0, 0.4))
# Out on the dominant side, chest height and forward: thumbs up, the palm turned toward the midline.
_comprar_end = P((118, 196), _comprar_a, 'wrist', yaw=-35, pitch=0, roll=-6, scale=1.12, depth=85,
                 via=(176, 236), ease='out', pole=(0.45, 1.0, 0.4))
_comprar_keys = [(0.0, [_comprar_over(_comprar_m0, (214, 188)), _comprar_base]),
                 (0.2, [_comprar_over(_comprar_m0, (214, 188)), _comprar_base])]
for _comprar_i in range(2):   # rubbing while passing over the palm
    _t = 0.2 + 0.3 * _comprar_i
    _comprar_keys += [(_t + 0.15, [_comprar_over(_comprar_m1, (208 - 8 * _comprar_i, 192)), _comprar_base]),
                      (_t + 0.3, [_comprar_over(_comprar_m0, (204 - 8 * _comprar_i, 194)), _comprar_base])]
_comprar_keys += [(1.3, [_comprar_end, _comprar_base]), (2.0, [_comprar_end, _comprar_base]),
                  (2.5, [dict(_comprar_over(_comprar_m0, (214, 188)), via=(150, 170)), _comprar_base])]
del _t
SIGNS['comprar'] = {
    'poster': 0.35, 'dur': 2.5, 'hands': ['right', 'left'], 'handshape': _comprar_m0, 'handshape_view': {'yaw': -85},
    'keys': _comprar_keys,
    # From over the palm, down and out to the dominant side, then up.
    'arrows': [{'d': 'M 198 262 Q 140 272 104 238'}],
    'mirror_second': True,
}
TITLES['comprar'] = 'Sinal de comprar em Libras'
