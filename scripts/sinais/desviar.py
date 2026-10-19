# DESVIAR: the support hand lies open, palm up, in front of the chest. The signing hand, flat and on
# its edge (palm toward the other hand), slides forward over the support palm and then swerves out
# to its own side, turning to end palm up. Once. (UFSC Signbank DESVIAR: B on B, rubbing, forward,
# radial flexion. The INES DESVIAR video shows only the signing hand swerving to the side.)
_desviar_b = hs_B()


def hs_desviar_flat():
    """B with the thumb lying alongside the index (fingers and thumb together)."""
    shape = hs_B()
    shape['thumb'] = (-22.0, 18.0, 20.0, 8.0, 6.0)
    return shape


_desviar_f = hs_desviar_flat()
# Support hand (defined as a right hand, then mirrored): palm up, tilted toward the viewer so the
# palm shows, fingers pointing across toward the midline.
_desviar_base = mirrored(P((136, 238), _desviar_b, 'wrist', yaw=-55, pitch=0, roll=96, scale=1.05, depth=60))
# Signing hand on its edge on the support palm, fingers forward and leaning toward the other side.
_desviar_on = P((206, 236), _desviar_f, 'wrist', yaw=60, pitch=30, roll=25, scale=1.05, depth=55, pole=(0.4, 1.0, 0.4))
_desviar_fwd = P((206, 246), _desviar_f, 'wrist', yaw=60, pitch=30, roll=25, scale=1.15, depth=85, pole=(0.4, 1.0, 0.4),
                 ease='linear')
_desviar_out = P((124, 222), _desviar_f, 'wrist', yaw=45, pitch=20, roll=-85, scale=1.15, depth=85, pole=(0.5, 1.0, 0.4),
                 via=(160, 246))
_desviar_back = dict(_desviar_on, via=(170, 250), ease='smooth')
SIGNS['desviar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _desviar_f,
    'keys': [(0.0, [_desviar_on, _desviar_base]), (0.3, [_desviar_on, _desviar_base]),
             (0.6, [_desviar_fwd, _desviar_base]), (1.0, [_desviar_out, _desviar_base]),
             (1.8, [_desviar_out, _desviar_base]), (2.4, [_desviar_back, _desviar_base])],
    'arrows': [{'trail': 0, 'from': 0.3, 'to': 1.0, 'offset': (0, 34), 'trim': 0.08}],
    'mirror_second': True,
}
TITLES['desviar'] = 'Sinal de desviar em Libras'
