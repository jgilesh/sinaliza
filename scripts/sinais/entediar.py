# ENTEDIAR: both hands with the four fingers together and bent down 90 degrees at the knuckles (B bent),
# palms down, start near the middle of the body; they move apart to the sides and stop there, with a
# small sway of the wrists. Bored face. (UFSC Signbank ENTEDIAR: B_bent, neutral space; the INES video
# for CHATEAR shows another sign.)


def hs_entediar_bent():
    """B bent at the base: the four fingers straight and together, folded 90 degrees at the
    knuckles; the thumb loose beside them."""
    return {'index': fing(2, 82, 6, 4), 'middle': fing(0, 84, 6, 4), 'ring': fing(-2, 84, 6, 4),
            'pinky': fing(-4, 82, 8, 5), 'thumb': (14.0, 20.0, 12.0, 8.0, 6.0)}


_entediar_h = hs_entediar_bent()


def _entediar_pose(x, y, sway=0.0, ease='smooth'):
    """Right hand, palm down: the back of the hand tipped up toward the viewer, the bent fingers
    hanging down in front of it; turned a little so the thumb side shows."""
    return P((x, y), _entediar_h, 'wrist', yaw=-25, pitch=62, roll=-4 + sway, scale=1.1, depth=70,
             pole=(0.5, 1.0, 0.4), ease=ease)


_entediar_in = _entediar_pose(164, 222)
_entediar_out = _entediar_pose(114, 218, ease='out')
_entediar_k = lambda p: [p, mirrored(p)]
_entediar_keys = [(0.0, _entediar_k(_entediar_in)), (0.3, _entediar_k(_entediar_in)), (0.9, _entediar_k(_entediar_out))]
for _entediar_i, _entediar_s in enumerate((10, -6, 0)):   # small sway of the wrists
    _entediar_keys.append((1.05 + 0.2 * _entediar_i, _entediar_k(_entediar_pose(114, 218, _entediar_s))))
_entediar_keys += [(1.85, _entediar_k(_entediar_out)), (2.3, _entediar_k(dict(_entediar_in, ease='smooth')))]
SIGNS['entediar'] = {
    'poster': 1.0, 'dur': 2.3, 'hands': ['right', 'left'], 'handshape': _entediar_h,
    'handshape_view': {'yaw': -60, 'pitch': -10},
    'keys': _entediar_keys,
    # Apart, out to the sides, above the hands.
    'arrows': [{'d': 'M 166 184 L 120 184'}, {'d': 'M 234 184 L 280 184'}],
    'mirror_second': True,
}
TITLES['entediar'] = 'Sinal de entediar em Libras'
