# POR QUE: both hands with the index out (1), crossed in an X in front of the chest, the backs of the hands
# to the viewer: the signer's right index points up and to the left, in front of the left index, which
# points up and to the right and stays still. The right hand lifts a little and comes back down to cross
# again, two or three times. Question face (same form as PORQUE; INES PORQUE, UFSC Signbank PORQUE).
pq_one = hs_1()
pq_right = lambda at: P(at, pq_one, 'wrist', yaw=180, pitch=-5, roll=60, scale=1.1, depth=78, pole=(0.25, 1.0, 0.45))
pq_left = mirrored(P((154, 234), pq_one, 'wrist', yaw=180, pitch=-5, roll=64, scale=1.1, depth=62, pole=(0.25, 1.0, 0.45)))
pq_down, pq_up = pq_right((154, 230)), pq_right((157, 213))
pq_keys = [(0.0, [pq_down, pq_left]), (0.25, [pq_down, pq_left])]
for k in range(3):
    t = 0.25 + 0.45 * k
    pq_keys += [(t + 0.2, [dict(pq_up, ease='out'), pq_left]), (t + 0.45, [dict(pq_down, ease='in'), pq_left])]
pq_keys += [(2.2, [pq_down, pq_left])]
SIGNS['por-que'] = {
    'poster': 0.0, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': pq_one,
    'keys': pq_keys,
    'arrows': [{'d': 'M 104 184 L 108 216', 'both': True}],
    'mirror_second': True,
}
TITLES['por-que'] = 'Sinal de por que em Libras'
