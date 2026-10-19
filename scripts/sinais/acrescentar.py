# ACRESCENTAR: both hands open and relaxed come together in front of the chest and close into a beak
# (fingertips gathered on the thumb). The support hand stays up, palm toward the body, fingers pointing
# across; the signing hand comes in from the side and up from below, and its beak touches the little-finger
# side of the support hand, as if adding one more part. Once. (UFSC Signbank COMPLEMENTAR; INES ACRESCENTAR
# agrees.)


def hs_acrescentar_open():
    """Relaxed open hand: fingers a little spread and a little curved, thumb out."""
    return {'index': fing(10, 8, 14, 9), 'middle': fing(2, 8, 14, 9), 'ring': fing(-6, 10, 14, 9),
            'pinky': fing(-13, 12, 15, 10), 'thumb': (34.0, 22.0, 10.0, 8.0, 8.0)}


def hs_acrescentar_beak():
    """Beak: fingers bent at the knuckles and middle joints, their tips gathered on the thumb's pad."""
    shape = {'index': fing(2, 52, 58, 34), 'middle': fing(0, 55, 58, 36), 'ring': fing(-1, 58, 56, 36),
             'pinky': fing(-2, 62, 54, 36)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


_acrescentar_open, _acrescentar_beak = hs_acrescentar_open(), hs_acrescentar_beak()
_acrescentar_pole = (0.4, 1.0, 0.45)
# Support (right-hand pose, mirrored): palm toward the body, fingers across toward the signing side,
# little finger at the bottom.
_acrescentar_sup = lambda shape: mirrored(P((166, 194), shape, 'wrist', yaw=180, pitch=-15, roll=88, scale=1.05,
                                            depth=55))
_acrescentar_sup_open, _acrescentar_sup_beak = _acrescentar_sup(_acrescentar_open), _acrescentar_sup(_acrescentar_beak)
# Signing hand: out to the side and low, open, palm forward and up ...
_acrescentar_out = P((110, 236), _acrescentar_open, 'wrist', yaw=-20, pitch=-30, roll=-30, scale=1.05, depth=60,
                     pole=_acrescentar_pole)
# ... then up from below to the little-finger side of the support hand, closed into a beak pointing up.
_acrescentar_on = P((208, 216), _acrescentar_beak, 'index_tip', yaw=-70, pitch=0, roll=8, scale=1.05, depth=58,
                    pole=_acrescentar_pole, via=(150, 250), ease='smooth')
SIGNS['acrescentar'] = {
    'poster': 1.2, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _acrescentar_beak,
    'handshape_view': {'yaw': -100},
    'keys': [(0.0, [_acrescentar_out, _acrescentar_sup_open]), (0.3, [_acrescentar_out, _acrescentar_sup_open]),
             (1.0, [_acrescentar_on, _acrescentar_sup_beak]), (1.9, [_acrescentar_on, _acrescentar_sup_beak]),
             (2.6, [dict(_acrescentar_out, via=(140, 250)), _acrescentar_sup_open])],
    'marks': [(194, 212, -95)],
    # In from the side, down and then up under the support hand.
    'arrows': [{'d': 'M 104 272 Q 160 290 192 246'}],
    'mirror_second': True,
}
TITLES['acrescentar'] = 'Sinal de acrescentar em Libras'
