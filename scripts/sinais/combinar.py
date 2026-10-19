# COMBINAR: the support hand is flat with the fingers up, in front of its own shoulder, palm facing
# the dominant hand. The dominant index (others folded) starts with its tip on the chin, then stands
# up in front of the chest and tips over from the wrist until its tip touches the support palm;
# it stands up again and touches again, 3 touches in all. (UFSC Signbank COMBINAR; INES COMBINAR1
# ends with the index touching an upturned palm.)


def hs_combinar_b():
    """B with the thumb resting along the side of the index."""
    shape = hs_B()
    shape['thumb'] = (8.0, 12.0, 8.0, 6.0, 4.0)
    return shape


_combinar_1, _combinar_b = hs_1(), hs_combinar_b()
# Support hand (defined as a right hand, then mirrored): fingers up, palm turned toward the
# midline and a little toward the viewer.
_combinar_sup = mirrored(P((160, 240), _combinar_b, 'wrist', yaw=45, pitch=0, roll=-4, scale=1.0, depth=60))
# Index on the chin: back of the hand to the viewer, the fingertip on the chin.
_combinar_chin = P((193, 142), _combinar_1, 'index_tip', yaw=150, pitch=-10, roll=8, scale=1.0, depth=40,
                   pole=(0.4, 1.0, 0.45))


def _combinar_idx(roll):
    """Index standing on the wrist in front of the chest; roll tips it toward the support palm."""
    return P((186, 238), _combinar_1, 'wrist', yaw=140, pitch=0, roll=roll, scale=1.0, depth=62,
             pole=(0.35, 1.0, 0.4))


_combinar_up, _combinar_touch = _combinar_idx(-4), _combinar_idx(52)
_combinar_keys = [(0.0, _combinar_chin), (0.3, _combinar_chin), (0.6, _combinar_up)]
for _combinar_t in (0.8, 1.1, 1.4):
    _combinar_keys += [(_combinar_t, _combinar_touch), (_combinar_t + 0.15, _combinar_up)]
_combinar_keys += [(2.0, _combinar_up), (2.4, _combinar_chin)]
SIGNS['combinar'] = {
    'poster': 0.8, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _combinar_1,
    'keys': [(t, [p, _combinar_sup]) for t, p in _combinar_keys],
    'marks': [(192, 143, 200)],
    # The index tips over from the wrist to the support palm and back (two heads: it repeats).
    'arrows': [{'d': circle_arrow(186, 238, 88, -76, -55, True), 'both': True}],
    'mirror_second': True,
}
TITLES['combinar'] = 'Sinal de combinar em Libras'
