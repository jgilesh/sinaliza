# BOBAGEM: both hands in the "key" shape (fist with the thumb pad pressed on the side of the bent
# index). They start together in front of the chest, knuckles toward each other and almost touching;
# at the same time they go up and out to the sides while the wrists turn (palms forward, knuckles up),
# and come back to the middle; twice. (UFSC Signbank BOBAGEM. The INES BOBAGEM video shows a
# variant with Y hands.)


def hs_bob_key():
    """Key: the index bent (looser than the folded fingers), the thumb's pad on the side of its middle
    phalanx, the other three fingers folded into the palm."""
    shape = fist({'index': fing(0, 70, 85, 40)})
    pts, frames = finger_chain('index', shape['index'])
    mid = vadd(pts[1], vmul(vsub(pts[2], pts[1]), 0.45))
    side = vadd(mid, (seg_radius('index', 1) + seg_radius('thumb', 2) + 0.3, 0.0, 0.0))
    shape['thumb'] = solve_thumb(side, pad_to=(-1.0, 0.0, 0.0), point=vsub(pts[2], pts[1]),
                                 pref=(-5.0, 20.0, 40.0, 15.0, 15.0), w_point=30.0)
    return shape


_bob_k = hs_bob_key()
# In the middle: back of the hand to the viewer, knuckles toward the other hand, thumb on top.
_bob_in = P((157, 226), _bob_k, 'wrist', yaw=190, pitch=0, roll=88, scale=1.1, depth=50, pole=(0.3, 1.0, 0.45))
# Up and out: the wrist has turned, palm forward, knuckles up.
_bob_out = P((128, 172), _bob_k, 'wrist', yaw=-10, pitch=0, roll=-12, scale=1.1, depth=55, via=(166, 176),
             pole=(0.3, 1.0, 0.45))
_bob_back = dict(_bob_in, via=(124, 222))
SIGNS['bobagem'] = {
    'poster': 0.65, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _bob_k, 'handshape_view': {'yaw': -40},
    'keys': [(0.0, [_bob_in, mirrored(_bob_in)]), (0.3, [_bob_in, mirrored(_bob_in)]),
             (0.65, [_bob_out, mirrored(_bob_out)]), (1.0, [_bob_back, mirrored(_bob_back)]),
             (1.35, [_bob_out, mirrored(_bob_out)]), (1.7, [_bob_back, mirrored(_bob_back)]),
             (2.4, [_bob_in, mirrored(_bob_in)])],
    # On the outer side of each loop: up and out, then down and back in toward the middle.
    'arrows': [{'d': circle_arrow(146, 200, 54, -115, 150, False)},
               {'d': circle_arrow(400 - 146, 200, 54, 295, 30, True)}],
    # The knuckles meet in the middle.
    'marks': [(200, 194, 0)],
    'mirror_second': True,
}
TITLES['bobagem'] = 'Sinal de bobagem em Libras'
