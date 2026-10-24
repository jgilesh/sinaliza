# SONHAR: the index fingertip touches the temple, the other fingers loose and a little curved; the hand
# rises in an arc up and out to beside the head, opening into 5 (fingers spread, palm forward), with a
# light ripple of the fingers at the end. (UFSC Signbank SONHAR: 1+5, têmpora; INES SONHAR agrees.)


def hs_sonhar_point():
    """Index out (a little bent), the other fingers loosely curled, the thumb resting against them."""
    shape = {'index': fing(4, 4, 14, 8), 'middle': fing(0, 58, 70, 40), 'ring': fing(-3, 62, 72, 42),
             'pinky': fing(-7, 66, 72, 42)}
    shape['thumb'] = (6.0, 34.0, 40.0, 18.0, 16.0)
    return shape


def hs_sonhar_open(wave=0):
    """5, with the fingers bending a little in turn (wave = 1 or 2) for the ripple."""
    b = {0: (0, 0, 0, 0), 1: (18, 0, 18, 0), 2: (0, 18, 0, 18)}[wave]
    return {'index': fing(14, b[0], 4 + b[0] * 0.6, 2), 'middle': fing(3, b[1], 3 + b[1] * 0.6, 2),
            'ring': fing(-8, b[2], 4 + b[2] * 0.6, 2), 'pinky': fing(-18, b[3], 5 + b[3] * 0.6, 3),
            'thumb': (40.0, 16.0, 6.0, 6.0, 4.0)}


_son_pt, _son_5 = hs_sonhar_point(), hs_sonhar_open()
_son_pole = (0.6, 1.0, 0.4)
# Index tip on the temple, palm forward, the hand outside the face (fingers leaning in).
_son_on = P((164, 88), _son_pt, 'index_tip', yaw=-6, pitch=0, roll=26, scale=1.05, depth=40, pole=_son_pole)
_son_end = lambda shape, **kw: P((98, 120), shape, 'wrist', yaw=-4, pitch=0, roll=-12, scale=1.1, depth=55,
                                pole=_son_pole, **kw)
_son_keys = [(0.0, [_son_on]), (0.4, [_son_on]), (1.0, [_son_end(_son_5, via=(120, 76))])]
for _son_i in range(4):
    _son_keys.append((round(1.15 + 0.15 * _son_i, 2), [_son_end(hs_sonhar_open(1 + _son_i % 2))]))
_son_keys += [(1.85, [_son_end(_son_5)]), (2.3, [_son_end(_son_5)]), (2.8, [dict(_son_on, via=(130, 80))])]
SIGNS['sonhar'] = {
    'poster': 0.4, 'dur': 2.8, 'hands': ['right'], 'handshape': _son_pt, 'handshape_view': {'yaw': 0},
    'keys': _son_keys,
    'marks': [(168, 80, 40)],
    # From the temple, up and out to beside the head.
    'arrows': [{'d': 'M 172 50 Q 160 22 130 22'}],
}
TITLES['sonhar'] = 'Sinal de sonhar em Libras'
