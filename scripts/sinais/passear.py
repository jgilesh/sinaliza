# PASSEAR: both hands flat (B), palms down, up beside the shoulders, fingers pointing in toward the
# neck; the hands flap up and down from the wrist in turn (one rises while the other drops), 3 times,
# body relaxed. (UFSC Signbank PASSEAR: B/B, shoulders, alternating; INES PASSEAR.)

_passear_b = hs_B()
_passear_b['thumb'] = (-22.0, 18.0, 20.0, 8.0, 6.0)   # thumb alongside the index
_passear_pole = (0.9, 0.6, 0.3)


def _passear_pose(lift):
    """Right hand beside the shoulder, palm down (the back seen a little from above), fingers in;
    lift > 0 raises the fingertips (wrist bending back)."""
    return P((110, 184 - lift * 0.25), _passear_b, 'wrist', yaw=140, pitch=-15, roll=88 - lift, scale=0.88, depth=40,
             pole=_passear_pole)


_passear_hi, _passear_lo = _passear_pose(30), _passear_pose(0)
_passear_keys = [(0.0, [_passear_lo, mirrored(_passear_lo)]), (0.25, [_passear_lo, mirrored(_passear_lo)])]
for _passear_k in range(6):
    _passear_a, _passear_z = (_passear_hi, _passear_lo) if _passear_k % 2 == 0 else (_passear_lo, _passear_hi)
    _passear_keys.append((round(0.5 + 0.3 * _passear_k, 2), [_passear_a, mirrored(_passear_z)]))
_passear_keys += [(2.5, [_passear_lo, mirrored(_passear_lo)]), (2.8, [_passear_lo, mirrored(_passear_lo)])]
SIGNS['passear'] = {
    'poster': 0.5, 'dur': 2.8, 'hands': ['right', 'left'], 'handshape': _passear_b,
    'keys': _passear_keys,
    'arrows': [{'d': circle_arrow(110, 184, 82, -40, -8, True), 'both': True},
               {'d': circle_arrow(290, 184, 82, 188, 220, True), 'both': True}],
    'mirror_second': True,
}
TITLES['passear'] = 'Sinal de passear em Libras'
