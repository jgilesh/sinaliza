# CONVERSAR: both hands flat (B), palms down, one above the other in front of the chest, the fingers
# pointing across the body; they turn alternately around each other, the upper hand rolling forward
# and down while the lower one comes back and up, several times. (UFSC Signbank CONVERSAR and INES
# CONVERSAR agree.)


def hs_conversar_flat():
    """Flat hand, fingers together and straight, the thumb resting along the index."""
    return {'index': fing(2, 0, 0, 0), 'middle': fing(0, 0, 0, 0), 'ring': fing(-2, 0, 0, 0),
            'pinky': fing(-4, 0, 0, 0), 'thumb': (-10.0, 12.0, 10.0, 4.0, 4.0)}


_conversar_b = hs_conversar_flat()
_CONV_CY, _CONV_RY, _CONV_RZ = 220.0, 11.0, 14.0


def _conversar_pose(phase, x, d0):
    """Right hand at `phase` on its roll (0 = top, 90 = front, 180 = bottom, 270 = back): palm down,
    the back of the hand tipped toward the viewer, fingers toward the midline."""
    p = math.radians(phase)
    depth = d0 + _CONV_RZ * math.sin(p)
    return P((x, _CONV_CY - _CONV_RY * math.cos(p)), _conversar_b, 'wrist', yaw=132, pitch=0, roll=92,
             scale=1.08 + 0.004 * (depth - d0), depth=depth, pole=(0.45, 1.0, 0.3), ease='linear')


# The right hand rolls a little in front of the left one, so wherever they pass each other the right
# hand is the nearer one (the drawing order stays true).
_conv_keys = []
_conv_n = 16
for _conv_i in range(_conv_n + 1):
    _conv_p = 360.0 * 2 * _conv_i / _conv_n
    _conv_keys.append((0.25 + 1.9 * _conv_i / _conv_n,
                       [_conversar_pose(_conv_p, 150, 78), mirrored(_conversar_pose(_conv_p + 180, 150, 58))]))
_conv_keys = [(0.0, _conv_keys[0][1])] + _conv_keys + [(2.6, _conv_keys[-1][1])]
SIGNS['conversar'] = {
    'poster': 0.25, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _conversar_b,
    'keys': _conv_keys,
    # Rolling circles on the outer side of each hand.
    'arrows': [{'d': circle_arrow(118, 222, 13, 200, 120, True)},
               {'d': circle_arrow(282, 222, 13, 340, 60, False)}],
    'mirror_second': True,
}
TITLES['conversar'] = 'Sinal de conversar em Libras'
