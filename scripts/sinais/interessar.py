# INTERESSAR: small C (thumb and index curved, the other fingers closed) at the eye, the thumb just below
# it and the index curved above, as if framing the look; the hand moves away from the face, forward and
# down, keeping the shape, and stops in front of the shoulder. Once. (UFSC Signbank INTERESSAR: Baby_C,
# eye; the INES INTERESSAR video agrees.)


def hs_interessar_c():
    """Baby C: index and thumb curved toward each other with a gap the size of an eye between their
    tips, the other fingers folded."""
    shape = fist({'index': fing(2, 10, 40, 28)})
    tip = finger_chain('index', shape['index'])[0][3]
    shape['thumb'] = solve_thumb((tip[0] + 1.0, tip[1] + 20.0, tip[2] + 3.0), pad_to=(0.0, -1.0, 0.3),
                                 pref=(-5.0, 45.0, 55.0, 15.0, 20.0))
    return shape


_interessar_c = hs_interessar_c()
_interessar_pole = (0.6, 1.0, 0.45)
# At the eye: the thumb tip just below its outer corner, the index curved above it, the palm toward the
# face, so the C between them frames the eye.
_interessar_eye = P((174, 110), _interessar_c, 'thumb_tip', yaw=30, pitch=10, roll=35, scale=0.92, depth=38,
                    pole=_interessar_pole)
# Away, forward and down, in front of the shoulder, the C kept.
_interessar_off = P((150, 168), _interessar_c, 'thumb_tip', yaw=25, pitch=10, roll=32, scale=1.02, depth=75,
                    pole=_interessar_pole, ease='out')
SIGNS['interessar'] = {
    'poster': 0.3, 'dur': 2.2, 'hands': ['right'], 'handshape': _interessar_c, 'handshape_view': {'yaw': -90},
    'keys': [(0.0, [_interessar_eye]), (0.4, [_interessar_eye]), (1.0, [_interessar_off]), (1.7, [_interessar_off]),
             (2.2, [dict(_interessar_eye, ease='smooth')])],
    # Away from the eye, forward and down.
    'arrows': [{'d': 'M 120 86 Q 106 110 112 136'}],
}
TITLES['interessar'] = 'Sinal de interessar em Libras'
