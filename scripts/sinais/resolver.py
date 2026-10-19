# RESOLVER: the open hand (5), fingers spread, palm forward, touches the side of the forehead with the
# thumb side; it moves away out to the side and forward while the fingers curl and close. Once.
# (UFSC Signbank RESOLVER: 5 at the forehead; INES RESOLVER.)
_res_5 = hs_5()


def hs_resolver_closed():
    """The hand closed at the end: fingers folded into the palm, the thumb over them."""
    shape = fist()
    shape['thumb'] = thumb_over(shape, ['index', 'middle'], at=0.5)
    return shape


_res_c = hs_resolver_closed()
_res_on = P((161, 81), _res_5, 'thumb_tip', yaw=15, pitch=0, roll=-8, scale=1.0, depth=35, pole=(0.7, 1.0, 0.45))
_res_mid = P((100, 100), _res_5, 'wrist', yaw=10, pitch=15, roll=-14, scale=1.1, depth=65, pole=(0.7, 1.0, 0.45),
             via=(108, 94))
_res_off = P((94, 128), _res_c, 'wrist', yaw=10, pitch=25, roll=-10, scale=1.25, depth=95, pole=(0.7, 1.0, 0.45))
SIGNS['resolver'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right'], 'handshape': _res_5,
    'keys': [(0.0, [_res_on]), (0.4, [_res_on]), (0.8, [_res_mid]), (1.1, [_res_off]), (1.9, [_res_off]),
             (2.4, [_res_on])],
    'marks': [(166, 76, -30)],
    'arrows': [{'d': 'M 100 20 Q 64 28 66 72'}],
}
TITLES['resolver'] = 'Sinal de resolver em Libras'
