# DOIS: V hand raised beside the face, palm forward, fingers up; held still (INES DOIS2).
_dois_v = hs_V()
_dois_on = P((124, 146), _dois_v, 'wrist', yaw=0, pitch=0, roll=2, scale=1.1, depth=60)
SIGNS['dois'] = {
    'poster': 1.0, 'dur': 2.2, 'hands': ['right'], 'handshape': _dois_v,
    # The hand is shown and held: no arrows (the number is shown, not moved).
    'keys': [(0.0, [_dois_on]), (2.2, [_dois_on])],
}
TITLES['dois'] = 'Sinal de dois em Libras'
