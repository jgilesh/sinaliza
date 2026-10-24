# OFERECER: both hands start in a beak (fingertips gathered on the thumb) in front of the chest; together
# they move forward and out to the sides, opening, and end open with the fingers spread and the palms
# up, as if offering something. Once. (UFSC Signbank OFERECER: Flower+5, both hands, chest; the INES
# OFERECER video shows it with one hand ending palm up.)


def hs_oferecer_beak():
    """Beak: fingers together, bent at the knuckles and middle joints, their tips on the thumb's pad."""
    shape = {'index': fing(1, 50, 30, 14), 'middle': fing(-1, 54, 30, 14), 'ring': fing(-3, 58, 28, 14),
             'pinky': fing(-5, 62, 26, 14)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


def hs_oferecer_open():
    """Open hand, the fingers spread and a little curved, the thumb apart."""
    return {'index': fing(12, 10, 14, 8), 'middle': fing(2, 10, 14, 8), 'ring': fing(-8, 12, 14, 8),
            'pinky': fing(-17, 14, 14, 8), 'thumb': (38.0, 24.0, 16.0, 8.0, 6.0)}


_oferecer_beak, _oferecer_open = hs_oferecer_beak(), hs_oferecer_open()
_oferecer_pole = (0.5, 1.0, 0.4)
# Near the chest: the beaks close to each other (not touching), fingertips up, seen from the side.
_oferecer_start = P((164, 240), _oferecer_beak, 'wrist', yaw=75, pitch=-25, roll=-8, scale=1.05, depth=50,
                    pole=_oferecer_pole)
_oferecer_mid = P((158, 240), lerp(_oferecer_beak, _oferecer_open, 0.4), 'wrist', yaw=60, pitch=5, roll=-45,
                  scale=1.15, depth=85, pole=_oferecer_pole, ease='in')
# Forward and out, open: the palm up and tipped toward the viewer, the fingers pointing out to the side
# and forward.
_oferecer_end = P((150, 238), _oferecer_open, 'wrist', yaw=60, pitch=30, roll=-95, scale=1.2, depth=110,
                  pole=_oferecer_pole, ease='out')
_oferecer_keys = [(0.0, _oferecer_start), (0.3, _oferecer_start), (0.65, _oferecer_mid), (1.0, _oferecer_end),
                  (1.9, _oferecer_end), (2.4, dict(_oferecer_start, ease='smooth'))]
SIGNS['oferecer'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _oferecer_beak,
    'handshape_view': {'yaw': 60, 'pitch': -10},
    'keys': [(t, [p, mirrored(p)]) for t, p in _oferecer_keys],
    # Forward and out to both sides.
    'arrows': [{'d': 'M 180 178 Q 146 166 114 184'}, {'d': 'M 220 178 Q 254 166 286 184'}],
    'mirror_second': True,
}
TITLES['oferecer'] = 'Sinal de oferecer em Libras'
