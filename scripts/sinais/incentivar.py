# INCENTIVAR: both hands open, fingers apart and a little curved, palms up and in; from low at the
# sides they swing up in an arc toward the chest, again and again, as if urging someone on.
# (UFSC Signbank ESTIMULAR; INES INCENTIVAR agrees.)


def hs_incentivar_5():
    """Open hand, fingers spread and a little curved at every joint, thumb apart."""
    return {'index': fing(14, 10, 22, 14), 'middle': fing(3, 10, 24, 16), 'ring': fing(-8, 10, 24, 16),
            'pinky': fing(-18, 12, 24, 16), 'thumb': (40.0, 18.0, 8.0, 8.0, 8.0)}


_incentivar_5 = hs_incentivar_5()
_incentivar_pole = (0.45, 1.0, 0.4)
# Low: out at the side by the waist, palm up and toward the viewer, the fingers pointing out.
_incentivar_lo = P((106, 262), _incentivar_5, 'wrist', yaw=45, pitch=0, roll=-80, scale=1.08, depth=60,
                   pole=_incentivar_pole, ease='smooth')
# High: in front of the chest, fingers up, the palm turned in toward the midline.
_incentivar_hi = P((132, 214), _incentivar_5, 'wrist', yaw=65, pitch=-10, roll=-6, scale=1.12, depth=80,
                   via=(92, 228), pole=_incentivar_pole)
_incentivar_k = lambda p: [p, mirrored(p)]
_incentivar_keys = [(0.0, _incentivar_k(_incentivar_lo)), (0.3, _incentivar_k(_incentivar_lo))]
for _incentivar_i in range(3):   # three upward swings
    _incentivar_t = 0.3 + 0.6 * _incentivar_i
    _incentivar_keys += [(_incentivar_t + 0.35, _incentivar_k(_incentivar_hi)),
                         (_incentivar_t + 0.6, _incentivar_k(_incentivar_lo))]
_incentivar_keys += [(2.5, _incentivar_k(_incentivar_lo))]
SIGNS['incentivar'] = {
    'poster': 0.65, 'dur': 2.5, 'hands': ['right', 'left'], 'handshape': _incentivar_5,
    'keys': _incentivar_keys,
    'arrows': [{'d': 'M 44 206 Q 58 162 98 150'}, {'d': 'M 356 206 Q 342 162 302 150'}],
    'mirror_second': True,
}
TITLES['incentivar'] = 'Sinal de incentivar em Libras'
