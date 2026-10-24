# DESMAIAR: flat hand (B) standing in front of the face, its edge on the nose, palm to the side. It
# turns and falls in a spiral down and out to the side of the waist, ending palm up. Once. Eyes close,
# the head droops. (UFSC Signbank DESMAIAR: B, front of the head, spiral, rotation. The INES DESMAIAR
# video starts with the hand flat on top of the head instead.)



def hs_desmaiar_B():
    """B: flat hand, fingers together, the thumb resting alongside the index."""
    return {'index': fing(2, 0, 0, 0), 'middle': fing(0, 0, 0, 0), 'ring': fing(-2, 0, 0, 0),
            'pinky': fing(-4, 0, 0, 0), 'thumb': (-18.0, 10.0, 10.0, 4.0, 4.0)}


_desmaiar_b = hs_desmaiar_B()


def _desmaiar_orient(f, n, guess):
    """yaw, pitch, roll of a right hand whose fingers point along f and whose palm faces n (screen)."""
    f, n = vunit(f), vunit(n)

    def err(q):
        a, b = rot((0.0, -1.0, 0.0), *q), rot((0.0, 0.0, 1.0), *q)
        return sum((x - y) ** 2 for x, y in zip(a, f)) + sum((x - y) ** 2 for x, y in zip(b, n))
    q, e, step = list(guess), err(guess), 16.0
    while step > 0.05:
        better = False
        for i in range(3):
            for d in (step, -step):
                cand = q[:]
                cand[i] += d
                ec = err(cand)
                if ec < e:
                    q, e, better = cand, ec, True
        if not better:
            step /= 2
    return q


def _desmaiar_pose(at, f, n, guess, anchor='wrist', **kw):
    q = _desmaiar_orient(f, n, guess)
    return q, P(at, _desmaiar_b, anchor, yaw=q[0], pitch=q[1], roll=q[2], **kw)


# On the face: fingers up, the little-finger edge on the nose, the palm toward the signer's left (a
# little toward the viewer, so the hand is not a bare line).
_desmaiar_q, _desmaiar_on = _desmaiar_pose((196, 150), (0.0, -1.0, 0.0), (1.0, 0.0, 0.12), [85.0, 0.0, 0.0],
                                           scale=0.95, depth=35, pole=(0.5, 1.0, 0.5))
# Falling: out beside the head, the palm turned to the viewer, fingers leaning out.
_desmaiar_q, _desmaiar_mid = _desmaiar_pose((140, 178), (-0.5, -0.85, 0.15), (0.0, 0.2, 1.0), _desmaiar_q,
                                            scale=1.0, depth=55, pole=(0.5, 1.0, 0.45), via=(150, 128), ease='linear')
# End: beside the waist, palm up and tipped toward the viewer, fingers pointing forward and in.
_desmaiar_q, _desmaiar_end = _desmaiar_pose((112, 246), (0.65, 0.35, 0.65), (0.0, -0.85, 0.5), _desmaiar_q,
                                            scale=1.05, depth=70, pole=(0.4, 1.0, 0.4), via=(108, 210), ease='out')
_desmaiar_keys = [(0.0, [_desmaiar_on]), (0.4, [_desmaiar_on]), (0.85, [_desmaiar_mid]), (1.3, [_desmaiar_end]),
                  (2.1, [_desmaiar_end]), (2.8, [dict(_desmaiar_on, via=(120, 180), ease='smooth')])]
SIGNS['desmaiar'] = {
    'poster': 0.0, 'dur': 2.8, 'hands': ['right'], 'handshape': _desmaiar_b,
    'keys': _desmaiar_keys,
    'marks': [(213, 112, 110)],
    'arrows': [{'d': 'M 150 94 Q 70 108 86 234'}],
}
TITLES['desmaiar'] = 'Sinal de desmaiar em Libras'
