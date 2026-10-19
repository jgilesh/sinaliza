# SUBSTITUIR: the support hand closed (S) across in front of the body, palm down. The signing hand,
# closed with the thumb up, comes down in an arc and settles on the back of the support hand, near the
# wrist, and stays there. (UFSC Signbank SUBSTITUIR and INES SUBSTITUIR agree.)


def hs_substituir_thumb_up():
    """Fist with the thumb straight out on the radial side (thumbs-up when the forearm points forward)."""
    return fist({'thumb': (50.0, 10.0, 0.0, 4.0, 2.0)})


_subst_s = hs_S()
_subst_a = hs_substituir_thumb_up()
# Support hand (a right-hand pose, mirrored): palm down, the fist pointing across toward the signing
# side, the back of the hand tipped up toward the viewer.
_subst_sup = mirrored(P((166, 256), _subst_s, 'wrist', yaw=128, pitch=0, roll=90, scale=1.1, depth=80,
                        pole=(0.4, 1.0, 0.5)))
_subst_pole = (1.0, 0.45, 0.3)   # the elbow out to the side: the forearm stays clear of the support fist
# Signing hand: thumb up, palm turned toward the support side, the folded fingers toward the viewer,
# resting on the back of the support hand near its wrist...
_subst_on = P((224, 234), _subst_a, 'wrist', yaw=90, pitch=58, roll=0, scale=1.1, depth=88, pole=_subst_pole,
              via=(170, 190), ease='out')
# ...coming from up beside the shoulder.
_subst_up = P((136, 184), _subst_a, 'wrist', yaw=70, pitch=30, roll=-6, scale=1.08, depth=60, pole=_subst_pole)
_subst_back = dict(_subst_up, via=(150, 236), ease='smooth')
SIGNS['substituir'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _subst_a,
    'handshape_view': {'yaw': 40, 'roll': -80},
    'keys': [(0.0, [_subst_up, _subst_sup]), (0.3, [_subst_up, _subst_sup]), (0.8, [_subst_on, _subst_sup]),
             (1.9, [_subst_on, _subst_sup]), (2.4, [_subst_back, _subst_sup])],
    # Above the path: an arc down onto the support hand.
    'arrows': [{'d': 'M 166 166 Q 214 156 226 194'}],
    # Where the signing fist rests on the support hand.
    'marks': [(200, 236, -60)],
    'mirror_second': True,
}
TITLES['substituir'] = 'Sinal de substituir em Libras'
