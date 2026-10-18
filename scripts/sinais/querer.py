# QUERER: clawed open hand, palm up, in front of the chest on the dominant side; the fingers bend
# and stretch two or three times while the hand pulls a little toward the body.


def hs_querer_claw(k=1.0):
    """5 claw: fingers spread and curved (bent at the middle and end joints, a little at the
    knuckles), the thumb out to the side and curved too. k = how much they bend (0..1)."""
    return {'index': fing(13, 18 * k, 70 * k, 45 * k), 'middle': fing(3, 18 * k, 72 * k, 46 * k),
            'ring': fing(-7, 20 * k, 70 * k, 45 * k), 'pinky': fing(-17, 22 * k, 66 * k, 42 * k),
            'thumb': (45.0, 5.0, 10.0, 10.0 + 15 * k, 10.0 + 25 * k)}


_quer_claw, _quer_open = hs_querer_claw(1.0), hs_querer_claw(0.6)
_quer = lambda shape, at, depth: P(at, shape, 'wrist', yaw=-25, pitch=45, roll=155, scale=1.12, depth=depth,
                                   pole=(0.5, 1.0, 0.4))
_quer_a = _quer(_quer_open, (140, 192), 85)
_quer_b = _quer(_quer_claw, (146, 190), 72)
_quer_c = _quer(_quer_open, (144, 191), 78)
_quer_d = _quer(_quer_claw, (150, 189), 64)
_quer_e = _quer(_quer_open, (148, 190), 70)
_quer_f = _quer(_quer_claw, (154, 188), 58)
SIGNS['querer'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right'], 'handshape': _quer_claw,
    'handshape_view': {'yaw': 45},
    'keys': [(0.0, [_quer_a]), (0.3, [_quer_a]), (0.5, [_quer_b]), (0.7, [_quer_c]), (0.9, [_quer_d]),
             (1.1, [_quer_e]), (1.3, [_quer_f]), (1.9, [_quer_f]), (2.4, [_quer_a])],
    # Beside the fingertips: the fingers bend and stretch (repeated).
    'arrows': [{'d': 'M 194 220 Q 206 207 196 192', 'both': True}],
}
TITLES['querer'] = 'Sinal de querer em Libras'
