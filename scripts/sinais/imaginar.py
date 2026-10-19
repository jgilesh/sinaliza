# IMAGINAR: open hand with the fingers spread (5), palm forward, the fingertips on the side of the
# forehead; the hand moves away diagonally up and out and comes back, 2 to 3 times (the eyes look
# up, dreamy). (UFSC Signbank IMAGINAR and INES IMAGINAR agree.)


def hs_imaginar_5():
    """Open hand, fingers spread, the thumb relaxed and apart (less stretched than the atlas 5)."""
    return {'index': fing(14, 0, 4, 2), 'middle': fing(3, 0, 3, 2), 'ring': fing(-8, 0, 4, 2),
            'pinky': fing(-18, 0, 5, 3), 'thumb': (30.0, 22.0, 12.0, 10.0, 8.0)}


_imag_5 = hs_imaginar_5()
_imag_on = P((166, 60), _imag_5, 'fingertips', yaw=25, pitch=0, roll=42, scale=1.0, depth=38, pole=(0.8, 1.0, 0.45))
_imag_off = P((134, 30), _imag_5, 'fingertips', yaw=15, pitch=-10, roll=22, scale=1.05, depth=60, pole=(0.8, 1.0, 0.45),
              ease='out')
_imag_back = dict(_imag_on, ease='smooth')
_imag_keys = [(0.0, [_imag_on]), (0.3, [_imag_on])]
for _imag_k in range(3):
    _imag_t = 0.3 + 0.6 * _imag_k
    _imag_keys += [(round(_imag_t + 0.3, 2), [_imag_off]), (round(_imag_t + 0.6, 2), [_imag_back])]
_imag_keys.append((2.6, [_imag_on]))
SIGNS['imaginar'] = {
    'poster': 0.3, 'dur': 2.6, 'hands': ['right'], 'handshape': _imag_5,
    'keys': _imag_keys,
    # The fingertips touch the side of the forehead.
    'marks': [(171, 56, 40)],
    'arrows': [{'d': 'M 182 42 Q 176 20 152 10', 'both': True}],
}
TITLES['imaginar'] = 'Sinal de imaginar em Libras'
