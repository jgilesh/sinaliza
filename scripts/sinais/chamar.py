# CHAMAR: flat hand raised at face height beside the chin, fingers up, palm forward; the fingers fold
# 90 degrees at the knuckles and the hand turns and comes back toward the body (palm toward it), as when
# beckoning someone to come. Twice. (UFSC Signbank CHAMAR: B+B_bent, neutral space, arc back; INES
# CHAMAR1 agrees.)


def hs_chamar_flat():
    """B: fingers together and straight, the thumb a little apart along the index."""
    shape = hs_B()
    shape['thumb'] = (-18.0, 18.0, 20.0, 8.0, 6.0)
    return shape


def hs_chamar_bent():
    """B bent at the base: the four fingers stay straight and together and fold 90 degrees at the
    knuckles; the thumb stays alongside."""
    return {'index': fing(2, 82, 6, 4), 'middle': fing(0, 84, 6, 4), 'ring': fing(-2, 84, 6, 4),
            'pinky': fing(-4, 82, 8, 5), 'thumb': (-18.0, 18.0, 20.0, 8.0, 6.0)}


_chamar_up, _chamar_bent = hs_chamar_flat(), hs_chamar_bent()
# Up: beside the chin, out from the face, the palm to the viewer and turned a little toward the midline.
_chamar_a = P((122, 168), _chamar_up, 'wrist', yaw=20, pitch=-10, roll=-6, scale=1.1, depth=50, pole=(0.6, 1.0, 0.45))
# Called in: the fingers fold over toward the signer, the hand turns (palm toward the face and body, the
# bent fingers seen from the side) and comes back a little, nearer the shoulder.
_chamar_b = P((134, 172), _chamar_bent, 'wrist', yaw=70, pitch=-25, roll=-4, scale=1.04, depth=36, pole=(0.6, 1.0, 0.45))
SIGNS['chamar'] = {
    'poster': 0.0, 'dur': 2.2, 'hands': ['right'], 'handshape': _chamar_up,
    'keys': [(0.0, [_chamar_a]), (0.3, [_chamar_a]), (0.6, [_chamar_b]), (0.85, [_chamar_a]), (1.15, [_chamar_b]),
             (1.45, [_chamar_a]), (2.2, [_chamar_a])],
    # The fingers fold over and the hand comes back toward the body.
    'arrows': [{'d': 'M 92 74 Q 122 58 144 84'}],
}
TITLES['chamar'] = 'Sinal de chamar em Libras'
