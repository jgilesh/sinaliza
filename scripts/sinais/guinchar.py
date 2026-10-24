# GUINCHAR: both index fingers bent into hooks (the other fingers closed) hook into each other in front
# of the chest, on the dominant side; together they slide across to the other side, like a tow truck
# pulling a car. Once. (UFSC Signbank GUINCHAR: 1_curved, both hands; the INES video shows another
# variant.)


def hs_guinchar_hook():
    """Index bent into a hook at the middle and end joints, the other fingers closed, the thumb over the
    middle finger."""
    shape = fist({'index': fing(2, 10, 80, 60)})
    shape['thumb'] = thumb_over(shape, ['middle'])
    return shape


_gui_hook = hs_guinchar_hook()


def _gui_pair(x):
    """The two hooks caught together at x: the dominant one from the left, palm up and its thumb side to
    the viewer, its hook curling up; the other hand (a right-hand pose, mirrored) from the right, palm
    down, its hook curling down into the first one."""
    dom = P((x - 4, 208), _gui_hook, 'index_tip', yaw=-80, pitch=0, roll=90, scale=1.25, depth=70, pole=(0.4, 1.0, 0.4),
            ease='smooth')
    sup = mirrored(P((400 - x - 4, 216), _gui_hook, 'index_tip', yaw=125, pitch=0, roll=90, scale=1.25, depth=70,
                     pole=(0.4, 1.0, 0.4), ease='smooth'))
    return [dom, sup]


_gui_a, _gui_b = _gui_pair(160), _gui_pair(236)
SIGNS['guinchar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _gui_hook, 'handshape_view': {'yaw': -80},
    'keys': [(0.0, _gui_a), (0.4, _gui_a), (1.3, _gui_b), (1.9, _gui_b), (2.4, _gui_a)],
    'arrows': [{'d': 'M 150 250 L 236 250'}],
    'mirror_second': True,
}
TITLES['guinchar'] = 'Sinal de guinchar em Libras'
