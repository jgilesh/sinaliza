# XINGAR: both hands in the "key" shape (fist, the thumb pad pressed on the side of the bent index).
# In alternation, each hand leaves the lips and is thrown forward, the index and thumb opening a
# little (an open pinch), then comes back; three or four throws in all. (UFSC Signbank OFENDER.)


def hs_xingar_key():
    """Key: the index bent (looser than the folded fingers), the thumb's pad on the side of its middle
    phalanx, the other three fingers folded into the palm."""
    shape = fist({'index': fing(0, 70, 85, 40)})
    pts, frames = finger_chain('index', shape['index'])
    mid = vadd(pts[1], vmul(vsub(pts[2], pts[1]), 0.45))
    side = vadd(mid, (seg_radius('index', 1) + seg_radius('thumb', 2) + 0.3, 0.0, 0.0))
    shape['thumb'] = solve_thumb(side, pad_to=(-1.0, 0.0, 0.0), point=vsub(pts[2], pts[1]),
                                 pref=(-5.0, 20.0, 40.0, 15.0, 15.0), w_point=30.0)
    return shape


def hs_xingar_open():
    """Open pinch: the index curved, the thumb apart from it and curved toward it, a gap between the
    tips; the other three fingers folded."""
    shape = fist({'index': fing(2, 35, 45, 25)})
    shape['thumb'] = (20.0, 35.0, 40.0, 10.0, 15.0)
    return shape


_xing_key, _xing_open = hs_xingar_key(), hs_xingar_open()
# Seen from the thumb side, so the thumb on the bent index (and then the open pinch) reads.
_xing_pole = (0.5, 1.0, 0.45)
_xing_lips = P((190, 127), _xing_key, 'thumb_tip', yaw=-100, pitch=0, roll=-8, scale=1.0, depth=35, pole=_xing_pole)
_xing_out = P((122, 168), _xing_open, 'thumb_tip', yaw=-100, pitch=25, roll=-25, scale=1.2, depth=95, pole=_xing_pole,
              ease='out')
_xing_keys = [(0.0, [_xing_lips, mirrored(_xing_out)]), (0.3, [_xing_lips, mirrored(_xing_out)])]
for _xing_k in range(4):                    # four throws, right and left in turn
    _xing_t = round(0.3 + 0.42 * (_xing_k + 1), 2)
    _xing_r, _xing_l = (_xing_out, _xing_lips) if _xing_k % 2 == 0 else (_xing_lips, _xing_out)
    _xing_keys.append((_xing_t, [dict(_xing_r, ease='out'), mirrored(dict(_xing_l, ease='out'))]))
_xing_keys.append((2.6, _xing_keys[-1][1]))
SIGNS['xingar'] = {
    'poster': 0.3, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _xing_key, 'handshape_view': {'yaw': -100},
    'keys': _xing_keys,
    # From the lips forward and out, on each side.
    'arrows': [{'d': 'M 170 112 Q 140 104 116 130'}, {'d': 'M 230 112 Q 260 104 284 130'}],
    'mirror_second': True,
}
TITLES['xingar'] = 'Sinal de xingar em Libras'
