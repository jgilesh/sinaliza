# CASA: both flat hands (B) lean toward each other until the fingertips touch, a roof in front of
# the body below the chin; the tips part a little and touch again. (INES CASA and UFSC Signbank
# agree.)
_casa_hs = hs_B()
_casa_roof = P((192, 163), _casa_hs, 'fingertips', yaw=125, pitch=0, roll=38, scale=1.05, depth=60, pole=(0.5, 1.0, 0.4))
_casa_open = dict(_casa_roof, at=(184, 172), roll=30)
SIGNS['casa'] = {
    'poster': 0.6, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _casa_hs,
    'keys': [(0.0, [_casa_open, mirrored(_casa_open)]), (0.3, [_casa_open, mirrored(_casa_open)]),
             (0.6, [_casa_roof, mirrored(_casa_roof)]), (0.85, [_casa_open, mirrored(_casa_open)]),
             (1.1, [_casa_roof, mirrored(_casa_roof)]), (1.9, [_casa_roof, mirrored(_casa_roof)]),
             (2.4, [_casa_open, mirrored(_casa_open)])],
    'mirror_second': True,
    'marks': [(200, 152, 0)],
    'arrows': [{'d': 'M 150 160 L 168 150', 'cap': True}, {'d': 'M 250 160 L 232 150', 'cap': True}],
}
TITLES['casa'] = 'Sinal de casa em Libras'
