# ABANDONAR: both hands with the middle finger bent and held by the thumb, the other fingers open
# (ready to flick); the dominant hand by the chin, the other raised by its shoulder. The fingers flick
# open at once and the dominant hand, now open, comes down forward in an arc to the front of the chest,
# palm down; the other hand opens where it is. Once. (UFSC Signbank ABANDONAR: 5m_closed, abertura,
# arco distal.)


def hs_abandonar_5m():
    """Flick ready: middle finger bent toward the palm, its tip held on the thumb pad; index, ring and
    little finger open and spread."""
    shape = {'index': fing(12, 0, 4, 2), 'middle': fing(2, 58, 80, 52), 'ring': fing(-8, 0, 4, 2),
             'pinky': fing(-18, 0, 5, 3)}
    shape['thumb'] = pinch_thumb(shape, ('middle',))
    return shape


_aban_m, _aban_5 = hs_abandonar_5m(), hs_5()
# Dominant: beside the chin, fingers up, palm turned toward the middle and the viewer.
_aban_r0 = P((160, 196), _aban_m, 'wrist', yaw=20, pitch=0, roll=8, scale=1.0, depth=40, pole=(0.5, 1.0, 0.45))
_aban_r1 = P((162, 190), _aban_5, 'wrist', yaw=50, pitch=0, roll=14, scale=1.0, depth=44, pole=(0.5, 1.0, 0.45))
# End: in front of the chest, palm down, fingers toward the other side and a little down.
_aban_r2 = P((160, 228), _aban_5, 'wrist', yaw=125, pitch=0, roll=105, scale=1.1, depth=75, pole=(0.45, 1.0, 0.4),
             via=(146, 214), ease='out')
# Other hand (given as its right-hand twin): raised by the shoulder, fingers up, palm toward the viewer.
_aban_l0 = P((132, 184), _aban_m, 'wrist', yaw=30, pitch=0, roll=-6, scale=1.0, depth=40, pole=(0.5, 1.0, 0.45))
_aban_l1 = P((128, 186), _aban_5, 'wrist', yaw=20, pitch=0, roll=-18, scale=1.0, depth=42, pole=(0.5, 1.0, 0.45))
_aban_k = lambda r, l: [r, mirrored(l)]
SIGNS['abandonar'] = {
    'poster': 0.2, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _aban_m, 'handshape_view': {'yaw': 0},
    'keys': [(0.0, _aban_k(_aban_r0, _aban_l0)), (0.4, _aban_k(_aban_r0, _aban_l0)), (0.55, _aban_k(_aban_r1, _aban_l1)),
             (1.0, _aban_k(_aban_r2, _aban_l1)), (1.9, _aban_k(_aban_r2, _aban_l1)),
             (2.6, _aban_k(dict(_aban_r0, via=(140, 230)), _aban_l0))],
    'arrows': [{'d': 'M 126 176 Q 114 216 140 248'}],
    'mirror_second': True,
}
TITLES['abandonar'] = 'Sinal de abandonar em Libras'
