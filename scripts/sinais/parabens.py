# PARABÉNS: both hands curved (C) and clasped, the dominant hand wrapped around the other, beside the
# face on the non-dominant side at chin height; the joined hands shake forward and back a few times.
# (INES PARABENIZAR1, UFSC Signbank PARABENIZAR.)
_par_c = hs_C()
# The other hand (behind): palm toward the dominant hand, fingers up, curling over its thumb side.
_par_l = lambda k: P((280 - 2 * k, 178 - 3 * k), _par_c, 'wrist', yaw=60, pitch=-10, roll=8, scale=1.1 + 0.06 * k,
                     depth=55 + 20 * k)
# The dominant hand (in front): back of the hand to the viewer, its fingers wrapped around the other hand.
_par_r = lambda k: P((238 - 2 * k, 202 - 3 * k), _par_c, 'wrist', yaw=150, pitch=0, roll=58, scale=1.1 + 0.06 * k,
                     depth=55 + 20 * k, pole=(0.3, 1.0, 0.45))
_par_keys = [(0.0, [_par_r(0), _par_l(0)]), (0.3, [_par_r(0), _par_l(0)])]
for _par_n in range(3):   # three shakes
    _par_keys += [(0.5 + 0.4 * _par_n, [_par_r(1), _par_l(1)]), (0.7 + 0.4 * _par_n, [_par_r(0), _par_l(0)])]
_par_keys += [(2.4, [_par_r(0), _par_l(0)])]
SIGNS['parabens'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _par_c, 'handshape_view': {'yaw': -60},
    'keys': _par_keys,
    # Forward and back (a short two-headed arrow beside the joined hands).
    'arrows': [{'d': 'M 306 140 Q 316 162 306 184', 'both': True}],
    'mirror_second': True,
}
TITLES['parabens'] = 'Sinal de parabéns em Libras'
