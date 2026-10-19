# APROVEITAR: Y hand (thumb and little finger out). It starts in front of the chest with the back of
# the hand up, rises to chin height on the signing side, swings out to the side and down, and comes
# back up to shoulder height while the wrist turns, ending with the palm toward the body. Once.
# (UFSC Signbank APROVEITAR.)

_apr_y = hs_Y()
_apr_pole = (0.5, 1.0, 0.4)
# In front of the chest, back of the hand up (palm down), the little finger toward the midline.
_apr_a = P((176, 222), _apr_y, 'wrist', yaw=-20, pitch=60, roll=95, scale=1.1, depth=70, pole=_apr_pole)
# Up to chin height, beside the face: palm forward, the Y reads.
_apr_b = P((140, 158), _apr_y, 'wrist', yaw=-10, pitch=0, roll=-10, scale=1.1, depth=65, pole=_apr_pole,
           via=(162, 180))
# Out to the side and down.
_apr_c = P((106, 206), _apr_y, 'wrist', yaw=-40, pitch=10, roll=-35, scale=1.1, depth=70, pole=_apr_pole,
           via=(110, 168))
# Back up to shoulder height: the wrist has turned, palm toward the body, thumb up.
_apr_d = P((124, 168), _apr_y, 'wrist', yaw=150, pitch=0, roll=60, scale=1.12, depth=70, pole=_apr_pole,
           via=(108, 196), ease='out')
SIGNS['aproveitar'] = {
    'poster': 0.65, 'dur': 2.6, 'hands': ['right'], 'handshape': _apr_y,
    'keys': [(0.0, [_apr_a]), (0.3, [_apr_a]), (0.65, [_apr_b]), (1.0, [_apr_c]), (1.35, [_apr_d]),
             (2.1, [_apr_d]), (2.6, [dict(_apr_a, via=(130, 230))])],
    # Outside the hand's path: from chin height out to the side and down, then up again.
    'arrows': [{'d': 'M 118 112 Q 64 132 72 192 Q 76 214 92 200'}],
}
TITLES['aproveitar'] = 'Sinal de aproveitar em Libras'
