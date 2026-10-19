# AGUENTAR: both hands in F (index bent onto the thumb, the other three fingers open and spread). The
# support hand lies palm down in front of the chest, fingers pointing across the body; the dominant hand
# crosses over it, little-finger edge down, comes down onto the back of the support hand and scrapes
# toward the body, twice. Tense face. (UFSC Signbank AGUENTAR: F/F, back of the weak hand, double
# brushing contact, proximal; INES AGÜENTAR1 agrees.)


def hs_aguentar_F():
    """F of Libras: the index bends mostly at the knuckle and its fingertip rests on the thumb tip, pad
    on pad; the other three fingers open and spread."""
    shape = {'index': fing(4, 80, 30, 20), 'middle': fing(3, 0, 0, 0), 'ring': fing(-6, 0, 0, 0),
             'pinky': fing(-15, 0, 0, 0)}
    shape['thumb'] = pinch_thumb(shape)
    return shape


_aguentar_f = hs_aguentar_F()
# Support hand (defined as a right hand, then mirrored): palm down, the back tipped up toward the
# viewer, fingers pointing across toward the dominant side.
_aguentar_base = mirrored(P((126, 258), _aguentar_f, 'wrist', yaw=130, pitch=0, roll=94, scale=1.08, depth=70,
                            pole=(0.5, 1.0, 0.35)))


def _aguentar_pose(at, scale, depth):
    """Dominant hand crossing over the support hand: palm toward the body (the back of the hand to the
    viewer), the three open fingers pointing up and across, the ring of the F at the top, the
    little-finger edge down on the back of the support hand."""
    return P(at, _aguentar_f, 'wrist', yaw=-150, pitch=0, roll=50, scale=scale, depth=depth, pole=(0.4, 1.0, 0.4))


# Up and forward; down on the back of the support hand; scraped back toward the body (a little higher
# on the tipped support hand, and further from the viewer).
_aguentar_up = _aguentar_pose((208, 236), 1.1, 82)
_aguentar_on = _aguentar_pose((204, 250), 1.08, 74)
_aguentar_back = _aguentar_pose((201, 246), 1.03, 58)
_aguentar_keys = [(0.0, [_aguentar_up, _aguentar_base]), (0.3, [_aguentar_up, _aguentar_base])]
for _aguentar_i in range(2):
    _aguentar_t = 0.3 + 0.6 * _aguentar_i
    _aguentar_keys += [(_aguentar_t + 0.15, [_aguentar_on, _aguentar_base]),
                       (_aguentar_t + 0.4, [_aguentar_back, _aguentar_base]),
                       (_aguentar_t + 0.6, [_aguentar_up, _aguentar_base])]
_aguentar_keys.append((2.2, [_aguentar_up, _aguentar_base]))
SIGNS['aguentar'] = {
    'poster': 0.45, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _aguentar_f, 'handshape_view': {'yaw': 40},
    'keys': _aguentar_keys,
    'marks': [(272, 240, 60)],
    # Down onto the back of the support hand, then scraping toward the body.
    'arrows': [{'d': 'M 168 198 Q 166 228 186 242'}],
    'mirror_second': True,
}
TITLES['aguentar'] = 'Sinal de aguentar em Libras'
