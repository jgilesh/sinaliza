# PERTO: both hands in A (fist, thumb up), thumb sides toward each other, come together in front of
# the chest until they almost touch; a short second approach. (INES PERTO1; Signbank 2217: A + A.)
perto_a = HANDSHAPES['A']()
# Palm turned toward the other hand and a little toward the viewer: the folded fingers and the thumb
# along the index read, and the two thumbs face each other.
perto_at = lambda x, ease='smooth': P((x, 206), perto_a, 'thumb_tip', yaw=-14, pitch=-10, roll=8, scale=1.15, depth=70,
                                      pole=(0.3, 1.0, 0.4), ease=ease)
perto_far, perto_near, perto_mid = perto_at(160), perto_at(191), perto_at(184)
SIGNS['perto'] = {
    'poster': 1.4, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': perto_a, 'handshape_view': {'yaw': -18, 'pitch': -8},
    'keys': [(0.0, [perto_far, mirrored(perto_far)]), (0.3, [perto_far, mirrored(perto_far)]),
             (0.75, [perto_near, mirrored(perto_near)]), (0.95, [perto_mid, mirrored(perto_mid)]),
             (1.15, [perto_near, mirrored(perto_near)]), (1.9, [perto_near, mirrored(perto_near)]),
             (2.4, [perto_far, mirrored(perto_far)])],
    'arrows': [{'trail': 0, 'from': 0.3, 'to': 0.75, 'offset': (-14, -64), 'trim': 0.05},
               {'trail': 1, 'from': 0.3, 'to': 0.75, 'offset': (14, -64), 'trim': 0.05}],
    'mirror_second': True,
}
TITLES['perto'] = 'Sinal de perto em Libras'
