# DEPOIS: L hand raised beside the head, index up, palm forward; the wrist bends and the hand arcs
# forward, ending with the index pointing ahead and a little down, once. (INES DEPOIS; Signbank 855:
# L, para a frente, arco.)
depois_l = hs_L()
depois_up = P((108, 132), depois_l, 'wrist', yaw=-5, pitch=-5, roll=-6, scale=1.1, depth=60, pole=(0.7, 1.0, 0.45))
# End: the fingers tip toward the viewer past horizontal (pitch), so the index points forward and a
# little down; the thumb still sticks out sideways, toward the midline.
depois_fwd = P((116, 140), depois_l, 'wrist', yaw=39, pitch=126, roll=33, scale=1.15, depth=85, pole=(0.7, 1.0, 0.45),
               ease='out')
SIGNS['depois'] = {
    'poster': 0.0, 'dur': 2.2, 'hands': ['right'], 'handshape': depois_l,
    'keys': [(0.0, [depois_up]), (0.4, [depois_up]), (0.95, [depois_fwd]), (1.7, [depois_fwd]),
             (2.2, [dict(depois_up, ease='smooth')])],
    # On the outer side: the index tips over forward and down.
    'arrows': [{'d': 'M 96 48 Q 52 96 80 172'}],
}
TITLES['depois'] = 'Sinal de depois em Libras'
