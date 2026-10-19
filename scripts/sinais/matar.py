# MATAR: both hands closed (S). The support fist stays in front of the chest, palm down. The signing
# fist rises to face height beside the head and strikes down hard on a diagonal, scraping past the thumb
# side of the support fist, and stops just below it, palm down too. Once. Serious face.
# (UFSC Signbank MATAR: S+S, on the support thumb. The INES MATAR1 video shows a one-handed variant: a
# fist beside the head stabbing down at the side of the body.)

_matar_s = hs_S()
_matar_pole = (0.45, 1.0, 0.45)
# Support (a right-hand pose, mirrored): palm down, the forearm pointing forward and a little up, so
# the folded fingers face the viewer and the thumb side faces the signing hand.
_matar_sup = mirrored(P((182, 222), _matar_s, 'wrist', yaw=0, pitch=68, roll=4, scale=1.1, depth=85,
                        pole=(0.3, 1.0, 0.45)))
# Signing fist raised beside the head, palm toward the midline and the viewer.
_matar_up = P((132, 150), _matar_s, 'wrist', yaw=35, pitch=0, roll=-6, scale=1.08, depth=50, pole=(0.6, 1.0, 0.4))
# ...down past the support thumb to just below the support fist, palm down like it.
_matar_down = P((206, 272), _matar_s, 'wrist', yaw=0, pitch=68, roll=4, scale=1.1, depth=88, pole=_matar_pole,
                via=(176, 214), ease='in')
_matar_back = dict(_matar_up, via=(126, 236), ease='smooth')
SIGNS['matar'] = {
    'poster': 0.2, 'dur': 2.3, 'hands': ['right', 'left'], 'handshape': _matar_s,
    'keys': [(0.0, [_matar_up, _matar_sup]), (0.35, [_matar_up, _matar_sup]), (0.7, [_matar_down, _matar_sup]),
             (1.7, [_matar_down, _matar_sup]), (2.3, [_matar_back, _matar_sup])],
    # Outside the path: down on a diagonal, past the support fist.
    'arrows': [{'d': 'M 112 168 Q 136 232 174 270'}],
    # Where the falling fist scrapes past the support thumb.
    'marks': [(192, 214, -70)],
    'mirror_second': True,
}
TITLES['matar'] = 'Sinal de matar em Libras'
