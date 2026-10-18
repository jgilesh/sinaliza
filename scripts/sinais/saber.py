# SABER: the fingertips of the flat hand touch the side of the forehead; the hand moves away to
# the side and closes into A (fist, thumb up) on the way.
_sab_b, _sab_a = hs_B(), hs_A()
_sab_on = P((157, 70), _sab_b, 'fingertips', yaw=118, pitch=0, roll=24, scale=1.0, depth=40, pole=(0.7, 1.0, 0.45))
_sab_off = P((108, 118), _sab_a, 'wrist', yaw=-30, pitch=0, roll=-8, scale=1.08, depth=60, pole=(0.7, 1.0, 0.45),
             ease='out', via=(128, 90))
SIGNS['saber'] = {
    'poster': 0.2, 'dur': 2.2, 'hands': ['right'], 'handshape': _sab_b,
    'keys': [(0.0, [_sab_on]), (0.4, [_sab_on]), (0.85, [_sab_off]), (1.8, [_sab_off]), (2.2, [dict(_sab_on, ease='smooth')])],
    'marks': [(160, 64, 40)],
    'arrows': [{'d': 'M 140 50 Q 116 44 100 58', 'cap': True}],
}
TITLES['saber'] = 'Sinal de saber em Libras'
