# PROVOCAR: both hands with the index out (others closed). The dominant hand is higher, near the
# shoulder, index up; the other hand is lower, in front of the chest, its index pointing at the
# dominant hand. The index fingers poke toward each other in turn, a few times.
# (UFSC Signbank PROVOCAR: 1/1; INES PROVOCAR1 agrees.)

_provocar_1 = hs_1()
_provocar_pole = (0.5, 1.0, 0.45)


def _provocar_high(poke):
    """Dominant index up beside the shoulder; poke tips it toward the other hand."""
    return P((132 + 10 * poke, 108 + 8 * poke), _provocar_1, 'index_tip', yaw=30, pitch=0, roll=4 + 20 * poke,
             scale=1.05, depth=50, pole=_provocar_pole)


def _provocar_low(poke):
    """Other index (a right-hand pose, mirrored) pointing up and across at the dominant hand."""
    return mirrored(P((228 + 10 * poke, 176 - 8 * poke), _provocar_1, 'index_tip', yaw=10, pitch=0, roll=52,
                      scale=1.05, depth=60 + 15 * poke))


_provocar_keys = [(0.0, [_provocar_high(0), _provocar_low(0)]), (0.3, [_provocar_high(0), _provocar_low(0)])]
for _provocar_k in range(3):
    _provocar_t = 0.55 + 0.4 * _provocar_k
    _provocar_keys.append((round(_provocar_t, 2), [_provocar_high(1), _provocar_low(0)]))
    _provocar_keys.append((round(_provocar_t + 0.2, 2), [_provocar_high(0), _provocar_low(1)]))
_provocar_keys += [(1.8, [_provocar_high(0), _provocar_low(0)]), (2.2, [_provocar_high(0), _provocar_low(0)])]
SIGNS['provocar'] = {
    'poster': 0.3, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _provocar_1,
    'keys': _provocar_keys,
    # Short two-headed pokes at each fingertip, toward the other hand.
    'arrows': [{'d': 'M 114 100 L 126 109', 'both': True}, {'d': 'M 166 190 L 154 181', 'both': True}],
    'mirror_second': True,
}
TITLES['provocar'] = 'Sinal de provocar em Libras'
