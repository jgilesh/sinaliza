# QUANDO: hand raised beside the face at shoulder height, palm forward, index up (1). The thumb opens to
# the side, pointing at the face (L), then the index folds into the palm: the hand ends closed with only
# the thumb out toward the face, and holds a moment. Question face (INES QUANDO1).


def hs_quando_end():
    """Fist with the thumb straight out to the side in the palm plane (the L without its index)."""
    return fist({'thumb': (48.0, 8.0, 0.0, 4.0, 2.0)})


qd_one, qd_l, qd_end = hs_1(), hs_L(), hs_quando_end()
qd_pose = lambda at, shape, scale=1.08: P(at, shape, 'wrist', yaw=8, pitch=0, roll=-6, scale=scale, depth=55,
                                          pole=(0.7, 1.0, 0.3))
QD_AT = (116, 168)
qd_low = qd_pose((112, 196), qd_one, 1.0)
SIGNS['quando'] = {
    'poster': 0.8, 'dur': 2.4, 'hands': ['right'], 'handshape': qd_end,
    'keys': [(0.0, [qd_low]), (0.35, [qd_pose(QD_AT, qd_one)]), (0.55, [qd_pose(QD_AT, qd_one)]),
             (0.72, [qd_pose(QD_AT, qd_l)]), (0.85, [qd_pose(QD_AT, qd_l)]), (1.0, [dict(qd_pose(QD_AT, qd_end), ease='out')]),
             (1.8, [qd_pose(QD_AT, qd_end)]), (2.4, [qd_low])],
    # The index folds down into the palm (on its outer side, clear of the face).
    'arrows': [{'d': 'M 96 92 Q 88 112 98 128'}],
}
TITLES['quando'] = 'Sinal de quando em Libras'
