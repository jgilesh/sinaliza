# QUEM: small C (thumb and index curved, the other fingers closed) in front of the shoulder; the hand goes
# down to chest height while the thumb and index close until they almost touch (UFSC Signbank QUEM-3).


def hs_quem_c(closed=False):
    """Baby C: index and thumb curved toward each other; open (a gap the size of a coin) or nearly closed."""
    shape = fist({'index': fing(2, 22, 42, 28) if closed else fing(2, 8, 38, 26)})
    tip = finger_chain('index', shape['index'])[0][3]
    gap = 6.0 if closed else 26.0
    shape['thumb'] = solve_thumb((tip[0] + 1.0, tip[1] + gap, tip[2] + 3.0), pad_to=(0.0, -1.0, 0.3),
                                 pref=(-5.0, 45.0, 55.0, 15.0, 20.0))
    return shape


qm_open, qm_closed = hs_quem_c(), hs_quem_c(True)
# Fingers up and the palm turned to the side (and a little forward), seen from the thumb side: the index
# arches over the thumb and the C between them reads at a glance.
qm_pose = lambda at, shape, scale: P(at, shape, 'index_tip', yaw=-62, pitch=-5, roll=-8, scale=scale, depth=60,
                                     pole=(0.3, 1.0, 0.45))
qm_top = qm_pose((146, 150), qm_open, 1.15)
qm_bottom = qm_pose((152, 204), qm_closed, 1.15)
SIGNS['quem'] = {
    'poster': 0.3, 'dur': 2.2, 'hands': ['right'], 'handshape': qm_open, 'handshape_view': {'yaw': -90},
    'keys': [(0.0, [qm_top]), (0.3, [qm_top]), (0.95, [qm_bottom]), (1.7, [qm_bottom]), (2.2, [qm_top])],
    'arrows': [{'d': 'M 108 158 L 110 206'}],
}
TITLES['quem'] = 'Sinal de quem em Libras'
