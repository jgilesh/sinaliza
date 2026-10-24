# IGNORAR: the hand in a beak (the fingers together and straight, their tips on the thumb tip) touches the
# tip of the nose with the fingertips, then moves across to the other side of the face, by the chin, and
# away forward, once (the head turns away with disdain; the face is not drawn changing). (UFSC Signbank
# IGNORAR: Beak, nose. The INES IGNORAR video shows another variant.)


def hs_ignorar_beak():
    """Beak: the four fingers together and bent mostly at the knuckles, nearly straight, their tips
    gathered on the thumb's pad."""
    shape = {'index': fing(2, 52, 34, 22), 'middle': fing(0, 56, 32, 22), 'ring': fing(-2, 60, 30, 20),
             'pinky': fing(-4, 64, 28, 20)}
    shape['thumb'] = pinch_thumb(shape)
    return shape


_ignorar_beak = hs_ignorar_beak()
_ignorar_pole = (0.5, 1.0, 0.45)
# On the nose: the bunched fingertips on its tip, the hand lying across beside the nose and seen from
# the thumb side, so the beak shows in profile pointing at the nose (the eyes stay clear).
_ignorar_nose = P((200, 116), _ignorar_beak, 'pinch', yaw=-70, pitch=0, roll=95, scale=1.0, depth=40, pole=_ignorar_pole)
# Across to the other side of the face, by the chin.
_ignorar_side = P((228, 140), _ignorar_beak, 'pinch', yaw=-70, pitch=0, roll=100, scale=1.0, depth=42,
                  pole=_ignorar_pole, ease='linear')
# Away, forward and down.
_ignorar_away = P((224, 180), _ignorar_beak, 'pinch', yaw=-60, pitch=10, roll=80, scale=1.12, depth=80,
                  pole=_ignorar_pole, ease='out')
SIGNS['ignorar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right'], 'handshape': _ignorar_beak, 'handshape_view': {'yaw': -70, 'roll': 60},
    'keys': [(0.0, [_ignorar_nose]), (0.35, [_ignorar_nose]), (0.75, [_ignorar_side]), (1.1, [_ignorar_away]),
             (1.9, [_ignorar_away]), (2.4, [dict(_ignorar_nose, ease='smooth', via=(180, 170))])],
    'marks': [(194, 110, -50)],
    # From the nose across to the other side of the chin, then away.
    'arrows': [{'d': 'M 248 112 Q 266 134 256 172'}],
}
TITLES['ignorar'] = 'Sinal de ignorar em Libras'
