# HOSPEDAR: both hands in V (index and middle straight and apart). The dominant V stands up beside the
# face, palm forward; the other touches the tips of its V near the nose. Then both lie down flat,
# palms down, fingers pointing to the dominant side: the dominant hand stretches far out to the side
# and the other stays by the cheek, while the head tilts that way and the eyes close, as when
# sleeping. Once. (UFSC Signbank HOSPEDAR: V/V; INES HOSPEDAR agrees.)


def hs_hospedar_v():
    """V: index and middle straight and apart, ring and little finger folded under the thumb."""
    shape = fist({'index': fing(12, 0, 0, 0), 'middle': fing(-8, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


_hospedar_v = hs_hospedar_v()
# Dominant hand. Up: beside the face, outside it, palm forward. Down: lying flat far out to the side at
# cheek height, palm down, the fingers pointing out; the back of the hand tipped up toward the viewer so
# the two spread fingers read.
_hospedar_r_up = P((130, 150), _hospedar_v, 'wrist', yaw=10, pitch=-8, roll=-4, scale=1.05, depth=58,
                   pole=(0.2, 1.0, 1.2))
_hospedar_r_down = P((142, 138), _hospedar_v, 'wrist', yaw=-140, pitch=0, roll=-90, scale=1.08, depth=70,
                     pole=(0.6, 1.0, 0.6), ease='smooth')
# Other hand, drawn as a right hand at the mirrored place and then mirrored. Up: the tips of its V
# beside the nose, the fingers slanting up toward the middle of the face, the back of the hand toward
# the viewer. Down: lying flat beside the cheek and jaw on the dominant side, palm down, fingers
# pointing to the dominant side, the arm passing under the chin.
_hospedar_l_up = mirrored(P((186, 116), _hospedar_v, 'index_tip', yaw=150, pitch=0, roll=40, scale=1.0, depth=40,
                            pole=(0.4, 1.0, 0.9)))
_hospedar_l_down = mirrored(P((240, 150), _hospedar_v, 'index_tip', yaw=140, pitch=0, roll=88, scale=1.02, depth=50,
                              pole=(0.4, 1.0, 0.9)))
SIGNS['hospedar'] = {
    'poster': 1.3, 'dur': 2.7, 'hands': ['right', 'left'], 'handshape': _hospedar_v,
    'keys': [(0.0, [_hospedar_r_up, _hospedar_l_up]), (0.4, [_hospedar_r_up, _hospedar_l_up]),
             (1.1, [_hospedar_r_down, _hospedar_l_down]), (2.0, [_hospedar_r_down, _hospedar_l_down]),
             (2.7, [_hospedar_r_up, _hospedar_l_up])],
    'marks': [(224, 112, 70)],
    # Both hands lie down and point out to the dominant side.
    'arrows': [{'d': 'M 110 90 Q 80 92 70 120'}],
}
TITLES['hospedar'] = 'Sinal de hospedar em Libras'
