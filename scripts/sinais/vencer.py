# VENCER: the support hand points its index across in front of the chest, toward the signing side.
# The signing hand, with three fingers up (W: index, middle and ring), touches the tip of that index
# and goes up and out to beside the head, closing its fingers onto the thumb (beak). Once.
# (UFSC Signbank VENCER; INES VENCER1.)


def hs_vencer_w():
    """W: index, middle and ring straight and a little apart; the little finger folded under the
    thumb."""
    shape = fist({'index': fing(8, 0, 0, 0), 'middle': fing(0, 0, 0, 0), 'ring': fing(-8, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['pinky'])
    return shape


def hs_vencer_beak():
    """Beak: fingers together and almost straight, bent at the knuckles, their tips on the thumb's pad."""
    shape = {'index': fing(1, 50, 30, 14), 'middle': fing(-1, 54, 30, 14), 'ring': fing(-3, 58, 28, 14),
             'pinky': fing(-5, 62, 26, 14)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


_ven_w, _ven_beak, _ven_one = hs_vencer_w(), hs_vencer_beak(), hs_1()
# Support (defined as a right hand, then mirrored): index across toward the signing side, palm down.
_ven_sup = mirrored(P((162, 222), _ven_one, 'index_tip', yaw=110, pitch=0, roll=92, scale=1.1, depth=70))
# Signing hand: palm to the viewer, the three fingers up and leaning in, their tips at the index tip.
_ven_on = P((233, 217), _ven_w, 'fingertips', yaw=10, pitch=0, roll=48, scale=1.1, depth=72, pole=(0.5, 1.0, 0.4))
_ven_end = P((122, 150), _ven_beak, 'wrist', yaw=40, pitch=0, roll=-6, scale=1.1, depth=60, pole=(0.7, 1.0, 0.4),
             via=(150, 200))
SIGNS['vencer'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _ven_w,
    'keys': [(0.0, [_ven_on, _ven_sup]), (0.4, [_ven_on, _ven_sup]), (1.1, [_ven_end, _ven_sup]),
             (1.9, [_ven_end, _ven_sup]), (2.4, [dict(_ven_on, via=(150, 220)), _ven_sup])],
    'marks': [(244, 206, 30)],
    'arrows': [{'d': 'M 160 228 Q 112 212 106 166'}],
    'mirror_second': True,
}
TITLES['vencer'] = 'Sinal de vencer em Libras'
