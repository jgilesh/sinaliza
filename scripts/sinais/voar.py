# VOAR: both flat hands (B), fingers together, raised beside the shoulders like wings, palms
# forward. The wrists bend down and back up, flapping like wings, 3 times, while the hands go down
# and out to the sides of the chest, ending palms down. (UFSC Signbank VOAR; INES VOAR agrees.)


def hs_voar_b():
    """B with the thumb resting along the side of the index (a flat wing)."""
    shape = hs_B()
    shape['thumb'] = (-12.0, 8.0, 10.0, 6.0, 4.0)
    return shape


_voar_b = hs_voar_b()


def _voar_pose(u, flap):
    """Right hand: u = 0 raised beside the shoulder ... 1 low beside the chest; flap = 0 wing up
    (palm forward, fingers up) ... 1 wrist bent down: the fingers point out to the side and a little
    down, the palm turned forward and down (as in the Signbank video, the wing tip drops sideways)."""
    at = (112 - 6 * u, 168 + 48 * u)
    return P(at, _voar_b, 'wrist', yaw=4 - 34 * flap, pitch=0, roll=-8 - 4 * u - 88 * flap, scale=1.05,
             depth=50 + 10 * u, pole=(0.2, 1.0, 0.3))


_voar_keys = [(0.0, _voar_pose(0, 0)), (0.3, _voar_pose(0, 0))]
for _voar_i, _voar_t in enumerate((0.5, 0.9, 1.3)):
    _voar_keys += [(_voar_t, _voar_pose(0.2 + 0.3 * _voar_i, 1)), (_voar_t + 0.2, _voar_pose(0.35 + 0.3 * _voar_i, 0.15))]
_voar_keys += [(1.75, _voar_pose(1, 1)), (2.3, _voar_pose(1, 1)), (2.8, _voar_pose(0, 0))]
_voar_keys = [(t, [p, mirrored(p)]) for t, p in _voar_keys]
SIGNS['voar'] = {
    'poster': 0.5, 'dur': 2.8, 'hands': ['right', 'left'], 'handshape': _voar_b,
    'keys': _voar_keys,
    # Wing beats: a two-headed arc outside each hand's fingertips, from "up" to "out".
    'arrows': [{'d': circle_arrow(106, 192, 92, -110, -155, False), 'both': True},
               {'d': circle_arrow(294, 192, 92, -70, -25, True), 'both': True}],
    'mirror_second': True,
}
TITLES['voar'] = 'Sinal de voar em Libras'
