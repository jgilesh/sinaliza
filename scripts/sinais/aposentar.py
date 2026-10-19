# APOSENTAR: fingerspelled A-P. The hand in A (fist, thumb up along the index) in front of the shoulder
# on the signing side changes to P (index up, the middle finger bent forward with the thumb on it) and
# then the wrist tips forward, so the index points ahead. Once. (UFSC Signbank APOSENTAR; the INES
# video holds the P across the chest instead.)


def hs_aposentar_A():
    """A: fist, the thumb straight up along the side of the index."""
    shape = fist()
    shape['thumb'] = solve_thumb((17.0, -44.0, -1.5), pad_to=(-1.0, 0.0, 0.0), point=(0.0, -1.0, 0.0),
                                 pref=(-5.0, 10.0, 20.0, 0.0, 0.0))
    return shape


def hs_aposentar_P():
    """P of Libras: index straight, middle finger straight but bent forward at the knuckle, ring and
    little fingers folded; the thumb's pad on the side of the middle finger."""
    shape = fist({'index': fing(4, 0, 0, 0), 'middle': fing(-2, 62, 6, 4)})
    shape['thumb'] = solve_thumb((8.0, -42.5, 10.0), pad_to=(-1.0, 0.0, 0.0), pref=(5.0, 30.0, 40.0, 15.0, 15.0))
    return shape


_aposentar_a, _aposentar_p = hs_aposentar_A(), hs_aposentar_P()
_aposentar_pole = (0.6, 1.0, 0.45)
# A: palm forward, so the folded fingers and the thumb along the side read. P: the thumb side toward the
# viewer (palm turned out), so the straight index, the middle finger pointing forward and the thumb on it read.
_aposentar_ahand = P((132, 176), _aposentar_a, 'wrist', yaw=-28, pitch=0, roll=-4, scale=1.1, depth=45, pole=_aposentar_pole)
_aposentar_up = P((126, 170), _aposentar_p, 'wrist', yaw=-60, pitch=-8, roll=-4, scale=1.1, depth=50, pole=_aposentar_pole)
# The wrist tips forward: the index points ahead and toward the midline.
_aposentar_fwd = P((128, 172), _aposentar_p, 'wrist', yaw=-25, pitch=50, roll=45, scale=1.12, depth=60, pole=_aposentar_pole,
                   ease='out')
SIGNS['aposentar'] = {
    'poster': 0.9, 'dur': 2.6, 'hands': ['right'], 'handshape': _aposentar_p, 'handshape_view': {'yaw': -65, 'pitch': -20},
    'keys': [(0.0, [_aposentar_ahand]), (0.45, [_aposentar_ahand]), (0.8, [_aposentar_up]), (1.15, [_aposentar_up]),
             (1.45, [_aposentar_fwd]), (2.1, [_aposentar_fwd]), (2.6, [_aposentar_ahand])],
    # The index tips forward from the wrist.
    'arrows': [{'d': 'M 110 66 Q 134 56 146 76'}],
}
TITLES['aposentar'] = 'Sinal de aposentar em Libras'
