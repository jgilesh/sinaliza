# FALAR: hand in P (index straight, middle finger bent forward at the knuckle with the thumb on it,
# ring and little fingers folded), palm down, fingers pointing across toward the signer's left, in
# front of the mouth; the hand makes small forward circles by the lips, 2 times. (UFSC Signbank
# FALAR: [Libras_P], chin/mouth, circular forward. The INES FALAR1 video moves the hand once forward,
# away from the mouth.)


def hs_falar_P():
    """P of Libras: index straight, middle finger straight but bent forward at the knuckle, ring and
    little fingers folded; the thumb's pad on the side of the middle finger."""
    shape = fist({'index': fing(4, 0, 0, 0), 'middle': fing(-2, 48, 8, 5)})
    shape['thumb'] = solve_thumb((8.0, -42.5, 10.0), pad_to=(-1.0, 0.0, 0.0), pref=(5.0, 30.0, 40.0, 15.0, 15.0))
    return shape


_falar_p = hs_falar_P()
_FALAR_C = (206.0, 130.0)   # index tip at the circle's centre, just past the middle of the mouth
_FALAR_R = 5.0


def _falar_pose(angle):
    """Angle 0 = nearest the lips (top), going forward (toward the viewer) and down, then back up."""
    a = math.radians(angle)
    at = (_FALAR_C[0], _FALAR_C[1] - _FALAR_R * math.cos(a))
    return P(at, _falar_p, 'index_tip', yaw=115, pitch=-20, roll=88, scale=1.0 + 0.05 * math.sin(a), depth=40 + 12 * math.sin(a),
             pole=(0.5, 1.0, 0.45), ease='linear')


_falar_keys = [(0.0, [_falar_pose(0)]), (0.3, [_falar_pose(0)])]
_falar_steps = 12                     # two circles, 6 steps each
for _falar_k in range(1, _falar_steps + 1):
    _falar_keys.append((0.3 + 1.2 * _falar_k / _falar_steps, [_falar_pose(60 * _falar_k)]))
_falar_keys.append((2.2, [dict(_falar_pose(0), ease='smooth')]))
SIGNS['falar'] = {
    'poster': 0.3, 'dur': 2.2, 'hands': ['right'], 'handshape': _falar_p,
    'handshape_view': {'yaw': -65, 'pitch': -20},
    'keys': _falar_keys,
    'arrows': [{'d': circle_arrow(136, 106, 8, 200, 130, True)}],
}
TITLES['falar'] = 'Sinal de falar em Libras'
