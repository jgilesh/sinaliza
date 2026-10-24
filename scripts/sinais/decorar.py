# DECORAR (memorise): open hand with the middle finger bent forward (5m) starts in the space in front of
# the body, palm up, and moves to the forehead on the signing side, where the tip of the middle finger
# touches; the palm ends toward the face. Once. (UFSC Signbank DECORAR: 5m, testa, proximal, contato
# final; INES DECORAR1 agrees.)


def hs_decorar_5m():
    """5 with the middle finger bent forward (toward the palm) at the knuckle and middle joint."""
    return {'index': fing(18, 0, 4, 2), 'middle': fing(0, 60, 45, 25), 'ring': fing(-12, 0, 4, 2),
            'pinky': fing(-22, 0, 5, 3), 'thumb': (20.0, 24.0, 12.0, 10.0, 8.0)}


_decorar_h = hs_decorar_5m()
_decorar_pole = (0.6, 1.0, 0.5)
# Start: in front of the body on the signing side, palm up, the fingers pointing forward and out.
_decorar_off = P((130, 206), _decorar_h, 'wrist', yaw=20, pitch=-55, roll=-40, scale=1.08, depth=80,
                 pole=_decorar_pole)
# On the forehead: palm toward the head and turned to the viewer, the bent middle fingertip on the
# forehead, the other fingers spread up beside it.
_decorar_on = P((168, 62), _decorar_h, 'middle_tip', yaw=40, pitch=-8, roll=-62, scale=0.98, depth=40,
                pole=_decorar_pole, via=(126, 130), ease='in')
SIGNS['decorar'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right'], 'handshape': _decorar_h, 'handshape_view': {'yaw': 30},
    'keys': [(0.0, [_decorar_off]), (0.35, [_decorar_off]), (1.0, [_decorar_on]), (1.8, [_decorar_on]),
             (2.4, [dict(_decorar_off, via=(120, 140))])],
    'marks': [(174, 54, 40)],
    'arrows': [{'d': 'M 102 196 Q 92 130 128 92'}],
}
TITLES['decorar'] = 'Sinal de decorar em Libras'
