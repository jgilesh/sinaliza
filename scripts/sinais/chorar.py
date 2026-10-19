# CHORAR: both index fingers up (the other fingers closed), backs of the hands to the viewer; the
# fingertips touch just under the eyes and slide down the cheeks toward the chin, like tears
# running down, once. (UFSC Signbank CHORAR-3 and INES CHORAR agree.)
_chorar_1 = hs_1()


def _chorar_pose(tip, roll):
    """Right hand: back of the hand to the viewer, the index up, its tip at `tip`."""
    return P(tip, _chorar_1, 'index_tip', yaw=165, pitch=-10, roll=roll, scale=1.0, depth=38,
             pole=(0.45, 1.0, 0.5))


_chorar_top = _chorar_pose((185, 105), 24)
_chorar_low = _chorar_pose((182, 127), 20)
_chorar_keys = [(0.0, [_chorar_top, mirrored(_chorar_top)]), (0.4, [_chorar_top, mirrored(_chorar_top)]),
                (1.2, [_chorar_low, mirrored(_chorar_low)]), (1.9, [_chorar_low, mirrored(_chorar_low)]),
                (2.4, [_chorar_top, mirrored(_chorar_top)])]
SIGNS['chorar'] = {
    'poster': 0.8, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _chorar_1, 'mirror_second': True,
    'keys': _chorar_keys,
    # The fingertips touch the face under the eyes and stay on it down the cheeks.
    'marks': [(176, 106, -90), (224, 106, 90)],
    'arrows': [{'d': 'M 162 116 L 159 138'}, {'d': 'M 238 116 L 241 138'}],
}
TITLES['chorar'] = 'Sinal de chorar em Libras'
