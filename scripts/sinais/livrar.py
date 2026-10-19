# LIVRAR: both hands with the thumb and index in a ring and the other fingers straight (F of ASL),
# the two rings hooked together in front of the chin; the hands let go and move apart to the sides
# of the head, opening wide, palms forward. Once. (UFSC Signbank LIVRAR: T[ASL_F] both hands; the
# INES LIVRAR video shows another variant.)


def hs_livrar_ring():
    """Ring: index curled onto the thumb, pad on pad; the other three straight and a little apart."""
    shape = {'index': fing(2, 50, 75, 52), 'middle': fing(0, 0, 4, 3), 'ring': fing(-6, 2, 4, 3),
             'pinky': fing(-13, 4, 5, 3)}
    shape['thumb'] = pinch_thumb(shape)
    return shape


_livrar_ring, _livrar_open = hs_livrar_ring(), hs_5()
# Rings hooked in front of the chin and neck: palms turned toward each other, seen a little from
# below so the two openings show; the index fingers meet in the middle.
_livrar_on = P((199, 172), _livrar_ring, 'pinch', yaw=75, pitch=-20, roll=10, scale=1.0, depth=50,
               ring=True, pole=(0.5, 1.0, 0.45))
# Open at the side of the head, palm forward.
_livrar_off = P((104, 120), _livrar_open, 'wrist', yaw=5, pitch=0, roll=-14, scale=1.05, depth=55,
                pole=(0.6, 1.0, 0.45), ease='out', ring=None)
# The rings let go: the shading of the opening stops here (None switches it off without fading).
_livrar_free = dict(_livrar_on, ring=None)
SIGNS['livrar'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _livrar_ring, 'handshape_ring': True,
    'handshape_view': {'yaw': 50, 'roll': -10},
    'keys': [(0.0, [_livrar_on, mirrored(_livrar_on)]), (0.45, [_livrar_on, mirrored(_livrar_on)]),
             (0.5, [_livrar_free, mirrored(_livrar_free)]),
             (0.95, [_livrar_off, mirrored(_livrar_off)]), (1.9, [_livrar_off, mirrored(_livrar_off)]),
             (2.3, [dict(_livrar_free, ease='smooth'), dict(mirrored(_livrar_free), ease='smooth')]),
             (2.4, [_livrar_on, mirrored(_livrar_on)])],
    'arrows': [{'d': 'M 172 186 Q 130 190 112 152'}, {'d': 'M 228 186 Q 270 190 288 152'}],
    'mirror_second': True,
}
TITLES['livrar'] = 'Sinal de livrar em Libras'
