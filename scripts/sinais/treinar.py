# TREINAR: the support arm stays close to the body, hand closed (S). The signing hand, open with
# the fingers together (B), rubs down the other arm from the shoulder toward the elbow, repeatedly.
# (UFSC Signbank TREINAR; INES TREINAMENTO is close.)

_treinar_b, _treinar_s = hs_B(), hs_S()
# Support arm: the fist in front of the waist (defined as a right hand, then mirrored).
_treinar_base = mirrored(P((176, 276), _treinar_s, 'wrist', yaw=150, pitch=0, roll=80, scale=1.05, depth=55,
                           pole=(0.2, 1.0, 0.6)))
# Signing hand on the upper arm: back of the hand to the viewer, fingers across the arm.
_treinar_hand = lambda at, d=30, **kw: P(at, _treinar_b, 'fingertips', yaw=151, pitch=-2, roll=96, scale=1.08,
                                         depth=d, pole=(0.4, 1.0, 0.4), **kw)
_treinar_top, _treinar_low = _treinar_hand((296, 206)), _treinar_hand((304, 240), ease='linear')
_treinar_lift = _treinar_hand((290, 212), d=50)
_treinar_keys = [(0.0, [_treinar_lift, _treinar_base]), (0.3, [_treinar_top, _treinar_base])]
_treinar_t = 0.3
for _treinar_k in range(3):
    _treinar_keys.append((round(_treinar_t + 0.4, 2), [_treinar_low, _treinar_base]))
    if _treinar_k < 2:
        _treinar_keys.append((round(_treinar_t + 0.6, 2), [_treinar_lift, _treinar_base]))
        _treinar_keys.append((round(_treinar_t + 0.75, 2), [_treinar_top, _treinar_base]))
    _treinar_t += 0.75
_treinar_keys += [(round(_treinar_t + 0.15, 2), [_treinar_low, _treinar_base]),
                  (round(_treinar_t + 0.6, 2), [_treinar_lift, _treinar_base])]
SIGNS['treinar'] = {
    'poster': 0.5, 'dur': round(_treinar_t + 0.6, 2), 'hands': ['right', 'left'], 'handshape': _treinar_b,
    'keys': _treinar_keys,
    'marks': [(306, 198, 60)],
    'arrows': [{'d': 'M 326 206 L 332 246'}],
    'mirror_second': True,
}
TITLES['treinar'] = 'Sinal de treinar em Libras'
