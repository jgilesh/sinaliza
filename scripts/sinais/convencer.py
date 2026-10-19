# CONVENCER: fingers straight and together, their tips on the thumb tip (bico), fingertips up toward the
# mouth; the hand swings in arcs from the mouth to the other side of the chin / neck and back, a few
# times, insisting. No contact. (UFSC Signbank CONVENCER: Beak, boca, arco ipsi/contralateral.)


def hs_convencer_bico():
    """Bico: the four fingers bent mostly at the knuckles, nearly straight, their tips gathered on
    the thumb pad."""
    shape = {'index': fing(-2, 52, 26, 14), 'middle': fing(-4, 50, 30, 16), 'ring': fing(-2, 50, 32, 18),
             'pinky': fing(2, 52, 34, 20)}
    shape['thumb'] = pinch_thumb(shape, ('index', 'middle'))
    return shape


_conv_h = hs_convencer_bico()
# Palm turned toward the middle and half to the viewer, tipped back so the bico shows in profile, the
# gathered tips up by the mouth.
_conv_mouth = P((192, 128), _conv_h, 'pinch', yaw=60, pitch=-30, roll=-5, scale=1.0, depth=40, pole=(0.5, 1.0, 0.45))
# On the other side of the chin, low by the neck; the wrist bends toward the thumb side (tips tilt in).
_conv_neck = P((218, 156), _conv_h, 'pinch', yaw=60, pitch=-30, roll=25, scale=1.0, depth=42, pole=(0.5, 1.0, 0.45),
               via=(198, 152))
_conv_back = dict(_conv_mouth, via=(212, 132))
SIGNS['convencer'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right'], 'handshape': _conv_h, 'handshape_view': {'yaw': 60, 'pitch': -20},
    'keys': [(0.0, [_conv_mouth]), (0.25, [_conv_mouth]), (0.55, [_conv_neck]), (0.85, [_conv_back]),
             (1.15, [_conv_neck]), (1.45, [_conv_back]), (2.4, [_conv_mouth])],
    'arrows': [{'d': 'M 158 194 Q 194 214 242 192', 'both': True}],
}
TITLES['convencer'] = 'Sinal de convencer em Libras'
