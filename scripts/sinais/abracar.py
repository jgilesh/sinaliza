# ABRAÇAR: both hands closed (S), the arms cross over the chest and each fist comes to rest near the
# opposite shoulder, palms toward the body; the hold sways a little from side to side, as in a hug.
# (UFSC Signbank ABRAÇAR: S+S, chest; INES ABRAÇAR agrees.)

_abracar_s = hs_S()


def _abracar_hand(at, roll, depth=22, **kw):
    """Right hand on the signer's left shoulder: back of the fist to the viewer, knuckles up and
    toward the shoulder, the thumb side turned a little to the viewer so the thumb across the folded
    fingers reads."""
    return P(at, _abracar_s, 'wrist', yaw=230, pitch=0, roll=roll, scale=1.1, depth=depth, pole=(0.3, 1.0, 0.1), **kw)


def _abracar_pair(dx, dy, depth=22):
    right = _abracar_hand((226 + dx, 214 + dy), 38, depth)
    left = mirrored(_abracar_hand((226 - dx, 214 + dy), 38, depth))
    return [right, left]


_abracar_near = _abracar_pair(-8, 18, 50)     # arms crossing, hands still a little away from the body
_abracar_hold = _abracar_pair(0, 0)
_abracar_r, _abracar_l = _abracar_pair(5, 1), _abracar_pair(-5, 1)    # the sway
SIGNS['abracar'] = {
    'poster': 0.6, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _abracar_s, 'handshape_view': {'yaw': -30},
    'keys': [(0.0, _abracar_near), (0.4, _abracar_hold), (0.6, _abracar_hold), (0.95, _abracar_r), (1.35, _abracar_l),
             (1.7, _abracar_hold), (2.0, _abracar_hold), (2.4, _abracar_near)],
    'marks': [(258, 196, 70), (142, 196, -70)],
    # A two-headed arc under the crossed forearms: the hug sways from side to side.
    'arrows': [{'d': 'M 168 266 Q 200 280 232 266', 'both': True}],
    'mirror_second': True,
}
TITLES['abracar'] = 'Sinal de abraçar em Libras'
