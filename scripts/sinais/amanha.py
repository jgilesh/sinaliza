# AMANHÃ: open hand, fingers spread, the middle finger bent forward; its tip touches the temple and
# the hand moves out to the side and a little down, away from the head, once. (INES AMANHÃ, signed
# there with the left hand; drawn for a right-handed signer like every sign here.)
def hs_amanha_5m():
    """5 with the middle finger bent forward (toward the palm) at the knuckle and middle joint."""
    return {'index': fing(18, 0, 4, 2), 'middle': fing(0, 60, 45, 25), 'ring': fing(-12, 0, 4, 2),
            'pinky': fing(-22, 0, 5, 3), 'thumb': (20.0, 24.0, 12.0, 10.0, 8.0)}


amanha_hand = hs_amanha_5m()
# Palm toward the head, turned toward the viewer, so the spread fingers and the bent middle finger
# (pointing at the temple) read beside the face.
amanha_on = P((160, 75), amanha_hand, 'middle_tip', yaw=40, pitch=-8, roll=-20, scale=0.98, depth=40, pole=(0.6, 1.0, 0.5))
amanha_off = P((128, 100), amanha_hand, 'middle_tip', yaw=34, pitch=-8, roll=-28, scale=1.0, depth=55, pole=(0.6, 1.0, 0.5),
               ease='out')
SIGNS['amanha'] = {
    'poster': 0.0, 'dur': 2.2, 'hands': ['right'], 'handshape': amanha_hand, 'handshape_view': {'yaw': 30},
    'keys': [(0.0, [amanha_on]), (0.45, [amanha_on]), (0.95, [amanha_off]), (1.7, [amanha_off]),
             (2.2, [dict(amanha_on, ease='smooth')])],
    'marks': [(164, 70, 55)],
    'arrows': [{'d': 'M 140 34 Q 112 32 96 58'}],
}
TITLES['amanha'] = 'Sinal de amanhã em Libras'
