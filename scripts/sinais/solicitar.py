# SOLICITAR: the flat hand, fingers together and up, palm toward the face, touches the chin with the
# fingertips; it then moves away forward, to the side and a little down, the fingers curving a
# little. Once. (UFSC Signbank SOLICITAR: B, chin; INES SOLICITAR.)


def hs_solicitar_bent():
    """B with the fingers curving a little forward (toward the palm side)."""
    return {'index': fing(2, 12, 18, 10), 'middle': fing(0, 12, 18, 10), 'ring': fing(-2, 14, 18, 10),
            'pinky': fing(-4, 16, 18, 10), 'thumb': (28.0, 16.0, 8.0, 6.0, 4.0)}


_solicitar_b, _solicitar_bent = hs_B(), hs_solicitar_bent()
# Fingertips on the chin, back of the hand to the viewer, fingers up.
_solicitar_on = P((198, 150), _solicitar_b, 'fingertips', yaw=172, pitch=-10, roll=6, scale=1.0, depth=40,
                  pole=(0.4, 1.0, 0.45))
# Forward, out to the side and down: still the back of the hand to the viewer.
_solicitar_off = P((114, 190), _solicitar_bent, 'wrist', yaw=160, pitch=-15, roll=-6, scale=1.1, depth=70,
                   pole=(0.5, 1.0, 0.45), ease='out')
SIGNS['solicitar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right'], 'handshape': _solicitar_b,
    'keys': [(0.0, [_solicitar_on]), (0.4, [_solicitar_on]), (1.0, [_solicitar_off]), (1.9, [_solicitar_off]),
             (2.4, [dict(_solicitar_on, ease='smooth')])],
    'marks': [(214, 146, 60)],
    'arrows': [{'d': 'M 168 178 Q 152 160 140 158'}],
}
TITLES['solicitar'] = 'Sinal de solicitar em Libras'
