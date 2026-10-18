# SENTIR: clawed open hand, palm toward the body, the fingertips (above all the middle finger) on
# the chest, with small quick movements while they stay in contact.


def hs_sentir_claw():
    """5 claw: fingers spread and curved, the middle finger reaching a little further."""
    return {'index': fing(14, 12, 50, 34), 'middle': fing(3, 8, 44, 30), 'ring': fing(-8, 14, 50, 34),
            'pinky': fing(-18, 18, 50, 34), 'thumb': (42.0, 12.0, 15.0, 15.0, 25.0)}


_sent_h = hs_sentir_claw()
_sent = lambda at, roll: P(at, _sent_h, 'middle_tip', yaw=150, pitch=-15, roll=roll, scale=1.12, depth=28,
                           pole=(0.5, 1.0, 0.4))
_sent_off = _sent((190, 200), 100)
_sent_a, _sent_b = _sent((200, 206), 104), _sent((200, 202), 110)
_sent_keys = [(0.0, [_sent_off]), (0.3, [_sent_a])]
for _sent_i in range(5):
    _sent_keys += [(0.42 + 0.24 * _sent_i, [_sent_b]), (0.54 + 0.24 * _sent_i, [_sent_a])]
_sent_keys += [(2.0, [_sent_a]), (2.4, [_sent_off])]
SIGNS['sentir'] = {
    'poster': 0.6, 'dur': 2.4, 'hands': ['right'], 'handshape': _sent_h,
    # Turned toward the thumb side: the curved, spread fingers read (palm forward they point at the viewer).
    'handshape_view': {'yaw': -45},
    'keys': _sent_keys,
    'marks': [(206, 208, 95)],
    # Small two-headed arrow beside the contact: the fingertips move a little, up and down, on the chest.
    'arrows': [{'d': 'M 226 196 Q 230 206 226 216', 'both': True}],
}
TITLES['sentir'] = 'Sinal de sentir em Libras'
