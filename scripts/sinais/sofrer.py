# SOFRER: both hands in Y (thumb and little finger out), palms down, the thumbs toward each other, in
# front of the belly; the two hands shake together in small quick movements up and down, not
# touching. (UFSC Signbank SOFRER; INES SOFRER shows it with one hand.)
_sofrer_y = hs_Y()
# Back of the hand to the viewer, little finger down, thumb across toward the other hand; tipped so
# the palm faces down and toward the body.
_sofrer = lambda dy: P((184, 238 + dy), _sofrer_y, 'thumb_tip', yaw=180, pitch=25, roll=172, scale=1.1, depth=62,
                       pole=(0.4, 1.0, 0.4), ease='linear')
_sofrer_k = lambda dy: [_sofrer(dy), mirrored(_sofrer(dy))]
_sofrer_keys = [(0.0, _sofrer_k(0)), (0.3, _sofrer_k(0))]
for _sofrer_i in range(5):   # a quick tremor
    _sofrer_t = 0.3 + 0.2 * _sofrer_i
    _sofrer_keys += [(_sofrer_t + 0.1, _sofrer_k(-5)), (_sofrer_t + 0.2, _sofrer_k(3))]
_sofrer_keys += [(1.45, _sofrer_k(0)), (2.2, _sofrer_k(0))]
SIGNS['sofrer'] = {
    'poster': 0.3, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _sofrer_y,
    'keys': _sofrer_keys,
    'arrows': [{'d': 'M 112 226 L 112 250', 'both': True}, {'d': 'M 288 226 L 288 250', 'both': True}],
    'mirror_second': True,
}
TITLES['sofrer'] = 'Sinal de sofrer em Libras'
