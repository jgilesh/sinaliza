# RESUMIR: both hands start open with the fingers spread, apart in front of the body. They come to
# the middle closing the fingers into a "bico" (all fingertips together on the thumb), until the
# fingertips of one hand meet those of the other in front of the chest, then stop. (UFSC Signbank
# RESUMIR; INES RESUMIR agrees.)


def hs_resumir_bico():
    """Bico: the four fingers bent mostly at the knuckles, nearly straight, their tips gathered on
    the thumb pad."""
    shape = {'index': fing(-2, 52, 26, 14), 'middle': fing(-4, 50, 30, 16), 'ring': fing(-2, 50, 32, 18),
             'pinky': fing(2, 52, 34, 20)}
    shape['thumb'] = pinch_thumb(shape, ('index', 'middle'))
    return shape


_resumir_bico, _resumir_5 = hs_resumir_bico(), hs_5()
# Open: palm forward, a little turned toward the midline, apart beside the body.
_resumir_open = P((116, 222), _resumir_5, 'wrist', yaw=20, pitch=0, roll=-14, scale=1.1, depth=60, pole=(0.35, 1.0, 0.4))
_resumir_mid = P((140, 214), lerp(_resumir_5, _resumir_bico, 0.55), 'wrist', yaw=45, pitch=0, roll=6, scale=1.1,
                 depth=66)
# Closed: the gathered fingertips point at the other hand and meet it in the middle; the hand is
# seen from the thumb side, palm turned toward the midline, so the bico reads.
_resumir_meet = P((197, 200), _resumir_bico, 'pinch', yaw=60, pitch=0, roll=48, scale=1.1, depth=70, ease='out')
_resumir_k = lambda p: [p, mirrored(p)]
SIGNS['resumir'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _resumir_bico, 'handshape_view': {'yaw': 60},
    'keys': [(0.0, _resumir_k(_resumir_open)), (0.35, _resumir_k(_resumir_open)), (0.65, _resumir_k(_resumir_mid)),
             (0.95, _resumir_k(_resumir_meet)), (1.9, _resumir_k(_resumir_meet)),
             (2.4, _resumir_k(dict(_resumir_open, ease='smooth')))],
    # Toward the middle, below the hands.
    'arrows': [{'d': 'M 112 262 Q 146 272 178 256'}, {'d': 'M 288 262 Q 254 272 222 256'}],
    'mirror_second': True,
}
TITLES['resumir'] = 'Sinal de resumir em Libras'
