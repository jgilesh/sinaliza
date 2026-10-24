# FRITAR: both hands in a claw (fingers spread and curved), palms up, in front of the chest; they go up
# and down in alternation while the fingers wiggle, like oil bubbling. (UFSC Signbank FRITAR: 5 claw on
# both hands, neutral space.)


def hs_fritar_claw(k=0.0):
    """Claw: fingers spread, bent at the knuckles and more at the middle and end joints; k (0..1) bends
    them a little more (the wiggle)."""
    return {'index': fing(12, 16 + 8 * k, 48 + 12 * k), 'middle': fing(3, 16 + 8 * k, 50 + 12 * k),
            'ring': fing(-7, 18 + 8 * k, 50 + 12 * k), 'pinky': fing(-16, 20 + 8 * k, 48 + 12 * k),
            'thumb': (34.0, 30.0, 20.0, 18.0, 26.0 + 10 * k)}


_frit_a, _frit_b = hs_fritar_claw(0.0), hs_fritar_claw(1.0)


def _frit_pose(at, shape):
    """Right hand: palm up and tipped toward the viewer, the fingers rising and leaning a little in toward
    the midline, so the curled fingertips (the claw) read in front of the palm."""
    return P(at, shape, 'wrist', yaw=10, pitch=-35, roll=10, scale=1.1, depth=62, pole=(0.45, 1.0, 0.4))


_FRIT_X, _FRIT_HI, _FRIT_LO = 140, 222, 244
_frit_keys = [(0.0, [_frit_pose((_FRIT_X, _FRIT_LO), _frit_a), mirrored(_frit_pose((_FRIT_X, _FRIT_LO), _frit_a))])]
_frit_t = 0.25
for _frit_i in range(3):   # right up while left down, then the other way; the fingers wiggle
    _frit_keys += [(round(_frit_t, 2), [_frit_pose((_FRIT_X, _FRIT_HI), _frit_b), mirrored(_frit_pose((_FRIT_X, _FRIT_LO), _frit_a))]),
                   (round(_frit_t + 0.3, 2), [_frit_pose((_FRIT_X, _FRIT_LO), _frit_a), mirrored(_frit_pose((_FRIT_X, _FRIT_HI), _frit_b))])]
    _frit_t += 0.6
_frit_keys += [(round(_frit_t + 0.3, 2), [_frit_pose((_FRIT_X, _FRIT_LO), _frit_a), mirrored(_frit_pose((_FRIT_X, _FRIT_LO), _frit_a))])]
SIGNS['fritar'] = {
    'poster': 0.25, 'dur': round(_frit_t + 0.3, 2), 'hands': ['right', 'left'], 'handshape': _frit_a,
    'handshape_view': {'yaw': -20, 'pitch': -20},
    'keys': _frit_keys,
    'arrows': [{'d': 'M 96 200 L 96 246', 'both': True}, {'d': 'M 304 200 L 304 246', 'both': True}],
    'mirror_second': True,
}
TITLES['fritar'] = 'Sinal de fritar em Libras'
