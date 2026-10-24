# INFLUENCIAR: the support hand holds its index up in front of the chest, palm toward the signer. The
# dominant hand, in a claw (fingers spread and curved), is above it at chin height, fingertips toward
# that index, and pushes toward it in small moves, three times; the support hand stays still.
# (UFSC Signbank INFLUENCIAR: 5_claw and 1; the INES video shows another variant.)


def hs_influenciar_claw():
    """5 claw: the fingers spread and bent at every joint, the thumb bent and apart."""
    return {'index': fing(13, 22, 58, 38), 'middle': fing(3, 22, 60, 40), 'ring': fing(-7, 22, 60, 40),
            'pinky': fing(-16, 24, 58, 38), 'thumb': (45.0, 20.0, 15.0, 25.0, 35.0)}


_inf_claw, _inf_one = hs_influenciar_claw(), hs_1()
# Support (defined as a right hand, then mirrored): index up, back of the hand turned to the viewer.
_inf_sup = mirrored(P((170, 240), _inf_one, 'wrist', yaw=150, pitch=0, roll=4, scale=1.05, depth=60))
# Dominant: up and to its own side of the index, palm forward and a little down, the curved fingertips
# pointing down and across at the index tip.
_inf_claw_at = lambda k: P((168 + 7 * k, 150 + 5 * k), _inf_claw, 'wrist', yaw=10, pitch=25, roll=115, scale=1.0,
                           depth=55 + 10 * k, pole=(0.5, 1.0, 0.45), ease='smooth')
_inf_back, _inf_push = _inf_claw_at(0), _inf_claw_at(1)
_inf_keys = [(0.0, [_inf_back, _inf_sup]), (0.3, [_inf_back, _inf_sup])]
for _inf_i in range(3):
    _inf_keys += [(0.5 + 0.4 * _inf_i, [_inf_push, _inf_sup]), (0.7 + 0.4 * _inf_i, [_inf_back, _inf_sup])]
_inf_keys.append((2.2, [_inf_back, _inf_sup]))
SIGNS['influenciar'] = {
    'poster': 0.5, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _inf_claw, 'handshape_view': {'yaw': 0},
    'keys': _inf_keys,
    'arrows': [{'d': 'M 150 196 L 166 206', 'both': True}],
}
TITLES['influenciar'] = 'Sinal de influenciar em Libras'
