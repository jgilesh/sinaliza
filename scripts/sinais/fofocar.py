# FOFOCAR: both hands in Y (thumb and little finger out), little fingers up, the backs of the hands
# toward the viewer, side by side in front of the face, touching by the little-finger edges. The tip
# of the dominant thumb touches the mouth and goes up to the nose; meanwhile the other hand moves a
# little away and comes back against it. Twice, with the gaze turned aside, as if whispering.
# (UFSC Signbank FOFOCAR: Y/Y, weak hand's little-finger side. The INES FOFOCAR1 video shows another
# variant: one hand, the thumb at the mouth and three fingers up.)



def hs_fofocar_y():
    """Y with the little finger nearly straight up beside the hand (not fanned out), the thumb out."""
    return fist({'pinky': fing(-6, 0, 0, 0), 'thumb': (46.0, 12.0, 0.0, 4.0, 0.0)})


_fofocar_y = hs_fofocar_y()
_fofocar_pole = (0.3, 1.0, 0.45)


def _fofocar_dom(up):
    """Dominant Y, palm toward the face, thumb tip on the mouth (up=0) or the nose (up=1)."""
    return P((200, 125 - 20 * up), _fofocar_y, 'thumb_tip', yaw=160, pitch=0, roll=4, scale=1.0, depth=35,
             pole=_fofocar_pole)


def _fofocar_sup(up, away):
    """Other Y (a right-hand pose, mirrored), its little-finger edge against the dominant hand's."""
    return mirrored(P((DX_FOFOCAR - 14 * away, 125 - 20 * up), _fofocar_y, 'thumb_tip', yaw=160, pitch=0, roll=4,
                      scale=1.0, depth=40, pole=_fofocar_pole))


DX_FOFOCAR = 88   # mirrored x of the support thumb tip (screen x = 400 - this)
_fofocar_keys = [(0.0, [_fofocar_dom(0), _fofocar_sup(0, 0)]), (0.3, [_fofocar_dom(0), _fofocar_sup(0, 0)])]
for _fofocar_k in range(2):
    _fofocar_t = 0.3 + 0.8 * _fofocar_k
    _fofocar_keys += [(round(_fofocar_t + 0.25, 2), [_fofocar_dom(1), _fofocar_sup(1, 1)]),
                      (round(_fofocar_t + 0.5, 2), [_fofocar_dom(0), _fofocar_sup(0, 0)]),
                      (round(_fofocar_t + 0.8, 2), [_fofocar_dom(0), _fofocar_sup(0, 0)])]
_fofocar_keys.append((2.4, [_fofocar_dom(0), _fofocar_sup(0, 0)]))
SIGNS['fofocar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _fofocar_y,
    'keys': _fofocar_keys,
    'marks': [(189, 128, -100)],
    'arrows': [{'d': 'M 166 128 L 166 104', 'both': True}],
    'mirror_second': True,
}
TITLES['fofocar'] = 'Sinal de fofocar em Libras'
