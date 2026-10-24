# APAVORADO: both hands open with the fingers spread (5), palms toward the chest, fingers up and in; in
# front of the chest they go up and down in alternation a few times, then both drop down together.
# No contact. (UFSC Signbank APAVORAR: 5/5, neutral space, alternating; INES APAVORAR agrees.)

_apav_5 = HANDSHAPES['5']()


def _apav_pose(at, pitch=0.0, roll=30.0, ease='smooth'):
    """Right hand, back of the hand to the viewer (palm toward the chest), the spread fingers tipped
    in toward the midline; pitch tips the fingers toward the viewer (palm down)."""
    return P(at, _apav_5, 'wrist', yaw=165, pitch=pitch, roll=roll, scale=1.1, depth=60,
             pole=(0.5, 1.0, 0.4), ease=ease)


_apav_hi = lambda x: _apav_pose((x, 220))
_apav_lo = lambda x: _apav_pose((x, 246))
_apav_keys = [(0.0, [_apav_lo(130), mirrored(_apav_lo(130))])]
_apav_t = 0.25
for _apav_i in range(2):   # alternating: right up while left down, then the other way
    _apav_keys += [(round(_apav_t, 2), [_apav_hi(130), mirrored(_apav_lo(130))]),
                   (round(_apav_t + 0.26, 2), [_apav_lo(130), mirrored(_apav_hi(130))])]
    _apav_t += 0.52
# Both drop together, the fingers tipping forward (palms down).
_apav_drop = _apav_pose((134, 280), pitch=30, roll=20, ease='in')
_apav_keys += [(round(_apav_t + 0.25, 2), [_apav_drop, mirrored(_apav_drop)]),
               (round(_apav_t + 0.65, 2), [_apav_drop, mirrored(_apav_drop)]),
               (round(_apav_t + 0.95, 2), [_apav_lo(130), mirrored(_apav_lo(130))])]
SIGNS['apavorado'] = {
    'poster': 0.25, 'dur': round(_apav_t + 0.95, 2), 'hands': ['right', 'left'], 'handshape': _apav_5,
    'keys': _apav_keys,
    # Up and down beside each hand (alternating), then a drop arrow down the middle.
    'arrows': [{'d': 'M 100 204 L 100 250', 'both': True}, {'d': 'M 300 204 L 300 250', 'both': True},
               {'d': 'M 200 256 L 200 292'}],
    'mirror_second': True,
}
TITLES['apavorado'] = 'Sinal de apavorado em Libras'
