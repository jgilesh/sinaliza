# GRITAR: hooked V (index and middle apart and bent like claws, the others folded) starts at the open
# mouth, the bent fingertips toward the lips; the hand rises in a diagonal, up and out above the head on
# the signing side, the eyes following it. Once. (UFSC Signbank GRITAR: V_curved, boca; INES GRITAR
# agrees.)


def hs_gritar_v():
    """Hooked V: index and middle spread and bent at the middle and end joints, ring and little finger
    folded under the thumb."""
    shape = fist({'index': fing(17, 10, 52, 36), 'middle': fing(-12, 10, 52, 36)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


_gritar_v = hs_gritar_v()
# At the mouth: the hand under the mouth corner, palm toward the face (back of the hand to the viewer),
# the two hooked fingers rising and curling in so their tips reach the lips.
_gritar_on = P((194, 128), _gritar_v, 'index_tip', yaw=150, pitch=-25, roll=-6, scale=1.0, depth=30,
               pole=(0.5, 1.0, 0.5))
# Up and out above the head on the signing side, palm toward the head and the viewer, fingers up.
_gritar_up = P((112, 96), _gritar_v, 'wrist', yaw=30, pitch=-10, roll=-14, scale=1.05, depth=60,
               pole=(0.7, 1.0, 0.45), via=(150, 112), ease='out')
SIGNS['gritar'] = {
    'poster': 1.2, 'dur': 2.2, 'hands': ['right'], 'handshape': _gritar_v, 'handshape_view': {'yaw': 30, 'pitch': -10},
    'keys': [(0.0, [_gritar_on]), (0.35, [_gritar_on]), (0.95, [_gritar_up]), (1.6, [_gritar_up]),
             (2.2, [dict(_gritar_on, via=(124, 150), ease='smooth')])],
    'arrows': [{'d': 'M 166 96 Q 154 56 124 40'}],
}
TITLES['gritar'] = 'Sinal de gritar em Libras'
