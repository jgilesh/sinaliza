# OK: the letters O then K spelled with the hand raised beside the shoulder, palm forward (UFSC
# Signbank; the INES video is missing). The O is seen from the thumb side, so its round opening
# reads; the K turns a little back toward the viewer, its middle finger pointing forward.


def hs_ok_K():
    """K of Libras: index straight up, middle finger straight and bent forward at the knuckle (toward
    the palm side), ring and little fingers folded; the thumb tip rests on the middle finger's first
    phalanx, between the index and the middle finger."""
    shape = fist({'index': fing(3, 0, 0, 0), 'middle': fing(-3, 80, 6, 4)})
    # The thumb tip sits in the gap in front of the index and middle knuckles, on the middle finger.
    shape['thumb'] = solve_thumb((7.5, -39.5, 8.5), pad_to=(-0.5, 0.0, -0.5), point=(-0.2, -0.8, 0.5),
                                 pref=(-5.0, 35.0, 40.0, 15.0, 20.0))
    return shape


_ok_O, _ok_K = hs_O(), hs_ok_K()
TITLES['ok'] = 'Sinal de ok em Libras'


def _ok_pose(shape, at=(128, 168), yaw=-62, roll=-4, pitch=0):
    return P(at, shape, 'wrist', yaw=yaw, pitch=pitch, roll=roll, scale=1.15, depth=55, pole=(0.5, 1.0, 0.4))


SIGNS['ok'] = {
    'poster': 1.5, 'dur': 2.4, 'hands': ['right'], 'handshape': _ok_K, 'handshape_view': {'yaw': -60},
    # O held, then the fingers open into K (the index rises, the middle finger points forward).
    'keys': [(0.0, [_ok_pose(_ok_O, yaw=-100, roll=0, pitch=15)]), (0.7, [_ok_pose(_ok_O, yaw=-100, roll=0, pitch=15)]), (1.05, [_ok_pose(_ok_K, (126, 166))]),
             (2.0, [_ok_pose(_ok_K, (126, 166))]), (2.4, [_ok_pose(_ok_O, yaw=-100, roll=0, pitch=15)])],
}
