# VER: hand in V (index and middle straight and apart, the others folded under the thumb), fingers up and
# palm forward, beside the eye on the cheek; it moves down and a little forward, stopping in front of the
# chest. Once. (UFSC Signbank VER: V, cheek. The INES VER1 video shows another variant.)


def hs_ver_v():
    """V: index and middle straight up and apart, ring and little finger folded under the thumb."""
    shape = fist({'index': fing(12, 0, 0, 0), 'middle': fing(-8, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


_ver_v = hs_ver_v()
_ver_pole = (0.6, 1.0, 0.45)
# Beside the eye, on the cheek side of the face: fingers up, palm forward.
_ver_eye = P((160, 94), _ver_v, 'fingertips', yaw=10, pitch=0, roll=6, scale=1.0, depth=40, pole=_ver_pole)
# In front of the chest, the fingers still up and tipped a little forward.
_ver_chest = P((168, 186), _ver_v, 'fingertips', yaw=5, pitch=20, roll=4, scale=1.1, depth=80, pole=_ver_pole,
               ease='out')
SIGNS['ver'] = {
    'poster': 0.3, 'dur': 2.2, 'hands': ['right'], 'handshape': _ver_v,
    'keys': [(0.0, [_ver_eye]), (0.4, [_ver_eye]), (1.0, [_ver_chest]), (1.7, [_ver_chest]),
             (2.2, [dict(_ver_eye, ease='smooth')])],
    # Down from the eye and forward.
    'arrows': [{'d': 'M 198 148 Q 206 170 194 190'}],
}
TITLES['ver'] = 'Sinal de ver em Libras'
