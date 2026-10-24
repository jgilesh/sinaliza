# ESCREVER NO QUADRO: the hand closed as if holding chalk (the thumb's pad on the side of the bent index,
# the other fingers folded) rises above the head on the other side and moves across to the signing side
# in a zigzag, writing on an imaginary board, palm forward (the eyes follow the hand; the face is not
# drawn changing). One pass. (UFSC Signbank ESCREVER-QUADRO: Key, zigzag. There is no INES video.)


def hs_escrever_no_quadro_key():
    """Key: the index bent (looser than the folded fingers), the thumb's pad on the side of its middle
    phalanx, the other three fingers folded into the palm (holding chalk)."""
    shape = fist({'index': fing(0, 70, 85, 40)})
    pts, frames = finger_chain('index', shape['index'])
    mid = vadd(pts[1], vmul(vsub(pts[2], pts[1]), 0.45))
    side = vadd(mid, (seg_radius('index', 1) + seg_radius('thumb', 2) + 0.3, 0.0, 0.0))
    shape['thumb'] = solve_thumb(side, pad_to=(-1.0, 0.0, 0.0), point=vsub(pts[2], pts[1]),
                                 pref=(-5.0, 20.0, 40.0, 15.0, 15.0), w_point=30.0)
    return shape


_enq_key = hs_escrever_no_quadro_key()
_enq_pole = (0.9, -0.2, 0.6)   # the elbow raised and out, so the forearm stays above the eyes
# Above the head, the palm forward and turned a little so the thumb on the bent index shows; the "chalk"
# (the index and thumb tips) tipped forward, toward the board.
_enq_pose = lambda at, **kw: P(at, _enq_key, 'wrist', yaw=-40, pitch=30, roll=0, scale=1.0, depth=70, pole=_enq_pole, **kw)
_enq_rest = P((150, 208), _enq_key, 'wrist', yaw=-40, pitch=20, roll=0, scale=1.0, depth=60, pole=(0.6, 1.0, 0.45))
# Writing: from the other side over to the signing side, in a zigzag.
_enq_path = [(222, 56), (206, 46), (190, 58), (174, 46), (158, 58), (140, 48)]
_enq_keys = [(0.0, _enq_rest), (0.2, _enq_rest), (0.6, _enq_pose(_enq_path[0]))]
for _enq_k, _enq_at in enumerate(_enq_path[1:], 1):
    _enq_keys.append((round(0.6 + 0.16 * _enq_k, 2), _enq_pose(_enq_at, ease='linear')))
_enq_keys += [(1.9, _enq_pose(_enq_path[-1])), (2.5, dict(_enq_rest, ease='smooth'))]
SIGNS['escrever-no-quadro'] = {
    'poster': 0.92, 'dur': 2.5, 'hands': ['right'], 'handshape': _enq_key, 'handshape_view': {'yaw': -40},
    'keys': [(t, [p]) for t, p in _enq_keys],
    # The zigzag above the head, toward the signing side.
    'arrows': [{'d': 'M 228 10 L 214 4 L 200 12 L 186 4 L 172 12 L 158 4 L 142 8'}],
}
TITLES['escrever-no-quadro'] = 'Sinal de escrever no quadro em Libras'
