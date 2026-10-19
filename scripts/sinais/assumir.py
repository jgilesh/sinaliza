# ASSUMIR: the support hand stands open and upright in front of the chest, palm toward the signing
# hand. The signing hand, index and middle straight and together (U), starts up on its own side,
# then comes across and bends at the wrist until the pads of the two fingers rest on the support
# palm. Once. (UFSC Signbank ASSUMIR: [Libras_U] on the weak hand's palm (B), final contact; the
# INES ASSUMIR1 video shows another variant.)


def hs_assumir_u():
    """U: index and middle straight up and together, the other two folded under the thumb."""
    shape = fist({'index': fing(1, 0, 0, 0), 'middle': fing(-1, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


_assumir_u, _assumir_b = hs_assumir_u(), hs_B()
# Support hand, defined as a right hand (palm toward the midline, turned a little to the viewer) and
# mirrored.
_assumir_sup = mirrored(P((180, 244), _assumir_b, 'wrist', yaw=62, pitch=0, roll=4, scale=1.05, depth=55))
# Start: U up on the signing side, palm to the viewer.
_assumir_up = P((126, 236), _assumir_u, 'wrist', yaw=10, pitch=0, roll=-4, scale=1.05, depth=60, pole=(0.4, 1.0, 0.4))
# On the support palm: back of the hand to the viewer, the two fingers leaning over to the palm.
_assumir_on = P((212, 196), _assumir_u, 'fingertips', yaw=140, pitch=0, roll=48, scale=1.05, depth=62,
                pole=(0.35, 1.0, 0.4), ease='out')
SIGNS['assumir'] = {
    'poster': 1.1, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _assumir_u,
    'keys': [(0.0, [_assumir_up, _assumir_sup]), (0.35, [_assumir_up, _assumir_sup]),
             (0.9, [_assumir_on, _assumir_sup]), (1.8, [_assumir_on, _assumir_sup]),
             (2.4, [dict(_assumir_up, ease='smooth'), _assumir_sup])],
    'marks': [(212, 190, -40)],
    'arrows': [{'d': 'M 118 164 Q 150 138 184 158'}],
    'mirror_second': True,
}
TITLES['assumir'] = 'Sinal de assumir em Libras'
