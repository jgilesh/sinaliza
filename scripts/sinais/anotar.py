# ANOTAR: the support hand open, palm up, in front of the chest. The dominant hand, closed with the
# thumb along its side (A), lands on that palm, then opens flat (B) and lies on it, palm down. It
# closes again and opens again: twice. (UFSC Signbank ANOTAR: A+B on the weak hand's palm, double
# contact. The INES ANOTAR1 video shows another variant.)

_anotar_a, _anotar_b = hs_A(), hs_B()
_anotar_pole = (0.35, 1.0, 0.4)
# Support hand, defined as a right hand (palm up, fingers toward the midline) and mirrored.
_anotar_sup = mirrored(P((132, 212), _anotar_b, 'wrist', yaw=-45, pitch=0, roll=84, scale=1.05, depth=60))
# Dominant: the fist stands on its little-finger edge on the support palm, knuckles forward, the thumb on top.
_anotar_fist = lambda lift=0, **kw: P((214, 194 - lift), _anotar_a, 'wrist', yaw=200, pitch=40, roll=90, scale=1.05,
                                      depth=70, pole=_anotar_pole, **kw)
# Then it opens flat and lies on the palm, palm down, fingers across it.
_anotar_flat = P((212, 196), _anotar_b, 'wrist', yaw=105, pitch=30, roll=95, scale=1.05, depth=70, pole=_anotar_pole)
_anotar_keys = [(0.0, _anotar_fist(14)), (0.3, _anotar_fist(14)), (0.5, _anotar_fist()), (0.8, _anotar_flat),
                (1.0, _anotar_fist(10)), (1.2, _anotar_fist()), (1.5, _anotar_flat), (2.0, _anotar_flat),
                (2.4, _anotar_fist(14))]
SIGNS['anotar'] = {
    'poster': 0.5, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _anotar_a,
    'keys': [(t, [p, _anotar_sup]) for t, p in _anotar_keys],
    'marks': [(262, 166, 20)],
    'arrows': [{'d': 'M 190 172 L 190 190', 'both': True}],
    'mirror_second': True,
}
TITLES['anotar'] = 'Sinal de anotar em Libras'
