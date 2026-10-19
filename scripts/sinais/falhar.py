# FALHAR: index up (1), the side of the finger against the side of the nose; it swings down in an
# arc, across to the front of the chin on the other side, and back up to the nose; about three
# times. Disappointed mouth. (UFSC Signbank FALHAR; INES FALHAR.)
_fal_one = hs_1()
# The palm faces the face (back of the hand mostly to the viewer, turned a little toward the thumb),
# so the index rises from the knuckle row with the folded fingers below it.
_fal_nose = P((191, 103), _fal_one, 'index_tip', yaw=150, pitch=0, roll=-4, scale=1.0, depth=35, pole=(0.45, 1.0, 0.45))
_fal_chin = P((214, 126), _fal_one, 'index_tip', yaw=130, pitch=0, roll=16, scale=1.0, depth=45, pole=(0.45, 1.0, 0.45),
              via=(196, 140))
_fal_up = dict(_fal_nose, via=(206, 116))
_fal_keys = [(0.0, [_fal_nose]), (0.3, [_fal_nose])]
for _fal_k in range(3):
    _fal_keys += [(0.3 + 0.6 * _fal_k + 0.3, [_fal_chin]), (0.3 + 0.6 * _fal_k + 0.6, [_fal_up])]
_fal_keys.append((2.6, [_fal_nose]))
SIGNS['falhar'] = {
    'poster': 0.0, 'dur': 2.6, 'hands': ['right'], 'handshape': _fal_one,
    'keys': _fal_keys,
    'marks': [(183, 108, -90)],
    'arrows': [{'d': 'M 158 146 Q 166 214 240 182', 'both': True}],
}
TITLES['falhar'] = 'Sinal de falhar em Libras'
