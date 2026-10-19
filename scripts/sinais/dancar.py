# DANÇAR: the support hand open, palm up, in front of the body; the signing hand in V with the two
# fingers pointing down like legs, back of the hand to the viewer, swings from side to side in an
# arc just above the support palm, a few times. (UFSC Signbank DANÇAR and INES DANÇAR1 agree.)


def hs_dancar_v():
    """V with the two fingers well apart, like legs; the others folded under the thumb."""
    shape = fist({'index': fing(16, 0, 0, 0), 'middle': fing(-12, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


_danc_v = hs_dancar_v()


def hs_dancar_open():
    """Open hand, fingers together and nearly straight, thumb apart (the support palm)."""
    return {'index': fing(2, 6, 8, 4), 'middle': fing(0, 6, 8, 4), 'ring': fing(-2, 6, 8, 4),
            'pinky': fing(-4, 8, 8, 4), 'thumb': (30.0, 16.0, 8.0, 6.0, 4.0)}


_danc_open = hs_dancar_open()
# Support hand, defined as a right hand (palm up, fingers toward the midline) and mirrored.
_danc_base = mirrored(P((156, 252), _danc_open, 'wrist', yaw=-50, pitch=0, roll=90, scale=1.1, depth=70))


def _danc_top(side):
    """Signing hand; side = -1 (toward the signer's right) .. +1 (left). The V hangs from the
    wrist and swings like a pendulum, the fingertips just above the support palm."""
    return P((206 + 13 * side, 236 - 3 * abs(side)), _danc_v, 'fingertips', yaw=180, pitch=-12, roll=180 + 16 * side,
             scale=1.05, depth=76, pole=(0.3, 1.0, 0.45))


_danc_l, _danc_m, _danc_r = _danc_top(-1.0), _danc_top(0.0), _danc_top(1.0)
_danc_keys = [(0.0, [_danc_m, _danc_base]), (0.3, [_danc_m, _danc_base])]
_danc_t = 0.3
for _danc_k in range(2):                  # two swings each way
    _danc_keys += [(round(_danc_t + 0.2, 2), [_danc_l, _danc_base]), (round(_danc_t + 0.4, 2), [_danc_m, _danc_base]),
                   (round(_danc_t + 0.6, 2), [_danc_r, _danc_base]), (round(_danc_t + 0.8, 2), [_danc_m, _danc_base])]
    _danc_t += 0.8
_danc_keys.append((round(_danc_t + 0.5, 2), [_danc_m, _danc_base]))
SIGNS['dancar'] = {
    'poster': 0.5, 'dur': round(_danc_t + 0.5, 2), 'hands': ['right', 'left'], 'handshape': _danc_v,
    'keys': _danc_keys,
    # A swing arrow under the support hand: side to side.
    'arrows': [{'d': 'M 180 276 Q 206 288 232 276', 'both': True}],
    'mirror_second': True,
}
TITLES['dancar'] = 'Sinal de dançar em Libras'
