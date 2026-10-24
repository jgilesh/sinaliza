# DURAR: in front of the chest, fingers up, the tips of the index and middle fingers resting on the pad
# of the thumb (ring and little finger bent); the two fingertips rub the thumb by turns, without stopping,
# while the hand moves slowly straight forward. (UFSC Signbank DURAR: contato contínuo, para frente,
# alternado; the INES video agrees.)


def hs_durar_rub(lift):
    """Index and middle curved onto the thumb pad, ring and little finger bent further; `lift` = which
    of the two fingertips is lifted a little off the thumb ('index' or 'middle')."""
    shape = {'index': fing(2, 42, 52, 30), 'middle': fing(-1, 44, 54, 32), 'ring': fing(-3, 62, 80, 50),
             'pinky': fing(-6, 64, 80, 50)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    shape[lift] = fing(shape[lift][0], shape[lift][1] - 14, shape[lift][2] - 18, shape[lift][3] - 10)
    return shape


_durar_i, _durar_m = hs_durar_rub('middle'), hs_durar_rub('index')
_durar_hold = hs_durar_rub('middle')


def _durar_pose(shape, k):
    # Palm toward the midline and the viewer: the fingertips curl onto the thumb at the front of the hand.
    return P((170 - 10 * k, 206 + 8 * k), shape, 'wrist', yaw=45, pitch=-8 - 10 * k, roll=-6, scale=1.0 + 0.14 * k,
             depth=60 + 40 * k, pole=(0.45, 1.0, 0.4), ease='linear')


_durar_keys = [(0.0, [_durar_pose(_durar_i, 0)]), (0.3, [_durar_pose(_durar_i, 0)])]
_durar_n = 8
for _durar_s in range(1, _durar_n + 1):
    _durar_keys.append((0.3 + 1.5 * _durar_s / _durar_n,
                        [_durar_pose(_durar_m if _durar_s % 2 else _durar_i, _durar_s / _durar_n)]))
_durar_keys += [(2.3, [_durar_pose(_durar_i, 1.0)]), (2.8, [dict(_durar_pose(_durar_i, 0), ease='smooth')])]
SIGNS['durar'] = {
    'poster': 0.3, 'dur': 2.8, 'hands': ['right'], 'handshape': _durar_hold, 'handshape_view': {'yaw': -60},
    'keys': _durar_keys,
    'arrows': [{'d': 'M 130 170 L 110 186'}],
}
TITLES['durar'] = 'Sinal de durar em Libras'
