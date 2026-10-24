# ALIVIAR: closed fist (S) resting on the upper chest, palm toward the body and the thumb side up;
# it slides a little down the chest, once, as the face relaxes. (UFSC Signbank ALIVIAR-2: S, chest,
# continuous contact; the INES ALIVIAR video shows another variant at the forehead.)

_aliviar_s = hs_S()
# Forearm rising across the body, knuckles up and toward the signer's left, the thumb side turned a
# little toward the viewer so the thumb lying across the folded fingers reads (straight from the back
# the fist is a blob with no thumb).
_aliviar_pose = lambda at, **kw: P(at, _aliviar_s, 'wrist', yaw=250, pitch=0, roll=52, scale=1.15, depth=24,
                                   pole=(0.6, 1.0, 0.2), **kw)
_aliviar_off = _aliviar_pose((184, 236))
_aliviar_on = _aliviar_pose((194, 212))
_aliviar_down = _aliviar_pose((194, 228), ease='smooth')
SIGNS['aliviar'] = {
    'poster': 0.6, 'dur': 2.4, 'hands': ['right'], 'handshape': _aliviar_s, 'handshape_view': {'yaw': -30},
    'keys': [(0.0, [_aliviar_off]), (0.3, [_aliviar_on]), (0.6, [_aliviar_on]), (1.3, [_aliviar_down]),
             (2.0, [_aliviar_down]), (2.4, [_aliviar_off])],
    'marks': [(236, 192, 75)],
    # A short arrow beside the fist: it slides down the chest.
    'arrows': [{'d': 'M 250 194 L 250 224'}],
}
TITLES['aliviar'] = 'Sinal de aliviar em Libras'
