# MOSTRAR: the dominant hand open, fingers together and the thumb apart, palm forward, at face height
# beside the face; the index of the other hand points at the heel of that palm. Both move forward a
# little together, once. (UFSC Signbank MOSTRAR: 5 and 1; INES MOSTRAR1 agrees, on the other side.)


def hs_mostrar_open():
    """Flat hand, fingers together, thumb well apart in the palm plane."""
    shape = hs_B()
    shape['thumb'] = (32.0, 12.0, 4.0, 4.0, 2.0)
    return shape


_mostrar_open, _mostrar_1 = hs_mostrar_open(), hs_1()


def _mostrar_pair(fwd):
    """fwd = 0 (start) .. 1 (moved forward): a little bigger and nearer, drifting out and down."""
    hand = P((138 - 6 * fwd, 158 + 6 * fwd), _mostrar_open, 'wrist', yaw=8, pitch=0, roll=-6,
             scale=1.02 + 0.1 * fwd, depth=40 + 35 * fwd, pole=(0.6, 1.0, 0.45))
    # The other index (a right-hand pose, mirrored) comes across and points up at the heel of the palm.
    point = mirrored(P((257 + 6 * fwd, 150 + 6 * fwd), _mostrar_1, 'index_tip', yaw=-15, pitch=0, roll=48,
                       scale=1.02 + 0.1 * fwd, depth=55 + 35 * fwd))
    return [hand, point]


_mostrar_a, _mostrar_z = _mostrar_pair(0), _mostrar_pair(1)
SIGNS['mostrar'] = {
    # The pointing hand is drawn in front of the open hand (no 'mirror_second').
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _mostrar_open,
    'keys': [(0.0, [_mostrar_a[0], _mostrar_a[1]]), (0.3, _mostrar_a), (0.9, _mostrar_z), (1.8, _mostrar_z),
             (2.4, _mostrar_a)],
    # Forward (toward the viewer): out and down beside the open hand.
    'arrows': [{'d': 'M 96 130 L 84 150'}],
}
TITLES['mostrar'] = 'Sinal de mostrar em Libras'
