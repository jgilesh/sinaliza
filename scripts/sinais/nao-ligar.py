# NÃO LIGAR: both hands closed (S) in front of the shoulders rise and open, the fingers spread and a
# little curved, up to the sides of the head behind the ears, palms toward the head, as if tossing
# something back over the shoulders; then they come down. Once. (UFSC Signbank LIGAR-NÃO-2: S/S; the
# INES NÃO LIGAR video shows another variant, one hand.)


def hs_nao_ligar_open():
    """Open hand, fingers spread and a little curved, thumb out."""
    return {'index': fing(14, 14, 20, 12), 'middle': fing(3, 14, 22, 14), 'ring': fing(-8, 16, 22, 14),
            'pinky': fing(-17, 18, 22, 14), 'thumb': (22.0, 22.0, 12.0, 8.0, 8.0)}


_nlig_s, _nlig_open = hs_S(), hs_nao_ligar_open()
# Fists in front of the shoulders, palms toward the viewer.
_nlig_low = P((150, 206), _nlig_s, 'wrist', yaw=20, pitch=0, roll=-6, scale=1.08, depth=62, pole=(0.6, 1.0, 0.45))
# Beside the head, behind the ear: open, palm turned toward the head, fingers up and back.
_nlig_up = P((124, 118), _nlig_open, 'wrist', yaw=68, pitch=0, roll=-4, scale=1.05, depth=34,
             pole=(0.8, 1.0, 0.4), ease='out')
SIGNS['nao-ligar'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _nlig_open,
    'keys': [(0.0, [_nlig_low, mirrored(_nlig_low)]), (0.35, [_nlig_low, mirrored(_nlig_low)]),
             (0.9, [_nlig_up, mirrored(_nlig_up)]), (1.6, [_nlig_up, mirrored(_nlig_up)]),
             (2.4, [dict(_nlig_low, ease='smooth'), mirrored(dict(_nlig_low, ease='smooth'))])],
    # Up and back beside the head, both hands.
    'arrows': [{'d': 'M 106 200 Q 92 156 100 112'}, {'d': 'M 294 200 Q 308 156 300 112'}],
    'mirror_second': True,
}
TITLES['nao-ligar'] = 'Sinal de não ligar em Libras'
