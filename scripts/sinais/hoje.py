# HOJE: both hands open, palms up, raised to shoulder height, come down together to the front of the
# waist, once. (INES HOJE1; Signbank 1458: B + B, espaço neutro.)
def hs_hoje_open():
    """Open hand, fingers almost together and a little curved (relaxed B), thumb open."""
    return {'index': fing(5, 8, 14, 8), 'middle': fing(1, 9, 15, 9), 'ring': fing(-3, 10, 16, 10),
            'pinky': fing(-8, 12, 18, 11), 'thumb': (14.0, 20.0, 12.0, 8.0, 6.0)}


hoje_hand = hs_hoje_open()
# Palm up and tipped a little toward the viewer, fingers pointing forward and out: the palm and the
# slightly curved fingers both show.
hoje_at = lambda at, depth: P(at, hoje_hand, 'wrist', yaw=40, pitch=22, roll=-98, scale=1.15, depth=depth)
hoje_up, hoje_down = hoje_at((128, 196), 55), hoje_at((136, 262), 75)
SIGNS['hoje'] = {
    'poster': 0.3, 'dur': 2.0, 'hands': ['right', 'left'], 'handshape': hoje_hand, 'handshape_view': {'yaw': 20},
    'keys': [(0.0, [hoje_up, mirrored(hoje_up)]), (0.3, [hoje_up, mirrored(hoje_up)]),
             (0.85, [hoje_down, mirrored(hoje_down)]), (1.6, [hoje_down, mirrored(hoje_down)]),
             (2.0, [hoje_up, mirrored(hoje_up)])],
    'arrows': [{'trail': 0, 'from': 0.3, 'to': 0.85, 'offset': (22, -8), 'trim': 0.1},
               {'trail': 1, 'from': 0.3, 'to': 0.85, 'offset': (-22, -8), 'trim': 0.1}],
    'mirror_second': True,
}
TITLES['hoje'] = 'Sinal de hoje em Libras'
