# NOME: U hand (index and middle straight and together), palm forward, starts in front of the chest
# and rises in a short arc up and out to beside the face, fingers up. No contact. (UFSC Signbank;
# INES shows only the end of the path, the hand held beside the shoulder.)


def hs_nome_U():
    """U of Libras: index and middle fingers straight and side by side, ring and little fingers folded
    under the thumb."""
    shape = fist({'index': fing(-1, 0, 0, 0), 'middle': fing(1, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


_nome_u = hs_nome_U()
_nome_start = P((178, 236), _nome_u, 'wrist', yaw=-10, pitch=0, roll=18, scale=1.15, depth=70, ease='smooth')
_nome_end = P((124, 172), _nome_u, 'wrist', yaw=-5, pitch=0, roll=-4, scale=1.15, depth=60, via=(140, 226))
SIGNS['nome'] = {
    'poster': 1.2, 'dur': 2.2, 'hands': ['right'], 'handshape': _nome_u,
    'keys': [(0.0, [_nome_start]), (0.3, [_nome_start]), (0.9, [_nome_end]), (1.8, [_nome_end]),
             (2.2, [dict(_nome_start, via=(150, 250))])],
    'arrows': [{'trail': 0, 'from': 0.3, 'to': 0.9, 'offset': (-26, -8), 'trim': 0.1}],
}
TITLES['nome'] = 'Sinal de nome em Libras'
