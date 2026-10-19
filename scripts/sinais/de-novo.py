# DE NOVO (repetir): L hand (index up, thumb out) beside the shoulder on the signing side, palm turned
# toward the body and the midline. The wrist turns quickly forward and down until the index points at the floor, palm
# down, thumb toward the midline. Once. (UFSC Signbank DE-NOVO: L, downward with pronation. The INES
# REPETIR video shows the same movement, signed with the left hand.)

_denovo_l = hs_L()
_denovo_pole = (0.6, 1.0, 0.4)
# Beside the shoulder: index up, palm toward the body and the midline, thumb out to the side.
_denovo_up = P((134, 180), _denovo_l, 'wrist', yaw=160, pitch=0, roll=-2, scale=1.1, depth=50, pole=_denovo_pole)
# Halfway: the index points forward, toward the viewer.
_denovo_mid = P((142, 202), _denovo_l, 'wrist', yaw=170, pitch=70, roll=-90, scale=1.12, depth=95, pole=_denovo_pole,
                ease='in')
# Down: the index points at the floor (and a little forward), palm down, thumb toward the midline; the
# elbow out to the side, so the forearm comes in level from the side.
_denovo_down = P((150, 216), _denovo_l, 'wrist', yaw=180, pitch=30, roll=-180, scale=1.12, depth=90,
                 pole=(1.0, 0.1, 0.0), ease='out')
SIGNS['de-novo'] = {
    'poster': 0.2, 'dur': 2.2, 'hands': ['right'], 'handshape': _denovo_l,
    'keys': [(0.0, [_denovo_up]), (0.35, [_denovo_up]), (0.55, [_denovo_mid]), (0.75, [_denovo_down]),
             (1.6, [_denovo_down]), (2.2, [dict(_denovo_up, ease='smooth')])],
    # Outside the hand: forward and down, turning.
    'arrows': [{'d': 'M 86 116 Q 68 178 96 238'}],
}
TITLES['de-novo'] = 'Sinal de de novo em Libras'
