# VIVER: the hand with the fingertips together on the thumb (bunched) rests on the chest on the heart
# side, palm toward the chest; the fingers open a little and close again, two or three times, like a
# pulse. (UFSC Signbank VIVER: Flower; INES VIVER agrees.)


def hs_viver_bunch():
    """Fingertips together on the thumb tip (flat O), the fingers bent mostly at the knuckles."""
    shape = {'index': fing(2, 52, 34, 22), 'middle': fing(0, 56, 32, 22), 'ring': fing(-2, 60, 30, 20),
             'pinky': fing(-4, 64, 28, 20)}
    shape['thumb'] = pinch_thumb(shape)
    return shape


def hs_viver_open():
    """The same hand opened a little: fingers apart and less bent, the thumb away from them."""
    wide = {'index': fing(8, 30, 22, 14), 'middle': fing(2, 32, 22, 14), 'ring': fing(-5, 34, 22, 14),
            'pinky': fing(-12, 38, 22, 14), 'thumb': (36.0, 30.0, 25.0, 10.0, 10.0)}
    return lerp(hs_viver_bunch(), wide, 0.65)


_viver_bunch, _viver_open = hs_viver_bunch(), hs_viver_open()
_viver_pole = (0.3, 1.0, 0.45)
# On the chest on the heart side (the viewer's right): the back of the hand to the viewer, the
# fingertips toward the chest and up.
_viver = lambda shape: P((224, 210), shape, 'wrist', yaw=215, pitch=-25, roll=40, scale=1.08, depth=34, pole=_viver_pole)
_viver_c, _viver_o = _viver(_viver_bunch), _viver(_viver_open)
_viver_keys = [(0.0, [_viver_c]), (0.4, [_viver_c])]
for _viver_i in range(3):   # opens and closes three times
    _viver_t = 0.4 + 0.44 * _viver_i
    _viver_keys += [(_viver_t + 0.22, [_viver_o]), (_viver_t + 0.44, [_viver_c])]
_viver_keys += [(2.4, [_viver_c])]
SIGNS['viver'] = {
    'poster': 0.4, 'dur': 2.4, 'hands': ['right'], 'handshape': _viver_bunch, 'handshape_view': {'yaw': -85},
    'keys': _viver_keys,
    'arrows': [{'d': 'M 262 160 Q 276 172 270 190', 'both': True}],
    'marks': [(212, 198, -110)],
}
TITLES['viver'] = 'Sinal de viver em Libras'
