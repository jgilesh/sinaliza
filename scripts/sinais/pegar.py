# PEGAR: open clawed hand raised in front, at face height on the signing side, palm forward; it
# snaps shut into a fist (S), as if grabbing something, and comes a little down and forward to
# shoulder height. Once. (UFSC Signbank PEGAR; INES PEGAR1.)


def hs_pegar_claw():
    """5 claw: fingers spread and curved (bent a little at the knuckles, more at the middle and end
    joints), the thumb out to the side and curved too."""
    return {'index': fing(13, 18, 66, 42), 'middle': fing(3, 18, 68, 44),
            'ring': fing(-7, 20, 66, 42), 'pinky': fing(-17, 22, 62, 40),
            'thumb': (45.0, 8.0, 10.0, 22.0, 30.0)}


_peg_claw, _peg_s = hs_pegar_claw(), hs_S()
# Palm forward and turned a little toward the midline, seen slightly from below: the curved fingers
# show in half profile.
_peg_open = P((126, 132), _peg_claw, 'wrist', yaw=-35, pitch=-10, roll=-10, scale=1.1, depth=60,
              pole=(0.6, 1.0, 0.45))
_peg_shut = P((128, 140), _peg_s, 'wrist', yaw=-30, pitch=-5, roll=-8, scale=1.12, depth=62,
              pole=(0.6, 1.0, 0.45), ease='out')
_peg_down = P((134, 170), _peg_s, 'wrist', yaw=-20, pitch=0, roll=-6, scale=1.18, depth=80,
              pole=(0.6, 1.0, 0.45))
SIGNS['pegar'] = {
    'poster': 0.3, 'dur': 2.2, 'hands': ['right'], 'handshape': _peg_claw,
    'keys': [(0.0, [_peg_open]), (0.4, [_peg_open]), (0.55, [_peg_shut]), (0.95, [_peg_down]),
             (1.8, [_peg_down]), (2.2, [dict(_peg_open, ease='smooth')])],
    # Beside the hand, on the outer side: a short move down (and a little forward).
    'arrows': [{'d': 'M 90 124 Q 86 144 94 162'}],
}
TITLES['pegar'] = 'Sinal de pegar em Libras'
