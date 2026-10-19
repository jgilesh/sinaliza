# DIMINUIR: both hands with the thumb and index open (an L), the other fingers closed, palms forward,
# at face height on either side; they come down to the front of the chest and a little toward the
# middle while the index bends down onto the thumb (a small pinch). Once. (UFSC Signbank DIMINUIR:
# Baby_beak_open + Baby_beak, both hands. The INES DIMINUIR1 video shows it with one hand.)


def hs_diminuir_pinch():
    """Small pinch: the index bends forward and its pad meets the thumb's pad above the fist."""
    shape = fist({'index': fing(2, 20, 60, 40)})
    shape['thumb'] = pinch_thumb(shape)
    return shape


_dim_open, _dim_pinch = hs_L(), hs_diminuir_pinch()
_dim_top = P((128, 168), _dim_open, 'wrist', yaw=-15, pitch=0, roll=-4, scale=1.05, depth=60, pole=(0.5, 1.0, 0.4))
_dim_low = P((146, 228), _dim_pinch, "wrist", yaw=-55, pitch=0, roll=45, scale=1.05, depth=60, pole=(0.4, 1.0, 0.4),
             ease='smooth')
_dim_back = dict(_dim_top, ease='smooth')
SIGNS['diminuir'] = {
    'poster': 0.75, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _dim_open,
    'keys': [(0.0, [_dim_top, mirrored(_dim_top)]), (0.35, [_dim_top, mirrored(_dim_top)]),
             (1.1, [_dim_low, mirrored(_dim_low)]), (1.9, [_dim_low, mirrored(_dim_low)]),
             (2.4, [_dim_back, mirrored(_dim_back)])],
    'arrows': [{'trail': 0, 'from': 0.35, 'to': 1.1, 'offset': (-30, -4), 'trim': 0.1},
               {'trail': 1, 'from': 0.35, 'to': 1.1, 'offset': (30, -4), 'trim': 0.1}],
    'mirror_second': True,
}
TITLES['diminuir'] = 'Sinal de diminuir em Libras'
