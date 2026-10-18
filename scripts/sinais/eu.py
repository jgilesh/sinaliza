# EU: index hand (1), the fingertip comes to the middle of the chest and touches it once.
# The fist sits a little to the signer's right with the back of the hand to the viewer and the index
# pointing across and in toward the chest, so the finger reads in profile instead of hiding behind
# the hand (INES: EU).
eu_one = hs_1()
eu_pose = lambda at, scale, pitch: P(at, eu_one, 'index_tip', yaw=180, pitch=pitch, roll=80, scale=scale, depth=45,
                                     pole=(0.15, 1.0, 0.6))
eu_off = eu_pose((186, 204), 1.24, 10)
eu_on = eu_pose((201, 218), 1.14, -12)
SIGNS['eu'] = {
    'poster': 0.8, 'dur': 2.0, 'hands': ['right'], 'handshape': eu_one,
    'keys': [(0.0, [eu_off]), (0.2, [eu_off]), (0.5, [dict(eu_on, ease='out')]), (1.5, [eu_on]), (2.0, [eu_off])],
    'marks': [(208, 214, 55)],
    'arrows': [{'d': 'M 176 186 Q 192 182 199 196'}],
}
TITLES['eu'] = 'Sinal de eu em Libras'
