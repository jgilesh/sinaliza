# DESCONFIAR: both hands open with the fingers together and a little curved. The non-signing hand is
# raised beside the head, palm forward; the signing hand is in front of the chest, palm up. The two
# make small alternating moves back and forth (one comes forward while the other goes back), a few
# times. (UFSC Signbank DESCONFIAR, which puts the raised hand on the non-signing side.)


def hs_desconfiar_bc():
    """Curved B: four fingers together, a little bent at every joint; the thumb alongside."""
    return {'index': fing(2, 12, 22, 14), 'middle': fing(0, 12, 24, 15), 'ring': fing(-2, 13, 24, 15),
            'pinky': fing(-4, 15, 22, 14), 'thumb': (10.0, 20.0, 15.0, 8.0, 8.0)}


_desc_b = hs_desconfiar_bc()
_desc_pole = (0.4, 1.0, 0.45)


def _desc_low(fwd):
    """Signing hand in front of the chest, palm up, fingers toward the midline and up; fwd = 0..1."""
    return P((176 - 4 * fwd, 230 + 6 * fwd), _desc_b, 'wrist', yaw=-50, pitch=0, roll=68,
             scale=1.08 + 0.1 * fwd, depth=55 + 35 * fwd, pole=_desc_pole)


def _desc_high(fwd):
    """Other hand raised beside the head, palm forward (a right-hand pose, mirrored)."""
    return mirrored(P((124 - 3 * fwd, 112 + 4 * fwd), _desc_b, 'wrist', yaw=8, pitch=0, roll=-4,
                      scale=1.02 + 0.1 * fwd, depth=30 + 35 * fwd, pole=(0.6, 1.0, 0.45)))


_desc_a = [_desc_low(1.0), _desc_high(0.0)]   # signing hand forward, raised hand back
_desc_z = [_desc_low(0.0), _desc_high(1.0)]   # and the other way round
_desc_keys = [(0.0, _desc_a), (0.3, _desc_a)]
for _desc_k in range(4):
    _desc_keys.append((round(0.6 + 0.3 * _desc_k, 2), _desc_z if _desc_k % 2 == 0 else _desc_a))
_desc_keys.append((2.2, _desc_a))
SIGNS['desconfiar'] = {
    'poster': 0.3, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _desc_b, 'handshape_view': {'yaw': -35},
    'keys': _desc_keys,
    'mirror_second': True,
    # Short back-and-forth arrows beside each hand (toward and away from the viewer).
    'arrows': [{'d': 'M 132 222 L 118 240', 'both': True}, {'d': 'M 306 62 L 318 78', 'both': True}],
}
TITLES['desconfiar'] = 'Sinal de desconfiar em Libras'
