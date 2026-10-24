# PULAR: the support hand open, palm up; the signing hand in V with the two fingers pointing down like
# legs stands on the support palm, springs up bending the fingers (knees bent in the air) and lands back
# on the palm. (UFSC Signbank PULAR: V + V curved on the palm of the B support hand; INES PULAR1 agrees.)


def hs_pular_v(bend=0.0):
    """V with the two fingers apart like legs, the others folded under the thumb; bend (0..1) curls the
    two fingers at the middle and end joints (the legs bent in the jump)."""
    shape = fist({'index': fing(14, 10 * bend, 55 * bend, 30 * bend),
                  'middle': fing(-10, 10 * bend, 55 * bend, 30 * bend)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


def hs_pular_open():
    """Support hand: open, fingers together and nearly straight, thumb apart."""
    return {'index': fing(2, 6, 8, 4), 'middle': fing(0, 6, 8, 4), 'ring': fing(-2, 6, 8, 4),
            'pinky': fing(-4, 8, 8, 4), 'thumb': (30.0, 16.0, 8.0, 6.0, 4.0)}


_pul_v, _pul_bent, _pul_open = hs_pular_v(0.0), hs_pular_v(1.0), hs_pular_open()
# Support hand, defined as a right hand (palm up, fingers toward the midline) and mirrored.
_pul_base = mirrored(P((156, 266), _pul_open, 'wrist', yaw=-50, pitch=0, roll=90, scale=1.1, depth=70))


def _pul_pose(at, shape, anchor='fingertips', ease='smooth'):
    """Signing hand hanging from the wrist, the V fingers pointing down; turned a little (thumb side
    toward the viewer), so the two legs read apart and their bend shows in the air."""
    return P(at, shape, anchor, yaw=-150, pitch=0, roll=180, scale=1.05, depth=76, pole=(0.3, 1.0, 0.45),
             ease=ease)


_pul_stand = _pul_pose((214, 252), _pul_v)
_pul_crouch = _pul_pose((214, 255), _pul_v)
_pul_air = _pul_pose((212, 222), _pul_bent, ease='out')
_pul_land = _pul_pose((214, 252), _pul_v, ease='in')
SIGNS['pular'] = {
    'poster': 0.7, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _pul_v, 'handshape_view': {'yaw': 180},
    'keys': [(0.0, [_pul_stand, _pul_base]), (0.3, [_pul_stand, _pul_base]), (0.4, [_pul_crouch, _pul_base]),
             (0.7, [_pul_air, _pul_base]), (1.0, [_pul_land, _pul_base]), (1.1, [_pul_crouch, _pul_base]),
             (1.2, [_pul_stand, _pul_base]), (2.4, [_pul_stand, _pul_base])],
    # Up from the palm and back down.
    'arrows': [{'d': 'M 244 248 L 244 210', 'both': True}],
    'marks': [(228, 254, 120)],
    'mirror_second': True,
}
TITLES['pular'] = 'Sinal de pular em Libras'
