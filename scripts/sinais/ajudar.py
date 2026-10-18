# AJUDAR: both hands flat (B), fingers together. The support hand lies across in front of the
# chest, palm up; the signing hand stands upright on it, palm forward and fingers up, the heel of
# the hand on the support hand. Both hands move forward together, once, as if pushing.
# (UFSC Signbank AJUDAR.)

_ajudar_b = hs_B()


def _ajudar_pair(dy, scale, depth):
    # Support hand, defined as a right hand (palm up, fingers toward the midline) and mirrored.
    base = mirrored(P((136, 238 + dy), _ajudar_b, 'wrist', yaw=-45, pitch=0, roll=84, scale=scale, depth=depth))
    top = P((192, 228 + dy), _ajudar_b, 'wrist', yaw=12, pitch=0, roll=-4, scale=scale, depth=depth + 6,
            pole=(0.35, 1.0, 0.4))
    return [top, base]


_ajudar_a, _ajudar_z = _ajudar_pair(0, 1.05, 50), _ajudar_pair(12, 1.2, 90)
SIGNS['ajudar'] = {
    'poster': 0.4, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _ajudar_b,
    'keys': [(0.0, _ajudar_a), (0.4, _ajudar_a), (1.0, _ajudar_z), (1.8, _ajudar_z), (2.4, _ajudar_a)],
    'arrows': [{'d': 'M 230 168 L 246 196'}],
    'mirror_second': True,
}
TITLES['ajudar'] = 'Sinal de ajudar em Libras'
