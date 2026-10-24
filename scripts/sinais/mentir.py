# MENTIR: index up with its tip curled into a hook, the other fingers folded under the thumb. The hook
# starts beside the mouth on the signing side, at the height of the upper lip, palm toward the face,
# and brushes down and in past the lips to the chin; 3 times. (UFSC Signbank MENTIR: 1 curvo, acima
# dos lábios; the INES video agrees.)


def hs_mentir_hook():
    """Index up, curled at the middle and end joints into a hook; others folded, thumb over the middle."""
    shape = fist({'index': fing(2, 0, 58, 38)})
    shape['thumb'] = thumb_over(shape, ['middle'])
    return shape


_mentir_h = hs_mentir_hook()
# Palm turned toward the face and a little toward the viewer: the hook shows in profile, its tip
# curling toward the mouth.
_mentir_top = P((180, 120), _mentir_h, 'index_tip', yaw=88, pitch=0, roll=-4, scale=1.0, depth=40,
                pole=(0.5, 1.0, 0.45), ease='smooth')
_mentir_low = P((192, 140), _mentir_h, 'index_tip', yaw=88, pitch=0, roll=10, scale=1.0, depth=40,
                pole=(0.5, 1.0, 0.45), ease='in', via=(184, 134))
_mentir_keys = [(0.0, [_mentir_top]), (0.3, [_mentir_top])]
for _mentir_i in range(3):
    _mentir_t = 0.3 + 0.5 * _mentir_i
    _mentir_keys += [(_mentir_t + 0.25, [_mentir_low]), (_mentir_t + 0.5, [_mentir_top])]
_mentir_keys += [(2.4, [_mentir_top])]
SIGNS['mentir'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right'], 'handshape': _mentir_h, 'handshape_view': {'yaw': -70},
    'keys': _mentir_keys,
    'arrows': [{'d': 'M 132 112 Q 130 138 148 152'}],
}
TITLES['mentir'] = 'Sinal de mentir em Libras'
