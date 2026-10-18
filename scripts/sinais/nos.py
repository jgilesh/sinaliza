# NÓS: index hand (1), palm toward the body, in front of the chest on the signer's right side. The hand
# makes small circles (two and a half turns): at the outer top the index points up near the shoulder,
# at the inner bottom it points across the chest to the other side, taking the signer into the group.
# The back of the hand faces the viewer the whole time, so the index reads against the shirt (INES: NÓS).
nos_one = hs_1()
NOS_C, NOS_R = (166, 244), 12


def nos_pose(angle):
    """Angle -135 = outer top (index up), 45 = inner bottom (index across the chest); clockwise on screen."""
    a = math.radians(angle)
    at = (NOS_C[0] + NOS_R * math.cos(a), NOS_C[1] + NOS_R * math.sin(a))
    roll = 42 + 42 * math.cos(math.radians(angle - 45))
    return P(at, nos_one, 'wrist', yaw=180, pitch=-8, roll=roll, scale=1.12, depth=45,
             pole=(0.2, 1.0, 0.55), ease='linear')


nos_angles = [-135 + 30 * k for k in range(31)]   # two and a half turns
nos_keys = [(0.0, [nos_pose(-135)]), (0.15, [nos_pose(-135)])]
for k, ang in enumerate(nos_angles[1:], 1):
    nos_keys.append((0.15 + 1.6 * k / 30, [nos_pose(ang)]))
nos_end = dict(nos_pose(45), ease='smooth')
nos_keys += [(2.2, [nos_end]), (2.7, [dict(nos_pose(-135), ease='smooth')])]
SIGNS['nos'] = {
    'poster': 2.0, 'dur': 2.7, 'hands': ['right'], 'handshape': nos_one,
    'keys': nos_keys,
    'arrows': [{'d': circle_arrow(NOS_C[0] - 5, NOS_C[1] - 34, 42, 140, 222, True)}],
}
TITLES['nos'] = 'Sinal de nós em Libras'
