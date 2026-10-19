# CONVIDAR: both hands flat (B), palms up. They go together to the side opposite the signing hand
# at chest height and come back in an arc to the front of the waist, apart, palms still up, as if
# calling someone to come. Once. (UFSC Signbank CONVIDAR, INES CONVIDAR.)

_convidar_b = hs_B()
_CONVIDAR_TILT = math.radians(30)   # the palms tilt this much toward the viewer, so they show


def _convidar_orient(phi, guess):
    """yaw, pitch, roll of a palm-up right hand whose fingers point phi degrees from the viewer's
    right toward the viewer (phi 0 = to the right, 90 = at the viewer, 180 = to the left)."""
    n = (0.0, -math.cos(_CONVIDAR_TILT), math.sin(_CONVIDAR_TILT))
    c, s = math.cos(math.radians(phi)), math.sin(math.radians(phi))
    f = (c, s * math.sin(_CONVIDAR_TILT), s * math.cos(_CONVIDAR_TILT))

    def err(q):
        a, b = rot((0.0, -1.0, 0.0), *q), rot((0.0, 0.0, 1.0), *q)
        return sum((x - y) ** 2 for x, y in zip(a, f)) + sum((x - y) ** 2 for x, y in zip(b, n))
    q, e, step = list(guess), err(guess), 16.0
    while step > 0.05:
        better = False
        for i in range(3):
            for d in (step, -step):
                cand = q[:]
                cand[i] += d
                ec = err(cand)
                if ec < e:
                    q, e, better = cand, ec, True
        if not better:
            step /= 2
    return q


def _convidar_path(p0, via, p1, phi0, phi1, guess, n, depth=(80, 85)):
    """Right-hand poses along a curved path while the fingers swing from phi0 to phi1."""
    out = []
    for k in range(n + 1):
        u = k / n
        at = tuple((1 - u) ** 2 * p0[i] + 2 * (1 - u) * u * via[i] + u * u * p1[i] for i in range(2))
        guess = _convidar_orient(phi0 + (phi1 - phi0) * u, guess)
        out.append(P(at, _convidar_b, 'wrist', yaw=guess[0], pitch=guess[1], roll=guess[2], scale=1.08 + 0.04 * u,
                     depth=depth[0] + (depth[1] - depth[0]) * u, pole=(0.3, 1.0, 0.4), ease='linear'))
    return out


# Right hand: from the far side (fingers pointing that way) to the front of the waist (fingers
# forward and out). Left hand (defined as a right hand, then mirrored): from out on its own side,
# fingers pointing out, to the front of the waist.
_CONVIDAR_N = 6
_convidar_r = _convidar_path((208, 212), (206, 252), (160, 248), 0, 125, (-60, 10, 88), _CONVIDAR_N)
_convidar_l = _convidar_path((124, 206), (130, 240), (160, 248), 180, 125, (60, 10, -88), _CONVIDAR_N, (95, 85))
_convidar_keys = [(0.0, [_convidar_r[0], mirrored(_convidar_l[0])])]
for _convidar_k in range(_CONVIDAR_N + 1):
    _convidar_keys.append((round(0.4 + 0.7 * _convidar_k / _CONVIDAR_N, 3),
                           [_convidar_r[_convidar_k], mirrored(_convidar_l[_convidar_k])]))
_convidar_keys.append((1.9, _convidar_keys[-1][1]))
_convidar_keys.append((2.6, [dict(_convidar_r[0], ease='smooth', via=(196, 250)),
                             mirrored(dict(_convidar_l[0], ease='smooth', via=(136, 240)))]))
SIGNS['convidar'] = {
    'poster': 1.5, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _convidar_b,
    'keys': _convidar_keys,
    'arrows': [{'d': 'M 232 192 Q 150 178 120 222'}],
    'mirror_second': True,
}
TITLES['convidar'] = 'Sinal de convidar em Libras'
