# BRINCAR: both hands in Y (thumb and little finger out), in front of the chest, one higher than the
# other; the backs of the hands toward the viewer, thumbs up, little fingers pointing toward the
# midline. The hands make small alternating circles (forward and back), repeated.
# (UFSC Signbank BRINCAR: Y/Y, circular, alternating, repeated; INES BRINCAR agrees.)
import math as _brincar_math

_brincar_y = hs_Y()
_BRINCAR_R, _BRINCAR_L = (140, 192), (140, 236)   # wrists; the left hand is defined as a right hand, then mirrored


def _brincar_pose(at, phase, mirror=False):
    """One hand on its circle: up/down on screen, nearer/further (scale and depth) for forward/back."""
    a = _brincar_math.radians(phase)
    p = P((at[0], at[1] - 9 * _brincar_math.sin(a)), _brincar_y, 'wrist', yaw=180, pitch=0, roll=90,
          scale=1.08 + 0.07 * _brincar_math.cos(a), depth=60 + 25 * _brincar_math.cos(a), pole=(0.4, 1.0, 0.4),
          ease='linear')
    return mirrored(p) if mirror else p


_brincar_keys = []
for _brincar_k in range(25):           # three circles, 8 steps each; the left hand half a turn behind
    _brincar_ph = 45 * _brincar_k
    _brincar_keys.append((round(0.075 * _brincar_k, 3), [_brincar_pose(_BRINCAR_R, _brincar_ph),
                                                         _brincar_pose(_BRINCAR_L, _brincar_ph + 180, True)]))
_brincar_keys.append((2.4, _brincar_keys[0][1]))
SIGNS['brincar'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _brincar_y,
    'keys': _brincar_keys,
    # A circle beside the wrist of each hand (outside it).
    'arrows': [{'d': circle_arrow(108, 192, 15, -60, 230, True)}, {'d': circle_arrow(292, 236, 15, 240, -50, False)}],
    'mirror_second': True,
}
TITLES['brincar'] = 'Sinal de brincar em Libras'
