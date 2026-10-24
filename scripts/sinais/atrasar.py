# ATRASAR: the support hand stands open (B), fingers up, palm toward the signing hand. The signing hand
# in L starts with the index up and the thumb tip on the support palm, palm forward; it turns about the
# thumb like a clock hand, the index sweeping forward and down along the support palm until it points
# down. Once. Worried face. (UFSC Signbank ATRASAR: L/B, weak hand's palm, continuous contact, arc,
# extension+flexion; INES ATRASAR agrees.)



def hs_atrasar_B():
    """Support hand: flat, fingers together, the thumb resting alongside the index."""
    return {'index': fing(2, 0, 0, 0), 'middle': fing(0, 0, 0, 0), 'ring': fing(-2, 0, 0, 0),
            'pinky': fing(-4, 0, 0, 0), 'thumb': (0.0, 14.0, 10.0, 6.0, 4.0)}


_atrasar_l, _atrasar_b = hs_L(), hs_atrasar_B()
_ATRASAR_PHI = math.radians(55)      # the support palm turns this far from "facing the viewer" toward the signing hand


def _atrasar_orient(f, n, guess):
    """yaw, pitch, roll of a right hand whose fingers point along f and whose palm faces n (screen)."""
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


# Support hand (defined as a right hand, then mirrored): fingers up, palm turned toward the signing
# hand and a good part toward the viewer, so the index can be seen sliding on it.
_atrasar_base = mirrored(P((178, 218), _atrasar_b, 'wrist', yaw=math.degrees(_ATRASAR_PHI), pitch=0, roll=-3, scale=1.0,
                           depth=60))
# Signing hand: the thumb points into the support palm (the turning axis), the index sweeps in the
# plane of that palm: from up, toward the viewer, to down (the wrist flexes).
_ATRASAR_X = (math.sin(_ATRASAR_PHI), 0.0, -math.cos(_ATRASAR_PHI))     # thumb direction
_ATRASAR_Z = (math.cos(_ATRASAR_PHI), 0.0, math.sin(_ATRASAR_PHI))      # palm normal at the start


def _atrasar_pose(theta, guess):
    c, s = math.cos(math.radians(theta)), math.sin(math.radians(theta))
    f = tuple(-c * u + s * v for u, v in zip((0.0, 1.0, 0.0), _ATRASAR_Z))
    n = tuple(c * v + s * u for u, v in zip((0.0, 1.0, 0.0), _ATRASAR_Z))
    q = _atrasar_orient(f, n, guess)
    return q, P((214, 196 + 8 * (1 - c) / 2), _atrasar_l, 'thumb_tip', yaw=q[0], pitch=q[1], roll=q[2], scale=1.0,
                depth=70, pole=(0.4, 1.0, 0.4), ease='linear')


_atrasar_poses, _atrasar_q = [], [-30.0, 0.0, 0.0]
for _atrasar_th in range(0, 181, 30):
    _atrasar_q, _atrasar_p = _atrasar_pose(_atrasar_th, _atrasar_q)
    _atrasar_poses.append(_atrasar_p)
_atrasar_keys = [(0.0, [_atrasar_poses[0], _atrasar_base]), (0.4, [_atrasar_poses[0], _atrasar_base])]
for _atrasar_k, _atrasar_p in enumerate(_atrasar_poses[1:], 1):
    _atrasar_keys.append((round(0.4 + 0.8 * _atrasar_k / (len(_atrasar_poses) - 1), 3), [_atrasar_p, _atrasar_base]))
_atrasar_keys += [(2.0, [_atrasar_poses[-1], _atrasar_base]), (2.6, [dict(_atrasar_poses[0], ease='smooth'), _atrasar_base])]
SIGNS['atrasar'] = {
    'poster': 0.0, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _atrasar_l,
    'keys': _atrasar_keys,
    'marks': [(214, 186, 10)],
    'arrows': [{'d': 'M 242 146 Q 292 202 230 264'}],
    'mirror_second': True,
}
TITLES['atrasar'] = 'Sinal de atrasar em Libras'
