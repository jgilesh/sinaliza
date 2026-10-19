# CONFUNDIR: both hands open with the fingers spread (5). They start up beside the head, palms
# turned in toward it, and come down to in front of the chest, where the fingers of one hand cross
# between the fingers of the other, palms toward the body, and stay crossed. Once. Puzzled face.
# (UFSC Signbank CONFUNDIR: 5+5, fingers, rubbing contact at the end. The INES CONFUNDIR video shows
# only the end: the crossed fingers rubbing in front of the chest.)

_conf_5 = hs_5()
_conf_pole = (0.5, 1.0, 0.4)
# Up beside the head, palm turned toward it (and a little to the viewer), fingers up and spread.
_conf_up = P((110, 148), _conf_5, 'wrist', yaw=50, pitch=0, roll=-18, scale=1.0, depth=50, pole=_conf_pole)
# In front of the chest, back of the hand to the viewer, fingers up and across toward the other hand;
# the right hand a little nearer and lower, so its fingers cross over the other hand's fingers.
_conf_r_x = P((156, 252), _conf_5, "wrist", yaw=172, pitch=0, roll=50, scale=1.05, depth=78, pole=_conf_pole,
              via=(132, 214))
_conf_l_x = P((156, 238), _conf_5, "wrist", yaw=172, pitch=0, roll=50, scale=1.05, depth=66, pole=_conf_pole,
              via=(132, 206))
_conf_A = [_conf_up, mirrored(_conf_up)]
_conf_Z = [_conf_r_x, mirrored(_conf_l_x)]
_conf_back = [dict(_conf_up, via=(118, 220)), mirrored(dict(_conf_up, via=(118, 220)))]
SIGNS['confundir'] = {
    'poster': 1.4, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _conf_5,
    'keys': [(0.0, _conf_A), (0.3, _conf_A), (1.0, _conf_Z), (2.0, _conf_Z), (2.6, _conf_back)],
    # Outside the hands: down and in from beside the head.
    'arrows': [{'trail': 0, 'from': 0.3, 'to': 1.0, 'offset': (-26, 0), 'trim': 0.1},
               {'trail': 1, 'from': 0.3, 'to': 1.0, 'offset': (26, 0), 'trim': 0.1}],
    'mirror_second': True,
}
TITLES['confundir'] = 'Sinal de confundir em Libras'
