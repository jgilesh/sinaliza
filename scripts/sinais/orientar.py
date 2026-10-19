# ORIENTAR: the support hand open (B), fingers pointing across toward the dominant side, palm toward
# the body, thumb up. The dominant hand, in an open beak, holds the support fingertips and both hands
# move together to the dominant side, as if leading someone. Once. (UFSC Signbank GUIA/ORIENTAR:
# Beak_open + B, at the fingertips of the support hand.)


def hs_orientar_beak():
    """Open beak: fingers together and gently bent, the thumb opposite them with a gap between."""
    return {'index': fing(1, 36, 34, 18), 'middle': fing(-1, 38, 34, 18), 'ring': fing(-3, 41, 32, 18),
            'pinky': fing(-5, 44, 30, 18), 'thumb': (6.0, 55.0, 60.0, 18.0, 18.0)}


_ori_beak, _ori_b = hs_orientar_beak(), hs_B()
# Support (left) hand: at its screen place, written as a right hand (back to the viewer, fingers across).
_ori_sup = lambda x: P((x, 220), _ori_b, 'wrist', yaw=180, pitch=0, roll=90, scale=1.05, depth=75, pole=(0.5, 1.0, 0.4))
_ori_dom = lambda x: P((x, 214), _ori_beak, 'fingertips', yaw=160, pitch=0, roll=90, scale=1.05, depth=80,
                       pole=(0.45, 1.0, 0.45))
_ori_a = [_ori_dom(206), _ori_sup(250)]
_ori_b2 = [_ori_dom(166), _ori_sup(210)]
SIGNS['orientar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _ori_beak, 'handshape_view': {'yaw': 60},
    'keys': [(0.0, _ori_a), (0.3, _ori_a), (1.0, _ori_b2), (1.9, _ori_b2), (2.4, _ori_a)],
    'mirror_second': True,
    'arrows': [{'d': 'M 204 176 L 160 176'}],
}
TITLES['orientar'] = 'Sinal de orientar em Libras'
