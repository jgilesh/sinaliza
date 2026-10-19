# AVALIAR: both hands closed with the thumb straight up (A). They move up and down in turn: the hand
# going up holds the thumb up, the hand going down turns the thumb toward the midline (palm down); then
# they swap, three times, like a scale weighing. No contact. (UFSC Signbank AVALIAR: A, alternado,
# pronação+supinação. INES AVALIAR1 shows another sign.)


def hs_avaliar_A():
    """A with the thumb standing straight up beside the fist (thumbs up): fist, thumb along the side of
    the index, its tip a little above the knuckles."""
    shape = fist()
    shape['thumb'] = solve_thumb((17.0, -44.0, -1.5), pad_to=(-1.0, 0.0, 0.0), point=(0.0, -1.0, 0.0),
                                 pref=(-5.0, 10.0, 20.0, 0.0, 0.0))
    return shape


_avaliar_a = hs_avaliar_A()
# Up: seen from the thumb side (palm turned a little outward), so the thumb stands clear beside the folded
# fingers.
_avaliar_up = P((146, 164), _avaliar_a, 'wrist', yaw=-30, pitch=0, roll=-4, scale=1.15, depth=65, pole=(0.45, 1.0, 0.4))
# Down: the forearm turns (palm toward the floor), the thumb points in toward the midline and a little down.
_avaliar_dn = P((152, 236), _avaliar_a, 'wrist', yaw=-30, pitch=0, roll=108, scale=1.15, depth=65, pole=(0.45, 1.0, 0.4))
_avaliar_keys = [(0.0, [_avaliar_up, mirrored(_avaliar_dn)]), (0.3, [_avaliar_up, mirrored(_avaliar_dn)])]
for _avaliar_i in range(2):
    _avaliar_t = 0.3 + 0.76 * _avaliar_i
    _avaliar_keys += [(_avaliar_t + 0.38, [_avaliar_dn, mirrored(_avaliar_up)]),
                      (_avaliar_t + 0.76, [_avaliar_up, mirrored(_avaliar_dn)])]
_avaliar_keys.append((2.1, [_avaliar_up, mirrored(_avaliar_dn)]))
SIGNS['avaliar'] = {
    'poster': 0.0, 'dur': 2.1, 'hands': ['right', 'left'], 'handshape': _avaliar_a, 'handshape_view': {'yaw': -30},
    'keys': _avaliar_keys,
    # Outside each hand: up and down, in turn.
    'arrows': [{'d': 'M 104 236 L 104 168', 'both': True}, {'d': 'M 296 236 L 296 168', 'both': True}],
    'mirror_second': True,
}
TITLES['avaliar'] = 'Sinal de avaliar em Libras'
