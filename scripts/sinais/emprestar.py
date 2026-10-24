# EMPRESTAR: the support hand closed (S), palm down, in front of the chest. The signing hand in V
# (index and middle up and apart) makes a short arc and lands with the base of the fingers on the back
# of the fist, the wrist turning so the palm faces up as it arrives. Contact at the end, once.
# (UFSC Signbank EMPRESTAR: V on S, back of the weak hand, arc, supination; INES EMPRESTAR agrees.)

_emprestar_v, _emprestar_s = hs_V(), hs_S()
# Support fist, defined as a right hand (palm down, knuckles toward the midline) and mirrored.
_emprestar_base = mirrored(P((146, 254), _emprestar_s, 'wrist', yaw=115, pitch=-10, roll=80, scale=1.2, depth=60,
                             pole=(0.5, 1.0, 0.3)))
# Start: above and nearer the body, the back of the V hand to the viewer, fingers up and leaning out.
_emprestar_up = P((150, 222), _emprestar_v, 'wrist', yaw=160, pitch=20, roll=-20, scale=1.08, depth=50,
                  pole=(0.45, 1.0, 0.4))
# Landed: the heel of the fingers on the back of the fist, palm turned up and toward the viewer, the two
# fingers pointing up and across the body.
_emprestar_on = P((214, 230), _emprestar_v, 'wrist', yaw=-10, pitch=-15, roll=30, scale=1.12, depth=66,
                  pole=(0.3, 1.0, 0.5), via=(182, 230), ease='in')
SIGNS['emprestar'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _emprestar_v,
    'keys': [(0.0, [_emprestar_up, _emprestar_base]), (0.3, [_emprestar_up, _emprestar_base]),
             (0.85, [_emprestar_on, _emprestar_base]), (1.8, [_emprestar_on, _emprestar_base]),
             (2.4, [dict(_emprestar_up, via=(200, 214), ease='smooth'), _emprestar_base])],
    'marks': [(262, 244, 60)],
    # The arc over to the back of the fist.
    'arrows': [{'d': 'M 162 192 Q 188 170 204 196'}],
    'mirror_second': True,
}
TITLES['emprestar'] = 'Sinal de emprestar em Libras'
