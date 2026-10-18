# ESCOLA = CASA + ESTUDAR. First the two flat hands (B) make a roof, fingertips touching (CASA);
# then both palms turn up in front of the chest, crossed, and the back of the dominant hand taps
# the palm of the other hand, three times (ESTUDAR). (INES ESCOLA; UFSC Signbank shows the same
# roof start.)
_esc_hs = hs_B()
_esc_roof = P((192, 163), _esc_hs, 'fingertips', yaw=125, pitch=0, roll=38, scale=1.05, depth=60, pole=(0.5, 1.0, 0.4))
_esc_open = dict(_esc_roof, at=(184, 172), roll=30)
# ESTUDAR: palms up, fingers across the body; the support hand (left, drawn as the mirrored right
# hand) lies still, the dominant hand crosses over it and taps it with its back.
_esc_sup = mirrored(P((224, 256), _esc_hs, 'fingertips', yaw=-55, pitch=0, roll=106, scale=1.05, depth=70))
_esc_tap = P((246, 204), _esc_hs, 'fingertips', yaw=-55, pitch=0, roll=64, scale=1.05, depth=80, pole=(0.4, 1.0, 0.4))
_esc_lift = dict(_esc_tap, at=(242, 186), roll=54)
_k = lambda r, l: [r, l]
SIGNS['escola'] = {
    'poster': 1.5, 'dur': 3.4, 'hands': ['right', 'left'], 'handshape': _esc_hs,
    'keys': [(0.0, _k(_esc_open, mirrored(_esc_open))), (0.25, _k(_esc_open, mirrored(_esc_open))),
             (0.5, _k(_esc_roof, mirrored(_esc_roof))), (0.85, _k(_esc_roof, mirrored(_esc_roof))),
             (1.3, _k(_esc_lift, _esc_sup)), (1.5, _k(_esc_tap, _esc_sup)), (1.7, _k(_esc_lift, _esc_sup)),
             (1.9, _k(_esc_tap, _esc_sup)), (2.1, _k(_esc_lift, _esc_sup)), (2.3, _k(_esc_tap, _esc_sup)),
             (3.0, _k(_esc_tap, _esc_sup)), (3.4, _k(_esc_open, mirrored(_esc_open)))],
    'mirror_second': True,
    'marks': [(200, 151, 0), (206, 258, 180)],
    'arrows': [{'d': 'M 266 190 L 266 208', 'both': True}],
}
del _k
TITLES['escola'] = 'Sinal de escola em Libras'
