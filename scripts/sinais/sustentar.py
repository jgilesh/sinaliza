# SUSTENTAR: the support hand holds its index out level in front of the chest, pointing toward the
# signing hand, palm down. The signing hand, fingers together and bent down onto the thumb (a beak),
# rests the base of the hand on that index and taps it lightly: it lifts a little and comes back
# down, three or four times. (UFSC Signbank SUSTENTAR: Beak on the weak hand's index; INES SUSTENTAR.)


def hs_sustentar_beak():
    """Beak: the four fingers together, bent mostly at the knuckles, their tips resting on the
    thumb's pad."""
    shape = {'index': fing(3, 62, 30, 18), 'middle': fing(0, 64, 30, 18), 'ring': fing(-3, 66, 30, 18),
             'pinky': fing(-6, 70, 30, 18)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


_sus_beak, _sus_one = hs_sustentar_beak(), hs_1()
# Support hand, defined as a right hand (index level, pointing toward the midline, palm down) and
# mirrored: its index tip lies under the signing hand's wrist, the rest of it shows beside.
_sus_sup = mirrored(P((222, 230), _sus_one, 'index_tip', yaw=40, pitch=0, roll=90, scale=1.05, depth=50))
# Signing hand: the wrist on the index, the hand tilted up with the beak hanging toward the support hand.
_sus_dom = lambda dy, ease='smooth': P((182, 216 - dy), _sus_beak, 'wrist', yaw=100, pitch=0, roll=25, scale=1.05,
                                       depth=56, pole=(0.3, 1.0, 0.4), ease=ease)
_sus_on, _sus_up = _sus_dom(0), _sus_dom(12, 'out')
_sus_keys = [(0.0, [_sus_on, _sus_sup]), (0.3, [_sus_on, _sus_sup])]
for _sus_k in range(4):
    _sus_keys += [(0.45 + 0.4 * _sus_k, [_sus_up, _sus_sup]), (0.7 + 0.4 * _sus_k, [dict(_sus_on, ease='in'), _sus_sup])]
_sus_keys.append((2.4, [_sus_on, _sus_sup]))
SIGNS['sustentar'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _sus_beak, 'handshape_view': {'yaw': -90},
    'keys': _sus_keys,
    'marks': [(178, 240, 180)],
    'arrows': [{'d': 'M 150 214 L 150 190', 'both': True}],
    'mirror_second': True,
}
TITLES['sustentar'] = 'Sinal de sustentar em Libras'
