# ACUSAR: hand in 4 (four fingers straight and apart, thumb folded on the palm), upright, the index
# side against the nose, palm toward the midline; the hand leaves the nose down and forward, toward the
# person being accused, the fingers tipping forward. Once. (UFSC Signbank ACUSAR: 4, nariz, contato
# inicial, para baixo e para a frente, direcional; INES ACUSAR agrees.)


def hs_acusar_4():
    """4: index, middle, ring and little fingers straight and spread; the thumb folded across the palm,
    its pad on the palm below the ring finger."""
    shape = {'index': fing(10, 0, 2, 1), 'middle': fing(2, 0, 2, 1), 'ring': fing(-7, 0, 2, 1),
             'pinky': fing(-16, 0, 3, 2)}
    target = (-3.0, -20.0, PALM_HALF_THICKNESS + seg_radius('thumb', 2) + 0.6)
    shape['thumb'] = solve_thumb(target, pad_to=(0.0, 0.0, -1.0), point=(-1.0, -0.6, 0.0),
                                 pref=(-15.0, 50.0, 60.0, 30.0, 30.0), w_point=120.0)
    return shape


_acusar_4 = hs_acusar_4()
# On the nose: the hand upright beside the nose on the signing side, palm turned toward the midline and
# the viewer, so the four spread fingers read; the side of the index against the nose.
_acusar_on = P((192, 82), _acusar_4, 'index_tip', yaw=30, pitch=0, roll=-14, scale=0.95, depth=35,
               pole=(0.45, 1.0, 0.5))
# Out: down and forward, toward the other person, the fingertips tipping toward the viewer.
_acusar_off = P((166, 214), _acusar_4, 'wrist', yaw=35, pitch=28, roll=-8, scale=1.15, depth=95,
                pole=(0.45, 1.0, 0.45), via=(160, 160), ease='out')
SIGNS['acusar'] = {
    'poster': 0.0, 'dur': 2.2, 'hands': ['right'], 'handshape': _acusar_4, 'handshape_view': {'yaw': 10},
    'keys': [(0.0, [_acusar_on]), (0.4, [_acusar_on]), (0.95, [_acusar_off]), (1.6, [_acusar_off]),
             (2.2, [dict(_acusar_on, via=(150, 170), ease='smooth')])],
    'marks': [(201, 106, 80)],
    'arrows': [{'d': 'M 140 120 Q 128 160 150 190'}],
}
TITLES['acusar'] = 'Sinal de acusar em Libras'
