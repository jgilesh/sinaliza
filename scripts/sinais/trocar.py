# TROCAR: both hands flat (B), palms up, side by side, the signing hand a little higher; the signing hand
# goes once around the support hand in a horizontal circle (in front of it over to the far side, then
# back behind it to where it started), the support hand barely moving. (UFSC Signbank TROCAR: B/B; INES
# TROCAR1 agrees.)


def hs_trocar_flat():
    """Flat hand, fingers together and nearly straight, thumb a little apart."""
    return {'index': fing(2, 6, 8, 4), 'middle': fing(0, 6, 8, 4), 'ring': fing(-2, 6, 8, 4),
            'pinky': fing(-4, 8, 8, 4), 'thumb': (28.0, 16.0, 8.0, 6.0, 4.0)}


_troc_b = hs_trocar_flat()
# Support hand, defined as a right hand (palm up, tipped toward the viewer, fingers toward the midline)
# and mirrored: on the support side, chest height.
_troc_base = mirrored(P((166, 232), _troc_b, 'wrist', yaw=-50, pitch=0, roll=92, scale=1.08, depth=66))


def _troc_pose(at, depth=70, yaw=-50, roll=92, ease='linear'):
    """Signing hand palm up, fingers toward the midline (or past it on the far side)."""
    return P(at, _troc_b, 'wrist', yaw=yaw, pitch=0, roll=roll, scale=1.08, depth=depth,
             pole=(0.45, 1.0, 0.4), ease=ease)


# The circle on screen: start on the signing side a little higher; in front of the support hand (lower on
# screen, nearer); the far side; behind it (higher on screen, farther) and back.
_troc_start = _troc_pose((110, 196), ease='smooth')
_troc_front = _troc_pose((180, 246), depth=96)
_troc_far = _troc_pose((262, 220), depth=80, roll=100)
_troc_behind = _troc_pose((184, 172), depth=50)
_troc_keys = [(0.0, [_troc_start, _troc_base]), (0.3, [_troc_start, _troc_base]),
              (0.65, [_troc_front, _troc_base]), (1.0, [_troc_far, _troc_base]),
              (1.35, [_troc_behind, _troc_base]), (1.7, [dict(_troc_start, ease='smooth'), _troc_base]),
              (2.4, [_troc_start, _troc_base])]
SIGNS['trocar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _troc_b,
    'keys': _troc_keys,
    # One loop around the support hand: under it from the signing side, up the far side, back over the top.
    'arrows': [{'d': 'M 100 222 Q 160 292 268 264 Q 318 242 290 198 Q 246 150 142 166'}],
    'mirror_second': True,
}
TITLES['trocar'] = 'Sinal de trocar em Libras'
