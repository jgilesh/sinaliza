# PROIBIR: both hands with the index finger out (1). The support hand holds still in front of the chin,
# its index horizontal, pointing toward the dominant side. The dominant hand starts beside the head, the
# index at the temple, and comes down fast, crossing in front of the support index, and stops just below
# it, its index pointing to the other side. Once. (UFSC Signbank PROIBIR: 1, 2 hands.)
_proi_1 = hs_1()
# Support (left) hand, given as its right-hand twin: back of the hand to the viewer, index horizontal on
# top of the folded fingers, pointing to the dominant side.
_proi_base = mirrored(P((210, 156), _proi_1, 'index_tip', yaw=180, pitch=0, roll=90, scale=1.05, depth=60,
                        pole=(0.4, 1.0, 0.4)))
# Dominant: index at the temple, leaning in, the hand outside the face, palm toward the face.
_proi_top = P((163, 88), _proi_1, 'index_tip', yaw=70, pitch=0, roll=16, scale=1.0, depth=42, pole=(0.6, 1.0, 0.5))
# End: just below the support index, palm down and back of the hand half to the viewer, index pointing
# to the other side.
_proi_end = P((210, 180), _proi_1, 'index_tip', yaw=125, pitch=0, roll=90, scale=1.05, depth=70, pole=(0.45, 1.0, 0.4),
              via=(170, 160), ease='in')
SIGNS['proibir'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _proi_1,
    'keys': [(0.0, [_proi_top, _proi_base]), (0.3, [_proi_top, _proi_base]), (0.6, [_proi_end, _proi_base]),
             (1.8, [_proi_end, _proi_base]), (2.4, [dict(_proi_top, via=(140, 140), ease='smooth'), _proi_base])],
    'arrows': [{'d': 'M 118 122 Q 112 190 146 228'}],
    'mirror_second': True,
}
TITLES['proibir'] = 'Sinal de proibir em Libras'
