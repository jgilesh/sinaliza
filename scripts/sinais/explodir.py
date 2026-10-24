# EXPLODIR: both hands closed (S) start with the forearms crossed level in front of the chest, one over
# the other, palms toward the body. They rise together to the front of the chin and burst apart in a
# quick arc up and out, ending above the shoulders with the palms forward. Once. Puffed cheeks (not
# drawn). (UFSC Signbank EXPLODIR: S, 2s, arco para cima; INES EXPLODIR agrees.)
_exp_s = hs_S()
_exp_pole = (0.6, 1.0, 0.4)
# Crossed: the right forearm level across the chest toward the support side, back of the fist to the
# viewer (knuckles toward the support side); the left forearm the same, mirrored, a little lower.
_exp_r0 = P((222, 200), _exp_s, 'wrist', yaw=180, pitch=0, roll=90, scale=1.0, depth=55, pole=(1.0, 0.25, 0.3))
_exp_l0 = mirrored(P((228, 242), _exp_s, 'wrist', yaw=180, pitch=0, roll=90, scale=1.0, depth=48, pole=(1.0, 0.25, 0.3)))
# Together in front of the chin, fists up, backs to the viewer, side by side (not over the face).
_exp_r1 = P((180, 196), _exp_s, 'wrist', yaw=170, pitch=0, roll=8, scale=1.05, depth=60, pole=_exp_pole)
_exp_l1 = mirrored(_exp_r1)
# Burst: fists up beside the head, above the shoulders, palms forward.
_exp_r2 = P((106, 120), _exp_s, 'wrist', yaw=0, pitch=0, roll=-10, scale=1.1, depth=50, pole=_exp_pole,
            via=(130, 140), ease='out')
_exp_l2 = mirrored(_exp_r2)
SIGNS['explodir'] = {
    'poster': 1.3, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _exp_s, 'handshape_view': {'yaw': 0},
    'keys': [(0.0, [_exp_r0, _exp_l0]), (0.35, [_exp_r0, _exp_l0]), (0.7, [_exp_r1, _exp_l1]),
             (0.75, [_exp_r1, _exp_l1]), (1.0, [_exp_r2, _exp_l2]), (2.0, [_exp_r2, _exp_l2]),
             (2.6, [dict(_exp_r0, ease='smooth'), dict(_exp_l0, ease='smooth')])],
    # From the middle, up and out to each side.
    'arrows': [{'d': 'M 180 170 Q 146 146 134 108'}, {'d': 'M 220 170 Q 254 146 266 108'}],
    'mirror_second': True,
}
TITLES['explodir'] = 'Sinal de explodir em Libras'
