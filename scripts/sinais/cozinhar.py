# COZINHAR: the support hand closed (S) in front of the belly, palm down, as if holding the pan handle.
# Above it the signing hand, the thumb pressing on the side of the bent index (as if holding a spoon),
# fingers pointing down, stirs in small circles, three times. No contact. (UFSC Signbank COZINHAR: Key
# over B/S, neutral space, circular; INES COZINHAR agrees.)


def hs_cozinhar_key():
    """Key grip: the fingers folded, the index a little less tightly (bent at the knuckle and middle
    joint); the thumb lies along the side of the index, its pad pressing on the index's middle phalanx."""
    shape = fist({'index': fing(-2, 62, 88, 40)})
    pts, frames = finger_chain('index', shape['index'])
    mid = vadd(pts[1], vmul(vsub(pts[2], pts[1]), 0.55))
    side = vadd(mid, (seg_radius('index', 1) + seg_radius('thumb', 2) * 0.9, 0.0, 0.0))
    shape['thumb'] = solve_thumb(side, pad_to=(-1.0, 0.0, 0.0), point=vsub(pts[2], pts[1]),
                                 pref=(-5.0, 20.0, 30.0, 10.0, 10.0))
    return shape


_coz_key, _coz_s = hs_cozinhar_key(), hs_S()
# Support fist, defined as a right hand and mirrored: in front of the belly, palm down, knuckles toward
# the midline, the back of the hand tipped a little toward the viewer.
_coz_base = mirrored(P((160, 274), _coz_s, 'wrist', yaw=125, pitch=0, roll=88, scale=1.08, depth=70))


def _coz_pose(angle, ease='linear'):
    """Signing hand on its circle (screen angle, clockwise), fingers pointing down, thumb side toward the
    viewer so the thumb on the bent index reads."""
    a = math.radians(angle)
    at = (_COZ_C[0] + _COZ_R[0] * math.cos(a), _COZ_C[1] + _COZ_R[1] * math.sin(a))
    return P(at, _coz_key, 'wrist', yaw=-70, pitch=0, roll=170, scale=1.22, depth=74 + 10 * math.sin(a),
             pole=(0.3, 1.0, 0.45), ease=ease)


_COZ_C, _COZ_R = (206, 194), (16, 6)
_coz_keys = [(0.0, [_coz_pose(-90), _coz_base]), (0.25, [_coz_pose(-90), _coz_base])]
_coz_n = 24                       # three circles, 8 steps each
for _coz_k in range(1, _coz_n + 1):
    _coz_keys.append((round(0.25 + 1.8 * _coz_k / _coz_n, 3), [_coz_pose(-90 + 45 * _coz_k), _coz_base]))
_coz_keys.append((2.5, [_coz_pose(-90), _coz_base]))
SIGNS['cozinhar'] = {
    'poster': 0.25, 'dur': 2.5, 'hands': ['right', 'left'], 'handshape': _coz_key, 'handshape_view': {'yaw': -60},
    'keys': _coz_keys,
    # Stirring: a flat circle around the wrist.
    'arrows': [{'d': 'M 240 182 A 36 11 0 1 1 172 188'}],
    'mirror_second': True,
}
TITLES['cozinhar'] = 'Sinal de cozinhar em Libras'
