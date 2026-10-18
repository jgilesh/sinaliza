# ONTEM: L hand, palm forward, the thumb tip on the cheek; the index bends into a hook and
# straightens, two times. (INES ONTEM; Signbank 2058: L, bochecha.)
ontem_up, ontem_bent = hs_L(), hs_L((10, 90, 55))   # bent: the index hooks toward the palm
# The palm turns a little toward the face (yaw), so the thumb points into the cheek and the hook is
# seen half in profile beside the face.
ontem_at = lambda shape: P((171, 116), shape, 'thumb_tip', yaw=30, pitch=-10, roll=-4, scale=1.05, pole=(0.6, 1.0, 0.5))
SIGNS['ontem'] = {
    'poster': 0.0, 'dur': 2.0, 'hands': ['right'], 'handshape': ontem_up,
    'keys': [(0.0, [ontem_at(ontem_up)]), (0.35, [ontem_at(ontem_up)]), (0.55, [ontem_at(ontem_bent)]),
             (0.75, [ontem_at(ontem_up)]), (0.95, [ontem_at(ontem_bent)]), (1.15, [ontem_at(ontem_up)]),
             (2.0, [ontem_at(ontem_up)])],
    'marks': [(176, 121, 140)],
    'arrows': [{'d': 'M 122 44 Q 152 38 156 70', 'both': True}],
}
TITLES['ontem'] = 'Sinal de ontem em Libras'
