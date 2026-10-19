# BATER: hand in P (index straight, middle finger pointing forward, the thumb on it) raised beside the
# head at shoulder height; it strikes forward and down like a slap, palm down, to the front of the
# chest, twice, and ends with the fingers relaxed and bunched (beak). (UFSC Signbank BATER: P+Beak,
# forward, radial flexion; INES BATER2 shows the same slap.)


def hs_bater_P():
    """P of Libras: index straight, middle finger straight but bent forward at the knuckle, ring and
    little fingers folded; the thumb's pad on the side of the middle finger."""
    shape = fist({'index': fing(4, 0, 0, 0), 'middle': fing(-2, 62, 6, 4)})
    # Thumb tip in front of the index, its pad on the radial side of the middle finger's first bone.
    shape['thumb'] = solve_thumb((8.0, -42.5, 10.0), pad_to=(-1.0, 0.0, 0.0), pref=(5.0, 30.0, 40.0, 15.0, 15.0))
    return shape


def hs_bater_beak():
    """Beak: fingers together, bent at the knuckles and middle joints, the tips gathered on the thumb."""
    shape = {'index': fing(2, 52, 58, 34), 'middle': fing(0, 55, 58, 36), 'ring': fing(-1, 58, 56, 36),
             'pinky': fing(-2, 62, 54, 36)}
    shape['thumb'] = pinch_thumb(shape, fingers=('index', 'middle'))
    return shape


_bat_p, _bat_beak = hs_bater_P(), hs_bater_beak()
# Raised: beside the head, index up, the thumb side toward the viewer (palm turned out), so the
# straight index, the middle finger pointing forward and the thumb tip on it read.
_bat_up = P((128, 150), _bat_p, 'wrist', yaw=-65, pitch=-10, roll=-4, scale=1.08, depth=45, pole=(0.6, 1.0, 0.45))
# Struck: in front of the chest, the palm down, fingers forward and toward the midline; the back of the
# hand tips a little toward the viewer, so the straight index and the middle finger pointing down read.
_bat_hit = P((150, 228), _bat_p, 'wrist', yaw=-240, pitch=20, roll=100, scale=1.15, depth=80, ease='in', via=(104, 192),
             pole=(0.4, 1.0, 0.4))
_bat_end = dict(_bat_hit, shape=_bat_beak, at=(150, 232), ease='smooth')
SIGNS['bater'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right'], 'handshape': _bat_p, 'handshape_view': {'yaw': -65, 'pitch': -20},
    'keys': [(0.0, [_bat_up]), (0.3, [_bat_up]), (0.55, [_bat_hit]), (0.85, [dict(_bat_up, via=(100, 196))]), (1.1, [_bat_hit]),
             (1.4, [_bat_end]), (1.95, [_bat_end]), (2.4, [dict(_bat_up, via=(110, 210))])],
    # From beside the head, forward and down to the front of the chest.
    'arrows': [{'d': 'M 92 156 Q 98 206 128 224'}],
}
TITLES['bater'] = 'Sinal de bater em Libras'
