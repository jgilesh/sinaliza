# DEIXAR: both hands raised at shoulder height, palms forward, the thumb holding the bent middle
# finger (the other fingers straight and spread). The hands move forward and down and open, as if
# letting something go, ending palms down with the fingers spread. Once. (UFSC Signbank DEIXAR;
# the INES DEIXAR1 video shows a one-handed variant beside the head.)


def hs_deixar_flick():
    """Spread hand with the middle finger bent forward and its tip held by the thumb pad."""
    shape = {'index': fing(12, 0, 4, 2), 'middle': fing(0, 60, 65, 40), 'ring': fing(-8, 0, 4, 2),
             'pinky': fing(-18, 0, 5, 3)}
    shape['thumb'] = pinch_thumb(shape, ('middle',))
    return shape


_deixar_hold, _deixar_open = hs_deixar_flick(), hs_5()
_deixar_up = P((120, 190), _deixar_hold, 'wrist', yaw=0, pitch=-8, roll=-8, scale=1.05, depth=50, pole=(0.5, 1.0, 0.4))
# Halfway the hand tips forward (fingers toward the viewer) and starts to open.
_deixar_mid = P((124, 200), lerp(_deixar_hold, _deixar_open, 0.5), 'wrist', yaw=0, pitch=66, roll=0, scale=1.1,
                depth=75, ease='in')
# End: palm down, the back of the hand toward the viewer and up, the spread fingers pointing forward,
# down and a little out.
_deixar_down = P((126, 206), _deixar_open, 'wrist', yaw=0, pitch=132, roll=16, scale=1.15, depth=100, ease='out')
_deixar_k = lambda p: [p, mirrored(p)]
SIGNS['deixar'] = {
    'poster': 0.0, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _deixar_hold,
    'keys': [(0.0, _deixar_k(_deixar_up)), (0.5, _deixar_k(_deixar_up)), (0.75, _deixar_k(_deixar_mid)),
             (1.0, _deixar_k(_deixar_down)), (1.9, _deixar_k(_deixar_down)), (2.6, _deixar_k(dict(_deixar_up, ease='smooth')))],
    # Forward and down, beside each hand (outside it).
    'arrows': [{'d': 'M 70 150 Q 62 190 84 214'}, {'d': 'M 330 150 Q 338 190 316 214'}],
    'mirror_second': True,
}
TITLES['deixar'] = 'Sinal de deixar em Libras'
