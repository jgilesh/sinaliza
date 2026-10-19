# EDUCADO: the support arm stretched down beside the body, hand closed (S); the dominant hand with the index
# and thumb stretched out (the others closed), index pointing across toward that arm, slides along it in
# one stroke from the shoulder down to the wrist, keeping contact; chin raised. (UFSC Signbank EDUCAR:
# G/S, 2a, continuous contact, contralateral, straight. The INES EDUCAR video is another sign, "educar".)

_edu_l, _edu_s = HANDSHAPES['L'](), hs_S()
# Support (left) arm, drawn as the right hand at the mirrored place: the arm goes down and a little forward,
# almost straight (the elbow opens outward), the fist hanging with its knuckles down and a little toward the viewer. The picture is only
# 300 px tall, so the arm reaches forward a little instead of hanging straight down out of the frame.
_edu_sup = mirrored(P((106, 250), _edu_s, 'wrist', yaw=-40, pitch=40, roll=172, scale=1.0, depth=205,
                      pole=(1.0, 0.3, -0.2)))


def _edu_pose(at, **kw):
    """Back of the hand to the viewer, turned a little so the thumb shows; index pointing across the body
    toward the support arm, its tip on the arm."""
    return P(at, _edu_l, 'index_tip', yaw=160, pitch=0, roll=96, scale=1.05, depth=95, pole=(0.3, 1.0, 0.5), **kw)


_edu_top = _edu_pose((266, 212))
_edu_elbow = _edu_pose((299, 230), ease='linear')
_edu_wrist = _edu_pose((293, 248), ease='out')
SIGNS['educado'] = {
    'poster': 0.3, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _edu_l,
    'keys': [(0.0, [_edu_top, _edu_sup]), (0.3, [_edu_top, _edu_sup]), (0.85, [_edu_elbow, _edu_sup]),
             (1.3, [_edu_wrist, _edu_sup]), (1.95, [_edu_wrist, _edu_sup]),
             (2.6, [dict(_edu_top, via=(250, 250)), _edu_sup])],
    # Down along the arm, on its outer side.
    'arrows': [{'d': 'M 302 194 Q 330 218 320 250'}],
    'marks': [(258, 200, -50)],
    'mirror_second': True,
}
TITLES['educado'] = 'Sinal de educado em Libras'
