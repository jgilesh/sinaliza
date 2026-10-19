# ACOSTUMAR: the support arm hangs at the side of the body. The dominant hand, flat with the thumb
# apart, palm toward that arm, touches the top of the arm near the shoulder and moves down it in short
# taps to near the elbow. (UFSC Signbank HABITUAR: B+B, braço; INES ACOSTUMAR.)
_acostumar_b = hs_B()
# Support (left) arm, drawn as the right hand at the mirrored place: the upper arm hangs down, the
# hand hangs below the picture.
_acostumar_sup = mirrored(P((128, 345), _acostumar_b, 'wrist', yaw=170, pitch=0, roll=180, scale=1.0, depth=40,
                            pole=(0.15, 1.0, 0.0)))


def _acostumar_at(y, lift=0.0, ease='smooth'):
    # Back of the hand to the viewer, palm on the outer front of the upper arm, fingers pointing out and
    # up, the thumb up.
    x = 262 + 0.12 * (y - 193)
    return P((x + 22 + lift * 0.4, y - lift), _acostumar_b, 'fingertips', yaw=140, pitch=0, roll=50, scale=1.05,
             depth=70, ease=ease, pole=(0.4, 1.0, 0.4))


_acostumar_ys = (212, 236, 260)
_acostumar_keys = [(0.0, [_acostumar_at(_acostumar_ys[0], 12), _acostumar_sup]),
                   (0.3, [_acostumar_at(_acostumar_ys[0], 12), _acostumar_sup])]
_acostumar_t = 0.3
for _acostumar_y in _acostumar_ys:
    _acostumar_keys += [(_acostumar_t + 0.18, [_acostumar_at(_acostumar_y, 0, 'in'), _acostumar_sup]),
                        (_acostumar_t + 0.36, [_acostumar_at(_acostumar_y + 8, 8), _acostumar_sup])]
    _acostumar_t += 0.36
_acostumar_keys += [(_acostumar_t + 0.6, [_acostumar_at(_acostumar_ys[-1] + 8, 8), _acostumar_sup]),
                    (_acostumar_t + 1.1, [_acostumar_at(_acostumar_ys[0], 12), _acostumar_sup])]
SIGNS['acostumar'] = {
    'poster': 0.48, 'dur': _acostumar_t + 1.1, 'hands': ['right', 'left'], 'handshape': _acostumar_b,
    'handshape_view': {'yaw': 20},
    'keys': _acostumar_keys,
    'marks': [(300, 214, 70)],
    # Down the outer side of the upper arm, in taps.
    'arrows': [{'d': 'M 316 222 L 322 270'}],
    'mirror_second': True,
}
TITLES['acostumar'] = 'Sinal de acostumar em Libras'
