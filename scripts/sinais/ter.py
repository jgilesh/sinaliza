# TER: L hand, index pointing across the body (up toward the neck), palm toward the body; the
# thumb tip taps the top of the chest, below the neck, twice.
_ter_l = hs_L()
_ter_on = P((186, 203), _ter_l, 'thumb_tip', yaw=70, pitch=-10, roll=68, scale=1.15, depth=30)
_ter_off = dict(_ter_on, at=(181, 199), depth=48)
SIGNS['ter'] = {
    'poster': 0.55, 'dur': 2.0, 'hands': ['right'], 'handshape': _ter_l,
    'keys': [(0.0, [_ter_off]), (0.35, [_ter_off]), (0.55, [_ter_on]), (0.75, [_ter_off]), (0.95, [_ter_on]),
             (1.15, [_ter_off]), (2.0, [_ter_off])],
    'marks': [(186, 203, 200)],
}
TITLES['ter'] = 'Sinal de ter em Libras'
