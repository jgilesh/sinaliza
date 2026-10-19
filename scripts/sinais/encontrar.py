# ENCONTRAR: both hands with the index up (others closed). The dominant hand waits, still, beside the
# face on its own side; the other hand comes up across the front of the body and stops against it,
# the two index fingers side by side, like two people meeting. Once. (UFSC Signbank ENCONTRAR: 1/1,
# final contact; the INES video makes the same meeting on the other side of the face.)

_encontrar_1 = hs_1()
_encontrar_wait = P((130, 92), _encontrar_1, 'index_tip', yaw=10, pitch=0, roll=-4, scale=1.05, depth=50,
                    pole=(0.6, 1.0, 0.45))
# Left hand, defined as a right hand on the mirrored side, then mirrored: palm toward the waiting hand.
_encontrar_low = mirrored(P((146, 218), _encontrar_1, 'index_tip', yaw=10, pitch=0, roll=20, scale=1.05, depth=55))
_encontrar_meet = mirrored(P((257, 99), _encontrar_1, 'index_tip', yaw=10, pitch=0, roll=4, scale=1.05, depth=75,
                             via=(214, 196), ease='out'))
SIGNS['encontrar'] = {
    'poster': 1.1, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _encontrar_1,
    'keys': [(0.0, [_encontrar_wait, _encontrar_low]), (0.3, [_encontrar_wait, _encontrar_low]),
             (1.0, [_encontrar_wait, _encontrar_meet]), (1.9, [_encontrar_wait, _encontrar_meet]),
             (2.4, [_encontrar_wait, dict(_encontrar_low, via=(214, 196))])],
    # Up and across the body to the waiting hand.
    'arrows': [{'d': 'M 268 214 Q 258 160 206 140'}],
    'marks': [(136, 82, -10)],
}
TITLES['encontrar'] = 'Sinal de encontrar em Libras'
