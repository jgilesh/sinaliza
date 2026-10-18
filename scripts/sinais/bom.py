# BOM: fingertips together on the thumb (O / "bico") in front of the mouth, palm toward the mouth;
# the hand moves forward and down and opens into a 5, ending palm up in front of the chest. No
# contact. (INES BOM1; Signbank 389: O+5, boca, sem contato.)
bom_o, bom_5 = HANDSHAPES['O'](), HANDSHAPES['5']()
# Start: the bunched fingertips just in front of the mouth, the back of the hand turned toward the
# viewer's left, so the rounded O shows in profile beside the chin.
bom_start = P((191, 137), bom_o, 'pinch', yaw=60, pitch=-40, roll=12, scale=1.0, depth=40, pole=(0.5, 1.0, 0.45))
# End: palm up and tipped toward the viewer, fingers spread forward and out.
# Halfway: the hand moves forward and down, opening, the palm turning up.
bom_mid = P((166, 182), lerp(bom_o, bom_5, 0.55), 'wrist', yaw=55, pitch=5, roll=-55, scale=1.1, depth=65, ease='in')
bom_end = P((150, 214), bom_5, 'wrist', yaw=48, pitch=42, roll=-105, scale=1.15, depth=80, ease='out')
bom_back = dict(bom_start, ease='smooth')
SIGNS['bom'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right'], 'handshape': bom_o, 'handshape_view': {'yaw': 60, 'pitch': -40},
    'keys': [(0.0, [bom_start]), (0.4, [bom_start]), (0.7, [bom_mid]), (1.0, [bom_end]), (1.9, [bom_end]), (2.4, [bom_back])],
    'arrows': [{'d': 'M 202 158 Q 202 192 176 212'}],
}
TITLES['bom'] = 'Sinal de bom em Libras'
