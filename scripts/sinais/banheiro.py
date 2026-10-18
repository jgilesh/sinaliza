# BANHEIRO: the support forearm lies across in front of the body, fist closed (S), back of the hand
# up; the dominant hand in "horns" (index and little finger out), palm down, taps the top of that
# forearm twice, bending at the wrist. (UFSC Signbank BANHEIRO and INES BANHEIRO.)


def hs_banheiro_horns():
    """Horns: index and little finger straight, middle and ring folded under the thumb."""
    shape = fist({'index': fing(4, 0, 0, 0), 'pinky': fing(-10, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['middle', 'ring'])
    return shape


_ban_horns, _ban_s = hs_banheiro_horns(), hs_S()
# Support (left) arm, drawn as the right hand at the mirrored place: fist across the body.
_ban_sup = mirrored(P((246, 240), _ban_s, 'wrist', yaw=120, pitch=0, roll=90, scale=1.0, depth=70, pole=(1.0, 0.25, 0.3)))
_ban_on = P((256, 230), _ban_horns, 'index_tip', yaw=150, pitch=0, roll=120, scale=1.05, depth=90, pole=(1.0, 0.3, 0.3))
_ban_up = dict(_ban_on, at=(262, 208), roll=96)
SIGNS['banheiro'] = {
    'poster': 0.5, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _ban_horns,
    'keys': [(0.0, [_ban_up, _ban_sup]), (0.3, [_ban_up, _ban_sup]), (0.5, [_ban_on, _ban_sup]), (0.75, [_ban_up, _ban_sup]),
             (0.95, [_ban_on, _ban_sup]), (1.8, [_ban_on, _ban_sup]), (2.4, [_ban_up, _ban_sup])],
    'mirror_second': True,
    'marks': [(270, 232, 60)],
    'arrows': [{'d': 'M 262 186 Q 284 190 284 212', 'cap': True}],
}
TITLES['banheiro'] = 'Sinal de banheiro em Libras'
