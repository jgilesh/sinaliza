# PAQUERAR: both hands in V, horizontal, palms down, the fingers pointing at each other: the
# dominant hand beside the chin, the support hand further out to the side and higher, at eye level.
# The hands move back and forth in small repeated movements (one rises as the other drops), while
# the gaze turns toward the support hand. (UFSC Signbank PAQUERAR; the INES PAQUERAR1 video shows
# another variant: a fist by the shoulder that flicks the index up.)
_paquerar_v = hs_V()


def _paquerar_pose(at, dy):
    # Back of the hand toward the viewer and up, the V spread horizontal, fingers toward the midline.
    return P((at[0], at[1] + dy), _paquerar_v, 'fingertips', yaw=150, pitch=0, roll=90, scale=1.0, depth=55,
             pole=(0.45, 1.0, 0.4))


_PAQUERAR_DOM, _PAQUERAR_SUP = (182, 152), (138, 104)   # support defined as a right hand, then mirrored
_paquerar_keys = [(0.0, [_paquerar_pose(_PAQUERAR_DOM, 0), mirrored(_paquerar_pose(_PAQUERAR_SUP, 0))])]
for _paquerar_i in range(6):
    _paquerar_d = 5 if _paquerar_i % 2 == 0 else -5
    _paquerar_keys.append((0.35 + 0.25 * _paquerar_i, [_paquerar_pose(_PAQUERAR_DOM, -_paquerar_d),
                                                       mirrored(_paquerar_pose(_PAQUERAR_SUP, _paquerar_d))]))
_paquerar_keys += [(2.0, _paquerar_keys[0][1]), (2.4, _paquerar_keys[0][1])]
SIGNS['paquerar'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _paquerar_v,
    'handshape_view': {'yaw': 150, 'roll': 90},
    'keys': _paquerar_keys,
    # Small up-and-down movement under each hand (two heads: it repeats).
    'arrows': [{'d': 'M 140 190 L 140 210', 'both': True}, {'d': 'M 296 144 L 296 164', 'both': True}],
    'mirror_second': True,
}
TITLES['paquerar'] = 'Sinal de paquerar em Libras'
