# COMPREENDER: the open hand, fingers spread, touches the temple on the signing side with the
# fingertips; it then moves away to the side, forward and down, the index closing onto the thumb in
# a ring while the other fingers stay open. Once. (UFSC Signbank COMPREENDER: 5 + T[ASL_F], temple,
# initial contact; INES COMPREENDER.)


def hs_compreender_ring():
    """Ring: index curled onto the thumb, pad on pad; the other three straight and spread."""
    shape = {'index': fing(4, 50, 72, 50), 'middle': fing(3, 0, 4, 3), 'ring': fing(-7, 2, 4, 3),
             'pinky': fing(-16, 4, 5, 3)}
    shape['thumb'] = pinch_thumb(shape)
    return shape


_compreender_5, _compreender_ring = hs_5(), hs_compreender_ring()
# Fingertips on the temple, palm toward the face and down.
_compreender_on = P((162, 78), _compreender_5, 'fingertips', yaw=150, pitch=-10, roll=70, scale=1.0, depth=40,
                    pole=(0.75, 1.0, 0.45), ring=None)
# Out to the side, forward and down, the fingers pointing out: the palm turned partly to the viewer
# so the ring on top and the three open fingers read.
_compreender_off = P((104, 150), _compreender_ring, 'wrist', yaw=40, pitch=0, roll=-70, scale=1.1, depth=70,
                     pole=(0.6, 1.0, 0.45), ease='out', ring=None)
_compreender_ringed = dict(_compreender_off, ring=True)   # the opening is shaded once the ring has closed
SIGNS['compreender'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right'], 'handshape': _compreender_ring, 'handshape_ring': True,
    'handshape_view': {'yaw': 50, 'roll': -10},
    'keys': [(0.0, [_compreender_on]), (0.4, [_compreender_on]), (1.0, [_compreender_off]), (1.05, [_compreender_ringed]), (1.9, [_compreender_ringed]), (1.95, [_compreender_off]),
             (2.4, [dict(_compreender_on, ease='smooth')])],
    'marks': [(168, 70, -50)],
    'arrows': [{'d': 'M 124 50 Q 84 46 72 84'}],
}
TITLES['compreender'] = 'Sinal de compreender em Libras'
