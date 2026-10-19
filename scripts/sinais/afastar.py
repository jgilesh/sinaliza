# AFASTAR: both hands flat (B), fingers up, together in front of the chin: the support hand palm
# forward, the signing hand beside it, palm turned in toward it. The signing hand stays; the support
# hand moves away, straight forward and out to the side, as if pushed away. Once.
# (UFSC Signbank AFASTAR. The INES AFASTAR1 video shows another variant.)
def hs_afastar_flat():
    """B: flat hand, fingers together, the thumb along the side of the index (kept in, so it never
    crosses over the other hand)."""
    return {'index': fing(2, 0, 0, 0), 'middle': fing(0, 0, 0, 0), 'ring': fing(-2, 0, 0, 0),
            'pinky': fing(-4, 0, 0, 0), 'thumb': (-18.0, 4.0, 10.0, 4.0, 4.0)}


_afa_b = hs_afastar_flat()
# Signing hand: palm turned in toward the support hand (and a little to the viewer), fingers up.
_afa_dom = P((176, 226), _afa_b, 'wrist', yaw=70, pitch=0, roll=4, scale=1.05, depth=60, pole=(0.5, 1.0, 0.4))
# Support hand (defined as a right hand, then mirrored): palm forward, fingers up, its thumb edge
# against the signing hand's palm.
_afa_near = mirrored(P((172, 228), _afa_b, 'wrist', yaw=-8, pitch=0, roll=-4, scale=1.05, depth=60))
_afa_far = mirrored(P((126, 216), _afa_b, 'wrist', yaw=-8, pitch=0, roll=-10, scale=1.25, depth=110, ease='out'))
SIGNS['afastar'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _afa_b,
    'keys': [(0.0, [_afa_dom, _afa_near]), (0.4, [_afa_dom, _afa_near]), (1.0, [_afa_dom, _afa_far]),
             (1.9, [_afa_dom, _afa_far]), (2.4, [_afa_dom, dict(_afa_near, ease='smooth')])],
    'arrows': [{'d': 'M 238 246 L 282 236'}],
    'mirror_second': True,
}
TITLES['afastar'] = 'Sinal de afastar em Libras'
