# MENSTRUAR: A hand (fist, thumb straight up beside the index), palm toward the other side. The top
# of the fist taps under the chin on the signing side and the hand drops to the front of the chest,
# twice. (UFSC Signbank MENSTRUAR: A, queixo. The INES video shows another variant, low at the belly.)


def hs_menstruar_up():
    """Thumbs up: fist, the thumb straight and out to the radial side, close to the index knuckle (the
    'A' of the Signbank entry as the video shows it: thumb up while the folded fingers face forward)."""
    return fist({'thumb': (40.0, 10.0, 8.0, 4.0, 4.0)})


_menstruar_a = hs_menstruar_up()


def _menstruar_pose(at, **kw):
    # Palm turned toward the midline and a little toward the viewer: the folded fingers show in front
    # and the thumb stands up along the side of the index.
    return P(at, _menstruar_a, 'thumb_tip', yaw=-170, pitch=70, roll=95, scale=1.05, pole=(0.45, 1.0, 0.45), **kw)


_menstruar_up = _menstruar_pose((191, 150), depth=40)
_menstruar_low = _menstruar_pose((184, 202), depth=62)
_menstruar_keys = [(0.0, [_menstruar_low]), (0.3, [_menstruar_low])]
for _menstruar_i in range(2):
    _menstruar_t = 0.3 + 0.8 * _menstruar_i
    _menstruar_keys += [(_menstruar_t + 0.3, [_menstruar_up]), (_menstruar_t + 0.42, [_menstruar_up]),
                        (_menstruar_t + 0.8, [dict(_menstruar_low, ease='out')])]
_menstruar_keys += [(2.4, [_menstruar_low])]
SIGNS['menstruar'] = {
    'poster': 0.66, 'dur': 2.4, 'hands': ['right'], 'handshape': _menstruar_a, 'handshape_view': {'yaw': 30},
    'keys': _menstruar_keys,
    'marks': [(191, 148, 0)],
    'marks_under': True,
    'arrows': [{'d': 'M 160 160 L 160 196'}],
}
TITLES['menstruar'] = 'Sinal de menstruar em Libras'
