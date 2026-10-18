# CHEGAR: both hands flat (B), fingers together, thumb apart. The support hand stands upright in
# front of the body on its own side, palm turned in toward the other hand. The signing hand starts
# up near the face and comes down in an arc, forward and across, until it comes close to the palm
# of the support hand (without touching). Once. (UFSC Signbank CHEGAR.)

_chegar_b = hs_B()
# Support hand (defined as a right hand, then mirrored to the left): upright, palm toward the midline.
_chegar_base = mirrored(P((130, 200), _chegar_b, 'wrist', yaw=62, pitch=0, roll=-4, scale=1.12, depth=80))
_chegar_up = P((146, 156), _chegar_b, 'wrist', yaw=55, pitch=0, roll=-10, scale=1.08, depth=45,
               pole=(0.5, 1.0, 0.45))
_chegar_end = P((224, 202), _chegar_b, 'fingertips', yaw=160, pitch=15, roll=78, scale=1.15, depth=85,
                via=(150, 190), pole=(0.4, 1.0, 0.4))
SIGNS['chegar'] = {
    'poster': 1.2, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _chegar_b,
    'keys': [(0.0, [_chegar_up, _chegar_base]), (0.4, [_chegar_up, _chegar_base]),
             (1.1, [_chegar_end, _chegar_base]), (1.9, [_chegar_end, _chegar_base]),
             (2.6, [dict(_chegar_up, via=(150, 200)), _chegar_base])],
    'arrows': [{'d': 'M 118 156 Q 104 210 158 228'}],
    'mirror_second': True,
}
TITLES['chegar'] = 'Sinal de chegar em Libras'
