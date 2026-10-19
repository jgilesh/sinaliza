# EXPULSAR: both hands closed (S) in front of the chest, the signing fist resting on the thumb side of
# the support fist. The signing hand leaves quickly up to beside the face on its own side, opening the
# index up and the thumb out toward the middle (palm forward), while the support hand drops a little.
# Once. (UFSC Signbank EXPULSAR: S+1 / S, initial contact on the thumb side of the support hand. The INES
# EXPULSAR video shows a variant that starts at the chin.)

_expul_s = hs_S()
_expul_l = hs_L()
_expul_pole = (0.45, 1.0, 0.45)
# Support hand (a right-hand pose, mirrored): palm toward the body, thumb on top, fingers across.
_expul_sup = mirrored(P((176, 236), _expul_s, 'wrist', yaw=150, pitch=0, roll=72, scale=1.1, depth=60,
                        pole=(0.3, 1.0, 0.45)))
_expul_sup_low = dict(mirrored(P((170, 262), _expul_s, 'wrist', yaw=150, pitch=0, roll=78, scale=1.1, depth=60,
                                 pole=(0.3, 1.0, 0.45))), ease='out')
# Signing fist on top of the support fist's thumb side, palm toward the body.
_expul_on = P((178, 212), _expul_s, 'wrist', yaw=160, pitch=0, roll=70, scale=1.1, depth=72, pole=_expul_pole)
# Beside the face on the signing side: index up, thumb toward the middle, palm forward.
_expul_off = P((126, 166), _expul_l, 'wrist', yaw=8, pitch=0, roll=-8, scale=1.08, depth=50, pole=(0.6, 1.0, 0.4),
               via=(144, 200), ease='out')
_expul_back = dict(_expul_on, via=(132, 214), ease='smooth')
SIGNS['expulsar'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _expul_l,
    'keys': [(0.0, [_expul_on, _expul_sup]), (0.4, [_expul_on, _expul_sup]), (0.75, [_expul_off, _expul_sup_low]),
             (1.8, [_expul_off, _expul_sup_low]), (2.4, [_expul_back, dict(_expul_sup, ease='smooth')])],
    # Outside the signing hand: quickly up and out from the support hand.
    'arrows': [{'d': 'M 146 232 Q 106 214 100 170'}],
    # Where the two fists touch at the start.
    'marks': [(214, 206, 30)],
    'mirror_second': True,
}
TITLES['expulsar'] = 'Sinal de expulsar em Libras'
