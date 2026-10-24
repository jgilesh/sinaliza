# CUIDAR: the support hand is closed (S) and lies across in front of the chest, palm down, knuckles
# toward the signing side. The dominant hand in V (index and middle up and apart) stands on the support
# wrist, the V leaning toward the other side, and rocks there in small repeated movements, the eyes on
# the hands. (UFSC Signbank CUIDAR: V over the weak hand's wrist, double contact, alternating. The INES
# CUIDAR1 video shows another variant.)
_cuidar_v, _cuidar_s = hs_V(), hs_S()
# Support fist (defined as a right hand, then mirrored to the left): palm down, lying level in front of
# the chest, the knuckles pointing forward, toward the viewer (so the dominant forearm, which runs down
# to the signing side, does not hide it).
_cuidar_sup = mirrored(P((186, 234), _cuidar_s, 'wrist', yaw=0, pitch=100, roll=0, scale=1.15, depth=80,
                         pole=(0.3, 1.0, 0.3)))


def _cuidar_at(lift=0.0, lean=0.0, ease='smooth'):
    """V standing on the support wrist, palm turned toward the viewer and the midline, the V leaning
    toward the support side; `lift` raises it off the wrist, `lean` rocks it."""
    return P((210, 220 - lift), _cuidar_v, 'wrist', yaw=28, pitch=-6, roll=16 + lean, scale=1.08, depth=80,
             pole=(0.4, 1.0, 0.4), ease=ease)


_cuidar_keys = [(0.0, [_cuidar_at(), _cuidar_sup]), (0.3, [_cuidar_at(), _cuidar_sup])]
_cuidar_t = 0.3
for _cuidar_i in range(3):
    _cuidar_keys += [(_cuidar_t + 0.18, [_cuidar_at(7, -10), _cuidar_sup]),
                     (_cuidar_t + 0.36, [_cuidar_at(0, 0, 'in'), _cuidar_sup])]
    _cuidar_t += 0.36
_cuidar_keys.append((_cuidar_t + 0.6, [_cuidar_at(), _cuidar_sup]))
SIGNS['cuidar'] = {
    'poster': 0.3, 'dur': _cuidar_t + 0.6, 'hands': ['right', 'left'], 'handshape': _cuidar_v,
    'keys': _cuidar_keys,
    'marks': [(234, 226, 80)],
    'arrows': [{'d': 'M 196 168 Q 214 156 232 166', 'both': True}],
    'mirror_second': True,
}
TITLES['cuidar'] = 'Sinal de cuidar em Libras'
