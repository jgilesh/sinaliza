# RECLAMAR: both hands in R (index and middle crossed), fingertips up, one on each side of the chin,
# palms turned in toward each other. Together (not alternating) they go up until the fingertips brush
# the sides of the chin and come down a little, about three times. (UFSC Signbank RECLAMAR. The INES
# RECLAMAR video shows another variant.)


def hs_reclamar_r():
    """R: index and middle straight and crossed (the index on the palm side, the middle behind it),
    ring and little fingers folded under the thumb."""
    shape = fist({'index': fing(-16, 12, 0, 0), 'middle': fing(16, -8, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['ring', 'pinky'])
    return shape


_rec_r = hs_reclamar_r()


def _rec_pose(dy):
    # Palm turned in toward the chin and a little toward the viewer, so the crossed fingers read.
    return P((182, 129 + dy), _rec_r, 'fingertips', yaw=0, pitch=0, roll=9, scale=0.95, depth=40,
             pole=(0.6, 1.0, 0.4))


_rec_up, _rec_down = _rec_pose(0), _rec_pose(14)
_rec_keys = [(0.0, [_rec_down, mirrored(_rec_down)]), (0.3, [_rec_down, mirrored(_rec_down)])]
for _rec_i in range(3):
    _rec_t = 0.3 + 0.5 * _rec_i
    _rec_keys += [(_rec_t + 0.25, [_rec_up, mirrored(_rec_up)]), (_rec_t + 0.5, [_rec_down, mirrored(_rec_down)])]
_rec_keys.append((2.4, [_rec_down, mirrored(_rec_down)]))
SIGNS['reclamar'] = {
    'poster': 0.55, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _rec_r,
    'keys': _rec_keys,
    'marks': [(174, 122, -50), (226, 122, 50)],
    'arrows': [{'d': 'M 146 162 L 146 136', 'both': True}, {'d': 'M 254 162 L 254 136', 'both': True}],
    'mirror_second': True,
}
TITLES['reclamar'] = 'Sinal de reclamar em Libras'
