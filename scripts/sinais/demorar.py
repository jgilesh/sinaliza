# DEMORAR: open hand with the fingers spread (5), the thumb tip on the chin, palm turned toward the
# other side; the fingers close slowly one after the other (little finger first, index last) until
# the hand is an A (fist, thumb straight up), the thumb still on the chin. Once. (UFSC Signbank
# DEMORAR: 5+A, chin; INES DEMORAR.)

_demorar_5 = hs_5()
_demorar_fist = fist()


def hs_demorar_A():
    """A: fist, the thumb straight up along the side of the index."""
    shape = fist()
    shape['thumb'] = solve_thumb((17.0, -44.0, -1.5), pad_to=(-1.0, 0.0, 0.0), point=(0.0, -1.0, 0.0),
                                 pref=(-5.0, 10.0, 20.0, 0.0, 0.0))
    return shape


_demorar_a = hs_demorar_A()


def _demorar_closed(names, thumb=None):
    """The 5 with the given fingers folded into the palm."""
    shape = dict(_demorar_5)
    for n in names:
        shape[n] = _demorar_fist[n]
    if thumb:
        shape['thumb'] = thumb
    return shape


_demorar_steps = [_demorar_5, _demorar_closed(['pinky']), _demorar_closed(['pinky', 'ring']),
                  _demorar_closed(['pinky', 'ring', 'middle']), _demorar_a]


def _demorar_pose(shape, yaw=55):
    # Palm toward the midline and the viewer, fingers leaning out, away from the face; the A turns a
    # little more toward the viewer (smaller yaw), so the thumb on the chin shows beside the fist.
    return P((190, 142), shape, 'thumb_tip', yaw=yaw, pitch=0, roll=-28, scale=1.0, depth=40, pole=(0.55, 1.0, 0.45))


_demorar_keys = [(0.0, [_demorar_pose(_demorar_5)]), (0.4, [_demorar_pose(_demorar_5)])]
for _demorar_i, _demorar_s in enumerate(_demorar_steps[1:], 1):
    _demorar_keys.append((round(0.4 + 0.35 * _demorar_i, 2), [_demorar_pose(_demorar_s, -15 if _demorar_s is _demorar_a else 55)]))
_demorar_keys += [(2.5, [_demorar_pose(_demorar_a, -15)]), (3.0, [_demorar_pose(_demorar_5)])]
SIGNS['demorar'] = {
    'poster': 0.0, 'dur': 3.0, 'hands': ['right'], 'handshape': _demorar_5,
    'keys': _demorar_keys,
    'marks': [(212, 140, 100)],
    # The fingers fold down one by one toward the palm.
    'arrows': [{'d': 'M 112 70 Q 98 96 116 116'}],
}
TITLES['demorar'] = 'Sinal de demorar em Libras'
