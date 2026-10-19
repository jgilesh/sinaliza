# PAGAR: the support hand lies open in front of the chest, palm up. The signing hand, in the "key"
# shape (fist with the thumb's pad on the side of the bent index, as if holding a banknote), comes
# down onto the support palm, touches it and slides a little forward, once. (UFSC Signbank PAGAR,
# INES PAGAR1 shows another variant.)


def hs_pagar_key():
    """Key: the index bent (looser than the folded fingers), the thumb's pad on the side of its middle
    phalanx, the other three fingers folded into the palm."""
    shape = fist({'index': fing(0, 70, 85, 40)})
    pts, frames = finger_chain('index', shape['index'])
    mid = vadd(pts[1], vmul(vsub(pts[2], pts[1]), 0.45))
    side = vadd(mid, (seg_radius('index', 1) + seg_radius('thumb', 2) + 0.3, 0.0, 0.0))
    shape['thumb'] = solve_thumb(side, pad_to=(-1.0, 0.0, 0.0), point=vsub(pts[2], pts[1]),
                                 pref=(-5.0, 20.0, 40.0, 15.0, 15.0), w_point=30.0)
    return shape


def hs_pagar_flat():
    """Support hand: open, fingers together and a little curved, thumb a little apart."""
    return {'index': fing(2, 8, 12, 8), 'middle': fing(0, 8, 12, 8), 'ring': fing(-2, 8, 12, 8),
            'pinky': fing(-4, 10, 12, 8), 'thumb': (22.0, 18.0, 10.0, 8.0, 6.0)}


_pagar_key, _pagar_flat = hs_pagar_key(), hs_pagar_flat()
# Support hand (defined as a right hand, then mirrored): palm up, tipped a little toward the viewer,
# fingers pointing across toward the midline.
_pagar_base = mirrored(P((140, 242), _pagar_flat, 'wrist', yaw=-50, pitch=0, roll=92, scale=1.1, depth=70))
# Knuckles forward and toward the other hand, thumb on top: the bent index with the thumb's pad on its
# side faces the viewer.
_pagar_pose = lambda at, scale, depth, **kw: P(at, _pagar_key, 'wrist', yaw=-132, pitch=63, roll=135, scale=scale,
                                              depth=depth, pole=(0.4, 1.0, 0.4), **kw)
_pagar_up = _pagar_pose((190, 180), 1.08, 60)
_pagar_on = _pagar_pose((206, 220), 1.1, 74, ease='in')
# Slid forward along the palm (toward the viewer): a little lower on the tipped palm and nearer.
_pagar_fwd = _pagar_pose((209, 225), 1.12, 90)
SIGNS['pagar'] = {
    'poster': 0.6, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _pagar_key, 'handshape_view': {'yaw': -40},
    'keys': [(0.0, [_pagar_up, _pagar_base]), (0.3, [_pagar_up, _pagar_base]), (0.75, [_pagar_on, _pagar_base]),
             (0.85, [_pagar_on, _pagar_base]), (1.2, [_pagar_fwd, _pagar_base]), (1.9, [_pagar_fwd, _pagar_base]),
             (2.4, [_pagar_up, _pagar_base])],
    'marks': [(250, 226, 50)],
    # Down onto the palm, then forward along it.
    'arrows': [{'d': 'M 168 172 Q 166 214 184 238'}],
    'mirror_second': True,
}
TITLES['pagar'] = 'Sinal de pagar em Libras'
