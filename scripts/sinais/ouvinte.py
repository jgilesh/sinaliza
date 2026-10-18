# OUVINTE: beside the ear, a clawed open hand (fingers spread and bent) closes into a fist (S),
# twice. Palm toward the ear and the viewer. (INES and UFSC Signbank agree: 5_claw+S.)
def hs_ouvinte_claw():
    """5 in a claw: fingers spread and bent at the middle and end joints, thumb out and bent."""
    return {'index': fing(13, 12, 55, 40), 'middle': fing(3, 12, 58, 42), 'ring': fing(-7, 14, 58, 42),
            'pinky': fing(-17, 16, 56, 40), 'thumb': (12.0, 30.0, 30.0, 18.0, 35.0)}


ouv_claw, ouv_s = hs_ouvinte_claw(), hs_S()
ouv = lambda shape: P((130, 134), shape, 'wrist', yaw=35, pitch=0, roll=-14, scale=0.95, depth=35, pole=(0.7, 1.0, 0.45))
SIGNS['ouvinte'] = {
    'poster': 0.0, 'dur': 2.2, 'hands': ['right'], 'handshape': ouv_claw, 'handshape_view': {'yaw': 30, 'pitch': -20},
    'keys': [(0.0, [ouv(ouv_claw)]), (0.3, [ouv(ouv_claw)]), (0.5, [ouv(ouv_s)]), (0.75, [ouv(ouv_claw)]),
             (0.95, [ouv(ouv_s)]), (1.6, [ouv(ouv_s)]), (2.2, [ouv(ouv_claw)])],
    'arrows': [],
}
TITLES['ouvinte'] = 'Sinal de ouvinte em Libras'
