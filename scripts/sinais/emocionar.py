# EMOCIONAR: the support arm lies across in front of the waist, hand closed (S). The signing hand,
# closed, starts on the support forearm and slides up along the arm to the shoulder, opening with
# the fingers spread (5) at the end, like a shiver going up the skin. Once.
# (UFSC Signbank EMOCIONAR; INES EMOCIONAR.)
_emo_s, _emo_5 = hs_S(), hs_5()
# Support (left) arm: forearm across the waist, the fist on the signing side, knuckles forward.
_emo_sup_pose = mirrored(P((230, 274), _emo_s, 'wrist', yaw=200, pitch=0, roll=100, scale=1.05, depth=140,
                           pole=(1.0, 1.0, 0.9)))
_emo_wr = _emo_sup_pose['at']
_emo_el = solve_elbow(SHOULDER['left'], _emo_wr, _emo_sup_pose['depth'], SIDE['left'], _emo_sup_pose['pole'])
_emo_sh = SHOULDER['left']


def _emo_on(k, lift=15.0):
    """A point on the support arm: k from 0 (wrist) to 1 (elbow) to 2 (shoulder), lifted a little
    off the arm's centre line toward the top of the sleeve."""
    if k <= 1:
        a, b, u = _emo_wr, _emo_el, k
    else:
        a, b, u = _emo_el, _emo_sh, k - 1
    return (a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u - lift)


# Signing hand: a fist resting on the forearm, back of the hand to the viewer; at the shoulder, open,
# palm on the shoulder, fingers spread up and out.
_emo_pole = (1.0, 0.35, 0.3)   # the signing elbow out to the side: its forearm stays above the support arm
_emo_a = P(_emo_on(0.5), _emo_s, 'wrist', yaw=170, pitch=0, roll=80, scale=1.05, depth=110, pole=_emo_pole)
_emo_b = P(_emo_on(1.0), _emo_s, 'wrist', yaw=170, pitch=0, roll=40, scale=1.05, depth=110, pole=_emo_pole,
           ease='linear')
_emo_c = P(_emo_on(1.75, 6), _emo_5, 'wrist', yaw=175, pitch=0, roll=24, scale=1.05, depth=60, pole=_emo_pole)
SIGNS['emocionar'] = {
    'poster': 1.5, 'dur': 2.8, 'hands': ['right', 'left'], 'handshape': _emo_5,
    'keys': [(0.0, [_emo_a, _emo_sup_pose]), (0.3, [_emo_a, _emo_sup_pose]), (0.9, [_emo_b, _emo_sup_pose]),
             (1.5, [_emo_c, _emo_sup_pose]), (2.3, [_emo_c, _emo_sup_pose]), (2.8, [_emo_a, _emo_sup_pose])],
    'marks': [],
    # Beside the support arm: up along it to the shoulder.
    'arrows': [{'d': 'M 300 270 L 300 212'}],
    'mirror_second': True,
}
TITLES['emocionar'] = 'Sinal de emocionar em Libras'
