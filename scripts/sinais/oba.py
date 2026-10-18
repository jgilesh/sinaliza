# OBA: both hands flat (B, thumb alongside), fingers up, palms against each other in front of the chest;
# the palms rub quickly, one hand going up while the other goes down, a few times. (UFSC Signbank OBA.
# The INES OBA1 video shows another, one-handed variant.)


def hs_oba_B():
    """Flat hand, fingers together and straight, the thumb lying alongside the index."""
    shape = hs_B()
    shape['thumb'] = (-25.0, 0.0, 20.0, 5.0, 5.0)
    return shape


_oba_b = hs_oba_B()
# Palms toward each other but turned a little to the viewer (a narrow V that opens toward us), so both
# palms and all the fingers show; the hands touch along the thumb side, behind.
_oba = lambda dy: P((177, 254 + dy), _oba_b, 'wrist', yaw=62, pitch=0, roll=5, scale=1.25, depth=50)
_oba_up, _oba_dn, _oba_mid = _oba(-7), _oba(7), _oba(0)
_oba_keys = [(0.0, [_oba_mid, mirrored(_oba_mid)]), (0.3, [_oba_mid, mirrored(_oba_mid)])]
for _oba_k in range(4):   # four quick rubs: right up / left down, then the other way
    _oba_t = 0.45 + 0.3 * _oba_k
    _oba_a, _oba_c = (_oba_up, _oba_dn) if _oba_k % 2 == 0 else (_oba_dn, _oba_up)
    _oba_keys.append((_oba_t, [_oba_a, mirrored(_oba_c)]))
_oba_keys += [(1.6, [_oba_mid, mirrored(_oba_mid)]), (2.2, [_oba_mid, mirrored(_oba_mid)])]
SIGNS['oba'] = {
    'poster': 0.45, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _oba_b,
    'keys': _oba_keys,
    # Up-and-down beside each hand: the palms slide against each other.
    'arrows': [{'d': 'M 148 194 V 230', 'both': True}, {'d': 'M 252 194 V 230', 'both': True}],
    'mirror_second': True,
}
TITLES['oba'] = 'Sinal de oba em Libras'
