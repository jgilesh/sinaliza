# COMUNICAR: both hands curved in C, facing each other in front of the chest; they move forward and back
# in alternation (one goes out while the other comes in), several times. No contact. (UFSC Signbank
# COMUNICAR: C, 2s, para a frente + para trás, alternado, repetido; INES COMUNICAR agrees.)
_com_c = hs_C()
_com_pole = (0.45, 1.0, 0.4)


def _com_pose(out):
    """Right hand: the C opening toward the other hand (palm toward the midline, turned a little to the
    viewer so the curved fingers and the thumb both read). out = 0 near the chest, 1 forward: forward
    it comes a little lower and nearer the viewer (bigger)."""
    return P((148 - 4 * out, 218 + 18 * out), _com_c, 'wrist', yaw=72, pitch=0, roll=4, scale=1.0 + 0.24 * out,
             depth=45 + 45 * out, pole=_com_pole)


_com_a = [_com_pose(1), mirrored(_com_pose(0))]   # right forward, left in
_com_b = [_com_pose(0), mirrored(_com_pose(1))]   # right in, left forward
SIGNS['comunicar'] = {
    'poster': 0.3, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _com_c, 'handshape_view': {'yaw': 60},
    'keys': [(0.0, _com_a), (0.3, _com_a), (0.7, _com_b), (1.1, _com_a), (1.5, _com_b), (1.9, _com_a),
             (2.6, _com_a)],
    # Outside each hand: forward and back (down-out = toward the viewer), in alternation.
    'arrows': [{'d': 'M 120 172 L 108 222', 'both': True}, {'d': 'M 280 172 L 292 222', 'both': True}],
    'mirror_second': True,
}
TITLES['comunicar'] = 'Sinal de comunicar em Libras'
