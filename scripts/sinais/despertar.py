# DESPERTAR: the thumb and index pinched together (the other fingers folded) come to the outer
# corner of the eye; the fingers open into L and the hand rises beside the head until the index
# points up above it. Once. (UFSC Signbank DESPERTAR: Baby_beak + L, one hand; the INES DESPERTAR
# video shows it with both hands.)


def hs_despertar_pinch():
    """Small pinch: the index bends forward and its pad meets the thumb's pad above the fist."""
    shape = fist({'index': fing(2, 20, 60, 40)})
    shape['thumb'] = pinch_thumb(shape)
    return shape


_despertar_pinch, _despertar_l = hs_despertar_pinch(), hs_L()
# Pinch at the outer corner of the eye, palm forward, the hand beside the face.
_despertar_on = P((174, 98), _despertar_pinch, 'pinch', yaw=10, pitch=0, roll=20, scale=1.0, depth=40,
                  pole=(0.7, 1.0, 0.45))
# L beside the head, palm forward, the index pointing up above the head.
_despertar_up = P((160, 72), _despertar_l, 'thumb_tip', yaw=5, pitch=0, roll=-4, scale=1.05, depth=50,
                  pole=(0.7, 1.0, 0.45), ease='out')
SIGNS['despertar'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right'], 'handshape': _despertar_l,
    'keys': [(0.0, [_despertar_on]), (0.45, [_despertar_on]), (0.95, [_despertar_up]), (1.9, [_despertar_up]),
             (2.4, [dict(_despertar_on, ease='smooth')])],
    'marks': [(178, 92, 40)],
    'arrows': [{'d': 'M 86 118 L 86 72'}],
}
TITLES['despertar'] = 'Sinal de despertar em Libras'
