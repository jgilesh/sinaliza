# EMAGRECER: both hands in I (only the little finger up), palms forward, apart at chest width; they
# come down and in to the front of the belly and end next to each other, the right hand a little
# higher. Once, with the cheeks sucked in. (UFSC Signbank EMAGRECER: i + i; INES EMAGRECER.)


def hs_emagrecer_i():
    """I of Libras: only the little finger straight, the others closed under the thumb."""
    shape = fist({'pinky': fing(-6, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['index', 'middle'], at=0.5)
    return shape


_ema_i = hs_emagrecer_i()
_ema = lambda at, roll, **kw: P(at, _ema_i, 'wrist', yaw=12, pitch=-6, roll=roll, scale=1.05, depth=60,
                                pole=(0.35, 1.0, 0.4), **kw)
_ema_r0 = _ema((140, 206), -6)
_ema_r1 = _ema((175, 246), 8, via=(150, 234))
_ema_l0 = mirrored(_ema_r0)
_ema_l1 = mirrored(_ema((177, 256), 8, via=(150, 244)))   # the left hand ends a little lower
_ema_rb, _ema_lb = dict(_ema_r0), dict(_ema_l0)
SIGNS['emagrecer'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _ema_i,
    'keys': [(0.0, [_ema_r0, _ema_l0]), (0.35, [_ema_r0, _ema_l0]), (1.05, [_ema_r1, _ema_l1]),
             (1.85, [_ema_r1, _ema_l1]), (2.4, [_ema_rb, _ema_lb])],
    'arrows': [{'trail': 0, 'from': 0.35, 'to': 1.05, 'offset': (-22, 26), 'trim': 0.08},
               {'trail': 1, 'from': 0.35, 'to': 1.05, 'offset': (22, 26), 'trim': 0.08}],
    'mirror_second': True,
}
TITLES['emagrecer'] = 'Sinal de emagrecer em Libras'
