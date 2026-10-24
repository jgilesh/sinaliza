# CASAR: both hands curved in C. The signing hand starts raised in front of its shoulder, palm forward,
# the other hand lower in front of the chest, palm up; the signing hand comes down toward the body,
# turning palm down, and the two hands clasp, the signing hand holding the other one. It stays.
# (UFSC Signbank CASAR: C+C, mão fraca: palma, contato final, proximal, pronação; INES agrees.)
_casar_c = hs_C()


def hs_casar_grip():
    """Clasping hand: fingers together and curled as around the other hand, thumb along the side."""
    return {'index': fing(2, 50, 60, 34), 'middle': fing(0, 52, 62, 36), 'ring': fing(-2, 54, 62, 36),
            'pinky': fing(-4, 56, 60, 34), 'thumb': (14.0, 30.0, 30.0, 10.0, 10.0)}


_casar_g = hs_casar_grip()
# Signing hand, raised: C seen from the thumb side, palm toward the midline and forward.
_casar_up = P((146, 176), _casar_c, 'wrist', yaw=55, pitch=0, roll=-8, scale=1.05, depth=60, pole=(0.45, 1.0, 0.4))
# Other hand (as a right hand, then mirrored): palm up, the C open upward, fingers toward the midline.
_casar_base = mirrored(P((168, 234), _casar_c, 'wrist', yaw=-70, pitch=-10, roll=84, scale=1.05, depth=70,
                         pole=(0.4, 1.0, 0.4)))
# Clasped: palm down over the other hand, fingers curled around its edge.
_casar_on = P((214, 222), _casar_g, 'fingertips', yaw=150, pitch=10, roll=96, scale=1.05, depth=80,
              via=(170, 196), pole=(0.45, 1.0, 0.4))
SIGNS['casar'] = {
    'poster': 1.2, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _casar_c, 'handshape_view': {'yaw': -60},
    'keys': [(0.0, [_casar_up, _casar_base]), (0.35, [_casar_up, _casar_base]), (0.95, [_casar_on, _casar_base]),
             (2.0, [_casar_on, _casar_base]), (2.6, [dict(_casar_up, via=(150, 220)), _casar_base])],
    'arrows': [{'d': 'M 120 176 Q 128 214 160 222'}],
    'mirror_second': True,
}
TITLES['casar'] = 'Sinal de casar em Libras'
