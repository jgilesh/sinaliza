# DEVER (owe, debt): the support hand closed with the thumb up (A), in front of the chest, palm toward
# the signing side. The signing index, its tip curled (1 curvo), palm down, taps the side of the support
# thumb and pulls back toward the signer, twice. (UFSC Signbank DEVER: 1_curved + A, final contact,
# backward. The INES DEVER1 video shows another sign, for the "obligation" sense.)



def hs_dever_thumb_up():
    """Fist with the thumb straight out on the radial side (thumbs-up when the forearm points forward)."""
    return fist({'thumb': (50.0, 10.0, 0.0, 4.0, 2.0)})


_dever_a = hs_dever_thumb_up()
_dever_1 = hs_1_curved()
# Support hand (a right-hand pose, mirrored): the forearm pointing forward, the curled fingers toward the
# viewer, the thumb up, the palm turned toward the signing hand.
_dever_sup = mirrored(P((186, 190), _dever_a, 'thumb_tip', yaw=90, pitch=65, roll=0, scale=1.12, depth=80,
                        pole=(0.3, 1.0, 0.45)))
# Signing hand: palm down and a little away, the back of the hand tipped toward the viewer, the index
# pointing across at the support thumb, its tip curled down.
_dever_pole = (0.5, 1.0, 0.4)
_dever_on = P((203, 208), _dever_1, 'index_tip', yaw=118, pitch=0, roll=88, scale=1.12, depth=85, pole=_dever_pole)
_dever_off = P((174, 204), _dever_1, 'index_tip', yaw=118, pitch=0, roll=78, scale=1.12, depth=80, pole=_dever_pole)
SIGNS['dever'] = {
    'poster': 0.5, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _dever_1,
    'handshape_view': {'yaw': -30, 'pitch': -25},
    'keys': [(0.0, [_dever_off, _dever_sup]), (0.3, [_dever_off, _dever_sup]), (0.5, [_dever_on, _dever_sup]),
             (0.65, [_dever_on, _dever_sup]), (0.95, [_dever_off, _dever_sup]), (1.15, [_dever_on, _dever_sup]),
             (1.3, [_dever_on, _dever_sup]), (1.6, [_dever_off, _dever_sup]), (2.2, [_dever_off, _dever_sup])],
    # Above the signing hand: in to the thumb and back.
    'arrows': [{'d': 'M 160 178 L 194 178', 'both': True}],
    # Where the index taps the side of the support thumb.
    'marks': [(208, 196, -30)],
    'mirror_second': True,
}
TITLES['dever'] = 'Sinal de dever em Libras'
