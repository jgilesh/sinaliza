# CONTAR (narrar): Y hand beside the head near the ear, the little finger up and the palm toward the head;
# the wrist turns (supination) and the hand moves a little forward and down until the thumb points up,
# twice, ending thumb up. No contact. (UFSC Signbank CONTAR: Y, beside the head, arc, supination. The INES
# CONTAR1 video is the other meaning, counting numbers.)

_con_y = HANDSHAPES['Y']()
# Little finger up: palm turned toward the head and a little toward the viewer, so the folded fingers,
# the raised little finger and the thumb reaching toward the face all read; the hand stays beside the
# ear, clear of the eyes.
_con_up = P((114, 134), _con_y, 'wrist', yaw=50, pitch=0, roll=-4, scale=1.0, depth=40, pole=(0.6, 1.0, 0.45))
# Thumb up: the forearm has turned, palm forward, the little finger pointing out and down.
_con_down = P((110, 150), _con_y, 'wrist', yaw=-10, pitch=0, roll=-80, scale=1.05, depth=55, pole=(0.6, 1.0, 0.45))
# Twice: thumb up, back to little finger up, thumb up again; held, then back to the start.
_con_keys = [(0.0, [_con_up]), (0.25, [_con_up]), (0.55, [_con_down]), (0.85, [_con_up]), (1.15, [_con_down]),
             (1.9, [_con_down]), (2.4, [_con_up])]
SIGNS['contar'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right'], 'handshape': _con_y,
    'keys': _con_keys,
    # The hand turns on the forearm, around the wrist.
    'arrows': [{'twist': 0, 'at': 0.0, 'r': (20, 7), 'drop': 12}],
}
TITLES['contar'] = 'Sinal de contar em Libras'
