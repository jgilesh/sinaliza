# OBRIGAR: the support hand open, palm up, in front of the waist. The signing hand in the "key"
# shape (fist with the thumb pad pressed on the side of the bent index) comes down from above and
# presses on the support palm, thumb side down, firmly, and stays there a moment. Once.
# (UFSC Signbank OBRIGAR; INES OBRIGAR.)


def hs_obrigar_key():
    """Key: the index bent (looser than the folded fingers), the thumb's pad on the side of its middle
    phalanx, the other three fingers folded into the palm."""
    shape = fist({'index': fing(0, 70, 85, 40)})
    pts, frames = finger_chain('index', shape['index'])
    mid = vadd(pts[1], vmul(vsub(pts[2], pts[1]), 0.45))
    side = vadd(mid, (seg_radius('index', 1) + seg_radius('thumb', 2) + 0.3, 0.0, 0.0))
    shape['thumb'] = solve_thumb(side, pad_to=(-1.0, 0.0, 0.0), point=vsub(pts[2], pts[1]),
                                 pref=(-5.0, 20.0, 40.0, 15.0, 15.0), w_point=30.0)
    return shape


def hs_obrigar_flat():
    """Support B: flat hand, fingers together, the thumb lying along the side of the index (seen palm
    up from the front, an open thumb would point at the viewer and show only as its tip)."""
    return {'index': fing(2, 0, 0, 0), 'middle': fing(0, 0, 0, 0), 'ring': fing(-2, 0, 0, 0),
            'pinky': fing(-4, 0, 0, 0), 'thumb': (-8.0, 6.0, 10.0, 6.0, 4.0)}


_obr_key, _obr_b = hs_obrigar_key(), hs_obrigar_flat()
# Support hand (defined as a right hand, then mirrored): palm up, tilted a little toward the viewer,
# fingers pointing across toward the midline.
_obr_base = mirrored(P((146, 268), _obr_b, 'wrist', yaw=-50, pitch=15, roll=94, scale=1.1, depth=70))
# Signing hand: thumb side down, the bent index and thumb toward the support palm.
_obr_up = P((150, 178), _obr_key, 'wrist', yaw=-60, pitch=0, roll=60, scale=1.1, depth=55, pole=(0.9, 0.6, 0.4))
_obr_on = P((216, 238), _obr_key, 'wrist', yaw=-60, pitch=0, roll=82, scale=1.1, depth=72, pole=(0.9, 0.6, 0.4),
            via=(190, 184))
_obr_press = dict(_obr_on, at=(216, 241), via=None, ease='out')
SIGNS['obrigar'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _obr_key, 'handshape_view': {'yaw': -75, 'roll': 10},
    'keys': [(0.0, [_obr_up, _obr_base]), (0.3, [_obr_up, _obr_base]), (0.75, [_obr_on, _obr_base]),
             (0.9, [_obr_press, _obr_base]), (1.8, [_obr_press, _obr_base]), (2.4, [dict(_obr_up, via=(150, 220)), _obr_base])],
    'marks': [(252, 248, 70)],
    'arrows': [{'d': 'M 184 156 Q 230 160 240 208'}],
    'mirror_second': True,
}
TITLES['obrigar'] = 'Sinal de obrigar em Libras'
