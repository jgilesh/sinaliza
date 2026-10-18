# DOENTE: the support hand (left) lies palm down in front of the chest; the open dominant hand,
# palm down too, comes down across it and rests on its back, once. (INES DOENTE1 and UFSC
# Signbank agree; in both videos the support hand is open, not a fist.)
doe_top, doe_base = hs_5(), hs_B()
# Support hand: bent down at the wrist, back of the hand forward, fingers hanging toward the middle
# (as in the INES video). The dominant hand lies across its back, fingers toward the other side,
# back of the hand forward: the two hands make a cross that reads at a glance.
doe_on = P((160, 214), doe_top, 'wrist', yaw=150, pitch=0, roll=96, scale=1.0, depth=72, pole=(0.4, 1.0, 0.35))
doe_up = dict(doe_on, at=(160, 190))
doe_sup = P((236, 196), doe_base, 'wrist', yaw=160, pitch=0, roll=152, scale=1.0, depth=66, pole=(0.4, 1.0, 0.35))
SIGNS['doente'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': doe_top,
    'keys': [(0.0, [doe_up, doe_sup]), (0.35, [doe_up, doe_sup]), (0.85, [doe_on, doe_sup]),
             (1.9, [doe_on, doe_sup]), (2.4, [doe_up, doe_sup])],
    'marks': [(214, 196, 20)],
    'arrows': [{'d': 'M 140 172 L 140 194'}],
    'mirror_second': True,
}
TITLES['doente'] = 'Sinal de doente em Libras'
