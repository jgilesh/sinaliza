# DIALOGAR: both hands in D (index up, the other fingertips resting on the thumb). The dominant index
# rests on the chin; the other hand waits beside the shoulder. The other hand comes to the chin while
# the dominant one steps away, then they trade back, like two people taking turns to talk, 3 times.
# (UFSC Signbank DIALOGAR: D/D, double contact, back and forth, repeated, alternating. The INES video
# shows both index fingers pointing at the chin from either side instead.)


def hs_dialogar_d():
    """D of Libras: index straight, middle, ring and little finger curved down onto the thumb's pad."""
    shape = {'index': fing(2, 0, 0, 0), 'middle': fing(0, 52, 70, 45), 'ring': fing(-2, 54, 68, 45),
             'pinky': fing(-4, 58, 64, 45)}
    shape['thumb'] = pinch_thumb(shape, fingers=('middle',))
    return shape


_dialogar_d = hs_dialogar_d()
# Dominant hand: index up with its tip on the chin, the palm turned toward the face and a little toward
# the viewer, so the curled fingers on the thumb read below the index.
_dialogar_r_on = P((194, 146), _dialogar_d, 'index_tip', yaw=55, pitch=0, roll=4, scale=1.0, depth=40, pole=(0.5, 1.0, 0.45))
_dialogar_r_off = P((166, 168), _dialogar_d, 'index_tip', yaw=45, pitch=0, roll=-8, scale=1.02, depth=55, pole=(0.5, 1.0, 0.45))
# Other hand (defined as a right hand, then mirrored): index up beside the shoulder, palm toward the
# midline and the viewer; at the chin its tip rests beside the dominant one.
_dialogar_l_off = mirrored(P((140, 172), _dialogar_d, 'index_tip', yaw=40, pitch=0, roll=-8, scale=1.02, depth=60,
                             pole=(0.5, 1.0, 0.45)))
_dialogar_l_on = mirrored(P((194, 146), _dialogar_d, 'index_tip', yaw=55, pitch=0, roll=4, scale=1.0, depth=42,
                            pole=(0.5, 1.0, 0.45)))
_dialogar_a, _dialogar_b = [_dialogar_r_on, _dialogar_l_off], [_dialogar_r_off, _dialogar_l_on]
_dialogar_keys = [(0.0, _dialogar_a), (0.3, _dialogar_a)]
for _dialogar_k in range(3):
    _dialogar_t = 0.3 + 0.6 * _dialogar_k
    _dialogar_keys += [(_dialogar_t + 0.3, _dialogar_b), (_dialogar_t + 0.6, _dialogar_a)]
_dialogar_keys.append((2.5, _dialogar_a))
SIGNS['dialogar'] = {
    'poster': 0.0, 'dur': 2.5, 'hands': ['right', 'left'], 'handshape': _dialogar_d,
    'handshape_view': {'yaw': 40, 'pitch': -10},
    'keys': _dialogar_keys,
    'marks': [(184, 144, -70)],
    'arrows': [{'d': 'M 276 160 Q 254 142 226 152', 'both': True}, {'d': 'M 128 176 Q 140 156 166 146', 'both': True}],
    'mirror_second': True,
}
TITLES['dialogar'] = 'Sinal de dialogar em Libras'
