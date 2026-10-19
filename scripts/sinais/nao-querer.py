# NÃO QUERER: open hand in a claw (fingers spread and bent), palm up and toward the body, in front of the
# chin on the signing side; the wrist turns quickly and the hand drops, ending in front of the waist with
# the palm down and the fingers pointing at the floor. Once. No contact. (UFSC Signbank QUERER-NÃO:
# 5_claw; INES QUERER-NÃO.)


def hs_nao_querer_claw():
    """5 in a claw: fingers spread and bent at the middle and end joints, thumb out and bent."""
    return {'index': fing(16, 12, 48, 34), 'middle': fing(4, 12, 50, 36), 'ring': fing(-8, 14, 50, 36),
            'pinky': fing(-19, 16, 48, 34), 'thumb': (22.0, 30.0, 30.0, 16.0, 30.0)}


_nq_claw = hs_nao_querer_claw()
# Start: palm up and toward the face, the clawed fingers pointing up in front of the chin on the signing
# side; the back of the hand to the viewer, turned a little so the bent fingers show from the side.
_nq_up = P((152, 192), _nq_claw, 'wrist', yaw=155, pitch=-30, roll=-6, scale=1.1, depth=55, pole=(0.45, 1.0, 0.4))
# End: low, the palm down and toward the body, fingers pointing down and a little forward.
_nq_down = P((148, 232), _nq_claw, 'wrist', yaw=205, pitch=30, roll=180, scale=1.1, depth=70, ease='out',
             via=(118, 214), pole=(0.45, 1.0, 0.4))
SIGNS['nao-querer'] = {
    'poster': 0.3, 'dur': 2.2, 'hands': ['right'], 'handshape': _nq_claw, 'handshape_view': {'yaw': 30, 'pitch': -20},
    'keys': [(0.0, [_nq_up]), (0.4, [_nq_up]), (0.75, [_nq_down]), (1.6, [_nq_down]),
             (2.2, [dict(_nq_up, via=(112, 220))])],
    # On the outer side: the hand turns over and drops.
    'arrows': [{'d': 'M 100 150 Q 80 196 106 238'}],
}
TITLES['nao-querer'] = 'Sinal de não querer em Libras'
