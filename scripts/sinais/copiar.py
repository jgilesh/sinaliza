# COPIAR: the support hand open, palm up, in front of its own shoulder. The dominant hand, open with
# the fingers spread, comes down onto that palm, scrapes across it and moves away to its own side,
# closing the fingers with the tips together, as if taking something and carrying it elsewhere.
# Once. (UFSC Signbank COPIAR: 5+Flower over B, the weak hand's palm. The INES COPIAR video shows
# another variant.)


def hs_copiar_bunch():
    """Fingertips together on the thumb tip (flat O), the fingers bent mostly at the knuckles."""
    shape = {'index': fing(2, 52, 34, 22), 'middle': fing(0, 56, 32, 22), 'ring': fing(-2, 60, 30, 20),
             'pinky': fing(-4, 64, 28, 20)}
    shape['thumb'] = pinch_thumb(shape)
    return shape


_copiar_5, _copiar_b, _copiar_bunch = hs_5(), hs_B(), hs_copiar_bunch()
_copiar_pole = (0.35, 1.0, 0.4)
# Support hand, defined as a right hand (palm up, fingers forward and toward the midline) and mirrored.
_copiar_sup = mirrored(P((132, 214), _copiar_b, 'wrist', yaw=-60, pitch=40, roll=100, scale=1.05, depth=60))
# Dominant, palm down, the back of the hand tilted up toward the viewer, fingers toward the support hand.
_copiar_hand = lambda at, shape, yaw=150, pitch=10, roll=90, **kw: P(at, shape, 'wrist', yaw=yaw, pitch=pitch, roll=roll,
                                                                     scale=1.05, depth=70, pole=_copiar_pole, **kw)
_copiar_above = _copiar_hand((196, 182), _copiar_5)
_copiar_touch = _copiar_hand((202, 202), _copiar_5)
# Away on its own side: fingertips together on the thumb, pointing down, the palm turned toward the viewer.
_copiar_away = _copiar_hand((124, 188), _copiar_bunch, yaw=30, pitch=20, roll=160, via=(160, 196), ease='out')
SIGNS['copiar'] = {
    'poster': 0.6, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _copiar_5,
    'keys': [(0.0, [_copiar_above, _copiar_sup]), (0.3, [_copiar_above, _copiar_sup]),
             (0.6, [_copiar_touch, _copiar_sup]), (1.3, [_copiar_away, _copiar_sup]),
             (2.0, [_copiar_away, _copiar_sup]), (2.6, [dict(_copiar_above, via=(150, 180)), _copiar_sup])],
    'marks': [(292, 204, 90)],
    # From the support palm back to the signing side.
    'arrows': [{'d': 'M 214 168 Q 172 152 138 162'}],
    'mirror_second': True,
}
TITLES['copiar'] = 'Sinal de copiar em Libras'
