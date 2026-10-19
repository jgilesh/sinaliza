# CONFIAR: curved hand (C) touches the front of the neck, just under the chin, palm toward the body;
# it leaves in an arc forward and out to the side, the wrist turning, and ends in front of the shoulder
# with the C open and the palm forward. Once. (UFSC Signbank CONFIAR: C, contato inicial, arco.)
_confiar_c = hs_C()
# Start: the C wraps the front of the neck, fingers toward the midline, seen mostly from the little-finger
# side so the curve of the fingers over the thumb reads.
_confiar_on = P((198, 166), _confiar_c, 'fingertips', yaw=112, pitch=-15, roll=82, scale=1.0, depth=40,
                pole=(0.45, 1.0, 0.4))
# End: in front of the shoulder, palm forward and toward the midline, fingers up and curved over the
# thumb: the C seen three-quarter, its opening toward the midline.
_confiar_off = P((122, 176), _confiar_c, 'wrist', yaw=55, pitch=0, roll=40, scale=1.15, depth=75, ease='out',
                 via=(150, 200), pole=(0.45, 1.0, 0.4))
SIGNS['confiar'] = {
    'poster': 0.9, 'dur': 2.3, 'hands': ['right'], 'handshape': _confiar_c, 'handshape_view': {'yaw': -70},
    'keys': [(0.0, [_confiar_on]), (0.4, [_confiar_on]), (0.9, [_confiar_off]), (1.7, [_confiar_off]),
             (2.3, [dict(_confiar_on, ease='smooth')])],
    'marks': [(200, 162, 0)],
    'marks_under': True,
    'arrows': [{'d': 'M 176 196 Q 150 214 120 204'}],
}
TITLES['confiar'] = 'Sinal de confiar em Libras'
