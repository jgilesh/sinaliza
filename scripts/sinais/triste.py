# TRISTE: hand in I (only the little finger up), brought to the chin; the wrist turns so the
# closed fingers rest under the chin, back of the hand forward, and the little finger points
# sideways, toward the other side. It rests there a moment. (UFSC Signbank TRISTE.)
def hs_triste_i():
    """I of Libras: only the little finger straight, the others closed under the thumb."""
    shape = fist({'pinky': fing(-6, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['index', 'middle'], at=0.5)
    return shape


tri_i = hs_triste_i()
tri_up = P((160, 216), tri_i, 'wrist', yaw=50, pitch=0, roll=-6, scale=1.0, depth=45, pole=(0.25, 1.0, 0.6))
# On the way up the wrist already turns, so the little finger sweeps under the chin, not across the mouth.
tri_mid = P((148, 182), tri_i, 'wrist', yaw=150, pitch=-8, roll=80, scale=1.0, depth=42, pole=(0.25, 1.0, 0.6))
tri_chin = P((161, 153), tri_i, 'wrist', yaw=180, pitch=-15, roll=88, scale=1.0, depth=40, pole=(0.25, 1.0, 0.6))
SIGNS['triste'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right'], 'handshape': tri_i,
    'keys': [(0.0, [tri_up]), (0.3, [tri_up]), (0.6, [tri_mid]), (0.85, [tri_chin]), (1.9, [tri_chin]), (2.15, [tri_mid]),
             (2.4, [tri_up])],
    'marks': [(176, 140, -50)],
    'arrows': [{'d': 'M 132 178 Q 130 152 150 138', 'cap': True}],
}
TITLES['triste'] = 'Sinal de triste em Libras'
