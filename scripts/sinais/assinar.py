# ASSINAR: the support hand stands open (B), fingers up, palm toward the signing hand. The signing hand,
# in the "key" shape (the index bent, the thumb's pad on its side, the other fingers folded), as if
# holding a pen, rubs the back of the bent index on that palm and slides down and in toward the body.
# Once. (UFSC Signbank ASSINAR "Key" on "B", rubbing; the INES ASSINAR video is quicker and less clear.)


def hs_assinar_key():
    """Key: the index bent (looser than the folded fingers), the thumb's pad on the side of its middle
    phalanx, the other three fingers folded into the palm."""
    shape = fist({'index': fing(0, 70, 85, 40)})
    pts, frames = finger_chain('index', shape['index'])
    mid = vadd(pts[1], vmul(vsub(pts[2], pts[1]), 0.45))
    side = vadd(mid, (seg_radius('index', 1) + seg_radius('thumb', 2) + 0.3, 0.0, 0.0))
    shape['thumb'] = solve_thumb(side, pad_to=(-1.0, 0.0, 0.0), point=vsub(pts[2], pts[1]),
                                 pref=(-5.0, 20.0, 40.0, 15.0, 15.0), w_point=30.0)
    return shape


_assinar_key, _assinar_b = hs_assinar_key(), hs_B()
_assinar_pole = (0.4, 1.0, 0.4)
# Support hand (defined as a right hand, then mirrored): fingers up, palm turned toward the signing hand
# and a little toward the viewer.
_assinar_base = mirrored(P((150, 238), _assinar_b, 'wrist', yaw=80, pitch=0, roll=-4, scale=1.05, depth=60))


def _assinar_pose(at, roll, scale, **kw):
    # Knuckles toward the support palm, the thumb side up and turned toward the viewer: the thumb's pad
    # on the bent index shows, and the back of the index rubs the palm.
    return P(at, _assinar_key, 'wrist', yaw=-132, pitch=63, roll=roll, scale=scale, depth=kw.pop('depth', 62),
             pole=_assinar_pole, **kw)


_assinar_top = _assinar_pose((196, 192), 135, 1.05)
_assinar_low = _assinar_pose((202, 222), 150, 1.0, depth=56, ease='smooth')
_assinar_off = _assinar_pose((178, 196), 135, 1.05)
SIGNS['assinar'] = {
    'poster': 0.5, 'dur': 2.3, 'hands': ['right', 'left'], 'handshape': _assinar_key, 'handshape_view': {'yaw': -40},
    'keys': [(t, [p, _assinar_base]) for t, p in [(0.0, _assinar_off), (0.3, _assinar_off), (0.5, _assinar_top),
                                                 (1.2, _assinar_low), (1.8, _assinar_low), (2.3, _assinar_off)]],
    'marks': [(238, 176, 30)],
    'arrows': [{'d': 'M 160 186 Q 160 214 176 228'}],
    'mirror_second': True,
}
TITLES['assinar'] = 'Sinal de assinar em Libras'
