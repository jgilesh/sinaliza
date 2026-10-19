# EMPATAR: both hands with the fingers together and bent 90 degrees at the knuckles (B bent), palms
# down, fingers pointing at each other; the hands come together and the fingertips touch in front of the
# chin, then they move apart to the sides and stop at the same height. Once. (UFSC Signbank EMPATAR:
# B_bent, 2s, contato final; INES EMPATAR agrees, lower, in front of the chest.)


def hs_empatar_bent():
    """B bent at the base: the four fingers straight and together, folded 90 degrees at the
    knuckles; the thumb alongside the index."""
    return {'index': fing(2, 82, 6, 4), 'middle': fing(0, 84, 6, 4), 'ring': fing(-2, 84, 6, 4),
            'pinky': fing(-4, 82, 8, 5), 'thumb': (-10.0, 20.0, 20.0, 8.0, 6.0)}


_emp_h = hs_empatar_bent()


def _emp_pose(x, y, **kw):
    """Right hand: palm down, back of the hand half to the viewer, fingertips toward the other hand."""
    return P((x, y), _emp_h, 'fingertips', yaw=110, pitch=-30, roll=0, scale=1.05, depth=60, pole=(0.45, 1.0, 0.4), **kw)


_emp_in_r, _emp_in_l = _emp_pose(170, 178), _emp_pose(172, 166)   # coming in, the hands not yet level
_emp_meet = _emp_pose(197, 160)
_emp_out = _emp_pose(146, 160, ease='out')
_emp_k = lambda r, l: [r, mirrored(l)]
SIGNS['empatar'] = {
    'poster': 1.4, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _emp_h, 'handshape_view': {'yaw': 75, 'pitch': -10},
    'keys': [(0.0, _emp_k(_emp_in_r, _emp_in_l)), (0.2, _emp_k(_emp_in_r, _emp_in_l)), (0.55, _emp_k(_emp_meet, _emp_meet)),
             (0.8, _emp_k(_emp_meet, _emp_meet)), (1.25, _emp_k(_emp_out, _emp_out)), (2.0, _emp_k(_emp_out, _emp_out)),
             (2.4, _emp_k(_emp_in_r, _emp_in_l))],
    # Apart to the sides, level: an arrow outside each hand, pointing out (clear of the face).
    'arrows': [{'d': 'M 124 150 Q 110 148 96 150'}, {'d': 'M 276 150 Q 290 148 304 150'}],
    'marks': [(200, 147, 0)],   # the fingertips touch in the middle
    'mirror_second': True,
}
TITLES['empatar'] = 'Sinal de empatar em Libras'
