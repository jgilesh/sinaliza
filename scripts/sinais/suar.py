# SUAR: index finger out (1), lying across the forehead, back of the hand to the viewer and the index
# pointing to the other side; it wipes across the forehead from the middle toward its own side and comes
# off to the side, once, as if wiping off sweat. (UFSC Signbank SUAR: 1, testa; INES SUAR differs.)
_suar_1 = hs_1()
# Back of the hand to the viewer, index horizontal on the forehead pointing to the other side, the
# folded fingers below it, tipped back a little (pitch) so the fist sits low against the brow.
_suar = lambda at, **kw: P(at, _suar_1, 'index_tip', yaw=180, pitch=-15, roll=88, scale=0.95, depth=40,
                           pole=(0.6, 1.0, 0.5), **kw)
_suar_mid = _suar((214, 61))
_suar_side = _suar((186, 63), ease='linear')
_suar_off = P((150, 92), _suar_1, 'index_tip', yaw=175, pitch=-10, roll=70, scale=1.02, depth=55, pole=(0.6, 1.0, 0.5),
              ease='out')
_suar_low = P((168, 176), _suar_1, 'index_tip', yaw=175, pitch=-10, roll=60, scale=1.05, depth=55, pole=(0.5, 1.0, 0.45))
SIGNS['suar'] = {
    'poster': 0.7, 'dur': 2.4, 'hands': ['right'], 'handshape': _suar_1,
    'keys': [(0.0, [_suar_low]), (0.2, [_suar_low]), (0.6, [_suar_mid]), (0.8, [_suar_mid]), (1.2, [_suar_side]),
             (1.45, [_suar_off]), (1.9, [_suar_off]), (2.4, [dict(_suar_low, via=(150, 140))])],
    'marks': [(224, 50, -60)],
    'arrows': [{'d': 'M 212 40 Q 180 32 150 50'}],
}
TITLES['suar'] = 'Sinal de suar em Libras'
