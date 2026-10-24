# REFLETIR: both hands open with the fingers spread (5) beside the temples, palms toward the head and
# fingers up; they move toward the head and away from it alternately (one comes in while the other goes
# out), two or three times. No contact. (UFSC Signbank REFLETIR: 5, both hands, temple. The INES
# REFLETIR1 video shows another variant.)


def hs_refletir_5():
    """Open hand, fingers spread, the thumb relaxed and apart (leaning up, so beside the temple it
    stays clear of the eye)."""
    return {'index': fing(14, 0, 4, 2), 'middle': fing(3, 0, 3, 2), 'ring': fing(-8, 0, 4, 2),
            'pinky': fing(-18, 0, 5, 3), 'thumb': (12.0, 26.0, 14.0, 10.0, 8.0)}


_refletir_5 = hs_refletir_5()
_refletir_pole = (0.8, 1.0, 0.45)
# Beside the temple, the palm turned toward the head and a little toward the viewer, so the spread
# fingers read; the fingertips lean in a little toward the head.
_refletir_pose = lambda x, **kw: P((x, 104), _refletir_5, 'wrist', yaw=65, pitch=0, roll=8, scale=1.0, depth=40,
                                   pole=_refletir_pole, **kw)
_refletir_in, _refletir_out = _refletir_pose(128), _refletir_pose(110)
_refletir_r = [(0.0, _refletir_out), (0.3, _refletir_out)]
_refletir_l = [(0.0, _refletir_in), (0.3, _refletir_in)]
for _refletir_k in range(3):
    _refletir_t = 0.3 + 0.5 * _refletir_k
    _refletir_r += [(_refletir_t + 0.25, _refletir_in), (_refletir_t + 0.5, _refletir_out)]
    _refletir_l += [(_refletir_t + 0.25, _refletir_out), (_refletir_t + 0.5, _refletir_in)]
_refletir_r.append((2.4, _refletir_out))
_refletir_l.append((2.4, _refletir_in))
SIGNS['refletir'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _refletir_5, 'handshape_view': {'yaw': 20},
    'keys': [(round(t, 2), [r, mirrored(l)]) for (t, r), (_, l) in zip(_refletir_r, _refletir_l)],
    # Toward the head and away, on both sides.
    'arrows': [{'d': 'M 68 52 L 94 52', 'both': True}, {'d': 'M 306 52 L 332 52', 'both': True}],
    'mirror_second': True,
}
TITLES['refletir'] = 'Sinal de refletir em Libras'
