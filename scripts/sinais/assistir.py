# ASSISTIR: small C (thumb and index curved, the other fingers closed) at the eye, the thumb on the
# cheek under the eye and the index curved above it, as if framing the look. The hand taps the cheek
# twice, moving back a little each time. (UFSC Signbank ASSISTIR; the INES ASSISTIR1 video shows
# a C with all the fingers.)


def hs_assistir_c():
    """Baby C: index and thumb curved toward each other with a gap the size of an eye between their
    tips, the other fingers folded."""
    shape = fist({'index': fing(2, 10, 40, 28)})
    tip = finger_chain('index', shape['index'])[0][3]
    shape['thumb'] = solve_thumb((tip[0] + 1.0, tip[1] + 20.0, tip[2] + 3.0), pad_to=(0.0, -1.0, 0.3),
                                 pref=(-5.0, 45.0, 55.0, 15.0, 20.0))
    return shape


_assistir_c = hs_assistir_c()
_assistir_pose = lambda at, **kw: P(at, _assistir_c, 'thumb_tip', yaw=30, pitch=10, roll=35, scale=0.92,
                                    depth=38, pole=(0.6, 1.0, 0.45), **kw)
_assistir_on = _assistir_pose((175, 109))
_assistir_off = _assistir_pose((167, 113))
SIGNS['assistir'] = {
    'poster': 0.35, 'dur': 2.2, 'hands': ['right'], 'handshape': _assistir_c, 'handshape_view': {'yaw': -90},
    'keys': [(0.0, [_assistir_off]), (0.2, [_assistir_off]), (0.35, [_assistir_on]), (0.6, [_assistir_off]),
             (0.75, [_assistir_on]), (1.0, [_assistir_off]), (2.2, [_assistir_off])],
    'marks': [(176, 116, 180)],
    'arrows': [{'d': 'M 140 92 L 128 98', 'both': True}],
}
TITLES['assistir'] = 'Sinal de assistir em Libras'
