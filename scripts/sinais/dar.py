# DAR: the fingertips gathered on the thumb (beak), palm up, near the chest; the hand moves straight
# forward and the fingers open at the end, as if handing something over. Once. (UFSC Signbank DAR:
# Flower, straight forward.)


def hs_dar_beak():
    """Beak: fingers together, bent at the knuckles and middle joints, their tips on the thumb's pad."""
    shape = {'index': fing(1, 50, 30, 14), 'middle': fing(-1, 54, 30, 14), 'ring': fing(-3, 58, 28, 14),
             'pinky': fing(-5, 62, 26, 14)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


def hs_dar_open():
    """The beak opened like a flower: fingers spread and gently curved, the thumb apart."""
    return {'index': fing(10, 24, 34, 18), 'middle': fing(2, 26, 34, 18), 'ring': fing(-6, 28, 34, 18),
            'pinky': fing(-14, 30, 34, 18), 'thumb': (36.0, 34.0, 30.0, 12.0, 12.0)}


_dar_beak, _dar_open = hs_dar_beak(), hs_dar_open()
_dar_start = P((166, 236), _dar_beak, 'wrist', yaw=60, pitch=-25, roll=12, scale=1.05, depth=60, pole=(0.5, 1.0, 0.4))
_dar_mid = P((160, 240), _dar_beak, 'wrist', yaw=-30, pitch=0, roll=40, scale=1.2, depth=95, pole=(0.5, 1.0, 0.4))
_dar_end = P((158, 240), _dar_open, 'wrist', yaw=-80, pitch=10, roll=70, scale=1.3, depth=115, pole=(0.5, 1.0, 0.4))
SIGNS['dar'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right'], 'handshape': _dar_beak, 'handshape_view': {'yaw': 60, 'pitch': -10},
    'keys': [(0.0, [_dar_start]), (0.3, [_dar_start]), (0.75, [_dar_mid]), (1.0, [_dar_end]), (1.9, [_dar_end]),
             (2.4, [_dar_start])],
    'arrows': [{'d': 'M 120 250 Q 110 226 124 202'}],
}
TITLES['dar'] = 'Sinal de dar em Libras'
