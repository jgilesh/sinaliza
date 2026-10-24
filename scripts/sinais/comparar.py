# COMPARAR: both hands open, fingers together and a little curved, one on each side of the face, palms
# toward the signer, fingers up; they move forward and back in turn (one goes forward while the
# other comes back), a few times, like weighing two things. (UFSC Signbank COMPARAR: B curved,
# alternating; INES COMPARAR agrees.)


def hs_comparar_curved():
    """B curved: fingers together and curved a little at every joint, the thumb beside them."""
    return {'index': fing(2, 18, 32, 20), 'middle': fing(0, 18, 34, 22), 'ring': fing(-2, 20, 34, 22),
            'pinky': fing(-4, 22, 32, 20), 'thumb': (18.0, 22.0, 14.0, 8.0, 10.0)}


_comparar_c = hs_comparar_curved()


def _comparar_pose(fwd):
    """Right hand beside the face; fwd = 0 (back, near the body) .. 1 (forward): nearer, so bigger,
    and a little lower and outward."""
    return P((126 - 8 * fwd, 150 + 10 * fwd), _comparar_c, 'wrist', yaw=125, pitch=0, roll=-4,
             scale=0.94 + 0.22 * fwd, depth=30 + 60 * fwd, pole=(0.7, 1.0, 0.45))


_comparar_a = [_comparar_pose(1.0), mirrored(_comparar_pose(0.0))]   # right hand forward, left back
_comparar_b = [_comparar_pose(0.0), mirrored(_comparar_pose(1.0))]   # and the other way round
_comparar_keys = [(0.0, _comparar_a), (0.3, _comparar_a), (0.7, _comparar_b), (1.1, _comparar_a), (1.5, _comparar_b),
                  (1.9, _comparar_a), (2.4, _comparar_a)]
SIGNS['comparar'] = {
    'poster': 0.2, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _comparar_c, 'handshape_view': {'yaw': 60},
    'keys': _comparar_keys,
    # Forward and back (toward the viewer and away), below each hand.
    'arrows': [{'d': 'M 92 96 L 78 118', 'both': True}, {'d': 'M 308 96 L 322 118', 'both': True}],
    'mirror_second': True,
}
TITLES['comparar'] = 'Sinal de comparar em Libras'
