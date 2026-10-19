# RESPIRAR: an open hand with the fingers spread and bent (claw), palm toward the body, rises from the
# chest to the nose and closes into a fist in front of it, as if drawing in air (eyes closed). Once.
# (UFSC Signbank RESPIRAR: 5_claw, nose; INES RESPIRAR agrees and makes it twice.)


def hs_respirar_claw():
    """5 in a claw: fingers spread and bent at the middle and end joints, thumb out and bent."""
    return {'index': fing(13, 12, 55, 40), 'middle': fing(3, 12, 58, 42), 'ring': fing(-7, 14, 58, 42),
            'pinky': fing(-17, 16, 56, 40), 'thumb': (12.0, 30.0, 30.0, 18.0, 35.0)}


_res_claw, _res_s = hs_respirar_claw(), hs_S()
# Back of the hand to the viewer (palm toward the body), turned a little so the bent fingers show from the
# side; at the chest the fingers point down, by the nose they point across the face.
_res_low = P((170, 240), _res_claw, 'wrist', yaw=160, pitch=0, roll=170, scale=1.05, depth=50, pole=(0.45, 1.0, 0.4))
_res_near = P((168, 156), _res_claw, 'wrist', yaw=160, pitch=0, roll=118, scale=1.05, depth=45, pole=(0.5, 1.0, 0.4))
# The fist in front of the nose, knuckles toward the other side, below the eyes; tipped toward the viewer
# so the folded fingers show.
_res_fist = P((168, 124), _res_s, 'wrist', yaw=180, pitch=35, roll=92, scale=1.0, depth=40, pole=(0.5, 1.0, 0.4))
SIGNS['respirar'] = {
    'poster': 0.75, 'dur': 2.6, 'hands': ['right'], 'handshape': _res_claw, 'handshape_view': {'yaw': -50, 'pitch': -20},
    'keys': [(0.0, [_res_low]), (0.3, [_res_low]), (0.75, [_res_near]), (1.05, [_res_fist]), (1.9, [_res_fist]),
             (2.6, [dict(_res_low, via=(140, 200))])],
    # Up from the chest to the nose, outside the hand.
    'arrows': [{'d': 'M 128 236 Q 116 180 138 136'}],
}
TITLES['respirar'] = 'Sinal de respirar em Libras'
