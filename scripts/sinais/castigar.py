# CASTIGAR: the support hand open, palm up, in front of the waist. The signing hand, fingers spread
# and hanging down like bent legs, comes down from above and lands its fingertips on the support
# palm, like someone kneeling; it lifts a little and lands again (2 touches).
# (UFSC Signbank CASTIGAR; INES CASTIGAR.)


def hs_castigar_flat():
    """Support B: flat hand, fingers together, the thumb lying along the side of the index (seen palm
    up from the front, an open thumb would point at the viewer and show only as its tip)."""
    return {'index': fing(2, 0, 0, 0), 'middle': fing(0, 0, 0, 0), 'ring': fing(-2, 0, 0, 0),
            'pinky': fing(-4, 0, 0, 0), 'thumb': (-8.0, 6.0, 10.0, 6.0, 4.0)}


def hs_castigar_legs():
    """5 with the fingers spread and a little bent at the knuckles and middle joints (legs)."""
    return {'index': fing(12, 14, 16, 8), 'middle': fing(3, 14, 16, 8), 'ring': fing(-7, 14, 16, 8),
            'pinky': fing(-16, 16, 16, 8), 'thumb': (16.0, 22.0, 14.0, 10.0, 10.0)}


_cas_legs, _cas_b = hs_castigar_legs(), hs_castigar_flat()
_cas_base = mirrored(P((146, 268), _cas_b, 'wrist', yaw=-50, pitch=15, roll=94, scale=1.1, depth=70))


def _cas_top(at, via=None, ease='smooth'):
    # Fingers hanging down, back of the hand to the viewer, turned a little so the fingers fan out.
    return P(at, _cas_legs, 'fingertips', yaw=160, pitch=0, roll=180, scale=1.1, depth=70, pole=(0.5, 1.0, 0.4),
             via=via, ease=ease)


_cas_high = _cas_top((220, 226))
_cas_on = _cas_top((226, 258), via=(214, 230), ease='in')
_cas_lift = _cas_top((224, 240), ease='smooth')
_cas_on2 = _cas_top((226, 258), ease='in')
SIGNS['castigar'] = {
    'poster': 0.85, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _cas_legs,
    'handshape_view': {'yaw': 0},
    'keys': [(0.0, [_cas_high, _cas_base]), (0.3, [_cas_high, _cas_base]), (0.85, [_cas_on, _cas_base]),
             (1.1, [_cas_lift, _cas_base]), (1.35, [_cas_on2, _cas_base]), (2.0, [_cas_on2, _cas_base]),
             (2.6, [dict(_cas_high, via=(190, 240)), _cas_base])],
    'marks': [(250, 250, 60)],
    'arrows': [{'d': 'M 268 190 L 268 226'}],
    'mirror_second': True,
}
TITLES['castigar'] = 'Sinal de castigar em Libras'
