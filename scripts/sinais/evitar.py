# EVITAR: Y hand (thumb and little finger out), the thumb tip on the forehead, the little finger up and
# the palm toward the face; the hand leaves the forehead in an arc forward and down, the wrist turning
# so the palm ends facing forward and down, once. (UFSC Signbank EVITAR: Y, forehead, arc forward,
# rotation; INES EVITAR agrees.)
_evi_y = HANDSHAPES['Y']()
# On the forehead: the thumb reaches in to the forehead from the side, the little finger up; the palm
# turned toward the face and a little toward the viewer, so the folded fingers and both raised digits
# read, and the hand stays above the eye.
_evi_on = P((183, 70), _evi_y, 'thumb_tip', yaw=50, pitch=0, roll=-30, scale=1.0, depth=40, pole=(0.7, 1.0, 0.45))
# Away, forward and down: the forearm has turned, palm forward and tipped down, little finger out.
_evi_off = P((116, 170), _evi_y, 'wrist', yaw=-35, pitch=30, roll=-60, scale=1.06, depth=70, pole=(0.6, 1.0, 0.45),
             via=(120, 92), ease='out')
SIGNS['evitar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right'], 'handshape': _evi_y,
    'keys': [(0.0, [_evi_on]), (0.4, [_evi_on]), (1.0, [_evi_off]), (1.9, [_evi_off]),
             (2.4, [dict(_evi_on, via=(118, 100), ease='smooth')])],
    'marks': [(188, 66, 30)],
    'arrows': [{'d': 'M 132 60 Q 96 60 86 126'}],
}
TITLES['evitar'] = 'Sinal de evitar em Libras'
