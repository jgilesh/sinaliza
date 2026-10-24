# FAZER: both hands closed in fists. The signing hand stands upright at shoulder height on its own
# side, palm toward the midline and a little forward; the other fist lies across lower down in front of
# the chest, palm toward the body, thumb on top. The upright fist taps down with its little-finger
# edge on the thumb of the lower fist, lightly, 3 times, like a hammer. (UFSC Signbank FAZER: S+S,
# mão fraca: polegar.)
_fazer_s = hs_S()
# Signing hand: upright, palm toward the midline and the viewer, so the folded fingers show.
_fazer_up = P((140, 176), _fazer_s, 'wrist', yaw=45, pitch=0, roll=4, scale=1.05, depth=62, pole=(0.5, 1.0, 0.45),
              ease='smooth')
_fazer_hit = dict(_fazer_up, at=(143, 184), ease='in')
# Other hand (defined as a right hand, then mirrored): lying across, palm toward the body and a little
# down, the thumb along the top, the knuckles toward the signing side.
_fazer_base = mirrored(P((195, 197), _fazer_s, 'wrist', yaw=168, pitch=36, roll=90, scale=1.05, depth=64,
                         pole=(0.4, 1.0, 0.4)))
_fazer_keys = [(0.0, [_fazer_up, _fazer_base]), (0.3, [_fazer_up, _fazer_base])]
for _fazer_i in range(3):
    _fazer_t = 0.3 + 0.36 * _fazer_i
    _fazer_keys += [(_fazer_t + 0.18, [_fazer_hit, _fazer_base]), (_fazer_t + 0.36, [_fazer_up, _fazer_base])]
_fazer_keys += [(2.2, [_fazer_up, _fazer_base])]
SIGNS['fazer'] = {
    'poster': 0.48, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _fazer_s, 'handshape_view': {'yaw': 30},
    'keys': _fazer_keys,
    'marks': [(172, 178, 45)],
    'arrows': [{'d': 'M 106 150 L 106 178', 'both': True}],
    'mirror_second': True,
}
TITLES['fazer'] = 'Sinal de fazer em Libras'
