# VIGIAR: the support hand closed (S) and lying across in front of the chest, back of the hand up;
# the signing hand in V, upright, palm forward, rests the heel of the hand on the back of that fist
# and swings from side to side, 2 times, like eyes keeping watch. (UFSC Signbank VIGIAR and INES
# VIGIAR agree.)
_vig_v = hs_V()
_vig_s = hs_S()
# Support fist, defined as a right hand (back up, knuckles toward the midline) and mirrored.
_vig_base = mirrored(P((150, 258), _vig_s, 'wrist', yaw=110, pitch=5, roll=90, scale=1.1, depth=66))
_VIG_AT = (204.0, 244.0)   # the signing wrist, resting on the back of the fist


def _vig_top(side):
    """Signing hand; side = -1 (leans toward the signer's right) .. +1 (left), pivoting on the wrist."""
    return P(_VIG_AT, _vig_v, 'wrist', yaw=-10, pitch=0, roll=-18 * side, scale=1.05, depth=72,
             pole=(0.35, 1.0, 0.45))


_vig_m, _vig_l, _vig_r = _vig_top(0.0), _vig_top(-1.0), _vig_top(1.0)
_vig_keys = [(0.0, [_vig_m, _vig_base]), (0.3, [_vig_m, _vig_base])]
_vig_t = 0.3
for _vig_k in range(2):
    _vig_keys += [(round(_vig_t + 0.25, 2), [_vig_l, _vig_base]), (round(_vig_t + 0.75, 2), [_vig_r, _vig_base])]
    _vig_t += 0.75
_vig_keys += [(round(_vig_t + 0.3, 2), [_vig_m, _vig_base]), (round(_vig_t + 0.8, 2), [_vig_m, _vig_base])]
SIGNS['vigiar'] = {
    'poster': 0.3, 'dur': round(_vig_t + 0.8, 2), 'hands': ['right', 'left'], 'handshape': _vig_v,
    'keys': _vig_keys,
    # The heel of the signing hand rests on the back of the fist.
    'marks': [(230, 240, 60)],
    # An arc above the fingertips: side to side.
    'arrows': [{'d': circle_arrow(_VIG_AT[0], _VIG_AT[1], 84, -114, -66, True), 'both': True}],
    'mirror_second': True,
}
TITLES['vigiar'] = 'Sinal de vigiar em Libras'
