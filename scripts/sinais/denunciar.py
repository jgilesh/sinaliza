# DENUNCIAR: the support hand stands open (B) at shoulder height on its own side, fingers up, palm
# toward the signing hand. The signing index (1), lying across and pointing at the support hand, goes
# from the mouth to touch the support palm, comes back to the mouth and goes again, twice, as if
# telling on someone. (UFSC Signbank DENUNCIAR; the INES video shows another form.)


def hs_denunciar_b():
    """B with the thumb resting along the side of the index."""
    shape = hs_B()
    shape['thumb'] = (8.0, 12.0, 8.0, 6.0, 4.0)
    return shape


_denunciar_1, _denunciar_b = hs_1(), hs_denunciar_b()
# Support hand (a right-hand pose, mirrored): fingers up, palm toward the midline and a little toward
# the viewer.
_denunciar_sup = mirrored(P((140, 206), _denunciar_b, 'wrist', yaw=45, pitch=0, roll=-4, scale=1.0, depth=60))
_denunciar_pole = (0.45, 1.0, 0.45)
# Index across, pointing at the support hand: back of the hand to the viewer.
_denunciar_mouth = P((196, 136), _denunciar_1, 'index_tip', yaw=150, pitch=0, roll=88, scale=1.0, depth=48,
                     pole=_denunciar_pole)
_denunciar_touch = P((242, 156), _denunciar_1, 'index_tip', yaw=150, pitch=0, roll=88, scale=1.0, depth=62,
                     pole=_denunciar_pole)
_denunciar_keys = [(0.0, _denunciar_mouth), (0.3, _denunciar_mouth), (0.65, _denunciar_touch), (1.0, _denunciar_mouth),
                   (1.35, _denunciar_touch), (2.0, _denunciar_touch), (2.4, _denunciar_mouth)]
SIGNS['denunciar'] = {
    'poster': 0.65, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _denunciar_1,
    'keys': [(t, [p, _denunciar_sup]) for t, p in _denunciar_keys],
    'arrows': [{'d': 'M 196 168 L 236 182', 'both': True}],
    'marks': [(236, 146, -60)],
    'mirror_second': True,
}
TITLES['denunciar'] = 'Sinal de denunciar em Libras'
