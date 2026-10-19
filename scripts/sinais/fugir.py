# FUGIR: both flat hands (B) lean together with the fingertips touching, a triangle in front of the
# chest, and rise to face height; then they part sharply: the dominant hand goes out and up beside the
# head and the other pulls back near the chin, both closing into a beak (fingertips on the thumb).
# Once. (UFSC Signbank FUGIR: B+Beak, mão fraca: pontas. INES FUGIR shows another variant.)


def hs_fugir_beak():
    """Beak: fingers straight-ish and together, bent at the knuckles, their tips gathered on the thumb's
    pad."""
    shape = {'index': fing(2, 52, 58, 34), 'middle': fing(0, 55, 58, 36), 'ring': fing(-1, 58, 56, 36),
             'pinky': fing(-2, 62, 54, 36)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


_fugir_b, _fugir_beak = hs_B(), hs_fugir_beak()
# The triangle: palms toward each other and a little down, fingertips touching at the top.
_fugir_low = P((194, 206), _fugir_b, 'fingertips', yaw=125, pitch=0, roll=38, scale=1.05, depth=60, pole=(0.5, 1.0, 0.4))
_fugir_high = dict(_fugir_low, at=(194, 174))
# Dominant hand: out and up beside the head, the beak pointing up, palm forward.
_fugir_r_end = P((104, 118), _fugir_beak, 'wrist', yaw=40, pitch=-20, roll=-10, scale=1.1, depth=60, ease='out',
                 pole=(0.5, 1.0, 0.4))
# Other hand: pulled back below the chin on its side, the beak pointing up.
_fugir_l_end = mirrored(P((164, 210), _fugir_beak, 'wrist', yaw=40, pitch=-20, roll=-10, scale=1.05, depth=45,
                          ease='out', pole=(0.5, 1.0, 0.4)))
SIGNS['fugir'] = {
    'poster': 0.9, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _fugir_b,
    'keys': [(0.0, [_fugir_low, mirrored(_fugir_low)]), (0.3, [_fugir_low, mirrored(_fugir_low)]),
             (0.7, [_fugir_high, mirrored(_fugir_high)]), (0.9, [_fugir_high, mirrored(_fugir_high)]),
             (1.15, [_fugir_r_end, _fugir_l_end]), (2.0, [_fugir_r_end, _fugir_l_end]),
             (2.6, [dict(_fugir_low, ease='smooth'), mirrored(dict(_fugir_low, ease='smooth'))])],
    'marks': [(200, 168, 0)],
    # Up together, then the dominant hand flies out and up.
    'arrows': [{'d': 'M 126 244 L 126 212'}, {'d': 'M 274 244 L 274 212'}, {'d': 'M 166 142 Q 146 124 138 94'}],
    'mirror_second': True,
}
TITLES['fugir'] = 'Sinal de fugir em Libras'
