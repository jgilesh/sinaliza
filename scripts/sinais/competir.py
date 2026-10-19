# COMPETIR: both hands with the index straight (1), level and pointing at each other, apart in front of
# the chest, palms down. Together the hands rise to beside the face, then come down in an arc out to the
# sides and down, the index fingers still pointing at each other. No contact. (UFSC Signbank COMPETIR:
# 1/1, neutral space, arc up then out and down; the INES COMPETIR video holds the two index fingers
# pointing at each other in front of the chest.)

_comp_one = HANDSHAPES['1']()


def _comp_pose(at, scale=1.08, depth=60, via=None, ease='smooth'):
    """Right hand (the left mirrors it): the index points across toward the midline, palm down, the back
    of the hand tipped toward the viewer so the index reads along the top of the fist."""
    pose = P(at, _comp_one, 'index_tip', yaw=120, pitch=0, roll=90, scale=scale, depth=depth,
             pole=(0.35, 1.0, 0.4), ease=ease)
    if via:
        pose['via'] = via
    return pose


_comp_start = _comp_pose((182, 212))
_comp_up = _comp_pose((150, 124), depth=55, via=(160, 160))        # beside the face, clear of it
_comp_end = _comp_pose((150, 228), scale=1.1, depth=65, via=(110, 172), ease='smooth')
_comp_back = dict(_comp_start, via=(170, 250))
_comp_k = lambda pose: [pose, mirrored(pose)]
SIGNS['competir'] = {
    'poster': 0.3, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _comp_one,
    'keys': [(0.0, _comp_k(_comp_start)), (0.3, _comp_k(_comp_start)), (0.75, _comp_k(_comp_up)),
             (1.35, _comp_k(_comp_end)), (2.0, _comp_k(_comp_end)), (2.6, _comp_k(_comp_back))],
    # Outside each hand: up, then out and down in an arc.
    'arrows': [{'d': 'M 124 206 C 112 120 70 112 82 222'}, {'d': 'M 276 206 C 288 120 330 112 318 222'}],
    'mirror_second': True,
}
TITLES['competir'] = 'Sinal de competir em Libras'
