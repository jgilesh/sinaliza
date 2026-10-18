# ATÉ: the support hand stands up (B), palm toward the dominant hand; the dominant hand, flat and
# lying palm down with the fingers toward the support hand, comes down in an arc from its own side
# and stops with its fingertips on the support palm. (INES ATÉ; Signbank 248: B_bent + B, contact
# at the end on the palm of the support hand.)
ate_b = hs_B()
# Support (left) hand: fingers up, palm toward the dominant hand and a little toward the viewer.
ate_base = P((214, 236), ate_b, 'wrist', yaw=74, pitch=-4, roll=4, scale=1.1, depth=70, pole=(0.3, 1.0, 0.4))
# Dominant hand: lying flat, palm down (back of the hand up, seen a little from above), fingers toward
# the support palm.
ate_dom = lambda at, **kw: P(at, ate_b, 'fingertips', yaw=112, pitch=8, roll=94, scale=1.1, depth=75,
                             pole=(0.45, 1.0, 0.45), **kw)
ate_start = ate_dom((166, 154))
ate_end = ate_dom((207, 202), via=(206, 160), ease='in')
ate_base_r = mirrored(ate_base)    # the support hand as given is the right hand's mirror image
SIGNS['ate'] = {
    'poster': 1.0, 'dur': 2.3, 'hands': ['right', 'left'], 'handshape': ate_b, 'handshape_view': {'yaw': 0},
    'keys': [(0.0, [ate_start, ate_base]), (0.35, [ate_start, ate_base]), (0.9, [ate_end, ate_base]),
             (1.7, [ate_end, ate_base]), (2.3, [dict(ate_start, via=(170, 205)), ate_base])],
    'marks': [(198, 216, -150)],
    'arrows': [{'d': 'M 132 128 Q 182 112 192 164'}],
    'mirror_second': True,
}
TITLES['ate'] = 'Sinal de até em Libras'
