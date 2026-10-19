# ROUBAR: the support hand stands open (B) in front of the chest, fingers up, palm toward the signing
# hand. The signing hand, open with the fingers spread (5), beside the support palm, closes into A
# (fist, thumb up) as if grabbing something and goes down, coming out under the support hand toward
# the body. Once. (UFSC Signbank ROUBAR: 5+A, support palm; INES ROUBAR1.)

_roubar_b, _roubar_5 = hs_B(), hs_5()
_roubar_b['thumb'] = (8.0, 12.0, 8.0, 6.0, 4.0)   # support thumb along the index


def hs_roubar_A():
    """A: fist, the thumb straight up along the side of the index."""
    shape = fist()
    shape['thumb'] = solve_thumb((17.0, -44.0, -1.5), pad_to=(-1.0, 0.0, 0.0), point=(0.0, -1.0, 0.0),
                                 pref=(-5.0, 10.0, 20.0, 0.0, 0.0))
    return shape


_roubar_a = hs_roubar_A()
# Support hand (a right-hand pose, mirrored): fingers up, palm toward the midline and a little toward
# the viewer.
_roubar_sup = mirrored(P((146, 226), _roubar_b, 'wrist', yaw=55, pitch=0, roll=-4, scale=1.0, depth=60))
_roubar_pole = (0.4, 1.0, 0.4)
# Open beside the support palm, palm toward it (and a little toward the viewer).
_roubar_open = P((160, 214), _roubar_5, 'wrist', yaw=50, pitch=0, roll=2, scale=1.0, depth=66, pole=_roubar_pole)
# Closed and down, under the support hand.
_roubar_down = P((206, 270), _roubar_a, 'wrist', yaw=25, pitch=0, roll=6, scale=1.0, depth=56, pole=_roubar_pole,
                 via=(186, 246), ease='in')
SIGNS['roubar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _roubar_5,
    'keys': [(0.0, [_roubar_open, _roubar_sup]), (0.35, [_roubar_open, _roubar_sup]),
             (0.95, [_roubar_down, _roubar_sup]), (1.8, [_roubar_down, _roubar_sup]),
             (2.4, [dict(_roubar_open, ease='smooth', via=(160, 246)), _roubar_sup])],
    'arrows': [{'d': 'M 134 196 Q 132 240 160 266'}],
    'mirror_second': True,
}
TITLES['roubar'] = 'Sinal de roubar em Libras'
