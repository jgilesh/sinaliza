# ENTREGAR: both hands in a beak (fingertips gathered on the thumb), palms up, in front of the chest;
# together they go forward in an arc, a little up, ending with the fingertips pointing forward, as
# if handing something over. Once. (UFSC Signbank ENTREGAR; INES ENTREGAR.)


def hs_entregar_beak():
    """Beak: fingers together, bent at the knuckles and middle joints, their tips gathered on the
    thumb's pad (the thumb's pad presses on the index and middle fingertips)."""
    shape = {'index': fing(1, 50, 30, 14), 'middle': fing(-1, 54, 30, 14), 'ring': fing(-3, 58, 28, 14),
             'pinky': fing(-5, 62, 26, 14)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


_ent_h = hs_entregar_beak()
# Palm turned up and toward the other hand, fingertips up: the beak reads from the palm side.
_ent_start = P((146, 252), _ent_h, 'wrist', yaw=60, pitch=-25, roll=12, scale=1.05, depth=75, pole=(0.5, 1.0, 0.4))
# Forward and a little up: the fingertips tip toward the viewer.
_ent_end = P((146, 226), _ent_h, 'wrist', yaw=45, pitch=45, roll=8, scale=1.35, depth=115, via=(140, 248),
             pole=(0.5, 1.0, 0.4))
_ent_back = dict(_ent_start, via=(150, 236))
SIGNS['entregar'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _ent_h, 'handshape_view': {'yaw': 60, 'pitch': -10},
    'keys': [(0.0, [_ent_start, mirrored(_ent_start)]), (0.3, [_ent_start, mirrored(_ent_start)]),
             (1.0, [_ent_end, mirrored(_ent_end)]), (1.9, [_ent_end, mirrored(_ent_end)]),
             (2.4, [_ent_back, mirrored(_ent_back)])],
    # Beside each hand: forward and a little up, in an arc.
    'arrows': [{'d': 'M 108 262 Q 98 236 112 212'}, {'d': 'M 292 262 Q 302 236 288 212'}],
    'mirror_second': True,
}
TITLES['entregar'] = 'Sinal de entregar em Libras'
