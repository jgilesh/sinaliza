# VIAJAR: fingertips bunched on the thumb (O) beside the chin on the signing side, palm toward the
# head and the fingertips toward it; the hand travels once in a diagonal up and out to above the
# head, the fingers opening into a loose claw on the way. (UFSC Signbank VIAJAR.)


def hs_viajar_claw():
    """Loose claw: fingers spread a little and curved (bent at every joint), the thumb apart and
    curved: the O opened."""
    return {'index': fing(10, 25, 40, 25), 'middle': fing(2, 25, 42, 26), 'ring': fing(-6, 27, 42, 26),
            'pinky': fing(-13, 30, 40, 24), 'thumb': (32.0, 32.0, 25.0, 15.0, 20.0)}


_via_o, _via_claw = hs_O(), hs_viajar_claw()
# Palm toward the head, turned a little to the viewer and seen a little from below, so the bunched
# fingertips and the thumb show; the fingers lean in toward the face.
_via_on = P((138, 168), _via_o, 'wrist', yaw=70, pitch=-15, roll=12, scale=1.1, depth=45,
            pole=(0.6, 1.0, 0.45))
_via_off = P((108, 72), _via_claw, 'wrist', yaw=35, pitch=-10, roll=8, scale=1.1, depth=70,
             pole=(0.6, 1.0, 0.45), ease='out')
SIGNS['viajar'] = {
    'poster': 0.2, 'dur': 2.4, 'hands': ['right'], 'handshape': _via_o, 'handshape_view': {'yaw': 60, 'pitch': -20},
    'keys': [(0.0, [_via_on]), (0.4, [_via_on]), (1.0, [_via_off]), (1.9, [_via_off]),
             (2.4, [dict(_via_on, ease='smooth')])],
    # Outside the hand's path: up and out, once.
    'arrows': [{'d': 'M 130 128 L 113 94'}],
}
TITLES['viajar'] = 'Sinal de viajar em Libras'
