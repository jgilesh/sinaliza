# PINTAR: the support hand open and upright (B) in front of the shoulder on its own side, palm toward
# the signing hand. The signing hand, flat, brushes its fingertips up and down the support palm like a
# brush, bending at the knuckles on the way up and straightening on the way down, three times.
# (UFSC Signbank PINTAR: B+B_bent / B, on the support palm. The INES PINTAR1 video shows a one-handed
# variant: the flat hand brushing up and down in the air, as if painting a wall.)

_pint_b = hs_B()


def hs_pintar_bent():
    """B bent at the knuckles: the fingers straight and together, folded forward at the base."""
    return {'index': fing(2, 55, 0, 0), 'middle': fing(0, 55, 0, 0), 'ring': fing(-2, 55, 0, 0),
            'pinky': fing(-4, 55, 0, 0), 'thumb': (28.0, 16.0, 8.0, 6.0, 4.0)}


_pint_bent = hs_pintar_bent()
# Support hand (a right-hand pose, mirrored): upright, palm turned toward the signing hand and the viewer.
_pint_sup = mirrored(P((166, 228), _pint_b, 'wrist', yaw=58, pitch=0, roll=-2, scale=1.1, depth=70,
                       pole=(0.3, 1.0, 0.45)))
_pint_pole = (0.5, 1.0, 0.4)
# Signing hand: palm down, fingers pointing across at the support palm, the back of the hand tipped up
# toward the viewer. Low: flat, the fingertips at the bottom of the support palm...
_pint_low = P((228, 210), _pint_b, 'fingertips', yaw=112, pitch=0, roll=84, scale=1.1, depth=82, pole=_pint_pole,
              ease='linear')
# ...high: bent at the knuckles, the fingertips near the top of the support palm.
_pint_high = P((228, 176), _pint_bent, 'fingertips', yaw=112, pitch=0, roll=70, scale=1.1, depth=82, pole=_pint_pole,
               ease='linear')
_pint_keys = [(0.0, [_pint_low, _pint_sup]), (0.3, [_pint_low, _pint_sup])]
for _pint_k in range(3):
    _pint_t = 0.3 + 0.6 * _pint_k
    _pint_keys += [(_pint_t + 0.3, [_pint_high, _pint_sup]), (_pint_t + 0.6, [_pint_low, _pint_sup])]
_pint_keys.append((2.6, [_pint_low, _pint_sup]))
SIGNS['pintar'] = {
    'poster': 0.6, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _pint_b,
    'keys': _pint_keys,
    # Beside the support hand: up and down along the palm.
    'arrows': [{'d': 'M 272 166 L 272 216', 'both': True}],
    # The fingertips brush the support palm.
    'marks': [(236, 192, 90)],
    'mirror_second': True,
}
TITLES['pintar'] = 'Sinal de pintar em Libras'
