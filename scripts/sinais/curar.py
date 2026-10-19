# CURAR: the support hand open and flat (B) across in front of the chest, palm toward the body. The
# signing hand, open, touches the support palm with its fingertips, then rises to beside the head, the
# fingers spread, and there closes the index onto the thumb in a ring, the other fingers staying open (F).
# Once. (UFSC Signbank CURAR: 5 -> F / B, on the support palm. The INES CURAR video shows another sign:
# both fists at the shoulders moving down, as in "strong, healthy".)

_curar_b = hs_B()
_curar_5 = hs_5()
_curar_f = hs_F()


def hs_curar_soft():
    """Open hand relaxed, the fingers a little bent and together, as it brushes the support palm."""
    return {'index': fing(6, 25, 30, 18), 'middle': fing(1, 25, 30, 18), 'ring': fing(-4, 25, 30, 18),
            'pinky': fing(-9, 28, 30, 18), 'thumb': (30.0, 20.0, 10.0, 8.0, 8.0)}


_curar_soft = hs_curar_soft()
# Support hand (a right-hand pose, mirrored): fingers pointing across, palm toward the body and tipped
# up a little, thumb on top.
_curar_sup = mirrored(P((168, 246), _curar_b, 'wrist', yaw=212, pitch=0, roll=88, scale=1.1, depth=70,
                        pole=(0.3, 1.0, 0.45)))
_curar_pole = (0.6, 1.0, 0.4)
# Signing hand: fingertips down on the support palm, back of the hand to the viewer...
_curar_on = P((200, 236), _curar_soft, 'fingertips', yaw=165, pitch=-25, roll=150, scale=1.08, depth=60,
              pole=(0.45, 1.0, 0.45))
# ...then up beside the head, palm forward, fingers spread...
_curar_open = P((124, 166), _curar_5, 'wrist', yaw=10, pitch=0, roll=-6, scale=1.08, depth=50, pole=_curar_pole,
                via=(118, 222), ease='out')
# ...and the index closes onto the thumb (F).
_curar_ring = dict(_curar_open, shape=_curar_f, yaw=25, via=None)
del _curar_ring['via']
_curar_back = dict(_curar_on, via=(130, 226))
SIGNS['curar'] = {
    'poster': 2.0, 'dur': 2.9, 'hands': ['right', 'left'], 'handshape': _curar_f, 'handshape_view': {'yaw': 40},
    'keys': [(0.0, [_curar_on, _curar_sup]), (0.4, [_curar_on, _curar_sup]), (0.95, [_curar_open, _curar_sup]),
             (1.3, [_curar_open, _curar_sup]), (1.6, [_curar_ring, _curar_sup]), (2.4, [_curar_ring, _curar_sup]),
             (2.9, [_curar_back, _curar_sup])],
    # Outside the path: up from the support palm to beside the head.
    'arrows': [{'d': 'M 160 250 Q 112 236 102 178'}],
    # Where the fingertips touch the support palm.
    'marks': [(196, 222, 10)],
    # The support hand is drawn in front: the signing fingertips touch its palm, on the body side.
}
TITLES['curar'] = 'Sinal de curar em Libras'
