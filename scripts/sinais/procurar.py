# PROCURAR: the support hand, closed (S), lies palm down in front of the stomach, knuckles toward the
# other side; the dominant hand in P (index straight, middle finger forward, the thumb on it), fingers
# pointing across the body and palm toward the body, makes small circles just above the back of the
# fist, a few times. (UFSC Signbank PROCURAR: [Libras_P]/S, on the back of the weak hand. The INES
# PROCURAR video shows the support hand open, palm down.)


def hs_procurar_P():
    """P of Libras: index straight, middle finger straight but bent forward at the knuckle, ring and
    little fingers folded; the thumb's pad on the side of the middle finger."""
    shape = fist({'index': fing(4, 0, 0, 0), 'middle': fing(-2, 62, 6, 4)})
    shape['thumb'] = solve_thumb((8.0, -42.5, 10.0), pad_to=(-1.0, 0.0, 0.0), pref=(5.0, 30.0, 40.0, 15.0, 15.0))
    return shape


_pro_p, _pro_s = hs_procurar_P(), hs_S()
# Support (left) hand, drawn as the right hand at the mirrored place: fist across the body, back up.
_pro_sup = mirrored(P((212, 262), _pro_s, 'wrist', yaw=120, pitch=0, roll=90, scale=1.05, depth=70,
                      pole=(1.0, 0.25, 0.3)))
_PRO_C, _PRO_R = (200, 212), (8, 5)


def _pro_pose(angle):
    """Dominant hand on its small circle above the fist: back of the hand to the viewer, turned a little
    so the palm faces down and in; index across the body, thumb up, the middle finger pointing down."""
    a = math.radians(angle)
    at = (_PRO_C[0] + _PRO_R[0] * math.cos(a), _PRO_C[1] + _PRO_R[1] * math.sin(a))
    return P(at, _pro_p, 'index_tip', yaw=150, pitch=0, roll=92, scale=1.1, depth=85, pole=(0.4, 1.0, 0.35),
             ease='linear')


_pro_keys = [(0.0, [_pro_pose(0), _pro_sup])]
_pro_n = 12
for _pro_k in range(_pro_n + 1):
    _pro_keys.append((0.25 + 1.6 * _pro_k / _pro_n, [_pro_pose(360.0 * 2 * _pro_k / _pro_n), _pro_sup]))
_pro_keys.append((2.3, [_pro_pose(0), _pro_sup]))
SIGNS['procurar'] = {
    'poster': 0.25, 'dur': 2.3, 'hands': ['right', 'left'], 'handshape': _pro_p,
    'handshape_view': {'yaw': -65, 'pitch': -20},
    'keys': _pro_keys,
    'arrows': [{'d': circle_arrow(_PRO_C[0] - 24, _PRO_C[1] - 26, 12, 150, 20, True)}],
    'mirror_second': True,
}
TITLES['procurar'] = 'Sinal de procurar em Libras'
