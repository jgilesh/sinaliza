# EMPURRAR: both hands open with the fingers spread (5), palms forward and fingers up, in front of
# the chest; they move forward together, once, with force, as if pushing something.
# (UFSC Signbank EMPURRAR, INES EMPURRAR.)



def hs_empurrar_5():
    """5 with the thumb a little closer to the index, so the two thumbs stay apart."""
    shape = hs_5()
    shape['thumb'] = (26.0, 14.0, 6.0, 6.0, 4.0)
    return shape


_empurrar_5 = hs_empurrar_5()
_empurrar_near = P((150, 240), _empurrar_5, 'wrist', yaw=0, pitch=0, roll=-12, scale=1.02, depth=40, pole=(0.4, 1.0, 0.4))
_empurrar_far = P((138, 242), _empurrar_5, 'wrist', yaw=0, pitch=0, roll=-14, scale=1.28, depth=115, ease='out',
                  pole=(0.4, 1.0, 0.4))
SIGNS['empurrar'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _empurrar_5,
    'keys': [(0.0, [_empurrar_near, mirrored(_empurrar_near)]), (0.5, [_empurrar_near, mirrored(_empurrar_near)]),
             (0.85, [_empurrar_far, mirrored(_empurrar_far)]), (1.7, [_empurrar_far, mirrored(_empurrar_far)]),
             (2.4, [dict(_empurrar_near, ease='smooth'), mirrored(dict(_empurrar_near, ease='smooth'))])],
    # Forward, toward the viewer: short arrows down and out from each hand.
    'arrows': [{'d': 'M 92 206 L 76 228'}, {'d': 'M 308 206 L 324 228'}],
    'mirror_second': True,
}
TITLES['empurrar'] = 'Sinal de empurrar em Libras'
