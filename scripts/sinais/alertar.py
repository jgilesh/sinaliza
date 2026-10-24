# ALERTAR: both hands start beside the eyes with the thumb and index pinched together (the other
# fingers folded); together they move out to the sides and a little up, opening into L, the index
# fingers pointing up and the palms forward. Once, no contact. (UFSC Signbank ALERTAR: Baby_O+L, both
# hands, eye, ipsilateral + distal. The INES ALERTAR1 video shows another variant.)


def hs_alertar_pinch():
    """Baby O: the index arches forward and its tip meets the thumb tip, a small round opening between
    them; the other fingers folded."""
    shape = fist({'index': fing(2, 22, 60, 40)})
    tip = finger_chain('index', shape['index'])[0][3]
    shape['thumb'] = solve_thumb((tip[0] + 1.0, tip[1] + 2.0, tip[2] + 3.0), pad_to=(0.0, -1.0, 0.3),
                                 pref=(-5.0, 45.0, 55.0, 15.0, 20.0))
    return shape


_alertar_pinch, _alertar_l = hs_alertar_pinch(), hs_L()
_alertar_pole = (0.7, 1.0, 0.45)
# Pinch beside the outer corner of the eye (not touching), palm forward, the hand beside the face.
_alertar_on = P((164, 100), _alertar_pinch, 'pinch', yaw=-70, pitch=0, roll=38, scale=1.0, depth=48, pole=_alertar_pole)
# Opened into L out to the side and up, palm forward, the index pointing up beside the head.
_alertar_up = P((140, 80), _alertar_l, 'thumb_tip', yaw=5, pitch=0, roll=-6, scale=1.05, depth=60, pole=_alertar_pole,
                ease='out')
_alertar_keys = [(0.0, _alertar_on), (0.45, _alertar_on), (0.95, _alertar_up), (1.9, _alertar_up),
                 (2.4, dict(_alertar_on, ease='smooth'))]
SIGNS['alertar'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _alertar_pinch,
    'handshape_view': {'yaw': -90},
    'keys': [(t, [p, mirrored(p)]) for t, p in _alertar_keys],
    # Out to the side and up, on both sides.
    'arrows': [{'d': 'M 130 144 Q 102 136 98 102'}, {'d': 'M 270 144 Q 298 136 302 102'}],
    'mirror_second': True,
}
TITLES['alertar'] = 'Sinal de alertar em Libras'
