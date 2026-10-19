# FECHAR: both flat hands (B), fingers up, start apart at shoulder height with the palms toward each other
# and come together in front of the face like two doors closing, turning palms forward; they end side by
# side in front of the chin. Once. (UFSC Signbank FECHAR: B/B, 2s. The INES FECHAR1 video shows a
# one-handed variant: one hand closes like a door.)


def hs_fechar_B():
    """Flat hand, fingers together and straight, the thumb lying alongside the index."""
    shape = hs_B()
    shape['thumb'] = (-25.0, 0.0, 20.0, 5.0, 5.0)
    return shape


_fec_b = hs_fechar_B()
# Open: out at shoulder height, palm toward the midline and a little toward the viewer.
_fec_open = P((112, 204), _fec_b, 'wrist', yaw=55, pitch=0, roll=-8, scale=1.08, depth=55, pole=(0.5, 1.0, 0.4))
# Closed: palms forward, the hands side by side in front of the chin, the thumb sides almost touching.
_fec_shut = P((171, 224), _fec_b, 'wrist', yaw=8, pitch=0, roll=3, scale=1.1, depth=70, pole=(0.35, 1.0, 0.4),
              via=(140, 206))
_fec_back = dict(_fec_open, via=(130, 236))
SIGNS['fechar'] = {
    'poster': 1.3, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _fec_b,
    'keys': [(0.0, [_fec_open, mirrored(_fec_open)]), (0.35, [_fec_open, mirrored(_fec_open)]),
             (0.95, [_fec_shut, mirrored(_fec_shut)]), (1.9, [_fec_shut, mirrored(_fec_shut)]),
             (2.6, [_fec_back, mirrored(_fec_back)])],
    # Below the hands: each hand swings in to the middle.
    'arrows': [{'d': 'M 100 246 Q 130 262 160 254'}, {'d': 'M 300 246 Q 270 262 240 254'}],
    'mirror_second': True,
}
TITLES['fechar'] = 'Sinal de fechar em Libras'
