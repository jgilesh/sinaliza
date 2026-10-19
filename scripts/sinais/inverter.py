# INVERTER: both hands with the index straight (1), crossed in front of the chest, backs of the hands to
# the viewer: the dominant index points up, the other lies across it pointing to the side. The hands rise
# a little and turn together, ending crossed the other way round: the dominant index lying across, the
# other pointing up. Once. (UFSC Signbank INVERTER: 1/1; INES INVERTER.)
_inv_one = HANDSHAPES['1']()


def _inv_pose(at, roll, depth, ease='smooth'):
    """Right-hand pose (the left hand is the mirror of one): back of the hand to the viewer; roll 0 = index
    up, roll 90 = index pointing across to the viewer's right."""
    return P(at, _inv_one, 'index_tip', yaw=180, pitch=0, roll=roll, scale=1.1, depth=depth,
             pole=(0.3, 1.0, 0.45), ease=ease)


# Start: right index up; the left index lies across in front of it, pointing to the signer's right.
_inv_r0, _inv_l0 = _inv_pose((194, 168), 0, 60), mirrored(_inv_pose((230, 194), 90, 80))
# Halfway, a little higher: both turned to a diagonal X.
_inv_r1, _inv_l1 = _inv_pose((212, 158), 45, 70), mirrored(_inv_pose((212, 158), 45, 70))
# End: the left index up; the right index lies across in front of it, pointing to the signer's left.
_inv_r2, _inv_l2 = _inv_pose((230, 194), 90, 80), mirrored(_inv_pose((194, 168), 0, 60))
SIGNS['inverter'] = {
    'poster': 1.2, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _inv_one,
    'keys': [(0.0, [_inv_r0, _inv_l0]), (0.35, [_inv_r0, _inv_l0]), (0.75, [_inv_r1, _inv_l1]),
             (1.15, [_inv_r2, _inv_l2]), (1.95, [_inv_r2, _inv_l2]), (2.6, [_inv_r0, _inv_l0])],
    'arrows': [{'d': circle_arrow(200, 196, 52, 200, 330, True)}],
    'mirror_second': True,
}
TITLES['inverter'] = 'Sinal de inverter em Libras'
