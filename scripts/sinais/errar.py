# ERRAR: the support hand lies open in front of the chest, palm up. The dominant hand in P (index up,
# middle finger pointing forward, the thumb between them) starts beside the chin and comes down in an
# arc until its fingertips land on the support palm. Once. Disapproving face. (UFSC Signbank ERRAR:
# P/B, weak hand's palm, final contact, arc; INES ERRAR agrees.)


def hs_errar_P():
    """P of Libras: index straight, middle finger straight but bent forward at the knuckle, ring and
    little fingers folded; the thumb's pad on the side of the middle finger."""
    shape = fist({'index': fing(4, 0, 0, 0), 'middle': fing(-2, 62, 6, 4)})
    shape['thumb'] = solve_thumb((8.0, -42.5, 10.0), pad_to=(-1.0, 0.0, 0.0), pref=(5.0, 30.0, 40.0, 15.0, 15.0))
    return shape


def hs_errar_flat():
    """Support hand: open, fingers together and a little curved, thumb a little apart."""
    return {'index': fing(2, 8, 12, 8), 'middle': fing(0, 8, 12, 8), 'ring': fing(-2, 8, 12, 8),
            'pinky': fing(-4, 10, 12, 8), 'thumb': (22.0, 18.0, 10.0, 8.0, 6.0)}


_errar_p, _errar_flat = hs_errar_P(), hs_errar_flat()
# Support hand (defined as a right hand, then mirrored): palm up, tipped a little toward the viewer,
# fingers pointing across toward the midline.
_errar_base = mirrored(P((140, 244), _errar_flat, 'wrist', yaw=-50, pitch=0, roll=92, scale=1.1, depth=70))
# Up: beside the chin, outside the face, index up, the thumb side toward the viewer (palm turned toward
# the face), so the straight index, the middle finger pointing forward and the thumb on it read.
_errar_up = P((136, 158), _errar_p, 'wrist', yaw=-65, pitch=-10, roll=8, scale=1.05, depth=45, pole=(0.3, 1.0, 0.8))
# Down: the fingertips on the support palm, the fingers pointing down at it, the thumb side toward the
# viewer.
_errar_on = P((226, 236), _errar_p, 'index_tip', yaw=-70, pitch=10, roll=150, scale=1.08, depth=74,
              pole=(0.4, 1.0, 0.4), via=(186, 276), ease='in')
SIGNS['errar'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _errar_p,
    'handshape_view': {'yaw': -65, 'pitch': -20},
    'keys': [(0.0, [_errar_up, _errar_base]), (0.35, [_errar_up, _errar_base]), (0.95, [_errar_on, _errar_base]),
             (1.8, [_errar_on, _errar_base]), (2.4, [dict(_errar_up, via=(150, 220), ease='smooth'), _errar_base])],
    'marks': [(246, 230, 70)],
    # From beside the chin, in an arc down onto the support palm.
    'arrows': [{'d': 'M 146 188 Q 160 222 190 222'}],
    'mirror_second': True,
}
TITLES['errar'] = 'Sinal de errar em Libras'
