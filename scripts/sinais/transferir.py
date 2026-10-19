# TRANSFERIR: both hands in V (index and middle straight and apart), side by side, palms down; together
# they travel in an arc from the side of the support hand over to the side of the dominant hand, the
# fingers pointing to the side at the start and down at the end. Once. (UFSC Signbank TRANSFERIR: V/V,
# 2s, neutral space.)

_tra_v = HANDSHAPES['V']()


def _tra_pose(at, roll, left=False, **kw):
    """Back of the hand to the viewer, fingers tipped toward the viewer (palm down and back). The left hand
    is given as a right hand at the mirrored place, its roll mirrored, so both hands point the same way."""
    if left:
        return mirrored(P((400 - at[0], at[1]), _tra_v, 'wrist', yaw=180, pitch=35, roll=360 - roll, scale=1.1,
                          depth=70, pole=(0.4, 1.0, 0.4), **({'via': (400 - kw['via'][0], kw['via'][1])} if 'via' in kw else {})))
    return P(at, _tra_v, 'wrist', yaw=180, pitch=35, roll=roll, scale=1.1, depth=70, pole=(0.4, 1.0, 0.4), **kw)


# Start on the support side (viewer's right), fingers down and toward that side; end on the dominant side,
# fingers down. The hands keep their spacing all the way.
_tra_a = [_tra_pose((198, 210), 140), _tra_pose((260, 210), 140, left=True)]
_tra_b = [_tra_pose((112, 214), 180, via=(150, 166)), _tra_pose((166, 214), 180, left=True, via=(212, 166))]
_tra_back = [_tra_pose((198, 210), 140, via=(150, 250)), _tra_pose((260, 210), 140, left=True, via=(212, 250))]
SIGNS['transferir'] = {
    'poster': 0.3, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _tra_v,
    'keys': [(0.0, _tra_a), (0.3, _tra_a), (1.05, _tra_b), (1.9, _tra_b), (2.6, _tra_back)],
    # Above the hands: one arc from the support side over to the dominant side.
    'arrows': [{'d': 'M 262 184 Q 192 140 116 180'}],
    'mirror_second': True,
}
TITLES['transferir'] = 'Sinal de transferir em Libras'
