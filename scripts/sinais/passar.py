# PASSAR: the support hand lies open in front of the chest, palm up. The signing hand, flat (B) and
# upright, palm toward the other side, starts by the mouth and comes straight down until it passes
# over the support palm. Once. (UFSC Signbank PASSAR; INES PASSAR shows the hand swinging up from
# the chest first.)
_passar_b = hs_B()
_passar_pole = (0.4, 1.0, 0.45)
# Support hand (defined as a right hand, then mirrored): palm up, fingers toward the midline.
_passar_base = mirrored(P((144, 260), _passar_b, 'wrist', yaw=-50, pitch=0, roll=92, scale=1.1, depth=70))
# Upright by the mouth: fingers up, the palm toward the midline and a little to the viewer.
_passar_up = P((182, 197), _passar_b, 'wrist', yaw=60, pitch=0, roll=6, scale=1.0, depth=45, pole=_passar_pole)
# Down: still upright, its edge passing over the support palm.
_passar_down = P((210, 256), _passar_b, 'wrist', yaw=60, pitch=0, roll=6, scale=1.1, depth=85, ease='in',
                 pole=_passar_pole)
SIGNS['passar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _passar_b,
    'keys': [(0.0, [_passar_up, _passar_base]), (0.3, [_passar_up, _passar_base]),
             (0.9, [_passar_down, _passar_base]), (1.8, [_passar_down, _passar_base]),
             (2.4, [dict(_passar_up, ease='smooth'), _passar_base])],
    'arrows': [{'d': 'M 146 156 L 168 200'}],
    'mirror_second': True,
}
TITLES['passar'] = 'Sinal de passar em Libras'
