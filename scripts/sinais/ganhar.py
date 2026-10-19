# GANHAR: the hand closed in a fist (S), palm forward, rises from in front of the chest to above the head
# on the signing side, like a victory gesture, and stays up there a moment. Once. No contact.
# (UFSC Signbank GANHAR; the INES GANHAR video shows another variant, an L hand that closes beside the
# head.)
_ganhar_s = hs_S()
# Low: in front of the chest, palm forward, turned a little so the thumb across the fingers shows.
_ganhar_low = P((164, 206), _ganhar_s, 'wrist', yaw=-20, roll=-4, scale=1.05, depth=55, pole=(0.3, 1.0, 0.6))
# High: beside the top of the head, the fist above it, clear of the face.
_ganhar_high = P((128, 76), _ganhar_s, 'wrist', yaw=-15, roll=-8, scale=1.1, depth=45, ease='out', pole=(0.3, 1.0, 0.6))
_ganhar_hold = dict(_ganhar_high, at=(128, 74), ease='smooth')
SIGNS['ganhar'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right'], 'handshape': _ganhar_s, 'handshape_view': {'yaw': -20},
    'keys': [(0.0, [_ganhar_low]), (0.3, [_ganhar_low]), (0.8, [_ganhar_high]), (1.8, [_ganhar_hold]),
             (2.4, [dict(_ganhar_low, ease='smooth')])],
    # Straight up, on the outer side of the arm.
    'arrows': [{'d': 'M 92 196 Q 86 130 96 76'}],
}
TITLES['ganhar'] = 'Sinal de ganhar em Libras'
