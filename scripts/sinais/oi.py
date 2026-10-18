# OI: fingerspelled O-I. The hand makes O in front of the upper chest, below the chin, then moves out
# and up to beside the face while it changes to I (only the little finger up), palm to the side.
# (INES OI, UFSC Signbank OI.)


def hs_oi_I():
    """Letter I: little finger straight up, the other fingers folded, thumb across the index and middle."""
    shape = fist({'pinky': fing(-4, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['index', 'middle'], at=0.5)
    return shape


_oi_o, _oi_i = hs_O(), hs_oi_I()
# O with the palm toward the midline and seen a little from below, so its round opening shows.
_oi_on = P((172, 212), _oi_o, 'wrist', yaw=60, pitch=-20, roll=-8, scale=1.1, depth=50)
_oi_mid = P((152, 204), _oi_o, 'wrist', yaw=55, pitch=-15, roll=-10, scale=1.1, depth=55, ease='in')
# I: palm turned partly to the viewer, so the folded fingers and the raised little finger both read.
_oi_end = P((118, 192), _oi_i, 'wrist', yaw=45, pitch=0, roll=-6, scale=1.12, depth=60, via=(130, 212), ease='out')
SIGNS['oi'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right'], 'handshape': _oi_o, 'handshape_view': {'yaw': 60, 'pitch': -20},
    'keys': [(0.0, [_oi_on]), (0.55, [_oi_on]), (0.7, [_oi_mid]), (0.95, [_oi_end]), (1.9, [_oi_end]),
             (2.4, [dict(_oi_on, via=(146, 236))])],
    # From where O was made, out and up to where I is held.
    'arrows': [{'d': 'M 150 230 Q 108 232 94 186'}],
}
TITLES['oi'] = 'Sinal de oi em Libras'
