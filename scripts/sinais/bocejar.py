# BOCEJAR: flat hand (B), fingers together; the hand rises and covers the mouth, palm on the mouth and
# fingers up (tilted a little toward the other side, under the eyes), and stays there a moment, as when
# yawning. (UFSC Signbank BOCEJAR: B, boca.)
_boc_b = hs_B()
# Back of the hand to the viewer, fingers up and leaning toward the other side; the fingertips stop
# under the eyes, the fingers cover the mouth.
_boc_on = P((209, 112), _boc_b, 'fingertips', yaw=180, pitch=-8, roll=22, scale=1.0, depth=38, pole=(0.5, 1.0, 0.45))
_boc_low = P((176, 196), _boc_b, 'fingertips', yaw=170, pitch=-5, roll=15, scale=1.05, depth=50, pole=(0.5, 1.0, 0.45))
SIGNS['bocejar'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right'], 'handshape': _boc_b,
    'keys': [(0.0, [_boc_low]), (0.2, [_boc_low]), (0.7, [_boc_on]), (1.9, [_boc_on]), (2.4, [_boc_low])],
    'marks': [(230, 142, 30)],
    'arrows': [{'d': 'M 146 214 Q 136 170 152 140'}],
}
TITLES['bocejar'] = 'Sinal de bocejar em Libras'
