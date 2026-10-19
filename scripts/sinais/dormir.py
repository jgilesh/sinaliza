# DORMIR: the open hand in a claw (fingers spread and curved) comes to the side of the forehead, the
# fingertips touch the temple and the hand closes into a fist there, once (head tilted, eyes closed:
# not drawn). (UFSC Signbank DORMIR: 5_claw+S, testa.)


def hs_dormir_claw():
    """5 in a claw: fingers spread and bent at the middle and end joints, thumb out and bent."""
    return {'index': fing(16, 12, 48, 34), 'middle': fing(4, 12, 50, 36), 'ring': fing(-8, 14, 50, 36),
            'pinky': fing(-19, 16, 48, 34), 'thumb': (22.0, 30.0, 30.0, 16.0, 30.0)}


_dormir_claw, _dormir_fist = hs_dormir_claw(), hs_S()
# Beside the head, fingers up and curled in toward the temple; the palm toward the head and a little
# toward the viewer, so the spread, curved fingers read. The eye stays clear.
_dormir_pose = lambda at, shape, **kw: P(at, shape, 'wrist', yaw=kw.pop('yaw', 55), pitch=0, roll=kw.pop('roll', 20),
                                         scale=0.95, depth=35, pole=(0.65, 1.0, 0.45), **kw)
_dormir_away = _dormir_pose((126, 110), _dormir_claw, roll=12)   # coming in (and going back) beside the head
_dormir_on = _dormir_pose((136, 104), _dormir_claw)
_dormir_shut = _dormir_pose((136, 104), _dormir_fist, yaw=70, roll=15)
SIGNS['dormir'] = {
    'poster': 0.75, 'dur': 2.4, 'hands': ['right'], 'handshape': _dormir_claw, 'handshape_view': {'yaw': 30, 'pitch': -20},
    'keys': [(0.0, [_dormir_away]), (0.3, [_dormir_away]), (0.65, [_dormir_on]), (0.85, [_dormir_on]),
             (1.15, [_dormir_shut]), (1.9, [_dormir_shut]), (2.4, [_dormir_away])],
    'marks': [(176, 62, 60)],
}
TITLES['dormir'] = 'Sinal de dormir em Libras'
