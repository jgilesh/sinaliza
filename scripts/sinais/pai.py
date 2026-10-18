# PAI: the open hand takes hold of the chin (as if holding a beard), thumb on one side and fingers
# on the other, palm toward the face; it slides down closing into a fist (S), which ends lying
# across under the chin, index side up against it. (UFSC Signbank PAI: Beak_open+S, chin; INES
# PAI2 the same. INES PAI1 is another sign.)


def hs_pai_open():
    """Open beak / wide C: fingers together, a little bent at the knuckles and middle joints, the
    thumb opposite them, wide apart (the hand about to take the chin)."""
    return {'index': fing(1, 30, 28, 14), 'middle': fing(0, 30, 30, 15), 'ring': fing(-1, 30, 30, 15),
            'pinky': fing(-3, 32, 30, 15), 'thumb': (24.0, 50.0, 45.0, 6.0, 8.0)}


_pai_open, _pai_s = hs_pai_open(), hs_S()
_pai_grab = P((201, 131), _pai_open, 'pinch', yaw=220, pitch=-10, roll=55, scale=1.0, depth=35, pole=(0.6, 1.0, 0.45))
_pai_fist = P((174, 157), _pai_s, 'wrist', yaw=180, pitch=40, roll=90, scale=0.92, depth=40, pole=(0.6, 1.0, 0.45))
SIGNS['pai'] = {
    'poster': 0.4, 'dur': 2.4, 'hands': ['right'], 'handshape': _pai_open,
    'handshape_view': {'yaw': 60},
    'keys': [(0.0, [_pai_grab]), (0.5, [_pai_grab]), (1.0, [_pai_fist]), (1.9, [_pai_fist]), (2.4, [_pai_grab])],
    'marks': [(172, 152, -40)],
    'arrows': [{'d': 'M 140 118 Q 132 146 150 160', 'cap': True}],
}
TITLES['pai'] = 'Sinal de pai em Libras'
