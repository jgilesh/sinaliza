# PROVAR: open hand (fingers together and straight, thumb apart) beside the forehead, palm forward;
# it comes down in an arc in front of the face and ends lying across in front of the chest, palm
# toward the body, fingers pointing to the other side. Once. (UFSC Signbank PROVAR, INES PROVAR1.)

_provar_b = hs_B()
_provar_up = P((120, 120), _provar_b, 'wrist', yaw=25, pitch=0, roll=-12, scale=1.05, depth=50, pole=(0.15, 1.0, 0.25))
_provar_down = P((160, 222), _provar_b, 'wrist', yaw=169, pitch=0, roll=90, scale=1.1, depth=60,
                 via=(164, 160), pole=(0.4, 1.0, 0.4))
SIGNS['provar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right'], 'handshape': _provar_b,
    'keys': [(0.0, [_provar_up]), (0.35, [_provar_up]), (1.0, [_provar_down]), (1.8, [_provar_down]),
             (2.4, [dict(_provar_up, via=(130, 180))])],
    'arrows': [{'d': 'M 94 122 Q 100 210 146 242'}],
}
TITLES['provar'] = 'Sinal de provar em Libras'
