# PERMANECER: both flat hands (B) come up in front of the chest with the palms forward, then go down
# firmly, turning the palms down, and stop in front of the waist. Once. (UFSC Signbank PERMANECER: B,
# 2s, espaço neutro. The INES PERMANECER video shows another variant, with one hand.)
_perm_b = hs_B()
_perm_pole = (0.5, 1.0, 0.4)
# Up: palms forward, fingers up, in front of the chest and a little apart.
_perm_up = P((150, 214), _perm_b, 'wrist', yaw=0, pitch=0, roll=10, scale=1.05, depth=55, pole=_perm_pole)
# Down: palms down, fingers forward and a little in, the backs of the hands seen from above.
_perm_down = P((138, 270), _perm_b, 'wrist', yaw=-57, pitch=129, roll=-56, scale=1.05, depth=70, pole=_perm_pole,
               ease='in')
_perm_low = P((140, 264), _perm_b, 'wrist', yaw=-57, pitch=129, roll=-56, scale=1.0, depth=60, pole=_perm_pole)
SIGNS['permanecer'] = {
    'poster': 1.2, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _perm_b,
    'keys': [(0.0, [_perm_low, mirrored(_perm_low)]), (0.4, [_perm_up, mirrored(_perm_up)]),
             (0.6, [_perm_up, mirrored(_perm_up)]), (0.95, [_perm_down, mirrored(_perm_down)]),
             (2.1, [_perm_down, mirrored(_perm_down)]), (2.6, [_perm_low, mirrored(_perm_low)])],
    # Outside each hand: firmly down.
    'arrows': [{'d': 'M 110 196 L 110 262'}, {'d': 'M 290 196 L 290 262'}],
    'mirror_second': True,
}
TITLES['permanecer'] = 'Sinal de permanecer em Libras'
