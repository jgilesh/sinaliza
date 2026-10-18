# DOR: open hand with the middle finger bent forward (5m), palm toward the body in front of the
# chin; the wrist turns and the hand moves down and forward until the palm faces down and the
# middle finger points down and forward. Twice. (UFSC Signbank DOR; INES DOR.)
def hs_dor_5m():
    """5m: open hand, fingers spread, the middle finger bent forward (toward the palm side) at the
    knuckle, thumb out."""
    return {'index': fing(12, 0, 4, 2), 'middle': fing(1, 72, 18, 10), 'ring': fing(-8, 0, 4, 2),
            'pinky': fing(-18, 0, 5, 3), 'thumb': (36.0, 16.0, 6.0, 6.0, 4.0)}


dor_5m = hs_dor_5m()
# Start: palm toward the chin, turned a little so the bent middle finger shows from the side.
dor_up = P((158, 186), dor_5m, 'wrist', yaw=130, pitch=0, roll=62, scale=0.95, depth=45, pole=(0.5, 1.0, 0.2))
# End: palm down, fingers toward the middle and the back of the hand tipped toward the viewer; the
# middle finger hangs down below the others.
dor_dn = P((160, 214), dor_5m, 'wrist', yaw=118, pitch=0, roll=88, scale=0.95, depth=75, pole=(0.5, 1.0, 0.2), via=(146, 194))
SIGNS['dor'] = {
    'poster': 0.65, 'dur': 2.6, 'hands': ['right'], 'handshape': dor_5m, 'handshape_view': {'yaw': 65, 'pitch': -15},
    'keys': [(0.0, [dor_up]), (0.3, [dor_up]), (0.65, [dor_dn]), (0.95, [dor_up]), (1.3, [dor_dn]),
             (2.0, [dor_dn]), (2.6, [dor_up])],
    'arrows': [{'d': 'M 136 162 Q 126 184 138 202'}],
}
TITLES['dor'] = 'Sinal de dor em Libras'
