# NASCER: both hands flat (B), fingers together, by the belly with the fingers down and the palms toward
# the body; they swing down and forward in an arc, turning, and end in front of the lower chest with the
# fingers up and the palms facing each other. Once. (UFSC Signbank NASCER: B+B, espaço neutro; INES
# NASCER agrees.)
_nascer_b = hs_B()
_nascer_pole = (0.35, 1.0, 0.4)
# By the belly: fingers down, palms toward the body and the midline.
_nascer_in = P((145, 220), _nascer_b, 'wrist', yaw=30, pitch=180, roll=-8, scale=1.05, depth=50, pole=_nascer_pole)
# Halfway: low and forward, the fingers pointing at the viewer, palms facing each other.
_nascer_mid = P((152, 248), _nascer_b, 'wrist', yaw=75, pitch=100, roll=0, scale=1.15, depth=85, pole=_nascer_pole,
                ease='linear')
# End: in front of the lower chest, fingers up, palms facing each other (turned a little to the viewer).
_nascer_out = P((150, 238), _nascer_b, 'wrist', yaw=65, pitch=0, roll=2, scale=1.15, depth=85, pole=_nascer_pole,
                ease='out')
SIGNS['nascer'] = {
    'poster': 1.3, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _nascer_b,
    'keys': [(0.0, [_nascer_in, mirrored(_nascer_in)]), (0.35, [_nascer_in, mirrored(_nascer_in)]),
             (0.75, [_nascer_mid, mirrored(_nascer_mid)]), (1.1, [_nascer_out, mirrored(_nascer_out)]),
             (1.9, [_nascer_out, mirrored(_nascer_out)]), (2.6, [_nascer_in, mirrored(_nascer_in)])],
    'arrows': [{'d': 'M 120 214 C 100 272, 124 292, 130 250'}, {'d': 'M 280 214 C 300 272, 276 292, 270 250'}],
    'mirror_second': True,
}
TITLES['nascer'] = 'Sinal de nascer em Libras'
