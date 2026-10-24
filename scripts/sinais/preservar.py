# PRESERVAR: both hands in claws (fingers apart and curved), fingertips at the corners of the mouth,
# palms toward the face; the hands close into fists and come down together to just under the chin,
# where the fists rest against the jaw. Once. (UFSC Signbank PRESERVAR: 5 garra > S, boca. The INES
# video shows another variant: open hands sweeping out from the mouth.)


def hs_preservar_claw():
    """Claw: all fingers spread and curved at every joint, the thumb curved opposite them."""
    return {'index': fing(12, 30, 55, 40), 'middle': fing(3, 30, 58, 42), 'ring': fing(-6, 32, 58, 42),
            'pinky': fing(-15, 34, 55, 40), 'thumb': (30.0, 30.0, 20.0, 20.0, 30.0)}


_preservar_claw, _preservar_s = hs_preservar_claw(), hs_S()
# Claw at the corner of the mouth: palm toward the face and the midline, seen from the back and the
# little-finger side, so the curved fingers show their side.
_preservar_on = P((168, 130), _preservar_claw, 'fingertips', yaw=125, pitch=0, roll=-18, scale=1.0, depth=40,
                  pole=(0.55, 1.0, 0.45))
# Fist under the jaw: palm toward the body, knuckles up, the back of the hand to the viewer.
_preservar_off = P((184, 168), _preservar_s, 'wrist', yaw=160, pitch=0, roll=-8, scale=1.0, depth=40,
                   pole=(0.55, 1.0, 0.45))
SIGNS['preservar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _preservar_claw,
    'handshape_view': {'yaw': 10, 'pitch': -20},
    'keys': [(0.0, [_preservar_on, mirrored(_preservar_on)]), (0.4, [_preservar_on, mirrored(_preservar_on)]),
             (0.95, [_preservar_off, mirrored(_preservar_off)]), (1.9, [_preservar_off, mirrored(_preservar_off)]),
             (2.4, [_preservar_on, mirrored(_preservar_on)])],
    'arrows': [{'d': 'M 136 132 L 136 164'}, {'d': 'M 264 132 L 264 164'}],
    'mirror_second': True,
}
TITLES['preservar'] = 'Sinal de preservar em Libras'
