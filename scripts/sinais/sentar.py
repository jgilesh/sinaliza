# SENTAR: the support hand in U (index and middle straight and together), lying across in front of the
# belly, palm down; the signing hand, with the index and middle fingers apart and curved like bent
# legs, comes down and sets their tips on the support fingers, like someone sitting on a bench. Once.
# (UFSC Signbank SENTAR "V_curved" on "U", INES SENTAR agree.)


def hs_sentar_u():
    """U of Libras: index and middle straight and side by side, ring and little fingers folded under the
    thumb."""
    shape = fist({'index': fing(-1, 0, 0, 0), 'middle': fing(1, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


def hs_sentar_legs():
    """V curved: index and middle apart, bent at the knuckle and more at the middle joint (bent legs),
    ring and little fingers folded under the thumb."""
    shape = fist({'index': fing(10, 30, 70, 30), 'middle': fing(-6, 30, 70, 30)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


_sentar_u, _sentar_legs = hs_sentar_u(), hs_sentar_legs()
_sentar_pole = (0.25, 1.0, 0.55)
# Support hand (defined as a right hand, then mirrored): palm down, tipped a little toward the viewer,
# the two fingers pointing across toward the midline.
_sentar_base = mirrored(P((146, 252), _sentar_u, 'wrist', yaw=125, pitch=0, roll=92, scale=1.1, depth=66))


def _sentar_top(lift, **kw):
    # Palm down, the fingers pointing forward (toward the viewer) and the hand seen a little from above:
    # the two bent fingers stand apart side by side and curve down onto the support fingers, like legs.
    return P((196, 242 - lift), _sentar_legs, 'fingertips', yaw=30, pitch=120, roll=-8, scale=1.1, depth=74,
             pole=_sentar_pole, **kw)


_sentar_high, _sentar_on = _sentar_top(24), _sentar_top(0, ease='in')
SIGNS['sentar'] = {
    'poster': 1.0, 'dur': 2.3, 'hands': ['right', 'left'], 'handshape': _sentar_legs, 'handshape_view': {'yaw': -22, 'pitch': -55},
    'keys': [(0.0, [_sentar_high, _sentar_base]), (0.35, [_sentar_high, _sentar_base]),
             (0.85, [_sentar_on, _sentar_base]), (1.8, [_sentar_on, _sentar_base]),
             (2.3, [dict(_sentar_high, ease='smooth'), _sentar_base])],
    'marks': [(212, 242, 55)],
    'arrows': [{'d': 'M 146 198 L 146 224'}],
    'mirror_second': True,
}
TITLES['sentar'] = 'Sinal de sentar em Libras'
