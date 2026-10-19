# APOIAR: the dominant fist with the thumb up stands on the palm of the other hand (flat, palm up).
# Both hands rise together in an arc toward the chin and then move forward, once, without losing
# contact. (UFSC Signbank APOIAR; the INES APOIAR1 video shows another variant.)


def hs_apoiar_thumb():
    """Fist with the thumb straight up, out to the side of the folded index (thumbs-up)."""
    shape = fist()
    shape['thumb'] = (40.0, 10.0, 0.0, 0.0, 0.0)
    return shape


_apoiar_t, _apoiar_b = hs_apoiar_thumb(), hs_B()


def _apoiar_pair(dx, dy, k=1.0, depth=0):
    """Dominant fist on the support palm; (dx, dy) moves both, k scales them (nearer the viewer)."""
    # Support hand (defined as a right hand, then mirrored): palm up and a little toward the viewer,
    # fingers across toward the midline.
    base = mirrored(P((140 - dx, 246 + dy), _apoiar_b, 'wrist', yaw=-45, pitch=0, roll=84, scale=1.05 * k,
                      depth=60 + depth))
    # Dominant: back of the fist to the viewer, thumb up, the wrist on the outer side.
    top = P((190 + dx, 224 + dy), _apoiar_t, 'wrist', yaw=150, pitch=0, roll=70, scale=1.05 * k, depth=66 + depth,
            pole=(0.35, 1.0, 0.4))
    return [top, base]


_apoiar_low = _apoiar_pair(0, -20)
_apoiar_high = _apoiar_pair(-4, -52)
_apoiar_fwd = _apoiar_pair(-8, -40, 1.15, 40)
SIGNS['apoiar'] = {
    'poster': 0.0, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _apoiar_t,
    'handshape_view': {'yaw': 30, 'roll': -60},
    'keys': [(0.0, _apoiar_low), (0.4, _apoiar_low), (0.9, _apoiar_high), (1.35, _apoiar_fwd), (2.0, _apoiar_fwd),
             (2.6, _apoiar_low)],
    # Up in an arc toward the chin (the forward part shows as the hands growing nearer).
    'arrows': [{'d': 'M 140 238 Q 118 186 150 156'}],
    'mirror_second': True,
}
TITLES['apoiar'] = 'Sinal de apoiar em Libras'
