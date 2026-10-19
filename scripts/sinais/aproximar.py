# APROXIMAR: both hands in A (fist, thumb up), apart in front of the chest, palms toward each other. The
# support hand stays; the dominant hand moves across to it until it touches it, once. (UFSC Signbank
# APROXIMAR: A + A, final contact, straight. The INES APROXIMAR1 video shows another variant: two index
# fingers up, one coming to the other.)
_aprox_a = HANDSHAPES['A']()


def _aprox_pose(x, y=196, ease='smooth'):
    # Palm turned toward the other hand and a little toward the viewer: the folded fingers and the thumb
    # along the index read, and the two thumbs face each other.
    return P((x, y), _aprox_a, 'thumb_tip', yaw=-14, pitch=-10, roll=8, scale=1.15, depth=70,
             pole=(0.3, 1.0, 0.4), ease=ease)


_aprox_sup = mirrored(_aprox_pose(182))            # support hand, on its own side of the midline (x 218)
_aprox_far = _aprox_pose(140)
_aprox_near = _aprox_pose(206, ease='in')          # touches the support hand
SIGNS['aproximar'] = {
    'poster': 1.1, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _aprox_a,
    'handshape_view': {'yaw': -18, 'pitch': -8},
    'keys': [(0.0, [_aprox_far, _aprox_sup]), (0.35, [_aprox_far, _aprox_sup]),
             (0.95, [_aprox_near, _aprox_sup]), (1.9, [_aprox_near, _aprox_sup]),
             (2.4, [_aprox_far, _aprox_sup])],
    'arrows': [{'trail': 0, 'from': 0.35, 'to': 0.95, 'offset': (-10, -62), 'trim': 0.05}],
    # The dominant thumb side comes to rest against the support hand.
    'marks': [(212, 186, 0)],
    'mirror_second': True,
}
TITLES['aproximar'] = 'Sinal de aproximar em Libras'
