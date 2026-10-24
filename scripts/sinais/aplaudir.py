# APLAUDIR: both hands open (5), fingers spread, raised beside the head with the palms forward; the
# wrists turn in and out several times (the Deaf applause). (UFSC Signbank APLAUDIR. INES APLAUDIR1
# shows hearing-style clapping instead.)
_aplaudir_5 = hs_5()
_aplaudir_pole = (0.8, 0.8, 0.5)
# Right hand beside the head (viewer's left), fingers up and leaning out a little; yaw = the wrist
# turn (0 = palm to the viewer, + = palm toward the head, - = palm outward).
_aplaudir = lambda yaw: P((108, 126), _aplaudir_5, "wrist", yaw=yaw, pitch=-6, roll=-18, scale=1.0, depth=45,
                          pole=_aplaudir_pole)
_aplaudir_k = lambda yaw: [_aplaudir(yaw), mirrored(_aplaudir(yaw))]
_aplaudir_keys = [(0.0, _aplaudir_k(0)), (0.3, _aplaudir_k(0))]
for _aplaudir_i in range(3):   # three turns in and out
    _aplaudir_t = 0.3 + 0.4 * _aplaudir_i
    _aplaudir_keys += [(_aplaudir_t + 0.2, _aplaudir_k(-50)), (_aplaudir_t + 0.4, _aplaudir_k(40))]
_aplaudir_keys += [(1.7, _aplaudir_k(0)), (2.4, _aplaudir_k(0))]
SIGNS['aplaudir'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _aplaudir_5,
    'keys': _aplaudir_keys,
    # A curved two-headed arrow around each wrist: the hand turns on the forearm.
    'arrows': [{'twist': 0, 'at': 0.3, 'r': (22, 7), 'drop': 6}, {'twist': 1, 'at': 0.3, 'r': (22, 7), 'drop': 6}],
    'mirror_second': True,
}
TITLES['aplaudir'] = 'Sinal de aplaudir em Libras'
