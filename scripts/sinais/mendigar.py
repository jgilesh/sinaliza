# MENDIGAR: the hand cupped (fingers together and a little curved), palm up, just below the chin on
# its own side; it moves out to the side and back to the front of the mouth, twice, with a pleading
# face (not drawn). (UFSC Signbank MENDIGAR; INES MENDIGAR: palm up, out to the side and back.)


def hs_mendigar_cup():
    """Cupped hand: fingers together, bent a little at every joint; the thumb beside them, a little bent."""
    return {'index': fing(2, 16, 22, 14), 'middle': fing(0, 16, 24, 15), 'ring': fing(-2, 16, 24, 15),
            'pinky': fing(-4, 18, 24, 15), 'thumb': (18.0, 26.0, 14.0, 10.0, 10.0)}


_mendigar_cup = hs_mendigar_cup()
# Palm up and tipped toward the viewer, the fingers pointing in toward the midline: the hollow of the
# cupped hand faces up, under the chin.
_mendigar_pose = lambda at, **kw: P(at, _mendigar_cup, 'wrist', yaw=kw.pop('yaw', -50), pitch=kw.pop('pitch', 15),
                                    roll=kw.pop('roll', 92), scale=1.0, depth=45, pole=(0.5, 1.0, 0.45), **kw)
_mendigar_in = _mendigar_pose((146, 166))
_mendigar_out = _mendigar_pose((118, 170))
SIGNS['mendigar'] = {
    'poster': 0.4, 'dur': 2.4, 'hands': ['right'], 'handshape': _mendigar_cup, 'handshape_view': {'yaw': 60},
    'keys': [(0.0, [_mendigar_in]), (0.4, [_mendigar_in]), (0.75, [_mendigar_out]), (1.1, [_mendigar_in]),
             (1.45, [_mendigar_out]), (1.8, [_mendigar_in]), (2.4, [_mendigar_in])],
    'arrows': [{'d': 'M 150 192 L 118 196', 'both': True}],
}
TITLES['mendigar'] = 'Sinal de mendigar em Libras'
