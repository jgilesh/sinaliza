# GASTAR: both hands beside the waist, palms up, start with the fingertips gathered on the thumb (O) and
# flick open into 5 (fingers straight and spread), out and up, as if throwing money away; twice, both
# hands together. (UFSC Signbank GASTAR: O+5, flank. The INES GASTAR1 video shows another variant, the
# hands opening at shoulder height.)
_gas_o, _gas_5 = HANDSHAPES['O'](), HANDSHAPES['5']()


def _gas_pose(shape, ease='smooth'):
    # Palm up and tipped toward the viewer, fingers pointing forward and out: the gathered fingertips and
    # then the open, spread fingers show.
    return P((122, 266), shape, 'wrist', yaw=40, pitch=22, roll=-98, scale=1.12, depth=70, ease=ease)


_gas_closed, _gas_open = _gas_pose(_gas_o), _gas_pose(_gas_5, 'out')
_gas_k = lambda pose: [pose, mirrored(pose)]
SIGNS['gastar'] = {
    'poster': 0.6, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _gas_5, 'handshape_view': {'yaw': 0},
    'keys': [(0.0, _gas_k(_gas_closed)), (0.35, _gas_k(_gas_closed)), (0.6, _gas_k(_gas_open)),
             (0.9, _gas_k(_gas_closed)), (1.15, _gas_k(_gas_open)), (1.9, _gas_k(_gas_open)),
             (2.4, _gas_k(_gas_closed))],
    'arrows': [{'d': 'M 74 240 Q 62 226 66 208'}, {'d': 'M 326 240 Q 338 226 334 208'}],
    'mirror_second': True,
}
TITLES['gastar'] = 'Sinal de gastar em Libras'
