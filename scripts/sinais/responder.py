# RESPONDER: the index and middle fingers straight and together (the thumb on the other folded
# fingers) touch the lips; then the hand moves forward and down toward the other side, the fingers
# ending pointed forward, palm down. Once. (UFSC Signbank RESPONDER. INES RESPONDER shows the hand
# moving out to the dominant side, upright.)


def hs_responder_h():
    """Index and middle straight and together, ring and little finger folded under the thumb."""
    shape = fist({'index': fing(-2, 0, 0, 0), 'middle': fing(2, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


_responder_h = hs_responder_h()
_responder_pole = (0.45, 1.0, 0.45)
# On the lips: fingers up, the back of the hand turned toward the viewer and to the side, so the two
# fingers show side by side with their nails.
_responder_on = P((198, 126), _responder_h, 'fingertips', yaw=180, pitch=0, roll=2, scale=1.0, depth=40,
                  pole=_responder_pole)
# Forward and down toward the other side: fingers pointing forward (toward the viewer) and a little down,
# palm down, the back of the hand seen from above.
_responder_off = P((222, 206), _responder_h, 'fingertips', yaw=0, pitch=125, roll=45, scale=1.15, depth=90,
                   ease='out', pole=_responder_pole)
SIGNS['responder'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right'], 'handshape': _responder_h,
    'keys': [(0.0, [_responder_on]), (0.4, [_responder_on]), (1.0, [_responder_off]), (1.9, [_responder_off]),
             (2.4, [dict(_responder_on, ease='smooth')])],
    'arrows': [{'d': 'M 228 128 Q 248 150 246 180'}],
    'marks': [(213, 134, 70)],
}
TITLES['responder'] = 'Sinal de responder em Libras'
