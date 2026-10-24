# ESCREVER: the support hand lies open in front of the chest, palm up. The signing hand, closed as if
# holding a pen (the thumb's pad on the side of the bent index, the other fingers folded), writes on that
# palm: it slides over it toward the fingertips with small zigzags, once. (UFSC Signbank ESCREVER: Key on
# the B weak hand, rubbing; the INES ESCREVER1 video agrees.)


def hs_escrever_key():
    """Key: the index bent (looser than the folded fingers), the thumb's pad on the side of its middle
    phalanx, the other three fingers folded into the palm (holding a pen)."""
    shape = fist({'index': fing(0, 70, 85, 40)})
    pts, frames = finger_chain('index', shape['index'])
    mid = vadd(pts[1], vmul(vsub(pts[2], pts[1]), 0.45))
    side = vadd(mid, (seg_radius('index', 1) + seg_radius('thumb', 2) + 0.3, 0.0, 0.0))
    shape['thumb'] = solve_thumb(side, pad_to=(-1.0, 0.0, 0.0), point=vsub(pts[2], pts[1]),
                                 pref=(-5.0, 20.0, 40.0, 15.0, 15.0), w_point=30.0)
    return shape


def hs_escrever_flat():
    """Support hand: open, fingers together and a little curved, thumb a little apart."""
    return {'index': fing(2, 8, 12, 8), 'middle': fing(0, 8, 12, 8), 'ring': fing(-2, 8, 12, 8),
            'pinky': fing(-4, 10, 12, 8), 'thumb': (22.0, 18.0, 10.0, 8.0, 6.0)}


_escrever_key, _escrever_flat = hs_escrever_key(), hs_escrever_flat()
# Support hand (defined as a right hand, then mirrored): palm up, tipped a little toward the viewer,
# fingers pointing across toward the midline.
_escrever_base = mirrored(P((140, 242), _escrever_flat, 'wrist', yaw=-50, pitch=0, roll=92, scale=1.1, depth=70))
# The fingers point down onto the support palm, the thumb side toward the viewer: the thumb's pad on the
# side of the bent index reads, and the "pen" (the index and thumb tips) rests on the palm.
_escrever_pose = lambda at, **kw: P(at, _escrever_key, 'index_tip', yaw=-60, pitch=30, roll=160, scale=1.1, depth=74,
                                    pole=(0.4, 1.0, 0.4), **kw)
_escrever_up = _escrever_pose((232, 214))
# Writing: from the heel of the support palm toward its fingertips, with small zigzags.
_escrever_path = [(236, 234), (228, 228), (220, 235), (212, 229), (204, 236)]
_escrever_keys = [(0.0, _escrever_up), (0.3, _escrever_up)]
for _escrever_k, _escrever_at in enumerate(_escrever_path):
    _escrever_keys.append((round(0.6 + 0.18 * _escrever_k, 2), _escrever_pose(_escrever_at, ease='linear')))
_escrever_keys += [(1.9, _escrever_pose(_escrever_path[-1])), (2.4, _escrever_up)]
SIGNS['escrever'] = {
    'poster': 0.96, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _escrever_key, 'handshape_view': {'yaw': -40},
    'keys': [(t, [p, _escrever_base]) for t, p in _escrever_keys],
    'marks': [(250, 240, 90)],
    # The zigzag over the palm, toward its fingertips.
    'arrows': [{'d': 'M 246 190 L 236 184 L 226 192 L 216 184 L 204 190'}],
    'mirror_second': True,
}
TITLES['escrever'] = 'Sinal de escrever em Libras'
