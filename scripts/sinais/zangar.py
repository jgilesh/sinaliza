# ZANGAR: both hands in S (fists), crossed at the wrists in front of the chest, palms toward the
# body; then the fists burst apart up and out, once and with force, ending above the shoulders with
# the palms forward. (UFSC Signbank INDIGNAR/ZANGAR; the INES ZANGAR video shows another variant:
# one clawed hand rubbing the chest.)
_zangar_s = hs_S()
# Crossed: the right fist on the viewer's right of the midline (the forearms cross at the wrists),
# back of the hand to the viewer, each fist leaning outward so the two fists stay apart.
_zangar_cross = P((209, 210), _zangar_s, 'wrist', yaw=225, pitch=0, roll=40, scale=1.05, depth=60, pole=(0.3, 1.0, 0.5))
# Open: above the shoulder, beside the head, palm forward.
_zangar_up = P((110, 150), _zangar_s, 'wrist', yaw=10, pitch=0, roll=-12, scale=1.1, depth=45, ease='out')
_zangar_back = dict(_zangar_cross, ease='smooth')
_zangar_k = lambda p: [p, mirrored(p)]
SIGNS['zangar'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _zangar_s,
    'keys': [(0.0, _zangar_k(_zangar_cross)), (0.4, _zangar_k(_zangar_cross)), (0.7, _zangar_k(_zangar_up)),
             (1.8, _zangar_k(_zangar_up)), (2.4, _zangar_k(_zangar_back))],
    # Up and out, from the crossed fists toward each raised fist, clear of the moving arms.
    'arrows': [{'d': 'M 164 156 Q 144 124 124 102'}, {'d': 'M 236 156 Q 256 124 276 102'}],
    'mirror_second': True,
}
TITLES['zangar'] = 'Sinal de zangar em Libras'
