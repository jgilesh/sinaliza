# MÃE: A hand (thumb straight up beside the fist) touches the cheek by the folded fingers; then the
# hand comes down, the thumb closes over the fingers (S) and the fist, lying across with the back
# of the fingers to the viewer, touches under the chin. (UFSC Signbank MÃE: A+S, cheek then chin;
# INES has no entry.)


def hs_mae_A():
    """A of Libras with the thumb standing up beside the fist (as in MÃE): fist, thumb straight
    along the side of the index, its tip a little above the knuckles."""
    shape = fist()
    shape['thumb'] = solve_thumb((17.0, -44.0, -1.5), pad_to=(-1.0, 0.0, 0.0), point=(0.0, -1.0, 0.0),
                                 pref=(-5.0, 10.0, 20.0, 0.0, 0.0))
    return shape


_mae_a, _mae_s = hs_mae_A(), hs_S()
_mae_cheek = P((163, 147), _mae_a, 'wrist', yaw=155, pitch=0, roll=4, scale=0.92, depth=35, pole=(0.6, 1.0, 0.45))
_mae_chin = P((174, 157), _mae_s, 'wrist', yaw=180, pitch=40, roll=90, scale=0.92, depth=40, pole=(0.6, 1.0, 0.45),
              via=(150, 160))
_mae_back = dict(_mae_cheek, via=(140, 170))
SIGNS['mae'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right'], 'handshape': _mae_a,
    'keys': [(0.0, [_mae_cheek]), (0.5, [_mae_cheek]), (1.0, [_mae_chin]), (1.9, [_mae_chin]), (2.4, [_mae_back])],
    'marks': [(182, 116, 70), (220, 146, 70)],
    'arrows': [{'d': 'M 138 126 Q 138 158 158 170', 'cap': True}],
}
TITLES['mae'] = 'Sinal de mãe em Libras'
