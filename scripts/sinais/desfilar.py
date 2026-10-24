# DESFILAR: the support forearm lies across in front of the chest, the hand open and flat, palm down. The
# signing hand, with the index and middle fingers pointing down like two legs, walks along the top of
# the support forearm with small touches, from the hand toward the elbow, like a model on a catwalk.
# Once. (UFSC Signbank DESFILAR and INES DESFILAR agree.)


def hs_desfilar_legs(swing=0.0):
    """Index and middle straight and a little apart (two legs) and bent down at the knuckles, ring and
    little finger folded, thumb out to the side. `swing` > 0 bends the index a little more at the knuckle
    and the middle finger less; < 0 the other way round (a step)."""
    shape = fist({'index': fing(8, 50 + 22 * swing, 4, 2), 'middle': fing(-6, 50 - 22 * swing, 4, 2)})
    shape['thumb'] = (44.0, 14.0, 6.0, 6.0, 4.0)
    return shape


def hs_desfilar_flat():
    """Support: open hand, fingers together, the thumb loose beside them."""
    return {'index': fing(2, 0, 0, 0), 'middle': fing(0, 0, 0, 0), 'ring': fing(-2, 0, 0, 0),
            'pinky': fing(-4, 0, 0, 0), 'thumb': (20.0, 10.0, 8.0, 6.0, 4.0)}


_desfilar_mid, _desfilar_a, _desfilar_b = hs_desfilar_legs(0.0), hs_desfilar_legs(1.0), hs_desfilar_legs(-1.0)
_desfilar_flat = hs_desfilar_flat()
# Support hand (defined as a right hand, then mirrored): across the body, palm down and seen a little
# from above, the fingers pointing toward the dominant side; the forearm runs level to the elbow.
_desfilar_base = mirrored(P((222, 236), _desfilar_flat, 'wrist', yaw=120, pitch=0, roll=94, scale=1.05, depth=70,
                            pole=(1.0, 0.3, 1.0)))


def _desfilar_at(shape, k, lift=0.0, ease='smooth'):
    # Palm down, the knuckles toward the viewer and the hand seen a little from above: the back of the hand
    # shows and the two fingers hang down side by side onto the forearm. k = 0 over the support hand's
    # wrist .. 1 near the elbow; `lift` raises the fingertips off the forearm between touches.
    x = 182 + 80 * k
    return P((x, 226 - lift), shape, 'fingertips', yaw=15, pitch=120, roll=-6, scale=1.05, depth=82, ease=ease,
             pole=(0.8, 0.6, 0.5))


_desfilar_keys = [(0.0, [_desfilar_at(_desfilar_mid, 0.0, 22)]), (0.3, [_desfilar_at(_desfilar_mid, 0.0, 22)]),
                  (0.55, [_desfilar_at(_desfilar_mid, 0.0, 0, 'in')])]
_desfilar_n = 4
for _desfilar_i in range(_desfilar_n):
    _desfilar_k = (_desfilar_i + 1) / _desfilar_n
    _desfilar_s = _desfilar_a if _desfilar_i % 2 == 0 else _desfilar_b
    _desfilar_t = 0.55 + 0.34 * (_desfilar_i + 1)
    _desfilar_keys += [(round(_desfilar_t - 0.17, 3), [_desfilar_at(_desfilar_s, _desfilar_k - 0.5 / _desfilar_n, 5)]),
                       (round(_desfilar_t, 3), [_desfilar_at(_desfilar_mid, _desfilar_k, 0, 'in')])]
_desfilar_end = 0.55 + 0.34 * _desfilar_n
_desfilar_keys += [(round(_desfilar_end + 0.5, 3), [_desfilar_at(_desfilar_mid, 1.0, 0)]),
                   (round(_desfilar_end + 1.0, 3), [_desfilar_at(_desfilar_mid, 0.0, 22)])]
SIGNS['desfilar'] = {
    'poster': 0.55, 'dur': round(_desfilar_end + 1.0, 3), 'hands': ['right', 'left'], 'handshape': _desfilar_mid,
    'handshape_view': {'yaw': 0, 'pitch': -50},
    'keys': [(t, [p[0], _desfilar_base]) for t, p in _desfilar_keys],
    'marks': [(170, 222, -60)],
    # Below the support forearm: along it, from the hand toward the elbow.
    'arrows': [{'d': 'M 176 262 L 262 262'}],
    'mirror_second': True,
}
TITLES['desfilar'] = 'Sinal de desfilar em Libras'
