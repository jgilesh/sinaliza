# COMER: flat hand, fingers together and up, held beside the mouth with the palm toward it (no
# contact); the fingers bend at the knuckles (90 degrees) toward the mouth, as if bringing food to
# it, two times. (UFSC Signbank COMER: B then B bent at the base; INES COMER.)


def hs_comer_bent():
    """B bent at the base: the four fingers stay straight and together and fold 90 degrees at the
    knuckles; the thumb stays alongside."""
    return {'index': fing(2, 82, 6, 4), 'middle': fing(0, 84, 6, 4), 'ring': fing(-2, 84, 6, 4),
            'pinky': fing(-4, 82, 8, 5), 'thumb': (-22.0, 18.0, 20.0, 8.0, 6.0)}


def hs_comer_flat():
    """B with the thumb resting alongside the index (as in the reference), not spread out."""
    shape = hs_B()
    shape['thumb'] = (-22.0, 18.0, 20.0, 8.0, 6.0)
    return shape


_comer_up, _comer_bent = hs_comer_flat(), hs_comer_bent()


def _comer_pose(shape):
    return P((150, 170), shape, 'wrist', yaw=44, pitch=-12, roll=-2, scale=1.1, depth=45, pole=(0.55, 1.0, 0.45))


_comer_a, _comer_b = _comer_pose(_comer_up), _comer_pose(_comer_bent)
SIGNS['comer'] = {
    'poster': 0.0, 'dur': 2.2, 'hands': ['right'], 'handshape': _comer_up,
    'keys': [(0.0, [_comer_a]), (0.3, [_comer_a]), (0.55, [_comer_b]), (0.8, [_comer_a]), (1.05, [_comer_b]),
             (1.3, [_comer_a]), (2.2, [_comer_a])],
    # The fingers fold over toward the mouth: a curved arrow from above the fingertips toward it.
    'arrows': [{'d': 'M 136 80 Q 164 74 172 106', 'both': False}],
}
TITLES['comer'] = 'Sinal de comer em Libras'
