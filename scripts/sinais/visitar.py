# VISITAR: P of Libras (index and middle out, the thumb resting between them on the middle finger),
# the middle fingertip touching just under the eye, palm toward the face; the hand comes down in an arc
# in front of the chest and ends beside the body on its own side, palm down, fingers pointing to that
# side. Once. (UFSC Signbank VISITAR: [Libras_P] at the cheek; INES VISITAR.)


def hs_visitar_p():
    """P of Libras: index straight, middle straight but tipped forward at the knuckle, the thumb's pad
    on the inside of the middle finger near its knuckle; ring and little finger folded."""
    shape = fist({'index': fing(6, 0, 0, 0), 'middle': fing(-4, 40, 0, 0)})
    target = on_surface(shape, 'middle', 0, 1, seg_radius('thumb', 2) * 0.9, at=0.75)
    shape['thumb'] = solve_thumb(target, pref=(10.0, 40.0, 40.0, 10.0, 10.0))
    return shape


_vis_p = hs_visitar_p()
_vis_on = P((181, 108), _vis_p, 'middle_tip', yaw=200, pitch=0, roll=-25, scale=1.0, depth=30, pole=(0.5, 1.0, 0.45))
_vis_off = P((112, 226), _vis_p, 'fingertips', yaw=270, pitch=-20, roll=-90, scale=1.15, depth=90, pole=(0.5, 1.0, 0.45),
             via=(210, 230))
SIGNS['visitar'] = {
    'poster': 0.0, 'dur': 2.6, 'hands': ['right'], 'handshape': _vis_p, 'handshape_view': {'yaw': -60},
    'keys': [(0.0, [_vis_on]), (0.4, [_vis_on]), (1.3, [_vis_off]), (2.0, [_vis_off]), (2.6, [dict(_vis_on, via=(150, 170))])],
    'marks': [(190, 114, 40)],
    'arrows': [{'trail': 0, 'from': 0.4, 'to': 1.3, 'offset': (12, 22), 'trim': 0.06}],
}
TITLES['visitar'] = 'Sinal de visitar em Libras'
