# AVANÇAR: both hands flat (B), upright in front of the chest, the support hand's palm facing the
# signing hand. The signing hand, palm forward, rubs the side of its index along the support palm and
# goes past it, up and forward on a diagonal toward the support hand's side, ending above the head;
# once. (UFSC Signbank AVANÇAR: B/B, contato inicial + esfregar, distal + para cima. INES AVANÇAR1
# shows another variant.)


def hs_avancar_B():
    """Flat hand: fingers together and straight, the thumb along the side of the hand."""
    return {'index': fing(2, 0, 0, 0), 'middle': fing(0, 0, 0, 0), 'ring': fing(-2, 0, 0, 0),
            'pinky': fing(-4, 0, 0, 0), 'thumb': (-4.0, 14.0, 16.0, 8.0, 6.0)}


_av_b = hs_avancar_B()
# Support hand (defined as a right hand, then mirrored): upright, the palm toward the signing hand and
# a little toward the viewer.
_av_base = mirrored(P((168, 258), _av_b, 'wrist', yaw=70, pitch=0, roll=-6, scale=1.05, depth=60))
_av_pose = lambda at, **kw: P(at, _av_b, 'wrist', yaw=kw.pop('yaw', 0), pitch=kw.pop('pitch', 0), roll=kw.pop('roll', 0),
                              scale=kw.pop('scale', 1.05), depth=kw.pop('depth', 62), pole=(0.4, 1.0, 0.45), **kw)
# Start: palm forward, the side of the index against the support palm.
_av_start = _av_pose((198, 256), yaw=-10)
_av_end = _av_pose((258, 96), roll=25, depth=95, scale=1.1, via=(250, 200), ease='out')
_av_back = dict(_av_start, via=(258, 196), ease='smooth')   # back down the same way, clear of the face
SIGNS['avancar'] = {
    'poster': 0.3, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _av_b,
    'keys': [(0.0, [_av_start, _av_base]), (0.4, [_av_start, _av_base]), (1.2, [_av_end, _av_base]),
             (1.9, [_av_end, _av_base]), (2.6, [_av_back, _av_base])],
    'arrows': [{'d': 'M 262 236 Q 284 196 290 140'}],
    'marks': [(219, 170, 0)],
    'mirror_second': True,
}
TITLES['avancar'] = 'Sinal de avançar em Libras'
