# COLOCAR: the support hand lies open in front of the chest, palm up. The signing hand, fingertips
# gathered on the thumb (as if holding something small), starts beside the head and comes down in an
# arc, in and down, until the fingertips touch the support palm. Once. (UFSC Signbank COLOCAR:
# Flower + B, final contact. INES COLOCAR1 shows a one-handed variant that moves out to the side.)


def hs_colocar_bunch():
    """Fingertips together on the thumb tip (flat O), the fingers bent mostly at the knuckles."""
    shape = {'index': fing(2, 52, 34, 22), 'middle': fing(0, 56, 32, 22), 'ring': fing(-2, 60, 30, 20),
             'pinky': fing(-4, 64, 28, 20)}
    shape['thumb'] = pinch_thumb(shape)
    return shape


def hs_colocar_flat():
    """Support hand: open, fingers together and a little curved, thumb a little apart."""
    return {'index': fing(2, 8, 12, 8), 'middle': fing(0, 8, 12, 8), 'ring': fing(-2, 8, 12, 8),
            'pinky': fing(-4, 10, 12, 8), 'thumb': (22.0, 18.0, 10.0, 8.0, 6.0)}


_colocar_bunch, _colocar_flat = hs_colocar_bunch(), hs_colocar_flat()
_colocar_pole = (0.45, 1.0, 0.4)
# Support hand (defined as a right hand, then mirrored): palm up, tipped a little toward the viewer,
# fingers pointing across toward the midline.
_colocar_base = mirrored(P((146, 250), _colocar_flat, 'wrist', yaw=-50, pitch=0, roll=92, scale=1.1, depth=70))
# Start: beside the head on the dominant side, the gathered fingertips up, thumb side to the viewer.
_colocar_up = P((112, 150), _colocar_bunch, 'wrist', yaw=-70, pitch=0, roll=-8, scale=1.05, depth=55, pole=_colocar_pole)
# End: the gathered fingertips pointing down onto the support palm, thumb side to the viewer.
_colocar_on = P((236, 232), _colocar_bunch, 'index_tip', yaw=-60, pitch=20, roll=170, scale=1.05, depth=72,
                via=(150, 196), ease='in', pole=_colocar_pole)
_colocar_back = dict(_colocar_up, via=(150, 230), ease='smooth')
SIGNS['colocar'] = {
    'poster': 1.0, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _colocar_bunch, 'handshape_view': {'yaw': -85},
    'keys': [(0.0, [_colocar_up, _colocar_base]), (0.35, [_colocar_up, _colocar_base]),
             (1.0, [_colocar_on, _colocar_base]), (1.9, [_colocar_on, _colocar_base]),
             (2.6, [_colocar_back, _colocar_base])],
    'arrows': [{'trail': 0, 'from': 0.35, 'to': 1.0, 'offset': (-22, 26), 'trim': 0.16}],
    'marks': [(252, 226, 60)],
    'mirror_second': True,
}
TITLES['colocar'] = 'Sinal de colocar em Libras'
