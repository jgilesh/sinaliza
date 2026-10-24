# VOTAR: the support hand is loosely closed in front of the chest, the opening between the thumb and
# the index on top, like a ballot box. The dominant hand, flat, fingers together and pointing down,
# palm toward the body, comes down and goes into it, like putting a vote in the box. Once. (UFSC
# Signbank VOTAR; INES VOTAR agrees.)


def hs_votar_box():
    """Loosely closed hand: fingers curled together, the thumb opposite them, a round opening left
    between the thumb and the index."""
    return {'index': fing(1, 50, 62, 34), 'middle': fing(0, 54, 64, 36), 'ring': fing(-1, 58, 64, 36),
            'pinky': fing(-2, 62, 62, 36), 'thumb': (12.0, 46.0, 50.0, 12.0, 18.0)}


def hs_votar_flat():
    """B with the fingers together and a little curved toward the palm, the thumb along the index."""
    return {'index': fing(2, 6, 12, 8), 'middle': fing(0, 6, 12, 8), 'ring': fing(-2, 6, 12, 8),
            'pinky': fing(-4, 8, 12, 8), 'thumb': (-18.0, 8.0, 10.0, 6.0, 4.0)}


_votar_box, _votar_flat = hs_votar_box(), hs_votar_flat()
# Support (defined as a right hand, then mirrored): back of the hand to the viewer, the knuckles toward
# the midline, the thumb and index on top with the opening between them turned up.
_votar_sup = mirrored(P((156, 252), _votar_box, 'wrist', yaw=-160, pitch=0, roll=80, scale=1.05, depth=70))
# Dominant: back of the hand to the viewer, fingers down and tipped away a little, above the opening.
_votar_hand = lambda y: P((214, y), _votar_flat, 'fingertips', yaw=180, pitch=-35, roll=180, scale=1.0, depth=75,
                          pole=(0.4, 1.0, 0.4))
_votar_up, _votar_in = _votar_hand(214), _votar_hand(246)
SIGNS['votar'] = {
    # The support hand is drawn last, in front: the fingertips go in behind its thumb and index.
    'poster': 1.1, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _votar_flat,
    'handshape_view': {'yaw': 0},
    'keys': [(0.0, [_votar_up, _votar_sup]), (0.4, [_votar_up, _votar_sup]), (1.0, [_votar_in, _votar_sup]),
             (1.8, [_votar_in, _votar_sup]), (2.4, [_votar_up, _votar_sup])],
    'arrows': [{'d': 'M 182 186 L 182 226'}],
}
TITLES['votar'] = 'Sinal de votar em Libras'
