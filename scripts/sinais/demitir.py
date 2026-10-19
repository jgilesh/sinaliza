# DEMITIR: the support hand open, palm up, in front of the waist. The signing hand, fingers together
# and bent at the knuckles, rests its fingertips on the support palm; then it leaves, going up and out
# to the side while the fingers straighten, ending flat with the palm down, as if sending someone
# away. Once. (UFSC Signbank DEMITIR; INES DEMITIR.)


def hs_demitir_flat():
    """Support B: flat hand, fingers together, the thumb lying along the side of the index (seen palm
    up from the front, an open thumb would point at the viewer and show only as its tip)."""
    return {'index': fing(2, 0, 0, 0), 'middle': fing(0, 0, 0, 0), 'ring': fing(-2, 0, 0, 0),
            'pinky': fing(-4, 0, 0, 0), 'thumb': (-8.0, 6.0, 10.0, 6.0, 4.0)}


def hs_demitir_bent():
    """B bent: fingers together and straight, bent at the knuckles about a right angle, thumb along the
    side of the hand."""
    return {'index': fing(2, 84, 4, 2), 'middle': fing(0, 86, 4, 2), 'ring': fing(-2, 86, 4, 2),
            'pinky': fing(-4, 86, 4, 2), 'thumb': (10.0, 14.0, 10.0, 6.0, 6.0)}


def hs_demitir_open():
    """B: flat hand, fingers together, the thumb along the side of the index."""
    return {'index': fing(2, 0, 0, 0), 'middle': fing(0, 0, 0, 0), 'ring': fing(-2, 0, 0, 0),
            'pinky': fing(-4, 0, 0, 0), 'thumb': (10.0, 14.0, 10.0, 6.0, 6.0)}


_dem_bent, _dem_open, _dem_b = hs_demitir_bent(), hs_demitir_open(), hs_demitir_flat()
_dem_base = mirrored(P((146, 268), _dem_b, 'wrist', yaw=-50, pitch=15, roll=94, scale=1.1, depth=70))
# On the palm: the back of the hand up, tipped toward the viewer, so the bent fingers hang down side by
# side onto the support palm.
_dem_on = P((226, 256), _dem_bent, 'fingertips', yaw=10, pitch=65, roll=20, scale=1.1, depth=72, pole=(0.5, 1.0, 0.4))
# Up and out to the side, flat, palm down, fingers toward the midline.
_dem_off = P((150, 196), _dem_open, 'wrist', yaw=140, pitch=0, roll=86, scale=1.15, depth=80, pole=(0.7, 1.0, 0.4),
             via=(196, 210))
SIGNS['demitir'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _dem_bent,
    'handshape_view': {'yaw': -60, 'pitch': -20},
    'keys': [(0.0, [_dem_on, _dem_base]), (0.4, [_dem_on, _dem_base]), (1.1, [_dem_off, _dem_base]),
             (1.9, [_dem_off, _dem_base]), (2.4, [dict(_dem_on, via=(196, 240)), _dem_base])],
    'marks': [(203, 252, -75)],
    'arrows': [{'d': 'M 190 230 Q 152 228 122 206'}],
    'mirror_second': True,
}
TITLES['demitir'] = 'Sinal de demitir em Libras'
