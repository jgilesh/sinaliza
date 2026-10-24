# AINDA NÃO: the fingers bent over the thumb ("Money"), the thumb tip resting under the chin, palm toward
# the other side; the fingers move in turn, brushing the thumb, in small repeated touches, without the hand
# leaving the chin. Lips pushed out (not drawn). (UFSC Signbank AINDA-NÃO: Money, queixo, contato duplo,
# alternado. The INES AINDA NÃO video did not download.)


def hs_ainda_nao_money(lift=(0, 0, 0, 0)):
    """Money: the fingers bent at the knuckles and middle joints, their tips together over the thumb,
    whose pad presses on the index fingertip. `lift` opens each finger a little (index, middle, ring,
    little finger) for the alternating rub."""
    base = {'index': (2, 52, 58, 34), 'middle': (0, 55, 58, 36), 'ring': (-1, 58, 56, 36), 'pinky': (-2, 62, 54, 36)}
    shape = {n: fing(a, m - k, p - k * 0.8, d - k * 0.4) for (n, (a, m, p, d)), k in zip(base.items(), lift)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index',))
    return shape


_ain_m = hs_ainda_nao_money()
# The thumb stays where it is; only the fingers move (the thumb of the base shape is kept in all of them).
_ain_a = dict(hs_ainda_nao_money((0, 16, 0, 16)), thumb=_ain_m['thumb'])
_ain_b = dict(hs_ainda_nao_money((14, 0, 16, 0)), thumb=_ain_m['thumb'])
# Thumb tip under the chin; the palm turned toward the other side and half toward the viewer, so the
# bent fingers and the thumb under them read.
_ain_pose = lambda shape: P((200, 147), shape, 'thumb_tip', yaw=58, pitch=0, roll=-6, scale=1.05, depth=40,
                            pole=(0.45, 1.0, 0.45))
_ain_keys = [(0.0, [_ain_pose(_ain_m)]), (0.3, [_ain_pose(_ain_m)])]
for _ain_i in range(4):
    _ain_keys.append((round(0.5 + 0.22 * _ain_i, 2), [_ain_pose(_ain_a if _ain_i % 2 == 0 else _ain_b)]))
_ain_keys += [(1.6, [_ain_pose(_ain_m)]), (2.4, [_ain_pose(_ain_m)])]
SIGNS['ainda-nao'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right'], 'handshape': _ain_m, 'handshape_view': {'yaw': 50, 'roll': -10},
    'keys': _ain_keys,
    'marks': [(214, 150, 110)],
}
TITLES['ainda-nao'] = 'Sinal de ainda não em Libras'
