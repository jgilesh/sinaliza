# CUIDADO: both open hands (5), palms forward, in front of the chest, make small alternating circles
# forward and back (one hand rises while the other drops), several times. No contact. (INES and UFSC
# Signbank agree.)
_cui_5 = hs_5()
_CUI_C, _CUI_RY, _CUI_RX = (142, 222), 20, 5


def _cui_pose(angle):
    """Right hand on its circle; angle 0 = top, the hand comes forward over the top (sagittal circle,
    seen from the front as an up-and-down path that grows when the hand is nearer)."""
    a = math.radians(angle)
    at = (_CUI_C[0] + _CUI_RX * math.sin(a), _CUI_C[1] - _CUI_RY * math.cos(a))
    near = math.sin(a)          # +1 = nearest the viewer
    return P(at, _cui_5, 'wrist', yaw=-6, pitch=-8 * near, roll=-6, scale=1.08 + 0.06 * near, depth=60 + 18 * near,
             pole=(0.4, 1.0, 0.4), ease='linear')


_cui_keys = []
_n = 24
for _k in range(_n + 1):
    _ang = 360.0 * 2 * _k / _n
    _cui_keys.append((0.1 + 2.0 * _k / _n, [_cui_pose(_ang), mirrored(_cui_pose(_ang + 180))]))
_cui_keys = [(0.0, _cui_keys[0][1])] + _cui_keys + [(2.5, _cui_keys[-1][1])]
SIGNS['cuidado'] = {
    'poster': 0.1, 'dur': 2.5, 'hands': ['right', 'left'], 'handshape': _cui_5, 'mirror_second': True,
    'keys': _cui_keys,
    'arrows': [{'d': 'M 96 236 Q 84 202 98 172'}, {'d': 'M 304 172 Q 316 202 302 236'}],
}
TITLES['cuidado'] = 'Sinal de cuidado em Libras'
