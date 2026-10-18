# BEBER: closed hand with the thumb stretched out (A, the thumb held out sideways); the hand comes
# up to the mouth with the thumb horizontal and its tip on the lips, the folded fingers above, and
# tips back on the wrist, as if drinking from a bottle. Once. (UFSC Signbank BEBER.)


def hs_beber_a():
    """Fist with the thumb stretched out to the side, in the plane of the palm."""
    return fist({'thumb': (50.0, 6.0, 0.0, 2.0, 0.0)})


_beber_hs = hs_beber_a()


def _beber_pose(at, pitch, roll, **kw):
    return P(at, _beber_hs, 'thumb_tip', yaw=15, pitch=pitch, roll=roll, scale=1.1, depth=42,
             pole=(0.25, 1.0, 0.5), **kw)


_beber_low = _beber_pose((150, 200), 0, -10)
_beber_on = _beber_pose((189, 126), 0, -2)
_beber_tip = _beber_pose((189, 125), -35, 10)
SIGNS['beber'] = {
    'poster': 0.6, 'dur': 2.4, 'hands': ['right'], 'handshape': _beber_hs,
    'keys': [(0.0, [_beber_low]), (0.25, [_beber_low]), (0.6, [_beber_on]), (0.8, [_beber_on]),
             (1.2, [_beber_tip]), (1.8, [_beber_tip]), (2.4, [_beber_low])],
    'marks': [(194, 133, 150)],
    # The hand tips back on the wrist: a short curved arrow over the fist.
    'arrows': [{'d': 'M 134 84 Q 142 68 162 68'}],
}
TITLES['beber'] = 'Sinal de beber em Libras'
