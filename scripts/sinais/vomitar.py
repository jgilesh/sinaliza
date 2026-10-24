# VOMITAR: closed fist (S) at the mouth, palm toward the face; the hand leaves the mouth forward and
# down and opens all at once into a spread hand (5), palm down, in front of the chest, showing what
# comes out of the mouth. Once. (UFSC Signbank VOMITAR: S+5, mouth; INES VOMITAR: the same path, ending
# with the palm up.)

_vomitar_s, _vomitar_5 = hs_S(), hs_5()
# At the mouth: below the nose (eyes clear), the back of the fist to the viewer, knuckles up and the
# thumb across the folded fingers turned a little to the viewer.
_vomitar_on = P((188, 161), _vomitar_s, 'wrist', yaw=230, pitch=0, roll=20, scale=1.08, depth=34, pole=(0.4, 1.0, 0.45))
# Out and down: spread fingers pointing forward and toward the midline, palm down, the back of the hand
# tipped toward the viewer so every finger reads.
_vomitar_off = P((144, 220), _vomitar_5, 'wrist', yaw=130, pitch=30, roll=80, scale=1.12, depth=70,
                 pole=(0.4, 1.0, 0.45), via=(160, 196), ease='out')
SIGNS['vomitar'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right'], 'handshape': _vomitar_s, 'handshape_view': {'yaw': -30},
    'keys': [(0.0, [_vomitar_on]), (0.4, [_vomitar_on]), (0.85, [_vomitar_off]), (1.7, [_vomitar_off]),
             (2.4, [dict(_vomitar_on, via=(140, 180), ease='smooth')])],
    'marks': [(212, 128, 70)],
    # Out of the mouth, forward and down, on the outer side of the path.
    'arrows': [{'d': 'M 160 142 Q 112 150 116 204'}],
}
TITLES['vomitar'] = 'Sinal de vomitar em Libras'
