# NÃO: index up, palm forward, in front of the shoulder; the hand swings from side to side like a
# windscreen wiper, three times. No contact. (INES NÃO1; Signbank 1957: 1.)
nao_one = hs_1()
# The wrist stays almost still and the hand tilts (roll) from side to side, the index swinging above it.
nao_at = lambda roll, dx=0: P((128 + dx, 190), nao_one, 'wrist', yaw=-8, pitch=-5, roll=roll, scale=1.15, depth=70,
                              pole=(0.35, 1.0, 0.4))
nao_l, nao_r, nao_mid = nao_at(-20, -3), nao_at(12, 3), nao_at(-2)
SIGNS['nao'] = {
    'poster': 0.0, 'dur': 2.2, 'hands': ['right'], 'handshape': nao_one,
    'keys': [(0.0, [nao_mid]), (0.25, [nao_mid]), (0.45, [nao_l]), (0.7, [nao_r]), (0.95, [nao_l]), (1.2, [nao_r]),
             (1.45, [nao_l]), (1.65, [nao_mid]), (2.2, [nao_mid])],
    'arrows': [{'d': circle_arrow(128, 190, 94, -120, -74, True), 'both': True}],
}
TITLES['nao'] = 'Sinal de não em Libras'
