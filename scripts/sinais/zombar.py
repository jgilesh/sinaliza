# ZOMBAR: both hands in L (thumb and index out), palms facing each other in front of the chest and
# shoulders, index fingers up. In turn, each wrist bends so the index tips forward, toward the person
# being mocked, and comes back, several times. (UFSC Signbank ZOMBAR: L/L, forward, alternating, wrist
# extension. The INES ZOMBAR video shows another variant.)
_zom_l = hs_L()


def _zom_pose(fwd, ease='smooth'):
    # Right hand (the left mirrors it): palm toward the midline and turned toward the viewer, so the index
    # and the thumb both read; forward = the index tips toward the viewer (pitch).
    return P((140, 230), _zom_l, 'wrist', yaw=45, pitch=60 if fwd else 0, roll=0 if fwd else 4, scale=1.1,
             depth=62 if fwd else 55, pole=(0.4, 1.0, 0.4), ease=ease)


_zom_up, _zom_fwd = _zom_pose(False), _zom_pose(True, 'out')
_zom_keys = [(0.0, [_zom_up, mirrored(_zom_up)]), (0.3, [_zom_up, mirrored(_zom_up)])]
_zom_t = 0.3
for _zom_i in range(4):   # right, left, right, left
    _zom_t += 0.2
    r, l = (_zom_fwd, _zom_up) if _zom_i % 2 == 0 else (_zom_up, _zom_fwd)
    _zom_keys.append((round(_zom_t, 2), [r, mirrored(l)]))
    _zom_t += 0.2
    _zom_keys.append((round(_zom_t, 2), [dict(_zom_up, ease='smooth'), mirrored(dict(_zom_up, ease='smooth'))]))
_zom_keys.append((2.2, [_zom_up, mirrored(_zom_up)]))
SIGNS['zombar'] = {
    'poster': 0.5, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _zom_l,
    'keys': _zom_keys,
    'arrows': [{'d': 'M 128 150 Q 116 156 114 172'}, {'d': 'M 272 150 Q 284 156 286 172'}],
    'mirror_second': True,
}
TITLES['zombar'] = 'Sinal de zombar em Libras'
