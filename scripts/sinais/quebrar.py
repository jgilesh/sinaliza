# QUEBRAR: both hands closed (S), side by side and touching in front of the lower chest, palms down,
# knuckles forward, as if holding a stick; they move apart and up while the wrists turn out, ending at
# shoulder height with the palms forward, as if snapping the stick. Once. (UFSC Signbank QUEBRAR,
# INES QUEBRAR1.)
_quebrar_s = hs_S()
# Start: palm down, the knuckles toward the viewer and seen a little from above (the back of the hand
# shows on top), the thumb side toward the other fist.
_quebrar_on = P((186, 236), _quebrar_s, 'wrist', yaw=-20, pitch=62, roll=-6, scale=1.1, depth=70,
                pole=(0.45, 1.0, 0.4))
# End: upright beside the shoulder, palm forward: the folded fingers and the thumb across them show.
_quebrar_off = P((128, 170), _quebrar_s, 'wrist', yaw=8, pitch=0, roll=-8, scale=1.15, depth=60, ease='out',
                 via=(150, 220), pole=(0.45, 1.0, 0.4))
_quebrar_back = dict(_quebrar_on, ease='smooth', via=(146, 222))
SIGNS['quebrar'] = {
    'poster': 0.3, 'dur': 2.1, 'hands': ['right', 'left'], 'handshape': _quebrar_s,
    'keys': [(0.0, [_quebrar_on, mirrored(_quebrar_on)]), (0.4, [_quebrar_on, mirrored(_quebrar_on)]),
             (0.9, [_quebrar_off, mirrored(_quebrar_off)]), (1.6, [_quebrar_off, mirrored(_quebrar_off)]),
             (2.1, [_quebrar_back, mirrored(_quebrar_back)])],
    # The fists start together (contact between the hands), then each arcs out and up.
    'marks': [(200, 222, 0)],
    'arrows': [{'d': 'M 164 250 Q 128 244 112 200'}, {'d': 'M 236 250 Q 272 244 288 200'}],
    'mirror_second': True,
}
TITLES['quebrar'] = 'Sinal de quebrar em Libras'
