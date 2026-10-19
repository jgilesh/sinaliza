# INCOMODAR: the support hand lies open, palm up, in front of the waist, fingers toward the signing
# side. The signing hand, open with the thumb apart, stands on its little-finger edge on the support
# palm: it starts tipped over across it and rises to upright, fingers up, knocking its edge on the
# palm, twice. Annoyed face. (UFSC Signbank INCOMODAR: B2, support palm; INES INCOMODAR.)

_incomodar_b = hs_B()
# Support hand (a right-hand pose, mirrored): palm up, tipped toward the viewer, fingers toward the
# signing side.
_incomodar_base = mirrored(P((160, 240), _incomodar_b, 'wrist', yaw=-38, pitch=0, roll=96, scale=1.05, depth=55))
_incomodar_pole = (0.35, 1.0, 0.4)
# Upright: fingers up, palm toward the midline and the viewer, the little-finger edge on the palm.
_incomodar_up = P((216, 220), _incomodar_b, 'wrist', yaw=55, pitch=0, roll=0, scale=1.0, depth=60, pole=_incomodar_pole)
# Tipped over across the support hand: fingers toward the other side and up, palm up.
_incomodar_down = P((210, 224), _incomodar_b, 'wrist', yaw=35, pitch=0, roll=58, scale=1.0, depth=60, pole=_incomodar_pole)
_incomodar_keys = [(0.0, _incomodar_down), (0.35, _incomodar_down), (0.65, _incomodar_up), (0.95, _incomodar_down),
                   (1.25, _incomodar_up), (1.9, _incomodar_up), (2.4, _incomodar_down)]
SIGNS['incomodar'] = {
    'poster': 0.65, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _incomodar_b,
    'keys': [(t, [p, _incomodar_base]) for t, p in _incomodar_keys],
    # The hand tips up from across the palm to upright and back (repeated).
    'arrows': [{'d': circle_arrow(214, 224, 82, -80, -40, True), 'both': True}],
    'marks': [(236, 240, 150)],
    'mirror_second': True,
}
TITLES['incomodar'] = 'Sinal de incomodar em Libras'
