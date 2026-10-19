# ASSOAR: both flat hands cover the nose like a tent, the palm side of the fingers against the sides
# of the nose, backs of the hands to the viewer; together they slide down off the nose, once, as if
# blowing it into a handkerchief. (UFSC Signbank ASSOAR: B, nose, continuous contact, down. The INES
# ASSOAR video shows a one-handed variant: one hand covers the nose and moves down and forward.)
_assoar_b = hs_B()


def hs_assoar_flat():
    """B with the thumb lying alongside the index."""
    shape = hs_B()
    shape['thumb'] = (-22.0, 18.0, 20.0, 8.0, 6.0)
    return shape


_assoar_f = hs_assoar_flat()


def _assoar_pose(y, pitch=0.0, depth=26):
    return P((194, y), _assoar_f, 'fingertips', yaw=140, pitch=pitch, roll=14, scale=0.95, depth=depth,
             pole=(0.55, 1.0, 0.45))


_assoar_on = _assoar_pose(104)
_assoar_off = dict(_assoar_pose(132, pitch=25, depth=40), ease='in')
_assoar_back = dict(_assoar_on, ease='smooth')
SIGNS['assoar'] = {
    'poster': 0.3, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _assoar_f,
    'keys': [(0.0, [_assoar_on, mirrored(_assoar_on)]), (0.3, [_assoar_on, mirrored(_assoar_on)]),
             (0.8, [_assoar_off, mirrored(_assoar_off)]), (1.6, [_assoar_off, mirrored(_assoar_off)]),
             (2.2, [_assoar_back, mirrored(_assoar_back)])],
    'marks': [(200, 100, 0)],
    'arrows': [{'d': 'M 140 110 L 140 140'}, {'d': 'M 260 110 L 260 140'}],
    'mirror_second': True,
}
TITLES['assoar'] = 'Sinal de assoar em Libras'
