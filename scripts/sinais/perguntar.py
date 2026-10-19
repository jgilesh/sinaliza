# PERGUNTAR: the support hand stands open and upright in front of the chest, palm toward the signing
# hand. The signing index (others folded) starts at the mouth, then comes forward and down and lies
# across the support palm, pointing up and in. Once. (UFSC Signbank PERGUNTAR: 1 on the weak hand's
# palm (B); the INES PERGUNTAR video shows another variant.)

_perguntar_1, _perguntar_b = hs_1(), hs_B()
# Support hand, defined as a right hand (fingers up, palm toward the midline, turned a little to
# the viewer) and mirrored.
_perguntar_sup = mirrored(P((166, 244), _perguntar_b, 'wrist', yaw=50, pitch=0, roll=-4, scale=1.05, depth=60))
# Index at the mouth: back of the hand to the viewer, fingertip at the lower lip.
_perguntar_mouth = P((194, 132), _perguntar_1, 'index_tip', yaw=150, pitch=-10, roll=8, scale=1.0, depth=40,
                     pole=(0.4, 1.0, 0.45))
# On the support palm: the index lying across it, pointing up and in; back of the hand to the viewer.
_perguntar_on = P((222, 186), _perguntar_1, 'index_tip', yaw=145, pitch=0, roll=50, scale=1.05, depth=64,
                  pole=(0.35, 1.0, 0.4), ease='out', via=(176, 190))
SIGNS['perguntar'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _perguntar_1,
    'keys': [(0.0, [_perguntar_mouth, _perguntar_sup]), (0.35, [_perguntar_mouth, _perguntar_sup]),
             (0.85, [_perguntar_on, _perguntar_sup]), (1.8, [_perguntar_on, _perguntar_sup]),
             (2.4, [dict(_perguntar_mouth, ease='smooth'), _perguntar_sup])],
    'marks': [(226, 200, 40)],
    'arrows': [{'d': 'M 172 130 Q 150 160 170 196'}],
    'mirror_second': True,
}
TITLES['perguntar'] = 'Sinal de perguntar em Libras'
