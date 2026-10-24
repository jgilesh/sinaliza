# LUTAR: the support hand stands open in front of its shoulder, fingers together and pointing up and
# across, thumb up, palm toward the dominant hand. The dominant fist with the thumb up (A), palm to the
# other side, goes up to the chin (below the mouth, keeping the face clear) and down to the stomach, brushing past the support palm
# each time, 2 to 3 times. (UFSC Signbank BATALHAR "batalhar, lutar": S on B, mão fraca palma, contato
# duplo. The INES LUTAR1 video shows another variant, with V hands.)


def hs_lutar_thumb():
    """A with the thumb clearly up: fist, the thumb straight and out beside the folded index."""
    shape = fist()
    shape['thumb'] = (40.0, 10.0, 0.0, 0.0, 0.0)
    return shape


_lut_a, _lut_b = hs_lutar_thumb(), hs_B()
# Support hand (written as a right hand, then mirrored): palm toward the midline and a little toward
# the viewer, fingers up and leaning in, thumb up.
_lut_base = mirrored(P((156, 222), _lut_b, 'wrist', yaw=62, pitch=0, roll=24, scale=1.05, depth=60))
# Dominant fist: thumb straight up on top, knuckles toward the support hand and turned a little to the
# viewer (back of the hand mostly to the viewer, palm to the other side), just in front of the support palm.
_lut_pose = lambda y, **kw: P((168, y), _lut_a, 'wrist', yaw=160, pitch=0, roll=88, scale=1.05, depth=72,
                              pole=(0.35, 1.0, 0.4), **kw)
_lut_up, _lut_down = _lut_pose(190), _lut_pose(270)
_lut_keys = [(0.0, [_lut_up, _lut_base]), (0.3, [_lut_up, _lut_base])]
for _lut_i in range(3):
    _lut_keys += [(0.3 + 0.6 * _lut_i + 0.3, [_lut_down, _lut_base]), (0.3 + 0.6 * _lut_i + 0.6, [_lut_up, _lut_base])]
_lut_keys.append((2.5, [_lut_up, _lut_base]))
SIGNS['lutar'] = {
    'poster': 0.6, 'dur': 2.5, 'hands': ['right', 'left'], 'handshape': _lut_a, 'handshape_view': {'yaw': 30, 'roll': -60},
    'keys': _lut_keys,
    # Up and down beside the dominant fist; the brush on the support palm.
    'arrows': [{'d': 'M 136 150 L 136 250', 'both': True}],
    'marks': [(214, 196, -40)],
    'mirror_second': True,
}
TITLES['lutar'] = 'Sinal de lutar em Libras'
