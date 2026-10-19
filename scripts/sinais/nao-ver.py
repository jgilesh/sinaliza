# NÃO VER: flat hand (B), fingers together, palm toward the face, comes down in front of the face from the
# forehead to the chin, passing over the eyes as if covering them, and then moves away down. Once. No
# contact. (UFSC Signbank VER-NÃO; INES VER-NÃO agrees.)


def hs_nao_ver_B():
    """Flat hand, fingers together and straight, the thumb lying alongside the index."""
    shape = hs_B()
    shape['thumb'] = (-25.0, 0.0, 20.0, 5.0, 5.0)
    return shape


_nao_ver_b = hs_nao_ver_B()
# Beside the face, ready: palm toward the signer's face, fingers up.
_nao_ver_ready = P((132, 150), _nao_ver_b, 'fingertips', yaw=150, roll=8, scale=1.0, depth=40, pole=(0.45, 1.0, 0.5))
# On the forehead: the back of the hand to the viewer, fingers up and leaning toward the other side.
_nao_ver_top = P((206, 50), _nao_ver_b, 'fingertips', yaw=180, roll=28, scale=1.0, depth=34, pole=(0.45, 1.0, 0.5))
# Over the eyes and nose, turning as it comes down.
_nao_ver_mid = P((224, 84), _nao_ver_b, 'fingertips', yaw=180, roll=55, scale=1.0, depth=36, pole=(0.45, 1.0, 0.5),
                 ease='linear')
# At the chin: fingers across, pointing to the other side.
_nao_ver_chin = P((238, 132), _nao_ver_b, 'fingertips', yaw=180, roll=82, scale=1.0, depth=40, pole=(0.45, 1.0, 0.5))
# Away, down in front of the chest.
_nao_ver_off = P((206, 214), _nao_ver_b, 'fingertips', yaw=170, roll=95, scale=1.05, depth=60, pole=(0.45, 1.0, 0.5))
SIGNS['nao-ver'] = {
    'poster': 0.7, 'dur': 2.6, 'hands': ['right'], 'handshape': _nao_ver_b,
    'keys': [(0.0, [_nao_ver_ready]), (0.2, [_nao_ver_ready]), (0.6, [_nao_ver_top]), (0.8, [_nao_ver_top]),
             (1.1, [_nao_ver_mid]), (1.4, [_nao_ver_chin]), (1.75, [_nao_ver_off]), (2.1, [_nao_ver_off]),
             (2.6, [dict(_nao_ver_ready, via=(120, 210))])],
    # Down in front of the face, on the side the fingers point to.
    'arrows': [{'d': 'M 268 54 Q 276 98 262 140'}],
}
TITLES['nao-ver'] = 'Sinal de não ver em Libras'
