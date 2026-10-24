# MEDIR: both hands in F (thumb and index in a ring, the other three fingers open) start together in
# front of the chest, the support hand below with the palm up. The dominant hand, palm forward, rises
# straight up to above the head, as if marking a height; the support hand stays still. Once.
# (UFSC Signbank MEDIR. The INES MEDIR video moves both hands apart at the same time, one up and one
# down.)
_medir_f = hs_F()
# Support hand (defined as a right hand, then mirrored): palm up and tipped toward the viewer, so the
# ring shows; fingers pointing across toward the midline.
_medir_base = mirrored(P((150, 238), _medir_f, 'wrist', yaw=-55, pitch=0, roll=92, scale=1.05, depth=70))
# Dominant hand: palm forward, turned a little toward the thumb side so the ring reads.
_medir = lambda at, s, d, **kw: P(at, _medir_f, 'wrist', yaw=35, pitch=0, roll=-4, scale=s, depth=d,
                                  pole=(0.6, 1.0, 0.45), **kw)
_medir_low = _medir((198, 222), 1.05, 70)
_medir_high = _medir((130, 94), 1.0, 60, ease='out', via=(122, 170))
_medir_keys = [(0.0, [_medir_low, _medir_base]), (0.5, [_medir_low, _medir_base]), (1.3, [_medir_high, _medir_base]),
               (2.1, [_medir_high, _medir_base]), (2.7, [dict(_medir_low, ease='smooth', via=(122, 170)), _medir_base])]
SIGNS['medir'] = {
    'poster': 1.6, 'dur': 2.7, 'hands': ['right', 'left'], 'handshape': _medir_f, 'handshape_view': {'yaw': 40},
    'keys': _medir_keys,
    'arrows': [{'d': 'M 150 222 Q 94 186 100 104'}],
    'mirror_second': True,
}
TITLES['medir'] = 'Sinal de medir em Libras'
