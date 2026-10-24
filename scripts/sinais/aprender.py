# APRENDER: the hand, open and curved, at the side of the forehead with the index side against it, the
# palm turned toward the head; it closes into a fist (as if grabbing an idea) and comes down a little as
# it closes. Three times. (UFSC Signbank APRENDER: S, forehead, radial side near it; INES APRENDER agrees.)


def hs_aprender_open():
    """Open curved hand: fingers a little apart, bent at the knuckles and middle joints, thumb opposite."""
    return {'index': fing(8, 30, 40, 22), 'middle': fing(1, 32, 42, 24), 'ring': fing(-6, 34, 42, 24),
            'pinky': fing(-13, 36, 42, 24), 'thumb': (24.0, 40.0, 40.0, 10.0, 12.0)}


_apr_open, _apr_fist = hs_aprender_open(), hs_S()


def _apr_pose(at, shape, ease='smooth', **kw):
    # Beside the forehead on the signing side, palm turned toward the head and partly to the viewer, the
    # fingers tipped in over the forehead: the curve of the open hand and the fist both read, eyes clear.
    return P(at, shape, 'wrist', yaw=55, pitch=-10, roll=40, scale=1.0, depth=38,
             pole=(0.7, 1.0, 0.45), ease=ease, **kw)


_apr_low = P((126, 168), _apr_open, 'wrist', yaw=30, pitch=0, roll=10, scale=1.0, depth=45, pole=(0.7, 1.0, 0.45))
_apr_keys = [(0.0, [_apr_low])]
_apr_t = 0.35
for _apr_i in range(3):   # open at the forehead, close and come down a little
    _apr_keys += [(round(_apr_t, 2), [_apr_pose((140, 74), _apr_open)]),
                  (round(_apr_t + 0.3, 2), [_apr_pose((140, 80), _apr_fist, ease='out')])]
    _apr_t += 0.5
_apr_keys += [(round(_apr_t + 0.2, 2), [_apr_pose((140, 80), _apr_fist)]),
              (round(_apr_t + 0.6, 2), [dict(_apr_low, via=(130, 130))])]
SIGNS['aprender'] = {
    'poster': 0.35, 'dur': round(_apr_t + 0.6, 2), 'hands': ['right'], 'handshape': _apr_open,
    'handshape_view': {'yaw': 40, 'roll': -5},
    'keys': _apr_keys,
    'marks': [(178, 44, 30)],
    # Open and close: two short arcs closing in beside the hand.
    'arrows': [{'d': 'M 106 50 Q 100 70 110 86'}],
}
TITLES['aprender'] = 'Sinal de aprender em Libras'
