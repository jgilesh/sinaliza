# BEM FEITO: the other hand lies open, palm up, in front of the chest; the dominant hand, closed (S),
# starts at chin height beside the face and comes down to strike the open palm with its little-finger
# side, twice. (INES BEM-FEITO1.)
_bf_s, _bf_b = hs_S(), hs_B()
# The fist seen from behind, a little turned so the thumb shows on top; knuckles toward the midline.
_bf_hit = P((166, 230), _bf_s, 'wrist', yaw=232, pitch=0, roll=80, scale=1.1, depth=55, ease='in', pole=(0.3, 1.0, 0.5))
_bf_up = P((126, 160), _bf_s, 'wrist', yaw=232, pitch=0, roll=60, scale=1.1, depth=45, ease='smooth', pole=(0.3, 1.0, 0.5))
# The open hand: palm up, tipped a little toward the viewer so the palm shows; fingers toward the midline.
_bf_palm = P((170, 246), _bf_b, 'fingertips', yaw=-50, pitch=0, roll=95, scale=1.1, depth=45)
SIGNS['bem-feito'] = {
    'poster': 0.75, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _bf_s,
    'keys': [(0.0, [_bf_up, _bf_palm]), (0.35, [_bf_up, _bf_palm]), (0.75, [_bf_hit, _bf_palm]),
             (0.95, [_bf_hit, _bf_palm]), (1.35, [_bf_up, _bf_palm]), (1.75, [_bf_hit, _bf_palm]),
             (2.15, [_bf_hit, _bf_palm]), (2.6, [_bf_up, _bf_palm])],
    # Down onto the palm (repeated), and the strike on the palm.
    'arrows': [{'d': 'M 108 176 Q 112 222 140 236'}],
    'marks': [(218, 226, 50)],
    'mirror_second': True,
}
TITLES['bem-feito'] = 'Sinal de bem feito em Libras'
