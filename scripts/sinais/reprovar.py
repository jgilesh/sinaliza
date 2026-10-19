# REPROVAR: the support hand is flat (B), upright in front of the chin, palm to the side, facing the
# dominant hand. The dominant fist with the thumb pointing down goes down along the support palm,
# from its top to below it, once. (UFSC Signbank REPROVAR; the INES REPROVAR video agrees but the
# hands leave the frame.)


def hs_reprovar_thumb():
    """Fist with the thumb straight out to the side of the folded index (pointing down in the sign)."""
    shape = fist()
    shape['thumb'] = (40.0, 10.0, 0.0, 0.0, 0.0)
    return shape


def hs_reprovar_b():
    """B with the thumb resting along the side of the index."""
    shape = hs_B()
    shape['thumb'] = (8.0, 12.0, 8.0, 6.0, 4.0)
    return shape


_reprovar_t, _reprovar_b = hs_reprovar_thumb(), hs_reprovar_b()
# Support hand (defined as a right hand, then mirrored): fingers up, palm toward the dominant hand
# and a little toward the viewer.
_reprovar_sup = mirrored(P((180, 232), _reprovar_b, 'wrist', yaw=55, pitch=0, roll=-2, scale=1.0, depth=60))


def _reprovar_fist(y, ease='smooth'):
    # Thumb down, the folded fingers toward the viewer, the wrist on the outer side.
    return P((170, y), _reprovar_t, 'thumb_tip', yaw=30, pitch=0, roll=95, scale=1.0, depth=66,
             pole=(0.35, 1.0, 0.4), ease=ease)


_reprovar_top, _reprovar_bottom = _reprovar_fist(198), _reprovar_fist(272, 'in')
SIGNS['reprovar'] = {
    'poster': 0.6, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _reprovar_t,
    'handshape_view': {'yaw': 20, 'roll': 60},
    'keys': [(0.0, [_reprovar_top, _reprovar_sup]), (0.6, [_reprovar_top, _reprovar_sup]),
             (1.1, [_reprovar_bottom, _reprovar_sup]), (1.9, [_reprovar_bottom, _reprovar_sup]),
             (2.4, [dict(_reprovar_top), _reprovar_sup])],
    # Down, beside the fist (outside it).
    'arrows': [{'d': 'M 126 176 L 126 244'}],
    'mirror_second': True,
}
TITLES['reprovar'] = 'Sinal de reprovar em Libras'
