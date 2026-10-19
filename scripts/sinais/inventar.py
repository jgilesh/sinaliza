# INVENTAR: index up (1), its tip on the middle of the forehead; the hand leaves the forehead in a
# straight diagonal up and out to above the head on the signing side, the index tipping forward.
# Once. (UFSC Signbank INVENTAR, INES INVENTAR.)

_inv_one = hs_1()
# On the forehead: the fist comes from the side of the face (index slanting up and in), so the eyes
# stay clear; palm toward the other side, turned a little to the viewer so the index reads.
_inv_on = P((198, 58), _inv_one, 'index_tip', yaw=55, pitch=0, roll=48, scale=1.0, depth=40,
            pole=(0.7, 1.0, 0.45))
# Up and out, above the head: the index tips forward (toward the viewer), still slanting in.
_inv_off = P((134, 34), _inv_one, 'index_tip', yaw=40, pitch=55, roll=22, scale=1.05, depth=70,
             pole=(0.7, 1.0, 0.45), ease='out')
SIGNS['inventar'] = {
    'poster': 0.3, 'dur': 2.2, 'hands': ['right'], 'handshape': _inv_one,
    'keys': [(0.0, [_inv_on]), (0.4, [_inv_on]), (0.85, [_inv_off]), (1.8, [_inv_off]),
             (2.2, [dict(_inv_on, ease='smooth')])],
    'marks': [(204, 52, 20)],
    'arrows': [{'d': 'M 176 40 L 150 22'}],
}
TITLES['inventar'] = 'Sinal de inventar em Libras'
