# ATRAPALHAR: both hands open with the fingers spread (5), palms toward the body. One hand is up
# beside the face, the other in front of the belly; they swap heights, crossing in front of the chest
# with the fingertips brushing as they pass, twice (up-down-up-down). Annoyed face.
# (UFSC Signbank ATRAPALHAR: 5+5, alternating, rubbing the fingertips. The INES ATRAPALHAR1 video shows
# another variant: the fingers of the two hands interlaced and crossing in front of the chest.)

_atrap_5 = hs_5()
_atrap_pole = (0.5, 1.0, 0.4)


def _atrap_up(x=140, y=172):
    # Raised beside the face (not over it), back of the hand to the viewer, fingers up and a little in.
    return P((x, y), _atrap_5, 'wrist', yaw=165, pitch=0, roll=12, scale=1.05, depth=60, pole=_atrap_pole)


def _atrap_low(x=152, y=258):
    # In front of the belly, back of the hand to the viewer, fingers pointing across toward the midline.
    return P((x, y), _atrap_5, 'wrist', yaw=165, pitch=0, roll=66, scale=1.05, depth=60, pole=_atrap_pole)


# Right hand drawn in front (a little nearer), the left hand (mirrored) behind it.
_atrap_A = [dict(_atrap_up(), depth=70), mirrored(_atrap_low())]
_atrap_B = [dict(_atrap_low(), depth=70), mirrored(_atrap_up())]
SIGNS['atrapalhar'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _atrap_5,
    'keys': [(0.0, _atrap_A), (0.3, _atrap_A), (0.7, _atrap_B), (1.1, _atrap_A), (1.5, _atrap_B),
             (1.9, _atrap_A), (2.4, _atrap_A)],
    # Outside each hand: up and down, alternately.
    'arrows': [{'d': 'M 98 166 L 98 252', 'both': True}, {'d': 'M 302 166 L 302 252', 'both': True}],
    # Where the fingertips brush as the hands cross.
    'marks': [(200, 214, 0)],
    'mirror_second': True,
}
TITLES['atrapalhar'] = 'Sinal de atrapalhar em Libras'
