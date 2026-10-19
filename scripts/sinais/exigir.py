# EXIGIR: the support hand lies open in front of the chest, palm up. The signing hand, in the "key"
# shape (fist with the thumb's pad on the side of the bent index), comes down firmly onto the support
# palm, twice. (UFSC Signbank EXIGIR, INES EXIGIR.)


def hs_exigir_key():
    """Key: the index bent (looser than the folded fingers), the thumb's pad on the side of its middle
    phalanx, the other three fingers folded into the palm."""
    shape = fist({'index': fing(0, 70, 85, 40)})
    pts, frames = finger_chain('index', shape['index'])
    mid = vadd(pts[1], vmul(vsub(pts[2], pts[1]), 0.45))
    side = vadd(mid, (seg_radius('index', 1) + seg_radius('thumb', 2) + 0.3, 0.0, 0.0))
    shape['thumb'] = solve_thumb(side, pad_to=(-1.0, 0.0, 0.0), point=vsub(pts[2], pts[1]),
                                 pref=(-5.0, 20.0, 40.0, 15.0, 15.0), w_point=30.0)
    return shape


def hs_exigir_flat():
    """Support hand: open, fingers together and a little curved, thumb a little apart."""
    return {'index': fing(2, 8, 12, 8), 'middle': fing(0, 8, 12, 8), 'ring': fing(-2, 8, 12, 8),
            'pinky': fing(-4, 10, 12, 8), 'thumb': (22.0, 18.0, 10.0, 8.0, 6.0)}


_exigir_key, _exigir_flat = hs_exigir_key(), hs_exigir_flat()
# Support hand (defined as a right hand, then mirrored): palm up, tipped a little toward the viewer,
# fingers pointing across toward the midline.
_exigir_base = mirrored(P((140, 242), _exigir_flat, 'wrist', yaw=-50, pitch=0, roll=92, scale=1.1, depth=70))


def _exigir_top(lift):
    # Knuckles forward and toward the other hand, thumb on top: the bent index with the thumb's pad on
    # its side faces the viewer, and the little-finger side of the fist lands on the support palm.
    return P((206, 220 - lift), _exigir_key, 'wrist', yaw=-132, pitch=63, roll=135, scale=1.1, depth=74,
             pole=(0.4, 1.0, 0.4))


_exigir_up, _exigir_down = _exigir_top(26), _exigir_top(0)
_exigir_keys = [(0.0, [_exigir_up, _exigir_base]), (0.3, [_exigir_up, _exigir_base]),
                (0.5, [dict(_exigir_down, ease='in'), _exigir_base]), (0.75, [_exigir_up, _exigir_base]),
                (0.95, [dict(_exigir_down, ease='in'), _exigir_base]), (1.25, [_exigir_up, _exigir_base]),
                (2.2, [_exigir_up, _exigir_base])]
SIGNS['exigir'] = {
    'poster': 0.3, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _exigir_key, 'handshape_view': {'yaw': -40},
    'keys': _exigir_keys,
    'marks': [(250, 226, 50)],
    'arrows': [{'d': 'M 172 178 L 172 206', 'both': True}],
    'mirror_second': True,
}
TITLES['exigir'] = 'Sinal de exigir em Libras'
