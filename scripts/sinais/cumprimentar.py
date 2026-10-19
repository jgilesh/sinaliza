# CUMPRIMENTAR: one hand holds the other in front of the chest, as in a handshake, and the clasped
# hands swing up and down together, 2 to 3 times. Drawn with the signing hand on top (palm down, its
# fingers wrapped over the edge of the other hand) and the support hand under it (palm up), so the
# fingers that wrap toward the viewer are the ones drawn in front. (UFSC Signbank CUMPRIMENTAR;
# INES CUMPRIMENTAR.)


def hs_cumprimentar_grip():
    """Gripping hand: fingers together and curled as around a handle, the thumb along the side of the
    index (A open)."""
    return {'index': fing(2, 48, 62, 34), 'middle': fing(0, 50, 64, 36), 'ring': fing(-2, 52, 64, 36),
            'pinky': fing(-4, 54, 62, 34), 'thumb': (14.0, 14.0, 12.0, 8.0, 8.0)}


def hs_cumprimentar_back():
    """The support hand's grip, its fingers curled a little tighter (they wrap behind the signing hand
    and stay hidden there)."""
    shape = hs_cumprimentar_grip()
    shape.update({'index': fing(2, 60, 80, 44), 'middle': fing(0, 62, 82, 46), 'ring': fing(-2, 64, 82, 46),
                  'pinky': fing(-4, 66, 80, 44)})
    return shape


_cum_g, _cum_gb = hs_cumprimentar_grip(), hs_cumprimentar_back()


def _cum_pair(dy):
    # The palms press together at the midline, thumbs on top; each hand's fingers point forward and
    # curl around the other hand. Seen from the front, the knuckles of the signing hand stack up and
    # its fingers wrap over the support hand; the support hand's fingers wrap behind the signing hand.
    top = P((178, 224 + dy), _cum_g, 'wrist', yaw=100, pitch=60, roll=35, scale=1.1, depth=80, pole=(0.5, 1.0, 0.4))
    base = mirrored(P((176, 224 + dy), _cum_gb, 'wrist', yaw=100, pitch=60, roll=35, scale=1.1, depth=80,
                      pole=(0.5, 1.0, 0.4)))
    return [top, base]


_cum_mid, _cum_up, _cum_down = _cum_pair(0), _cum_pair(-10), _cum_pair(10)
_cum_keys = [(0.0, _cum_mid), (0.3, _cum_mid)]
for _cum_i in range(2):
    _cum_t = 0.3 + 0.5 * _cum_i
    _cum_keys += [(_cum_t + 0.25, _cum_up), (_cum_t + 0.5, _cum_down)]
_cum_keys += [(1.6, _cum_mid), (2.2, _cum_mid)]
SIGNS['cumprimentar'] = {
    'poster': 0.0, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _cum_g, 'handshape_view': {'yaw': -60},
    'keys': _cum_keys,
    'arrows': [{'d': 'M 268 196 L 268 236', 'both': True}],
    'mirror_second': True,
}
TITLES['cumprimentar'] = 'Sinal de cumprimentar em Libras'
