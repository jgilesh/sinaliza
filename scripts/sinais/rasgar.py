# RASGAR: both hands in the "key" shape (thumb's pad on the side of the bent index, the other fingers
# folded), together in front of the chest, palms down, as if holding a sheet of paper. They pull apart to
# the sides: the signing hand turns at the wrist until the thumb is on top, and the other hand moves to its
# side still palm down. Once. No contact. (UFSC Signbank RASGAR; the INES RASGAR1 video shows another
# variant, one hand tearing at the chest.)


def hs_rasgar_key():
    """Key: the index bent (looser than the folded fingers), the thumb's pad on the side of its middle
    phalanx, the other three fingers folded into the palm."""
    shape = fist({'index': fing(0, 70, 85, 40)})
    pts, frames = finger_chain('index', shape['index'])
    mid = vadd(pts[1], vmul(vsub(pts[2], pts[1]), 0.45))
    side = vadd(mid, (seg_radius('index', 1) + seg_radius('thumb', 2) + 0.3, 0.0, 0.0))
    shape['thumb'] = solve_thumb(side, pad_to=(-1.0, 0.0, 0.0), point=vsub(pts[2], pts[1]),
                                 pref=(-5.0, 20.0, 40.0, 15.0, 15.0), w_point=30.0)
    return shape


_rasgar_key = hs_rasgar_key()
_rasgar_pole = (0.4, 1.0, 0.45)
# Together: palm down, knuckles forward and in, the thumb on top of the bent index (seen from the front
# and a little above).
_rasgar_in = P((163, 206), _rasgar_key, 'wrist', yaw=60, pitch=55, roll=95, scale=1.1, depth=60, pole=_rasgar_pole)
# Apart. Signing hand: turned so the thumb is on top and the thumb's pad on the index shows.
_rasgar_out_r = P((114, 214), _rasgar_key, 'wrist', yaw=-40, pitch=40, roll=-80, scale=1.1, depth=60, pole=_rasgar_pole,
                  ease='out')
# Other hand: same as at the start, only further out (palm still down).
_rasgar_out_l = dict(_rasgar_in, at=(112, 208), ease='out')
SIGNS['rasgar'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _rasgar_key, 'handshape_view': {'yaw': -40},
    'keys': [(0.0, [_rasgar_in, mirrored(_rasgar_in)]), (0.4, [_rasgar_in, mirrored(_rasgar_in)]),
             (0.95, [_rasgar_out_r, mirrored(_rasgar_out_l)]), (1.8, [_rasgar_out_r, mirrored(_rasgar_out_l)]),
             (2.4, [dict(_rasgar_in, ease='smooth'), mirrored(dict(_rasgar_in, ease='smooth'))])],
    # Apart, out to each side, above the hands.
    'arrows': [{'d': 'M 172 170 Q 146 162 120 168'}, {'d': 'M 228 170 Q 254 162 280 168'}],
    'mirror_second': True,
}
TITLES['rasgar'] = 'Sinal de rasgar em Libras'
