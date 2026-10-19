# VOLTAR: the support hand is closed (fist, thumb side up) in front of the chest. The signing hand, with
# the index bent into a hook (the other fingers closed), comes in an arc from the side, at shoulder
# height, and hooks the index over the thumb side of the fist, pointing down. Once. (UFSC Signbank
# VOLTAR; INES VOLTAR1.)


def hs_voltar_X():
    """Index bent into a hook (X): it rises from the knuckle and curls down at the middle and end
    joints; the other fingers closed, the thumb across the middle finger."""
    shape = fist({'index': fing(2, 0, 80, 45)})
    shape['thumb'] = thumb_over(shape, ['middle'])
    return shape


_voltar_x, _voltar_s = hs_voltar_X(), hs_S()
# Support fist (a right-hand pose, mirrored): palm toward the body, thumb on top.
_voltar_sup = mirrored(P((178, 236), _voltar_s, 'wrist', yaw=120, pitch=0, roll=72, scale=1.05, depth=58,
                         pole=(0.3, 1.0, 0.45)))
_voltar_pole = (0.45, 1.0, 0.45)
# On the fist: back of the hand to the viewer and up, the hook pointing down onto the thumb side.
_voltar_on = P((210, 206), _voltar_x, 'index_tip', yaw=105, pitch=0, roll=76, scale=1.05, depth=64, pole=_voltar_pole)
# Start: out at the side, at shoulder height, the hook already formed, seen from the thumb side.
_voltar_out = P((112, 160), _voltar_x, 'index_tip', yaw=-50, pitch=0, roll=-10, scale=1.05, depth=52, pole=_voltar_pole)
SIGNS['voltar'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _voltar_x, 'handshape_view': {'yaw': -75, 'pitch': -15},
    'keys': [(0.0, [_voltar_out, _voltar_sup]), (0.3, [_voltar_out, _voltar_sup]),
             (0.95, [dict(_voltar_on, via=(150, 140)), _voltar_sup]), (1.8, [_voltar_on, _voltar_sup]),
             (2.4, [dict(_voltar_out, via=(160, 200)), _voltar_sup])],
    'arrows': [{'d': 'M 108 140 Q 150 112 192 160'}],
    'marks': [(222, 198, 40)],
    'mirror_second': True,
}
TITLES['voltar'] = 'Sinal de voltar em Libras'
