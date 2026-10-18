# POR FAVOR: both flat hands (B) pressed palm to palm, fingers up, in front of the chest below the
# chin, as in prayer; the joined hands rock a little from side to side. (UFSC Signbank; the INES
# video shows another form.)
_pf_b = hs_B()


def _pf_poses(r, cx=200, cy=246):
    """Both hands, palms together, turned r degrees (clockwise on screen) about the wrists' midpoint."""
    s = 1.15
    off = PALM_HALF_THICKNESS * s
    a = math.radians(r)
    dx, dy = off * math.cos(a), off * math.sin(a)
    right = P((cx - dx, cy - dy), _pf_b, 'wrist', yaw=100, pitch=0, roll=r, scale=s, depth=60, pole=(0.3, 1.0, 0.5))
    left = P((cx + dx, cy + dy), _pf_b, 'wrist', yaw=100, pitch=0, roll=-r, scale=s, depth=60, pole=(0.3, 1.0, 0.5))
    return [right, left]


_pf_keys = [(0.0, _pf_poses(0)), (0.3, _pf_poses(0))]
for _k in range(2):
    _pf_keys += [(0.3 + 0.6 * _k + 0.3, _pf_poses(-9)), (0.3 + 0.6 * _k + 0.6, _pf_poses(9))]
_pf_keys += [(1.8, _pf_poses(0)), (2.4, _pf_poses(0))]
SIGNS['por-favor'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _pf_b, 'handshape_view': {'yaw': 0},
    'keys': _pf_keys,
    'arrows': [{'d': 'M 178 160 Q 200 149 222 160', 'both': True}],
}
TITLES['por-favor'] = 'Sinal de por favor em Libras'
