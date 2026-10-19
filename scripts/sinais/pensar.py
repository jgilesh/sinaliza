# PENSAR: index up (1), its tip on the temple on the signing side, the palm turned toward the face; the
# tip stays on the temple with small taps (the eyes look up, thoughtful). (UFSC Signbank PENSAR: 1,
# temple. The INES PENSAR1 video shows another variant: the open hand by the temple, moving away.)

_pensar_one = hs_1()


def _pensar_pose(at, roll=24, yaw=35, ease='smooth'):
    # Beside the head, palm turned toward the face and partly to the viewer, so the thumb over the folded
    # fingers and the index rising to the temple read; the hand stays out at the side, clear of the eyes.
    return P(at, _pensar_one, 'index_tip', yaw=yaw, pitch=0, roll=roll, scale=1.0, depth=38,
             pole=(0.7, 1.0, 0.45), ease=ease)


_pensar_on = _pensar_pose((161, 78))
_pensar_off = _pensar_pose((154, 82), roll=16, ease='out')   # the tip lifts a little off the temple
_pensar_low = _pensar_pose((138, 128), roll=10)
_pensar_keys = [(0.0, [_pensar_low]), (0.35, [_pensar_on])]
for _pensar_i in range(3):   # small taps on the temple
    _pensar_t = 0.55 + 0.32 * _pensar_i
    _pensar_keys += [(round(_pensar_t + 0.14, 2), [_pensar_off]), (round(_pensar_t + 0.28, 2), [dict(_pensar_on, ease='in')])]
_pensar_keys += [(2.1, [_pensar_on]), (2.5, [_pensar_low])]
SIGNS['pensar'] = {
    'poster': 0.5, 'dur': 2.5, 'hands': ['right'], 'handshape': _pensar_one,
    'handshape_view': {'yaw': 20},
    'keys': _pensar_keys,
    'marks': [(163, 74, 40)],
}
TITLES['pensar'] = 'Sinal de pensar em Libras'
