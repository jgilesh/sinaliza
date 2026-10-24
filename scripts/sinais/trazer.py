# TRAZER: flat hand (B) raised beside the shoulder, palm forward and fingers up; it comes down in an
# arc toward the body and ends in front of the waist, fingers down and palm toward the body, as if
# bringing something close. Once. (UFSC Signbank TRAZER; the INES TRAZER video shows another variant:
# the flat hand comes in from the side to the chest.)



def hs_trazer_flat():
    """Flat hand, fingers together and straight, the thumb resting close beside the index."""
    return {'index': fing(2, 0, 0, 0), 'middle': fing(0, 0, 0, 0), 'ring': fing(-2, 0, 0, 0),
            'pinky': fing(-4, 0, 0, 0), 'thumb': (-16.0, 10.0, 10.0, 4.0, 4.0)}


_trazer_b = hs_trazer_flat()
_trazer_up = P((112, 160), _trazer_b, 'wrist', yaw=0, pitch=0, roll=-12, scale=1.1, depth=70, pole=(0.05, 1.0, 0.1))
# In front of the waist: fingers down, back of the hand to the viewer (palm toward the body).
_trazer_down = P((176, 208), _trazer_b, 'wrist', yaw=180, pitch=-35, roll=172, scale=1.12, depth=45,
                 pole=(0.4, 1.0, 0.3), via=(110, 226), ease='smooth')
SIGNS['trazer'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right'], 'handshape': _trazer_b,
    'keys': [(0.0, [_trazer_up]), (0.35, [_trazer_up]), (1.1, [_trazer_down]), (1.8, [_trazer_down]),
             (2.4, [dict(_trazer_up, via=(100, 214))])],
    # Down in an arc toward the body, outside the hand's path.
    'arrows': [{'d': 'M 82 184 Q 82 250 134 258'}],
}
TITLES['trazer'] = 'Sinal de trazer em Libras'
