# CHEIRAR: hand in 4 (four fingers straight and apart, thumb folded on the palm) lying across just under
# the nose, palm toward the face and fingers pointing to the other side; it slides under the nose toward
# the signing side, keeping contact, and moves off beside the face. Once. (UFSC Signbank CHEIRAR: 4, nose,
# continuous contact, contralateral + ipsilateral. The INES CHEIRAR video shows another variant.)


def hs_cheirar_4():
    """4: index, middle, ring and little fingers straight and spread; the thumb folded across the palm,
    its pad on the palm below the ring finger."""
    shape = {'index': fing(10, 0, 2, 1), 'middle': fing(2, 0, 2, 1), 'ring': fing(-7, 0, 2, 1),
             'pinky': fing(-16, 0, 3, 2)}
    target = (-3.0, -20.0, PALM_HALF_THICKNESS + seg_radius('thumb', 2) + 0.6)
    shape['thumb'] = solve_thumb(target, pad_to=(0.0, 0.0, -1.0), point=(-1.0, -0.6, 0.0),
                                 pref=(-15.0, 50.0, 60.0, 30.0, 30.0), w_point=120.0)
    return shape


_cheirar_4 = hs_cheirar_4()
_cheirar_pole = (0.6, 1.0, 0.45)
# Back of the hand to the viewer, fingers across to the other side, the index edge under the nose.
_cheirar_pose = lambda at, **kw: P(at, _cheirar_4, 'index_tip', yaw=170, pitch=-15, roll=100, scale=0.95, depth=40,
                                   pole=_cheirar_pole, **kw)
_cheirar_start = _cheirar_pose((228, 116))
_cheirar_end = _cheirar_pose((198, 116), ease='linear')
# Off beside the face on the signing side, the fingers still pointing across.
_cheirar_off = P((158, 124), _cheirar_4, 'index_tip', yaw=160, pitch=-15, roll=92, scale=1.0, depth=55,
                 pole=_cheirar_pole, ease='out')
SIGNS['cheirar'] = {
    'poster': 0.6, 'dur': 2.4, 'hands': ['right'], 'handshape': _cheirar_4, 'handshape_view': {'yaw': 10},
    'keys': [(0.0, [_cheirar_start]), (0.35, [_cheirar_start]), (0.9, [_cheirar_end]), (1.25, [_cheirar_off]),
             (1.9, [_cheirar_off]), (2.4, [dict(_cheirar_start, ease='smooth')])],
    'marks': [(226, 112, 50)],
    # Under the nose toward the signing side.
    'arrows': [{'d': 'M 238 162 L 174 162'}],
}
TITLES['cheirar'] = 'Sinal de cheirar em Libras'
