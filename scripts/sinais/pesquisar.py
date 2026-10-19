# PESQUISAR: the support hand stands open (B), fingers up, palm toward the signing hand. The signing
# hand in D (index straight, the other fingertips resting on the thumb), palm down, puts the tip of
# the index on the support palm and scrapes it up and down several times, as if searching.
# (UFSC Signbank PESQUISAR: D on B, weak hand's palm; INES INVESTIGAR agrees.)


def hs_pesquisar_d():
    """D of Libras: index straight, middle, ring and little finger curved down onto the thumb's pad."""
    shape = {'index': fing(2, 0, 0, 0), 'middle': fing(0, 52, 70, 45), 'ring': fing(-2, 54, 68, 45),
             'pinky': fing(-4, 58, 64, 45)}
    shape['thumb'] = pinch_thumb(shape, fingers=('middle',))
    return shape


_pesquisar_d, _pesquisar_b = hs_pesquisar_d(), hs_B()
# Support hand (defined as a right hand, then mirrored): fingers up, palm turned toward the signing
# hand and a little toward the viewer, so the index can be seen on it.
_pesquisar_base = mirrored(P((150, 238), _pesquisar_b, 'wrist', yaw=55, pitch=0, roll=-4, scale=1.05, depth=60))


def _pesquisar_pose(y):
    return P((241, y), _pesquisar_d, 'index_tip', yaw=55, pitch=0, roll=92, scale=1.05, depth=58, pole=(0.4, 1.0, 0.4))


_pesquisar_hi, _pesquisar_lo = _pesquisar_pose(196), _pesquisar_pose(212)
_pesquisar_keys = [(0.0, [_pesquisar_hi, _pesquisar_base]), (0.3, [_pesquisar_hi, _pesquisar_base])]
for _pesquisar_i in range(3):
    _pesquisar_t = 0.3 + 0.4 * _pesquisar_i
    _pesquisar_keys += [(_pesquisar_t + 0.2, [_pesquisar_lo, _pesquisar_base]),
                        (_pesquisar_t + 0.4, [_pesquisar_hi, _pesquisar_base])]
_pesquisar_keys.append((2.0, [_pesquisar_hi, _pesquisar_base]))
SIGNS['pesquisar'] = {
    'poster': 0.3, 'dur': 2.0, 'hands': ['right', 'left'], 'handshape': _pesquisar_d,
    'handshape_view': {'yaw': 92, 'pitch': -20},
    'keys': _pesquisar_keys,
    'marks': [(241, 184, 0)],
    'arrows': [{'d': 'M 284 180 L 284 220', 'both': True}],
    'mirror_second': True,
}
TITLES['pesquisar'] = 'Sinal de pesquisar em Libras'
