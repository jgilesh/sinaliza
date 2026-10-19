# SATISFEITO: the support hand lies open and level in front of the chest, palm down, fingers across
# toward the signing side. The signing fist comes up under it and touches the support palm, and
# stays. Once. (UFSC Signbank SATISFAZER: S under the weak hand's palm (B); the INES SATISFAZER video
# is missing and INES SATISFEITO shows another sign.)

_satisfeito_s, _satisfeito_b = hs_S(), hs_B()
# Support hand, defined as a right hand (palm down, fingers pointing across toward the midline, the
# back tipped a little toward the viewer) and mirrored.
_satisfeito_sup = mirrored(P((150, 214), _satisfeito_b, 'wrist', yaw=145, pitch=0, roll=90, scale=1.05, depth=60))
# Fist: back of the fingers to the viewer, thumb on top, knuckles pointing across.
_satisfeito = lambda at, **kw: P(at, _satisfeito_s, 'wrist', yaw=180, pitch=0, roll=80, scale=1.05, depth=64,
                                 pole=(0.35, 1.0, 0.4), **kw)
_satisfeito_low, _satisfeito_on = _satisfeito((166, 272)), _satisfeito((170, 240), ease='out')
SIGNS['satisfeito'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _satisfeito_s,
    'keys': [(0.0, [_satisfeito_low, _satisfeito_sup]), (0.35, [_satisfeito_low, _satisfeito_sup]),
             (0.8, [_satisfeito_on, _satisfeito_sup]), (1.8, [_satisfeito_on, _satisfeito_sup]),
             (2.4, [dict(_satisfeito_low, ease='smooth'), _satisfeito_sup])],
    'marks': [(214, 234, 130)],
    'arrows': [{'d': 'M 146 282 L 146 248'}],
    'mirror_second': True,
}
TITLES['satisfeito'] = 'Sinal de satisfeito em Libras'
