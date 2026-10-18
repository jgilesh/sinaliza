# MEU / MINHA: flat hand (B, thumb open) comes to the middle of the chest and rests there a moment, palm on
# the chest, fingers pointing across to the signer's left, thumb up. Seen from the back of the hand
# (INES MEU1 and UFSC Signbank agree).
meu_b = hs_B()
meu_pose = lambda at, scale, pitch: P(at, meu_b, 'wrist', yaw=180, pitch=pitch, roll=84, scale=scale, depth=40,
                                      pole=(0.2, 1.0, 0.55))
meu_off = meu_pose((150, 222), 1.12, -20)
meu_on = meu_pose((160, 232), 1.02, 0)
SIGNS['meu'] = {
    'poster': 0.9, 'dur': 2.0, 'hands': ['right'], 'handshape': meu_b,
    'keys': [(0.0, [meu_off]), (0.2, [meu_off]), (0.55, [dict(meu_on, ease='out')]), (1.5, [meu_on]), (2.0, [meu_off])],
    'marks': [(207, 213, 15)],
}
TITLES['meu'] = 'Sinal de meu em Libras'
