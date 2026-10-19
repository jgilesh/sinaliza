# CUSPIR: hooked index (the other fingers closed) with its bent tip on the lips; the hand leaves the mouth
# in an arc forward and down, the wrist turning, and ends with the hooked index pointing down, as if
# something were thrown out of the mouth. Once. (UFSC Signbank CUSPIR: 1_curved, mouth, arc forward,
# supination; INES CUSPIR agrees.)


def hs_cuspir_hook():
    """Index up with its tip curled forward (toward the palm side) at the middle and end joints, the
    other fingers closed, the thumb over the middle finger."""
    shape = fist({'index': fing(2, 0, 55, 40)})
    shape['thumb'] = thumb_over(shape, ['middle'])
    return shape


_cuspir_h = hs_cuspir_hook()
# On the mouth: the hand below the corner of the mouth, palm toward the face, the index rising and its
# hooked tip touching the lips; the hand stays below the nose so the eyes stay clear.
_cuspir_on = P((194, 128), _cuspir_h, 'index_tip', yaw=72, pitch=-10, roll=12, scale=1.02, depth=30,
               pole=(0.35, 1.0, 0.6))
# Thrown: forward and down, out on the dominant side, the wrist turned so the hooked index points down,
# seen from the thumb side.
_cuspir_off = P((132, 224), _cuspir_h, 'index_tip', yaw=-70, pitch=0, roll=170, scale=1.12, depth=85,
                pole=(0.45, 1.0, 0.45), via=(150, 196), ease='out')
SIGNS['cuspir'] = {
    'poster': 0.0, 'dur': 2.2, 'hands': ['right'], 'handshape': _cuspir_h, 'handshape_view': {'yaw': -35, 'pitch': -15},
    'keys': [(0.0, [_cuspir_on]), (0.35, [_cuspir_on]), (0.85, [_cuspir_off]), (1.6, [_cuspir_off]),
             (2.2, [dict(_cuspir_on, via=(130, 170), ease='smooth')])],
    'marks': [(200, 131, 160)],
    # Out of the mouth, forward and down to the dominant side.
    'arrows': [{'d': 'M 188 194 Q 182 228 150 238'}],
}
TITLES['cuspir'] = 'Sinal de cuspir em Libras'
