# APAGAR A LUZ: the open hand, fingers loose and apart, palm down beside the face, goes up to above the
# head on the dominant side and closes into a fist (S), like a light going out. Once. No contact.
# (UFSC Signbank APAGAR-LUZ "5_lax+S", INES APAGAR LUZ.)


def hs_apagar_a_luz_lax():
    """Open hand, fingers loose: spread and a little curved, thumb open."""
    return {'index': fing(12, 12, 20, 12), 'middle': fing(3, 12, 22, 14), 'ring': fing(-7, 14, 24, 15),
            'pinky': fing(-15, 16, 26, 16), 'thumb': (36.0, 18.0, 8.0, 8.0, 6.0)}


_apagar_a_luz_lax, _apagar_a_luz_s = hs_apagar_a_luz_lax(), hs_S()
# Beside the chin, palm down (the back of the hand to the viewer, seen a little from above), fingers loose
# and apart, pointing in.
_apagar_a_luz_low = P((112, 150), _apagar_a_luz_lax, 'wrist', yaw=160, pitch=-20, roll=70, scale=1.05, depth=50,
                      pole=(0.6, 1.0, 0.45))
# Above the head on the dominant side: a fist, palm forward, knuckles up.
_apagar_a_luz_high = P((112, 64), _apagar_a_luz_s, 'wrist', yaw=-10, pitch=0, roll=-6, scale=1.1, depth=50,
                       ease='out', pole=(0.6, 1.0, 0.45))
SIGNS['apagar-a-luz'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right'], 'handshape': _apagar_a_luz_lax, 'handshape_view': {'yaw': 0},
    'keys': [(0.0, [_apagar_a_luz_low]), (0.35, [_apagar_a_luz_low]), (1.0, [_apagar_a_luz_high]),
             (1.8, [_apagar_a_luz_high]), (2.4, [dict(_apagar_a_luz_low, via=(76, 112))])],
    # Up, between the hand's path and the face (the arm rises on the outer side).
    'arrows': [{'d': 'M 148 122 L 148 72'}],
}
TITLES['apagar-a-luz'] = 'Sinal de apagar a luz em Libras'
