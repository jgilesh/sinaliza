# CANSADO: both hands in a claw (fingers spread and bent), fingertips on the upper chest, palms
# toward the body; they drag down the chest to the waist and, at the end, turn palms up and close
# into fists. Once. (UFSC Signbank CANSAR: 5_claw+S, continuous contact, down; INES CANSAR.)
def hs_cansado_claw():
    """5 in a claw: fingers spread and bent at the middle and end joints, thumb out and bent."""
    return {'index': fing(16, 12, 48, 34), 'middle': fing(4, 12, 50, 36), 'ring': fing(-8, 14, 50, 36),
            'pinky': fing(-19, 16, 48, 34), 'thumb': (22.0, 30.0, 30.0, 16.0, 30.0)}


can_claw, can_s = hs_cansado_claw(), hs_S()
# Back of the hand toward the viewer, turned a little so the bent fingers show from the side;
# the fingertips touch the chest and lean toward the middle.
can_top = P((174, 206), can_claw, 'fingertips', yaw=165, pitch=0, roll=14, scale=0.95, depth=40, pole=(0.5, 1.0, -0.6))
can_low = P((167, 262), can_claw, 'fingertips', yaw=165, pitch=-10, roll=10, scale=0.95, depth=40, pole=(0.5, 1.0, -0.6),
            ease='linear')
can_end = P((152, 268), can_s, 'wrist', yaw=290, pitch=0, roll=80, scale=0.95, depth=70, pole=(0.5, 1.0, -0.6))
can_back = dict(can_top, ease='smooth')
SIGNS['cansado'] = {
    'poster': 0.0, 'dur': 2.8, 'hands': ['right', 'left'], 'handshape': can_claw, 'handshape_view': {'yaw': 30, 'pitch': -20},
    'keys': [(0.0, [can_top, mirrored(can_top)]), (0.35, [can_top, mirrored(can_top)]),
             (1.15, [can_low, mirrored(can_low)]), (1.5, [can_end, mirrored(can_end)]),
             (2.1, [can_end, mirrored(can_end)]), (2.8, [can_back, mirrored(can_back)])],
    'marks': [(178, 199, -20), (222, 199, 20)],
    'arrows': [{'d': 'M 136 214 L 136 252'}, {'d': 'M 264 214 L 264 252'}],
    'mirror_second': True,
}
TITLES['cansado'] = 'Sinal de cansado em Libras'
