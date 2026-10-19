# ESTRAGAR: both hands closed in S. The signing hand starts raised beside the head, the other in
# front of the chest. The raised hand comes down, scraping past the thumb side of the other hand, and
# goes on down at the side of the body, while the other hand rises to in front of the chin: the hands
# swap heights, once. (UFSC Signbank ESTRAGAR.)

_estr_s = hs_S()
_estr_pole = (0.45, 1.0, 0.45)
# Signing hand: raised beside the head, palm turned toward the midline and the viewer.
_estr_r_up = P((140, 120), _estr_s, 'wrist', yaw=40, pitch=0, roll=-6, scale=1.08, depth=45, pole=_estr_pole)
# ...down past the other hand, to low at the side.
_estr_r_down = P((140, 242), _estr_s, 'wrist', yaw=40, pitch=10, roll=-10, scale=1.12, depth=70, pole=_estr_pole,
                 via=(166, 206), ease='linear')
# Other hand (a right-hand pose, mirrored): in front of the chest, palm toward the body, thumb on top...
_estr_l_low = P((186, 226), _estr_s, 'wrist', yaw=150, pitch=0, roll=70, scale=1.1, depth=60, pole=(0.3, 1.0, 0.45))
# ...rising to in front of the chin.
_estr_l_up = P((190, 172), _estr_s, 'wrist', yaw=150, pitch=0, roll=60, scale=1.1, depth=55, pole=(0.3, 1.0, 0.45),
               ease='linear')
_estr_a = [_estr_r_up, mirrored(_estr_l_low)]
_estr_z = [_estr_r_down, mirrored(_estr_l_up)]
_estr_back = [dict(_estr_r_up, via=(96, 180), ease='smooth'), dict(mirrored(_estr_l_low), ease='smooth')]
SIGNS['estragar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _estr_s,
    'keys': [(0.0, _estr_a), (0.4, _estr_a), (1.1, _estr_z), (1.9, _estr_z), (2.4, _estr_back)],
    # The signing hand comes down (outside, on its side); the other goes up (on its side).
    'arrows': [{'d': 'M 104 104 Q 94 168 112 228'}, {'d': 'M 258 236 L 258 178'}],
    # Where the falling hand scrapes past the other hand's thumb side.
    'marks': [(170, 172, -50)],
    'marks_under': True,
    'mirror_second': True,
}
TITLES['estragar'] = 'Sinal de estragar em Libras'
