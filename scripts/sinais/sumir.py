# SUMIR: both hands open with the fingers a little curved, fingertips of one hand touching those of the
# other in front of the chin and chest. The hands move apart, up and out to the sides, closing into a
# bunch (fingertips together) by the time they reach shoulder height. Once. Frowning face. (UFSC
# Signbank SUMIR. The INES SUMIR video uses one hand that closes into a fist in front of the neck.)


def hs_sumir_open():
    """Open hand, fingers a little apart and slightly curved, thumb open."""
    return {'index': fing(8, 12, 18, 10), 'middle': fing(1, 12, 18, 10), 'ring': fing(-6, 14, 18, 11),
            'pinky': fing(-13, 16, 20, 12), 'thumb': (24.0, 24.0, 20.0, 10.0, 8.0)}


def hs_sumir_bico():
    """Bico: the four fingers bent mostly at the knuckles, nearly straight, their tips gathered on
    the thumb pad."""
    shape = {'index': fing(-2, 52, 26, 14), 'middle': fing(-4, 50, 30, 16), 'ring': fing(-2, 50, 32, 18),
             'pinky': fing(2, 52, 34, 20)}
    shape['thumb'] = pinch_thumb(shape, ('index', 'middle'))
    return shape


_sumir_open, _sumir_bico = hs_sumir_open(), hs_sumir_bico()
# Start: fingertips meeting at the midline in front of the throat, the fingers pointing up and in, the
# palm turned toward the other hand and partly toward the viewer.
_sumir_start = P((199, 166), _sumir_open, 'fingertips', yaw=50, pitch=-10, roll=24, scale=1.05, depth=60,
                 pole=(0.5, 1.0, 0.45))
# End: beside the head, outside the face, fingers up and bunched, palm toward the viewer and the face.
_sumir_end = P((126, 104), _sumir_bico, 'fingertips', yaw=35, pitch=0, roll=-4, scale=1.0, depth=55,
               pole=(0.6, 1.0, 0.45), via=(150, 132), ease='out')
_sumir_keys = [(0.0, [_sumir_start, mirrored(_sumir_start)]), (0.4, [_sumir_start, mirrored(_sumir_start)]),
               (1.1, [_sumir_end, mirrored(_sumir_end)]), (2.0, [_sumir_end, mirrored(_sumir_end)]),
               (2.6, [dict(_sumir_start, ease='smooth'), mirrored(dict(_sumir_start, ease='smooth'))])]
SIGNS['sumir'] = {
    'poster': 0.0, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _sumir_bico, 'handshape_view': {'yaw': -40, 'pitch': -30},
    'keys': _sumir_keys,
    'arrows': [{'trail': 0, 'from': 0.4, 'to': 1.1, 'offset': (-14, 8), 'trim': 0.12},
               {'trail': 1, 'from': 0.4, 'to': 1.1, 'offset': (14, 8), 'trim': 0.12}],
    'mirror_second': True,
}
TITLES['sumir'] = 'Sinal de sumir em Libras'
