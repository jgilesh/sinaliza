# SOLETRAR: open hand, fingers apart and a little curved, palm forward, in front of the shoulder on
# the signing side; the fingers wiggle one by one, as if typing, while the hand moves out to the side.
# (UFSC Signbank SOLETRAR: 5_claw, fingers wiggling, ipsilateral; INES SOLETRAR.)


def hs_soletrar(phase=None):
    """5 with the fingers a little curved; `phase` bends one finger more (the wiggle)."""
    base = {'index': (12, 14, 22), 'middle': (3, 14, 24), 'ring': (-7, 16, 24), 'pinky': (-15, 18, 26)}
    shape = {}
    for k, (n, (abd, mcp, pip)) in enumerate(base.items()):
        if phase is not None and k in phase:
            shape[n] = fing(abd, mcp + 30, pip + 28)
        else:
            shape[n] = fing(abd, mcp, pip)
    shape['thumb'] = (36.0, 18.0, 8.0, 8.0, 6.0)
    return shape


_soletrar_rest = hs_soletrar()
_soletrar_phases = [(3,), (2,), (1,), (0,), (3,), (2,)]
_soletrar_a, _soletrar_b = (150, 206), (106, 196)


def _soletrar_pose(at, shape, **kw):
    return P(at, shape, 'wrist', yaw=6, pitch=0, roll=-8, scale=1.05, depth=60, pole=(0.6, 1.0, 0.45), **kw)


_soletrar_keys = [(0.0, [_soletrar_pose(_soletrar_a, _soletrar_rest)]), (0.3, [_soletrar_pose(_soletrar_a, _soletrar_rest)])]
for _soletrar_i, _soletrar_ph in enumerate(_soletrar_phases, 1):
    _soletrar_u = _soletrar_i / len(_soletrar_phases)
    _soletrar_at = tuple(_soletrar_a[j] + (_soletrar_b[j] - _soletrar_a[j]) * _soletrar_u for j in range(2))
    _soletrar_keys.append((round(0.3 + 0.18 * _soletrar_i, 2),
                           [_soletrar_pose(_soletrar_at, hs_soletrar(_soletrar_ph), ease='linear')]))
_soletrar_end = round(0.3 + 0.18 * len(_soletrar_phases), 2)
_soletrar_keys += [(_soletrar_end + 0.2, [_soletrar_pose(_soletrar_b, _soletrar_rest)]),
                   (_soletrar_end + 0.6, [_soletrar_pose(_soletrar_b, _soletrar_rest)]),
                   (_soletrar_end + 1.1, [_soletrar_pose(_soletrar_a, _soletrar_rest)])]
SIGNS['soletrar'] = {
    'poster': 0.75, 'dur': _soletrar_end + 1.1, 'hands': ['right'], 'handshape': _soletrar_rest,
    'keys': _soletrar_keys,
    'arrows': [{'d': 'M 142 106 L 96 100'}],
}
TITLES['soletrar'] = 'Sinal de soletrar em Libras'
