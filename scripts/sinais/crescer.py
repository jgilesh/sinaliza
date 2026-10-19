# CRESCER: flat hand (B), palm down, fingers pointing toward the midline, on the signing side; it
# rises in steps (three stops) from the lower chest to above the head, showing the height growing.
# No contact. (UFSC Signbank CRESCER; INES CRESCER1 shows the same with the other hand.)
_crescer_b = hs_B()


def _crescer_at(y, x, ease='smooth'):
    # Palm down and tipped a little toward the viewer's side so the back of the hand and the row of
    # fingers show; the fingers point across toward the midline.
    return P((x, y), _crescer_b, 'wrist', yaw=118, pitch=0, roll=86, scale=1.1, depth=70, ease=ease)


_crescer_stops = [_crescer_at(262, 108), _crescer_at(196, 94), _crescer_at(128, 82), _crescer_at(38, 92)]
_crescer_keys = [(0.0, [_crescer_stops[0]]), (0.3, [_crescer_stops[0]])]
_crescer_t = 0.3
for _crescer_s in _crescer_stops[1:]:
    _crescer_keys += [(_crescer_t + 0.3, [_crescer_s]), (_crescer_t + 0.5, [_crescer_s])]
    _crescer_t += 0.5
# Back down on the outer side, clear of the face.
_crescer_keys += [(_crescer_t + 0.6, [_crescer_stops[-1]]), (_crescer_t + 1.1, [dict(_crescer_stops[0], via=(52, 160))])]
SIGNS['crescer'] = {
    'poster': 1.8, 'dur': _crescer_t + 1.1, 'hands': ['right'], 'handshape': _crescer_b,
    'handshape_view': {'yaw': 20},
    'keys': _crescer_keys,
    # Up the outer side of the path, in steps.
    'arrows': [{'d': 'M 50 252 L 50 228 L 42 222 L 42 162 L 34 156 L 34 64'}],
}
TITLES['crescer'] = 'Sinal de crescer em Libras'
