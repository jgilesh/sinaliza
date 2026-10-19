# AGENDAR: the support hand open (B), upright in front of the chest, palm turned toward the signing
# hand. The signing hand touches the support palm with the fingertips together on the thumb, then
# stretches the index and slides it down the palm, as if writing a note; two touches.
# (UFSC Signbank AGENDAR: Money+G, double contact; INES AGENDAR.)


def hs_agendar_bunch():
    """Fingertips together on the thumb tip (flat O), the fingers bent mostly at the knuckles."""
    shape = {'index': fing(2, 52, 34, 22), 'middle': fing(0, 56, 32, 22), 'ring': fing(-2, 60, 30, 20),
             'pinky': fing(-4, 64, 28, 20)}
    shape['thumb'] = pinch_thumb(shape)
    return shape


_agendar_b, _agendar_bunch, _agendar_one = hs_B(), hs_agendar_bunch(), hs_1()
# Support hand (defined as a right hand, then mirrored): palm toward the signing hand and a little
# toward the viewer, fingers up and leaning toward the midline.
_agendar_base = mirrored(P((152, 252), _agendar_b, 'wrist', yaw=44, pitch=-4, roll=22, scale=1.1, depth=70))
_agendar_hand = lambda at, shape, anchor, d=74, **kw: P(at, shape, anchor, yaw=140, pitch=5, roll=45, scale=1.05,
                                                       depth=d, pole=(0.4, 1.0, 0.4), **kw)
_agendar_off = _agendar_hand((220, 212), _agendar_bunch, 'index_tip', d=60)
_agendar_tap = _agendar_hand((236, 212), _agendar_bunch, 'index_tip')
_agendar_top = _agendar_hand((236, 210), _agendar_one, 'index_tip')
_agendar_low = _agendar_hand((242, 234), _agendar_one, 'index_tip', ease='linear')
_agendar_up = _agendar_hand((224, 212), _agendar_one, 'index_tip', d=60)
SIGNS['agendar'] = {
    'poster': 0.85, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _agendar_one,
    'keys': [(0.0, [_agendar_off, _agendar_base]), (0.3, [_agendar_off, _agendar_base]),
             (0.5, [_agendar_tap, _agendar_base]), (0.7, [_agendar_top, _agendar_base]),
             (0.95, [_agendar_low, _agendar_base]), (1.15, [_agendar_up, _agendar_base]),
             (1.3, [_agendar_top, _agendar_base]), (1.55, [_agendar_low, _agendar_base]),
             (2.1, [_agendar_low, _agendar_base]), (2.6, [_agendar_off, _agendar_base])],
    'marks': [(268, 216, 80)],
    'arrows': [{'d': 'M 288 210 L 292 240'}],
    'mirror_second': True,
}
TITLES['agendar'] = 'Sinal de agendar em Libras'
