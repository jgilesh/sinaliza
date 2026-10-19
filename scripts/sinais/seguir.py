# SEGUIR: both hands in A (fist, thumb up), palms toward the signer's left, one just behind the
# other in front of the chin: the knuckles of the signing hand rest on the back of the other hand.
# Together, without separating, they move forward and down to in front of the chest. Once.
# (UFSC Signbank SEGUIR, INES SEGUIR.)



def hs_seguir_up():
    """A as in a thumbs-up: fingers folded into a fist, the thumb straight and raised from the side of
    the index, pointing away from the fist."""
    shape = fist()
    shape['thumb'] = (36.0, 4.0, 0.0, 2.0, 0.0)
    return shape


_seg_a = hs_seguir_up()
_seg_pole = (0.4, 1.0, 0.45)


def _seg_pair(dx, dy, scale, depth):
    """Both hands, side by side; the left hand is given as a right-hand pose and mirrored."""
    # Signing hand: palm toward the other hand, turned a little to the viewer, so the folded fingers
    # and the raised thumb read.
    right = P((181 + dx, 184 + dy), _seg_a, 'wrist', yaw=40, pitch=40, roll=-55, scale=scale, depth=depth,
              pole=_seg_pole)
    # Leading hand: palm the same way (away from the signing hand), its back toward it.
    left = mirrored(P((178 - dx, 184 + dy), _seg_a, 'wrist', yaw=145, pitch=35, roll=58, scale=scale,
                      depth=depth, pole=_seg_pole))
    return [right, left]


_seg_on, _seg_off = _seg_pair(0, 0, 1.05, 45), _seg_pair(0, 46, 1.2, 95)
_seg_back = [dict(_seg_on[0], via=(176, 250)), dict(_seg_on[1], via=(224, 250))]
SIGNS['seguir'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _seg_a, 'handshape_view': {'yaw': 40, 'pitch': 40, 'roll': -55},
    'keys': [(0.0, _seg_on), (0.4, _seg_on), (1.1, _seg_off), (1.9, _seg_off), (2.4, _seg_back)],
    # Beside the hands: forward and down, together.
    'arrows': [{'d': 'M 256 160 Q 270 186 260 216'}],
    'mirror_second': True,
}
TITLES['seguir'] = 'Sinal de seguir em Libras'
