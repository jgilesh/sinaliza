#!/usr/bin/env python3
"""Draws every sign illustration in one shared style (no images from the internet).

Each sign is a few key poses for one or two hands: which point of the hand goes
where on the body, the hand's orientation and how much each finger bends. The
script projects a simple 3D hand onto the picture, solves the arms (two-bone IK),
samples the motion and writes an animated SVG (SMIL) to media/sinais/<id>.svg.

    python3 scripts/desenhar_sinais.py                 # all signs
    python3 scripts/desenhar_sinais.py agua cafe       # some signs
    python3 scripts/desenhar_sinais.py --sheet DIR     # also write review sheets (static frames) to DIR
"""
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'media' / 'sinais'

W, H = 400, 300
FPS = 20
# "Warm character" palette: warm coloured line art instead of near-black ink.
INK = '#5a3426'          # hand outline: strong enough to read every finger on a phone
LINE_SKIN = '#7b4532'    # face / neck outline
SKIN = '#e2a77f'         # tanned, olive-warm skin
SKIN_SHADE = '#c98a63'
SKIN_DEEP = '#ad6a48'
SKIN_LIGHT = '#eebb96'
SKIN_DARK = SKIN_SHADE
HAIR = '#36211a'
HAIR_MID = '#4a2d21'
HAIR_LIGHT = '#6d4532'
SHIRT = '#5a87b8'        # chambray button-up, long sleeves: only hands and face are skin
SHIRT_SHADE = '#4873a3'
SHIRT_DEEP = '#3a6290'
SHIRT_LIGHT = '#7ba3cd'
SHIRT_LINE = '#23466c'
SHIRT_DARK = SHIRT_SHADE
LIPS = '#b65a52'
MOUTH = '#6c2a27'
TEETH = '#fffaf3'
GOLD = '#d4a640'
ACCENT = '#f26b2d'
NAIL = '#f6d6c4'
NAIL_LINE = '#c0846a'
CREASE_INK = '#a35f40'   # knuckle creases: dark enough to read on a phone
NAIL_DOT = 0.15      # a nail shows when the dorsal face of the last phalanx faces the viewer by more than this
END_ON = 0.866       # ...unless that phalanx points this much at (or away from) the viewer: under half its length shows
LINE = 1.6          # visible outline width (hands)
THIN = 0.8          # line between two fingers folded into a fist
BODY_LINE = 1.5     # outline width (body, sleeves)
ARM_UPPER, ARM_FORE = 118.0, 104.0
SHOULDER = {'right': (139.0, 193.0), 'left': (261.0, 193.0)}   # signer's right = viewer's left
DELTOID = 19.0      # shoulder (deltoid) radius: the torso outline is drawn around the joint
SIDE = {'right': -1, 'left': 1}                                 # direction "outward" on screen

# Body landmarks (viewer coordinates) used by the sign specs.
SPOT = {
    'chin': (200, 143), 'chin_r': (192, 141),
    'mouth': (200, 125), 'mouth_r': (189, 124), 'cheek_r': (178, 114),
    'forehead': (200, 70), 'forehead_r': (187, 72),
    'chest': (200, 214),
}

# ---------------------------------------------------------------- hand model
# A rebuilt anatomical hand. Right hand in its own frame: palm facing the viewer (+z is the
# palmar side), fingers up (-y), thumb on the viewer's right (+x is the radial side). Units
# are picture pixels at scale 1. The left hand is the mirror image.
#
# Every digit is a chain of bones. Each bone carries a local frame: a = along the bone toward
# the tip, p = its palmar (pad) side, l = a x p, the hinge axis. Finger joints are hinges that
# only flex toward the palmar side of their bone; a finger may spread a little at the knuckle
# (MCP) but never twists. The thumb has its own frame at the CMC joint (base of the palm,
# radial side): it abducts in the palm plane and out of it, rotates about its own axis when it
# opposes, then flexes at the MCP and IP joints toward its pad. Nails, creases and knuckle
# wrinkles are placed from those frames, so they always sit on the correct side, and every
# part is layered by its real depth.
FINGERS = {  # knuckle (MCP) position, bone lengths (proximal, middle, distal), width
    'pinky':  ((-12.0, -33.0), (12.5, 8.5, 7.5), 7.1),
    'ring':   ((-4.2, -36.2), (16.5, 11.0, 8.5), 8.0),
    'middle': ((4.0, -37.2), (18.0, 11.5, 9.0), 8.4),
    'index':  ((12.0, -35.2), (16.0, 10.5, 8.5), 8.2),
}
THUMB_CMC = (9.0, -5.0, 1.5)      # base of the palm near the wrist, radial side, a little palmar
THUMB_LENS = (16.0, 12.5, 10.5)   # metacarpal (inside the thenar mound), proximal, distal
THUMB_W = 9.6
THUMB_ALPHA0 = 38.0   # at rest the thumb metacarpal leans this far from the fingers, toward the radial side
THUMB_RHO0 = 65.0     # ...and is turned so its pad faces mostly the fingers (ulnar), a little palmar
# Joint limits (degrees). Fingers: abduction at the MCP only, flexion toward the palm.
# Thumb: abd = in the palm plane (radial abduction), palm = out of the palm plane (palmar
# abduction), opp = rotation about its own axis (nail toward the palmar side), then flexion.
LIMITS = {'finger': (('abd', -20, 20), ('mcp', -15, 90), ('pip', 0, 110), ('dip', 0, 85)),
          'thumb': (('abd', -30, 60), ('palm', 0, 80), ('opp', -20, 100), ('mcp', 0, 60), ('ip', -10, 80))}
# Palm outline (control polygon of a smooth curve): narrow heel at the wrist, straight-ish
# little-finger edge, knuckle line arching over the finger bases. The thumb's fleshy base
# (thenar mound) is drawn with the palm, from the thumb's metacarpal.
PALM = [(-10.5, 1.5), (9.5, 1.5), (14.5, -5), (16.8, -15), (17.4, -26), (17.2, -33), (14.8, -38.4), (8, -40.4),
        (0, -41), (-8, -39.8), (-14, -36.8), (-16.6, -31), (-17, -18), (-14.8, -6)]
CREASE = [(-17, -26), (-8, -29.5), (2.5, -31)]          # heart line (the life line is the thenar edge)
HEAD_LINE = [(15.5, -23), (5, -21), (-6.5, -16.5)]
PALM_HALF_THICKNESS = 4.5
DIGITS = ['pinky', 'ring', 'middle', 'index', 'thumb']
TAPER = (1.0, 0.91, 0.82)        # finger width at each phalanx, base to tip
THUMB_TAPER = (1.0, 0.97, 0.88)
THENAR = (7.6, THUMB_W * THUMB_TAPER[1] / 2)   # fleshy base radius at the wrist end, and at the knuckle (= the thumb)
ROOT_INSET = 0.15  # a digit's root zone (where the palm outline is left out) stays this far inside its outline
WEB_SAG = 0.12    # how far the thumb-index web's free edge dips toward the thumb base (fraction)
WEB_STEPS = 8     # points along that free edge


def vadd(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def vsub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def vmul(a, k):
    return (a[0] * k, a[1] * k, a[2] * k)


def vdot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def vcross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def vunit(a):
    n = math.sqrt(vdot(a, a))
    return (a[0] / n, a[1] / n, a[2] / n) if n > 1e-9 else (0.0, 0.0, 0.0)


def vrot(v, k, deg):
    """Rotates v about the unit axis k by deg degrees (Rodrigues)."""
    r = math.radians(deg)
    c, s = math.cos(r), math.sin(r)
    kv, kd = vcross(k, v), vdot(k, v)
    return tuple(v[i] * c + kv[i] * s + k[i] * kd * (1 - c) for i in range(3))


def fing(abd, mcp, pip, dip=None):
    """Finger parameters. The DIP follows the PIP (about 2/3 of it) unless given."""
    return (float(abd), float(mcp), float(pip), float(pip * 2 / 3 if dip is None else dip))


def finger_chain(name, q):
    """Joint points (MCP, PIP, DIP, tip) and one frame (a, p, l) per bone, hand coordinates."""
    (bx, by), lens, _ = FINGERS[name]
    abd, *flex = q
    s = math.radians(abd)
    a, p = (math.sin(s), -math.cos(s), 0.0), (0.0, 0.0, 1.0)
    l = vcross(a, p)              # hinge axis: the same for every joint, so the finger never twists
    pts, frames = [(bx, by, 0.0)], []
    for length, f in zip(lens, flex):
        a, p = vrot(a, l, f), vrot(p, l, f)
        frames.append((a, p, l))
        pts.append(vadd(pts[-1], vmul(a, length)))
    return pts, frames


def thumb_base_frame(abd, palm, opp):
    """Frame of the thumb metacarpal at the CMC joint."""
    al = math.radians(THUMB_ALPHA0 + abd)
    a = (math.sin(al), -math.cos(al), 0.0)
    u = (-math.cos(al), -math.sin(al), 0.0)        # in the palm plane, toward the fingers
    r = math.radians(THUMB_RHO0)
    p = vadd(vmul((0.0, 0.0, 1.0), math.cos(r)), vmul(u, math.sin(r)))
    a, p = vrot(a, u, palm), vrot(p, u, palm)      # palmar abduction: out of the palm plane
    p = vrot(p, a, opp)                            # opposition: turns about its own axis
    return a, p, vcross(a, p)


def thumb_chain(q):
    """Joint points (CMC, MCP, IP, tip) and frames of the thumb, hand coordinates."""
    abd, palm, opp, mcp, ip = q
    a, p, l = thumb_base_frame(abd, palm, opp)
    pts, frames = [THUMB_CMC], []
    for length, f in zip(THUMB_LENS, (0.0, mcp, ip)):
        a, p = vrot(a, l, f), vrot(p, l, f)
        frames.append((a, p, l))
        pts.append(vadd(pts[-1], vmul(a, length)))
    return pts, frames


def digit_chain(shape, name):
    return thumb_chain(shape['thumb']) if name == 'thumb' else finger_chain(name, shape[name])


def digit_points(shape, name):
    return digit_chain(shape, name)[0]


def seg_radius(name, k, scale=1.0):
    if name == 'thumb':
        return (THENAR[1] if k == 0 else THUMB_W * THUMB_TAPER[k] / 2) * scale
    return FINGERS[name][2] * TAPER[k] / 2 * scale


THUMB_PREF = (0.0, 40.0, 45.0, 15.0, 15.0)   # a relaxed, slightly opposed thumb


def solve_thumb(target, pad_to=None, point=None, pref=THUMB_PREF, w_point=60.0, w_pad=40.0):
    """Thumb parameters (inside the joint limits) whose tip reaches `target` (hand coordinates),
    with its pad turned toward `pad_to` and its last bone pointing along `point` when given,
    staying close to a natural pose. Pattern search from a few starts."""
    names = [n for n, _, _ in LIMITS['thumb']]
    lim = [(lo, hi) for _, lo, hi in LIMITS['thumb']]
    pad_to = vunit(pad_to) if pad_to is not None else None
    point = vunit(point) if point is not None else None

    def err(q):
        pts, frames = thumb_chain(q)
        e = sum((x - y) ** 2 for x, y in zip(pts[-1], target))
        if pad_to is not None:
            e += w_pad * (1 - vdot(frames[-1][1], pad_to))
        if point is not None:
            e += w_point * (1 - vdot(frames[-1][0], point))
        return e + 6.0 * sum(((x - y) / (hi - lo)) ** 2 for x, y, (lo, hi) in zip(q, pref, lim))

    best_all, e_all = None, float('inf')
    for start in (pref, (pref[0] - 15, pref[1] + 15, pref[2] + 20, pref[3], pref[4]),
                  (pref[0] + 15, pref[1] - 15, pref[2] - 20, pref[3] + 10, pref[4] + 10),
                  (pref[0], pref[1] + 25, pref[2] + 35, pref[3] + 15, pref[4] + 15)):
        best = [min(max(v, lo), hi) for v, (lo, hi) in zip(start, lim)]
        e_best, step = err(best), 16.0
        while step > 0.05:
            improved = False
            for i in range(5):
                for d in (step, -step):
                    cand = best[:]
                    cand[i] = min(max(cand[i] + d, lim[i][0]), lim[i][1])
                    e = err(cand)
                    if e < e_best:
                        best, e_best, improved = cand, e, True
            if not improved:
                step /= 2
        if e_best < e_all:
            best_all, e_all = best, e_best
    return tuple(round(v, 2) for v in best_all)


def on_surface(shape, name, k, side, gap=0.0, at=0.5):
    """A point on bone k of a digit, pushed out of it on its palmar (side=+1) or dorsal
    (side=-1) face by its radius plus `gap`."""
    pts, frames = digit_chain(shape, name)
    c = vadd(pts[k], vmul(vsub(pts[k + 1], pts[k]), at))
    return vadd(c, vmul(frames[k][1], side * (seg_radius(name, k) + gap)))


# ---- handshapes (right hand; anatomical parameters only, no sideways twist)
def curl(abd=0.0, tight=0.0):
    """A finger folded into the palm (fist); fist() fits its last joint to the finger."""
    return ('curl', float(abd), float(tight))


def fit_curl(name, abd, tight):
    """Folded finger whose fingertip rests on the palm surface (not inside it): the DIP is
    chosen so the tip pad just touches the palm."""
    best = None
    for dip in range(20, 86):
        q = fing(abd, 86 + tight, 100 + tight, dip)
        tip = finger_chain(name, q)[0][3]
        e = abs(tip[2] - (PALM_HALF_THICKNESS + seg_radius(name, 2) + 0.4))
        if best is None or e < best[0]:
            best = (e, q)
    return best[1]


def fist(shape=None):
    s = {'index': curl(-2), 'middle': curl(0), 'ring': curl(3), 'pinky': curl(7)}
    s.update(shape or {})
    return {k: fit_curl(k, *v[1:]) if v[0] == 'curl' else v for k, v in s.items()}


def thumb_over(shape, names, gap=0.4, at=0.45):
    """Thumb lying across the front of the folded `names`, its pad on their middle phalanges,
    pointing toward the little finger."""
    pts = [on_surface(shape, n, 1, -1, gap + seg_radius('thumb', 2), at=at) for n in names]
    target = tuple(sum(p[i] for p in pts) / len(pts) for i in range(3))
    return solve_thumb(target, pad_to=(0.0, 0.0, -1.0), point=(-1.0, -0.25, 0.0), pref=(-10.0, 45.0, 60.0, 35.0, 45.0),
                       w_point=250.0)


def seg_closest3(p0, p1, q0, q1):
    """Closest points of two 3D segments: (s on p, t on q, distance)."""
    d1, d2, r = vsub(p1, p0), vsub(q1, q0), vsub(p0, q0)
    a, e, f = vdot(d1, d1), vdot(d2, d2), vdot(d2, r)
    c, b = vdot(d1, r), vdot(d1, d2)
    den = a * e - b * b
    s = min(max((b * f - c * e) / den, 0.0), 1.0) if den > 1e-9 else 0.0
    t = (b * s + f) / e
    if t < 0.0:
        t, s = 0.0, min(max(-c / a, 0.0), 1.0)
    elif t > 1.0:
        t, s = 1.0, min(max((b - c) / a, 0.0), 1.0)
    P, Q = vadd(p0, vmul(d1, s)), vadd(q0, vmul(d2, t))
    return s, t, math.sqrt(vdot(vsub(P, Q), vsub(P, Q)))


def pinch_contact(qt, shape, finger):
    """How the thumb's distal phalanx meets a finger's distal phalanx: gap between their
    surfaces, where along each bone they are closest (0 = joint, 1 = tip), and how much each pad
    faces the other digit there."""
    tp, tf = thumb_chain(qt)
    fp, ff = finger_chain(finger, shape[finger])
    s, t, dist = seg_closest3(tp[2], tp[3], fp[2], fp[3])
    P, Q = vadd(tp[2], vmul(vsub(tp[3], tp[2]), s)), vadd(fp[2], vmul(vsub(fp[3], fp[2]), t))
    u = vunit(vsub(Q, P))
    return {'gap': dist - seg_radius('thumb', 2) - seg_radius(finger, 2), 's': s, 't': t,
            'pad_to': vdot(tf[2][1], u), 'fpad_to': -vdot(ff[2][1], u), 'pads': vdot(tf[2][1], ff[2][1]),
            'nail_palm': -tf[2][1][2]}


def pinch_thumb(shape, fingers=('index',), pref=(-8.0, 25.0, 0.0, 12.0, 15.0), along=(0.5, 0.9)):
    """Opposed thumb whose PAD presses on the pad of the fingertip(s): the thumb's distal phalanx
    touches each finger's distal phalanx near both tips, on the thumb's pad side and the finger's
    pad side, the two pads facing each other (pulp to pulp). Its nail then faces away from the
    finger, toward the thumb side, never the way the palm faces; the thumb stays well inside its
    joint limits. `along` = where on the thumb's distal phalanx the contact sits (0 = IP joint,
    1 = tip): on the pulp, not on the very end. Pattern search from a few starts."""
    lim = [(lo, hi) for _, lo, hi in LIMITS['thumb']]
    margin = (4.0, 4.0, 8.0, 4.0, 8.0)           # keep clear of the limits (opposition and IP most)

    def err(q):
        e = 0.0
        for fg in fingers:
            m = pinch_contact(q, shape, fg)
            e += 6.0 * m['gap'] ** 2
            e += 200.0 * max(0.0, 0.85 - m['pad_to']) ** 2 + 200.0 * max(0.0, 0.3 - m['fpad_to']) ** 2
            e += 200.0 * max(0.0, m['pads'] + 0.35) ** 2 + 200.0 * max(0.0, m['nail_palm'] - 0.4) ** 2
            e += 400.0 * max(0.0, along[0] - m['s'], m['s'] - along[1]) ** 2
            e += 100.0 * max(0.0, 0.5 - m['t'], m['t'] - 0.95) ** 2
        e += 4.0 * sum(((x - y) / (hi - lo)) ** 2 for x, y, (lo, hi) in zip(q, pref, lim))
        e += 0.3 * sum(max(0.0, lo + mg - x, x - hi + mg) ** 2 for x, (lo, hi), mg in zip(q, lim, margin))
        return e

    best_all, e_all = None, float('inf')
    for start in (pref, (pref[0] - 10, pref[1] + 15, pref[2] + 15, pref[3] + 10, pref[4] + 10),
                  (pref[0] + 10, pref[1] - 10, pref[2] - 10, pref[3], pref[4]),
                  (pref[0], pref[1] + 25, pref[2] + 35, pref[3] + 15, pref[4] + 20)):
        best = [min(max(v, lo), hi) for v, (lo, hi) in zip(start, lim)]
        e_best, step = err(best), 16.0
        while step > 0.05:
            improved = False
            for i in range(5):
                for dd in (step, -step):
                    cand = best[:]
                    cand[i] = min(max(cand[i] + dd, lim[i][0]), lim[i][1])
                    e = err(cand)
                    if e < e_best:
                        best, e_best, improved = cand, e, True
            if not improved:
                step /= 2
        if e_best < e_all:
            best_all, e_all = best, e_best
    return tuple(round(v, 2) for v in best_all)


def hs_1():
    """Index straight, others closed, thumb over the middle finger (INES 14)."""
    shape = fist({'index': fing(2, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['middle'])
    return shape


def hs_1_curved():
    """Index up with the tip curled forward (toward the palm side) at the middle and end joints,
    others closed, thumb over the middle finger (INES 15)."""
    shape = fist({'index': fing(2, 0, 40, 30)})
    shape['thumb'] = thumb_over(shape, ['middle'])
    return shape


def hs_B():
    """Flat hand, fingers together, thumb open (INES 63)."""
    return {'index': fing(2, 0, 0, 0), 'middle': fing(0, 0, 0, 0), 'ring': fing(-2, 0, 0, 0),
            'pinky': fing(-4, 0, 0, 0), 'thumb': (28.0, 16.0, 8.0, 6.0, 4.0)}


def hs_L(index=(0.0, 0.0, 0.0)):
    """Index up, thumb out sideways in the palm plane, other fingers closed (INES 8)."""
    return fist({'index': fing(2, *index), 'thumb': (48.0, 8.0, 0.0, 4.0, 2.0)})


def hs_ring():
    """OK ring (café): the index curls toward the palm side (DIP about 2/3 of the PIP) and the
    opposed thumb comes up to it, PAD ON PAD: the thumb's pulp presses on the index's pulp, the two
    pads facing each other, so the thumbnail faces the thumb side (seen full from the radial side,
    never facing the way the palm does) and the opening between them stays round; the other three
    fingers open and spread like a fan, each a little more bent than the one before but mostly
    straight: strongly bent, they would cross one another when the palm turns toward the mouth."""
    shape = {'index': fing(2, 50, 75, 52), 'middle': fing(-2, 2, 4, 3), 'ring': fing(-10, 6, 6, 4),
             'pinky': fing(-19, 10, 8, 6)}
    shape['thumb'] = pinch_thumb(shape)
    return shape


def hs_F():
    """F of Libras (família): the index bends mostly at the knuckle and its fingertip rests on the
    thumb tip, PAD ON PAD (the thumb's pulp under the index's pulp, the pads facing each other, the
    thumbnail toward the thumb side); the other three fingers open and spread (INES 54)."""
    shape = {'index': fing(4, 80, 30, 20), 'middle': fing(3, 0, 0, 0), 'ring': fing(-6, 0, 0, 0),
             'pinky': fing(-15, 0, 0, 0)}
    shape['thumb'] = pinch_thumb(shape)
    return shape


def hs_S():
    """Fist, thumb across the front of the index and middle fingers."""
    shape = fist({'index': curl(-1, 2), 'middle': curl(1, 2), 'ring': curl(4, 2), 'pinky': curl(8, 2)})
    shape['thumb'] = thumb_over(shape, ['index', 'middle'], at=0.5)
    return shape


def hs_A():
    """Fist, thumb straight up against the side of the index."""
    shape = fist()
    side = vadd(on_surface(shape, 'index', 0, 1, 0.0, at=0.75), (seg_radius('index', 0) + seg_radius('thumb', 2) * 0.9, 0.0, -2.0))
    shape['thumb'] = solve_thumb(side, pad_to=(-1.0, 0.0, 0.0), point=(0.0, -1.0, 0.0), pref=(-5.0, 12.0, 25.0, 8.0, 8.0))
    return shape


def hs_Y():
    """Thumb and little finger out, the other three folded."""
    return fist({'pinky': fing(-18, 0, 0, 0), 'thumb': (46.0, 12.0, 0.0, 4.0, 0.0)})


def hs_V():
    """Index and middle up and apart, the others folded under the thumb."""
    shape = fist({'index': fing(12, 0, 0, 0), 'middle': fing(-8, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


def hs_5():
    """Open hand, all fingers spread."""
    return {'index': fing(14, 0, 4, 2), 'middle': fing(3, 0, 3, 2), 'ring': fing(-8, 0, 4, 2),
            'pinky': fing(-18, 0, 5, 3), 'thumb': (40.0, 16.0, 6.0, 6.0, 4.0)}


def hs_C():
    """Curved hand: fingers together and bent, the thumb opposite them, a C seen from the side."""
    return {'index': fing(1, 38, 46, 26), 'middle': fing(0, 38, 48, 28), 'ring': fing(-1, 38, 48, 28),
            'pinky': fing(-2, 40, 48, 28), 'thumb': (18.0, 48.0, 52.0, 10.0, 14.0)}


def hs_O():
    """All fingertips curved together onto the thumb, a round opening seen from the side: the
    thumb's pad presses on the index's pad (pulp to pulp), the other tips close beside it."""
    shape = {'index': fing(2, 46, 68, 42), 'middle': fing(1, 48, 68, 44), 'ring': fing(3, 50, 66, 44),
             'pinky': fing(6, 54, 64, 44)}
    shape['thumb'] = pinch_thumb(shape)
    return shape


def rot(p, yaw, pitch, roll):
    """Yaw turns the palm (0 = palm to viewer, 180 = back of hand), pitch tips the fingers
    toward the viewer, roll turns the hand on screen (clockwise)."""
    x, y, z = p
    a = math.radians(yaw)
    x, z = x * math.cos(a) + z * math.sin(a), -x * math.sin(a) + z * math.cos(a)
    a = math.radians(pitch)
    y, z = y * math.cos(a) + z * math.sin(a), -y * math.sin(a) + z * math.cos(a)
    a = math.radians(roll)
    x, y = x * math.cos(a) - y * math.sin(a), x * math.sin(a) + y * math.cos(a)
    return (x, y, z)


def anchor_point(shape, anchor):
    if anchor == 'wrist':
        return (0.0, 0.0, 0.0)
    if anchor == 'pinch':
        a, b = digit_points(shape, 'thumb')[-1], digit_points(shape, 'index')[-1]
        return tuple((p + q) / 2 for p, q in zip(a, b))
    if anchor == 'fingertips':
        a, b = digit_points(shape, 'index')[-1], digit_points(shape, 'middle')[-1]
        return tuple((p + q) / 2 for p, q in zip(a, b))
    return digit_points(shape, anchor.replace('_tip', ''))[-1]


# ---- small 2D/3D geometry used for layering and occlusion
def _closest(p, a, b):
    """Parameter t and distance of the point on segment ab (2D) closest to p."""
    abx, aby = b[0] - a[0], b[1] - a[1]
    L2 = abx * abx + aby * aby
    t = 0.0 if L2 < 1e-9 else max(0.0, min(1.0, ((p[0] - a[0]) * abx + (p[1] - a[1]) * aby) / L2))
    return t, math.hypot(a[0] + abx * t - p[0], a[1] + aby * t - p[1])


def seg_seg(a0, a1, b0, b1):
    """Closest points of two 2D segments: (s on a, t on b, distance)."""
    def cr(o, p, q):
        return (p[0] - o[0]) * (q[1] - o[1]) - (p[1] - o[1]) * (q[0] - o[0])
    d1, d2, d3, d4 = cr(b0, b1, a0), cr(b0, b1, a1), cr(a0, a1, b0), cr(a0, a1, b1)
    if d1 * d2 < 0 and d3 * d4 < 0:
        s = d1 / (d1 - d2)
        t = d3 / (d3 - d4)
        return s, t, 0.0
    cands = []
    t, d = _closest(a0, b0, b1); cands.append((d, 0.0, t))
    t, d = _closest(a1, b0, b1); cands.append((d, 1.0, t))
    s, d = _closest(b0, a0, a1); cands.append((d, s, 0.0))
    s, d = _closest(b1, a0, a1); cands.append((d, s, 1.0))
    d, s, t = min(cands)
    return s, t, d


def inside(pt, poly_pts):
    x, y, c = pt[0], pt[1], False
    for i in range(len(poly_pts)):
        (x1, y1), (x2, y2) = poly_pts[i - 1][:2], poly_pts[i][:2]
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
            c = not c
    return c


def palm_curve(palm, n=8):
    """The palm outline as drawn (the smooth curve through the midpoints of the control
    polygon, see smooth_cmds), sampled as a closed polyline."""
    m = len(palm)
    mids = [((palm[i][0] + palm[(i + 1) % m][0]) / 2, (palm[i][1] + palm[(i + 1) % m][1]) / 2) for i in range(m)]
    out = []
    for i in range(m):
        a, c, b = mids[i - 1], palm[i], mids[i]
        for s in range(n):
            t = s / n
            out.append(((1 - t) ** 2 * a[0] + 2 * (1 - t) * t * c[0] + t * t * b[0],
                        (1 - t) ** 2 * a[1] + 2 * (1 - t) * t * c[1] + t * t * b[1]))
    return out


def line_crossings(p, u, poly_pts):
    """Parameters t where the line p + t*u (2D, u a unit vector) crosses a closed polyline."""
    ts = []
    for i in range(len(poly_pts)):
        (x1, y1), (x2, y2) = poly_pts[i - 1][:2], poly_pts[i][:2]
        ex, ey = x2 - x1, y2 - y1
        den = u[0] * ey - u[1] * ex
        if abs(den) < 1e-9:
            continue
        wx, wy = x1 - p[0], y1 - p[1]
        t = (wx * ey - wy * ex) / den
        s = (wx * u[1] - wy * u[0]) / den
        if 0.0 <= s <= 1.0:
            ts.append(t)
    return ts


def near_poly(pt, poly_pts, r):
    """Inside the closed polyline, or within r of its edge."""
    if inside(pt, poly_pts):
        return True
    return any(_closest(pt, poly_pts[i - 1], poly_pts[i])[1] < r for i in range(len(poly_pts)))


def surface_curve(J, n, l, r, phis, along=None, shift=0.0, bulge=0.0):
    """Points on a bone's surface around joint J: n = the face normal, l = hinge axis. Angles
    are clamped to the half that faces the viewer."""
    phi0 = math.degrees(math.atan2(l[2], n[2]))
    lo, hi = phi0 - 82, phi0 + 82
    out = []
    for i, ph in enumerate(phis):
        ph = min(max(ph, lo), hi)
        nrm = vadd(vmul(n, math.cos(math.radians(ph))), vmul(l, math.sin(math.radians(ph))))
        q = vadd(J, vmul(nrm, r))
        if along is not None:
            mid = 1.0 if i == len(phis) // 2 else 0.0
            q = vadd(q, vmul(along, shift + bulge * mid))
        out.append(q)
    return out


def nail_outline(J, T, frame, r):
    """The fingernail as a patch on the dorsal face of the distal phalanx, from near the DIP to
    just past the bone tip, clamped to the half of the surface that faces the viewer, so an
    oblique nail is narrower and slides toward the dorsal edge. 14 points, 3D."""
    a, p, l = frame
    d = vmul(p, -1.0)
    L = math.sqrt(vdot(vsub(T, J), vsub(T, J)))
    phi0 = math.degrees(math.atan2(l[2], d[2]))
    lo, hi = max(-50.0, phi0 - 84), min(50.0, phi0 + 84)
    if lo > hi:
        lo = hi = max(min(phi0, 50.0), -50.0)
    s0, s1 = 0.36 * L, L + 0.36 * r

    def pt(s, ph):
        rad = r * 0.96 if s <= L else r * 0.96 * math.sqrt(max(0.0, 1 - ((s - L) / (r * 1.05)) ** 2))
        nrm = vadd(vmul(d, math.cos(math.radians(ph))), vmul(l, math.sin(math.radians(ph))))
        return vadd(vadd(J, vmul(a, s)), vmul(nrm, rad))

    sides = [s0 + (s1 - s0) * k / 3 for k in range(4)]
    mid = (lo + hi) / 2
    out = [pt(s, lo) for s in sides]
    out += [pt(s1 + 0.12 * r, lo + (mid - lo) * 0.5), pt(s1 + 0.18 * r, mid), pt(s1 + 0.12 * r, hi - (hi - mid) * 0.5)]
    out += [pt(s, hi) for s in sides[::-1]]
    out += [pt(s0 - 0.05 * r, hi - (hi - mid) * 0.5), pt(s0 - 0.08 * r, mid), pt(s0 - 0.05 * r, lo + (mid - lo) * 0.5)]
    return out


def hand_geometry(pose, mirror):
    """Projects one hand: 3D joints and frames on screen, the palm, and per-part decisions
    (front/back of the palm, depth order of the digits, which nails, creases and knuckle
    wrinkles show). Screen coordinates: x right, y down, z toward the viewer."""
    shape, yaw, pitch, roll, scale = pose['shape'], pose['yaw'], pose['pitch'], pose['roll'], pose['scale']
    if mirror:   # left hand = mirror image of the right hand
        yaw, roll = -yaw, -roll
    sx = -1.0 if mirror else 1.0

    def tv(v):   # a direction
        return rot((v[0] * sx, v[1], v[2]), yaw, pitch, roll)

    def tf(p):
        x, y, z = tv(p)
        return (x * scale, y * scale, z * scale)

    ax, ay, _ = tf(anchor_point(shape, pose['anchor']))
    wx, wy = pose['at'][0] - ax, pose['at'][1] - ay

    def scr(p):
        x, y, z = tf(p)
        return (wx + x, wy + y, z)

    n = tv((0.0, 0.0, 1.0))            # palm normal (palmar side)
    facing = n[2]
    # Seen from the back, fingers start right at the knuckles: the top edge comes down a little.
    drop = 3.0 * min(max(-facing, 0.0), 1.0)
    palm = [scr((x, y + (drop if y < -34 else 0.0), 0.0)) for x, y in PALM]
    # Give the palm some thickness, so a hand seen from the side is a slab, not a line:
    # each outline point moves half the thickness toward the side it faces.
    nx, ny, _ = tf((0.0, 0.0, PALM_HALF_THICKNESS))
    cx, cy = sum(p[0] for p in palm) / len(palm), sum(p[1] for p in palm) / len(palm)
    palm = [(x + nx, y + ny, z) if (x - cx) * nx + (y - cy) * ny >= 0 else (x - nx, y - ny, z) for x, y, z in palm]
    # Near the knuckle row the hand is the round heads of the finger bones, not a box: there the
    # palm's outline never reaches past the outer side of the first or last finger, so a turned hand
    # has no "shoulder" beside the index or the little finger (the finger's edge runs on into the
    # hand's edge).
    fx, fy, _ = tv((0.0, -1.0, 0.0))
    fl = math.hypot(fx, fy)
    if fl > 0.2:
        ex, ey = -fy / fl, fx / fl
        lam = []
        for name in ('index', 'middle', 'ring', 'pinky'):
            (bx, by), _, w = FINGERS[name]
            kx, ky, _ = scr((bx, by, 0.0))
            lam.append(((kx - wx) * ex + (ky - wy) * ey, w * scale / 2))
        lo, hi = min(l - r for l, r in lam), max(l + r for l, r in lam)
        out = []
        for (x, y, z), (_, hy) in zip(palm, PALM):
            k = min(max((-26.0 - hy) / 5.0, 0.0), 1.0)
            l = (x - wx) * ex + (y - wy) * ey
            d = (min(max(l, lo), hi) - l) * k
            out.append((x + ex * d, y + ey * d, z))
        palm = out
    o = tf((0.0, 0.0, 0.0))
    axes = [tuple(c - oc for c, oc in zip(tf(v), o)) for v in ((1.0, 0, 0), (0, 1.0, 0), (0, 0, 1.0))]
    back_z = -PALM_HALF_THICKNESS
    knuckles = []
    for name in ('pinky', 'ring', 'middle', 'index'):
        (bx, by), _, w = FINGERS[name]
        knuckles.append([scr((bx - w * 0.3, by + 1.2, back_z)), scr((bx, by - 0.2, back_z)),
                         scr((bx + w * 0.3, by + 1.2, back_z))])
    origin = scr((0.0, 0.0, 0.0))
    nv = n if facing >= 0 else vmul(n, -1.0)       # palm normal turned toward the viewer
    edge_on = abs(facing) < 0.12

    def ahead(p):   # distance in front of the palm's mid-plane, toward the viewer (hand units)
        return vdot(vsub(p, origin), nv) / scale

    curve = palm_curve(palm)
    geo = {'wrist': (wx, wy), 'palm': palm, 'palm_curve': curve, 'crease': [scr((x, y, 0.0)) for x, y in CREASE],
           'head_line': [scr((x, y, 0.0)) for x, y in HEAD_LINE], 'knuckles': knuckles,
           'axes': axes, 'scale': scale, 'palm_facing': facing, 'palm_n': n, 'palm_o': origin,
           'mirror': mirror, 'shape': shape, 'digits': {}}
    for name in DIGITS:
        hp, hf = digit_chain(shape, name)
        pts = [scr(p) for p in hp]
        frames = [tuple(tv(v) for v in fr) for fr in hf]
        radii = [seg_radius(name, k, scale) for k in range(3)]
        front = [edge_on or ahead(vmul(vadd(pts[k], pts[k + 1]), 0.5)) > (-1.5 if name == 'thumb' else -2.5)
                 for k in range(3)]
        if name != 'thumb' and not edge_on:
            # Where a finger bone is not over the palm in the picture, being a little behind the
            # palm's plane hides nothing: it stays in the layer of the bone before it, so one
            # finger is never split into a front stub and a back remainder with two outlines.
            for k in (1, 2):
                if front[k] != front[k - 1] and not any(
                        near_poly(vadd(pts[k], vmul(vsub(pts[k + 1], pts[k]), t)), curve, radii[k] * 0.7)
                        for t in (0.0, 0.25, 0.5, 0.75, 1.0)):
                    front[k] = front[k - 1]
        w = (THUMB_W if name == 'thumb' else FINGERS[name][2]) * scale
        dg = {'pts': pts, 'frames': frames, 'r': radii, 'front': front, 'w': w,
              'segs': (1, 2) if name == 'thumb' else (0, 1, 2), 'trim': True}
        if name != 'thumb':
            # A finger in front of the palm (or of the back of the hand) grows out of it: its
            # outline starts where its axis crosses the palm's drawn edge, and its fill reaches
            # into the palm, so there is no rounded base drawn over the hand.
            ux, uy, L = unit2(pts[0], pts[1])
            ins = inside(pts[0], curve)
            ts = line_crossings(pts[0], (ux, uy), curve)
            if ins:
                ts = [t for t in ts if 0.0 < t <= L]
                tb = min(ts) if ts else min(3.4 * scale, L * 0.5)
                tf_ = 0.0
            else:
                ts = [t for t in ts if -1.6 * radii[0] <= t <= 0.0]
                tb = max(ts) if ts else None
                tf_ = None if tb is None else tb - 0.6 * radii[0]
            dg['trim'] = tb is not None
            dg['knuckle_in'] = ins
            dg['side_s'] = (tb, tb)
            if tb is not None:
                dg['ink_base'] = (pts[0][0] + ux * tb, pts[0][1] + uy * tb)
                dg['fill_base'] = (pts[0][0] + ux * tf_, pts[0][1] + uy * tf_)
        geo['digits'][name] = dg
    _finger_roots(geo)
    # The web between thumb and index (first web space) and the thumb's fleshy base: skin from
    # the thumb's base (CMC) out to its MCP joint, across to the index knuckle (MCP) and back
    # through the palm. Its free edge runs from the thumb MCP to the index knuckle, sagging a
    # little toward the thumb base, so the opening of a ring or a C stops there and a thumb
    # seen from the side never looks detached from the hand.
    th_pts = digit_points(shape, 'thumb')
    C, T, I = th_pts[0], th_pts[1], (FINGERS['index'][0][0], FINGERS['index'][0][1], 0.0)
    M = vmul(vadd(T, I), 0.5)
    Q = vadd(M, vmul(vsub(C, M), 2 * WEB_SAG))
    edge = [vadd(vadd(vmul(T, (1 - u) ** 2), vmul(Q, 2 * (1 - u) * u)), vmul(I, u * u))
            for u in (k / WEB_STEPS for k in range(WEB_STEPS + 1))]
    geo['web'] = [scr(p) for p in [C] + edge]
    geo['web_hand'] = [C] + edge
    _fold_groups(geo)
    _depth_order(geo)
    _details(geo, pose)
    # Palm creases only on the palm side, knuckle bumps only on the back.
    geo['lines_vis'] = facing > 0.35
    geo['knuckles_vis'] = facing < -0.35
    geo['life_vis'] = geo['digits']['thumb']['front'][0] and facing > 0.25
    return geo


NEIGHBOURS = {'index': ('middle',), 'middle': ('index', 'ring'), 'ring': ('middle', 'pinky'), 'pinky': ('ring',)}


def _finger_roots(geo):
    """Where each side line of a finger in front of the palm starts. A finger rises from its
    knuckle: a side that faces open space, or a folded neighbour, runs down to the knuckle row
    (so the whole proximal phalanx reads, and its edge continues past the palm's top edge instead
    of turning into it); a side that faces an open neighbour lying alongside it starts at the
    palm's edge, where the web between the two fingers is."""
    digs, curve, sc = geo['digits'], geo['palm_curve'], geo['scale']
    for name in ('index', 'middle', 'ring', 'pinky'):
        dg = digs[name]
        if not dg['trim'] or not dg['knuckle_in']:
            continue
        P0, P1 = dg['pts'][0], dg['pts'][1]
        ux, uy, L = unit2(P0, P1)
        if L < 0.5 * sc:
            continue
        nx, ny = -uy, ux
        tb = dg.setdefault('axis_tb', dg['side_s'][0])
        dg['side_s'] = (tb, tb)
        starts = []
        for sg in (1, -1):
            web = False
            for nb in NEIGHBOURS[name]:
                ng = digs[nb]
                if ng.get('hidden'):
                    continue
                Q0, Q1 = ng['pts'][0], ng['pts'][1]
                # beside it on screen, not stacked behind it (a side view)
                if abs((Q0[0] - P0[0]) * nx + (Q0[1] - P0[1]) * ny) < 0.6 * (dg['r'][0] + ng['r'][0]):
                    continue
                vx, vy, M = unit2(Q0, Q1)
                q = geo['shape'][nb]
                if is_tight(geo['shape'], nb) or q[1] > 60 or q[2] > 70:     # folded: no web at the palm's edge
                    continue
                if M < 0.5 * sc or ux * vx + uy * vy < 0.75:
                    continue
                if ((Q0[0] - P0[0]) * nx + (Q0[1] - P0[1]) * ny) * sg <= 0:
                    continue
                if seg_seg(P0, P1, Q0, Q1)[2] < dg['r'][0] + ng['r'][0] + 1.5 * sc:
                    web = True
            if web:
                p = (P0[0] + nx * sg * dg['r'][0], P0[1] + ny * sg * dg['r'][0])
                ts = [t for t in line_crossings(p, (ux, uy), curve) if 0.0 < t <= L]
                starts.append(max(min(ts) - 0.3 * sc, 0.0) if ts else dg['side_s'][0])
            else:
                starts.append(0.0)
        dg['side_s'] = tuple(starts)
        s0 = min(starts)
        dg['ink_base'] = (P0[0] + ux * s0, P0[1] + uy * s0)


def is_tight(shape, name):
    """A finger folded into a fist: its fingertip rests on the palm surface, inside the palm."""
    if name == 'thumb':
        return False
    q = shape[name]
    if q[2] < 60:
        return False
    tip = finger_chain(name, q)[0][3]
    return tip[2] < PALM_HALF_THICKNESS + 2.6 * seg_radius(name, 2) and inside(tip, PALM)


def _fold_groups(geo):
    """A digit folded back over itself in the picture (a hooked index, a curled thumb) is drawn
    in two groups: the part nearer the viewer goes on top, with its own outline. A finger folded
    into a fist is one silhouette instead: its tip is pressed into the palm, the inside of the
    curl is flesh, so no inner outline shows (no loops or hooks inside the hand)."""
    for name, dg in geo['digits'].items():
        dg['tight'] = is_tight(geo['shape'], name)
        pts, radii, groups = dg['pts'], dg['r'], [0, 0, 0]
        # The inside of a fist curl is flesh: filled from the knuckle round to the tip and on into
        # the palm where the tip presses on it (so a side view shows no palm edge in there).
        n, R = geo['palm_n'], radii[2] + LINE + 0.6
        dg['curl'] = [q[:2] for q in pts] + [(pts[3][0] - n[0] * R, pts[3][1] - n[1] * R)]
        # Seen with the palm edge-on, the half of the fingertip that presses into the palm lies on
        # the palm's edge: a patch of skin over it hides that part of the tip's outline (and the
        # palm's edge under it), so the tip merges into the palm instead of showing a hook.
        n2 = math.hypot(n[0], n[1])
        wgt = min(max((n2 - 0.8) / 0.15, 0.0), 1.0)
        T = pts[3]
        if n2 > 1e-6:
            ux, uy = -n[0] / n2, -n[1] / n2
        else:
            ux, uy = 0.0, 0.0
        wx, wy, Rw = -uy, ux, R * wgt
        dg['tipcover'] = [(T[0] + wx * Rw, T[1] + wy * Rw), (T[0] + wx * Rw + ux * Rw, T[1] + wy * Rw + uy * Rw),
                          (T[0] - wx * Rw + ux * Rw, T[1] - wy * Rw + uy * Rw), (T[0] - wx * Rw, T[1] - wy * Rw)]
        if dg['tight']:
            dg['group'] = groups
            continue
        best, pick = 0.0, None
        for j in range(dg['segs'][0] + 1, 3):
            A, J, B = pts[j - 1], pts[j], pts[j + 1]
            u0, u1 = (A[0] - J[0], A[1] - J[1]), (B[0] - J[0], B[1] - J[1])
            L0, L1 = math.hypot(*u0), math.hypot(*u1)
            if min(L0, L1) < 0.8:
                continue
            c = (u0[0] * u1[0] + u0[1] * u1[1]) / (L0 * L1)
            far, (p0, p1) = (A, (J, B)) if L0 <= L1 else (B, (J, A))
            overlap = radii[j - 1] + radii[j] - _closest(far, p0, p1)[1]
            weight = (c + 0.2) * min(L0, L1)
            if c > 0.2 and overlap > 0 and weight > best:
                best, pick = weight, (j, (J[2] + B[2]) / 2 > (A[2] + J[2]) / 2)
        if pick:
            j, distal_near = pick
            groups = [1 if (k >= j) == distal_near else 0 for k in range(3)]
        dg['group'] = groups


def _segments(dg, layer=None, group=None):
    out = []
    for k in dg['segs']:
        if (layer is None or dg['front'][k] == (layer == 'front')) and (group is None or dg['group'][k] == group):
            out.append((dg['pts'][k], dg['pts'][k + 1], dg['r'][k]))
    return out


def _overlap_vote(segs_a, segs_b, sc):
    """> 0 when the first set of bones is nearer where the two overlap on screen."""
    vote = 0.0
    for a0, a1, ra in segs_a:
        for b0, b1, rb in segs_b:
            s, t, dist = seg_seg(a0, a1, b0, b1)
            ov = ra + rb - dist
            if ov <= 0:
                continue
            za, zb = a0[2] + (a1[2] - a0[2]) * s, b0[2] + (b1[2] - b0[2]) * t
            if abs(za - zb) > 0.6 * sc:
                vote += ov * (1 if za > zb else -1)
    return vote


def _depth_order(geo):
    """Draw order inside each layer (behind / in front of the palm). The units are digit parts:
    a whole digit, or its two groups when it folds over itself or when another digit passes
    between its base and its tip (a thumb tip in front of the index base but behind its tip).
    Order comes from where parts overlap on screen and which one is nearer there."""
    sc, digs = geo['scale'], geo['digits']
    # Split a digit whose bones lie on both sides of one bone of another digit.
    for name, dg in digs.items():
        if any(dg['group']) or dg['tight']:
            continue
        for other, og in digs.items():
            if other == name:
                continue
            for kb in og['segs']:
                rel = {}
                for k in dg['segs']:
                    if dg['front'][k] != og['front'][kb]:
                        continue
                    v = _overlap_vote([(dg['pts'][k], dg['pts'][k + 1], dg['r'][k])],
                                      [(og['pts'][kb], og['pts'][kb + 1], og['r'][kb])], sc)
                    if abs(v) > 0.3 * sc:
                        rel[k] = v > 0
                over = [k for k, v in rel.items() if v]
                under = [k for k, v in rel.items() if not v]
                if over and under and (max(under) < min(over) or max(over) < min(under)):
                    j = max(min(over), min(under))
                    dg['group'] = [1 if k >= j else 0 for k in range(3)]
                    break
            if any(dg['group']):
                break
    geo['order'] = {}
    for layer in ('back', 'front'):
        items = [(nm, g) for nm, dg in digs.items() for g in (0, 1) if _segments(dg, layer, g)]
        segs = {it: _segments(digs[it[0]], layer, it[1]) for it in items}
        meanz = {it: sum(a[2] + b[2] for a, b, _ in segs[it]) / (2 * len(segs[it])) for it in items}
        ahead = {it: set() for it in items}   # ahead[X] = parts that X must be drawn over
        for i, A in enumerate(items):
            for B in items[i + 1:]:
                vote = _overlap_vote(segs[A], segs[B], sc)
                if vote > 0:
                    ahead[A].add(B)
                elif vote < 0:
                    ahead[B].add(A)
        order, left = [], set(items)
        while left:
            free = [it for it in left if not (ahead[it] & (left - {it}))]   # covers nothing still undrawn
            pick = min(free or left, key=lambda it: (meanz[it], DIGITS.index(it[0]), it[1]))
            order.append(pick)
            left.remove(pick)
        geo['order'][layer] = {it: i for i, it in enumerate(order)}
        # Fingers folded into the fist that come one after another in depth share one outer
        # outline (drawn first, under all of them); between them only a thin line shows. So
        # a fist seen from the side has one clean top edge, not a stack of near-parallel lines.
        start, run = {}, None
        for i, it in enumerate(order):
            if digs[it[0]]['tight']:
                run = i if run is None else run
                start[it] = run
            else:
                run = None
        geo.setdefault('run_start', {})[layer] = start


def _covering(geo, pt, z, skip):
    """True when some part of the hand covers screen point pt and is nearer than depth z."""
    tol = 1.0 * geo['scale']
    for name, dg in geo['digits'].items():
        for k in range(3):
            if (name, k) == skip:
                continue
            a, b, r = dg['pts'][k], dg['pts'][k + 1], dg['r'][k]
            if name == 'thumb' and k == 0:
                r = (THENAR[0] + THENAR[1]) / 2 * geo['scale']
            t, d = _closest(pt, a, b)
            if d < r * 0.97:
                zf = a[2] + (b[2] - a[2]) * t + math.sqrt(r * r - d * d)
                if zf > z + tol:
                    return True
    n, o = geo['palm_n'], geo['palm_o']
    if abs(n[2]) > 0.1 and inside(pt, geo['palm']):
        zp = o[2] - ((pt[0] - o[0]) * n[0] + (pt[1] - o[1]) * n[1]) / n[2] + PALM_HALF_THICKNESS * geo['scale'] / abs(n[2])
        if zp > z + tol:
            return True
    return False


def _details(geo, pose):
    n, facing = geo['palm_n'], geo['palm_facing']
    for name, dg in geo['digits'].items():
        pts, frames, radii = dg['pts'], dg['frames'], dg['r']
        # Nail: on the dorsal face of the distal phalanx, only when that face looks at the viewer.
        a2, p2, l2 = frames[2]
        dors = vmul(p2, -1.0)
        outline = nail_outline(pts[2], pts[3], frames[2], radii[2])
        c = tuple(sum(q[i] for q in outline) / len(outline) for i in range(3))
        into_palm = vdot(a2, n) < -0.25 and facing > 0.2
        dg['nail'] = outline
        dg['nail_dot'] = dors[2]
        # Only a fingertip seen end-on (pointing at the viewer or away, its last phalanx shorter
        # than half its length on screen) leaves its nail out: there it would be a sliver on the rim
        # of a stub. Any fingertip that still shows most of its length and
        # whose nail side faces the viewer gets its nail, so a finger seen from the back never reads
        # as turned around.
        end_on = abs(a2[2]) > END_ON
        dg['nail_vis'] = dors[2] > NAIL_DOT and not end_on and not into_palm and not _covering(geo, c, c[2], (name, 2))
        # Joint creases (palmar side) and knuckle wrinkles (dorsal side).
        dg['creases'], dg['crease_vis'], dg['wrinkles'], dg['wrinkle_vis'] = [], [], [], []
        for j in (1, 2):
            pa = vunit(vadd(frames[j - 1][1], frames[j][1]))
            aa = vunit(vadd(frames[j - 1][0], frames[j][0]))
            l = frames[j][2]
            r = radii[j] * 0.98
            cr = surface_curve(pts[j], pa, l, r, (-58, 0, 58))
            cm = cr[1]
            dg['creases'].append(cr)
            dg['crease_vis'].append(pa[2] > 0.3 and not _covering(geo, cm, cm[2], (name, j)))
            da = vmul(pa, -1.0)
            # One small arc per knuckle (two read as clutter at phone size).
            wr = [surface_curve(pts[j], da, l, r, (-38, 0, 38), along=aa, shift=0.05 * radii[j], bulge=0.26 * radii[j])]
            wm = wr[0][1]
            dg['wrinkles'].append(wr)
            dg['wrinkle_vis'].append(da[2] > 0.3 and not _covering(geo, wm, wm[2], (name, j)))
        # A fingertip pointing at the viewer gets a round outline (it is the nearest part).
        dg['pad_vis'] = a2[2] > 0.9 and not _covering(geo, pts[3], pts[3][2] + radii[2], (name, 2))
    # Knuckle bumps on the back of the hand, one per finger, where nothing nearer covers them.
    geo['knuckle_vis'] = []
    for kn, name in zip(geo['knuckles'], ('pinky', 'ring', 'middle', 'index')):
        geo['knuckle_vis'].append(facing < -0.35 and not _covering(geo, kn[1], kn[1][2], (name, 0)))
    if pose.get('ring'):
        # The opening of a thumb-index ring, shaded so it reads as a hole even over the face;
        # only when the ring faces the viewer enough for the opening to show.
        ix, th = geo['digits']['index']['pts'], geo['digits']['thumb']['pts']
        loop = ix + th[1:][::-1]
        nz = sum(loop[i - 1][0] * loop[i][1] - loop[i][0] * loop[i - 1][1] for i in range(len(loop)))
        nxv = sum((loop[i - 1][1] - loop[i][1]) * (loop[i - 1][2] + loop[i][2]) for i in range(len(loop)))
        nyv = sum((loop[i - 1][2] - loop[i][2]) * (loop[i - 1][0] + loop[i][0]) for i in range(len(loop)))
        cen = tuple(sum(q[i] for q in loop) / len(loop) for i in range(3))
        # Shaded only when the ring faces the viewer enough and nothing nearer (the palm seen from
        # the back, another finger) covers the opening.
        geo['hole_vis'] = (abs(nz) / (math.sqrt(nz * nz + nxv * nxv + nyv * nyv) or 1) > 0.35
                           and not _covering(geo, cen, cen[2], ('index', 2)))
        ring_pts = [(q[0], q[1]) for q in loop]
        cx, cy = sum(q[0] for q in ring_pts) / len(ring_pts), sum(q[1] for q in ring_pts) / len(ring_pts)
        half = geo['digits']['index']['r'][1]

        def pull(x, y, by):
            k = min(1, by / max(math.hypot(cx - x, cy - y), 1e-6))
            return (x + (cx - x) * k, y + (cy - y) * k)
        # Pull the digits' axes in by half a finger width, so only the real opening is shaded; at
        # the bottom the opening ends at the web's free edge (just inside its outline), so no
        # unshaded sliver is left between the shading and the web.
        web_edge = [(q[0], q[1]) for q in geo['web'][2:-1]]    # from the thumb MCP side to the index side
        geo['hole'] = [pull(x, y, half * 0.9) for x, y in ring_pts] + [pull(x, y, LINE + 0.2) for x, y in web_edge]


def solve_elbow(shoulder, wrist, depth, side, pole=None):
    """Two-bone IK in 3D: the wrist sits `depth` px in front of the shoulders; the elbow
    hangs down, a little outward and forward. Returns the elbow on screen."""
    S = (shoulder[0], shoulder[1], 0.0)
    D = (wrist[0] - S[0], wrist[1] - S[1], depth)
    d = math.sqrt(sum(c * c for c in D))
    u = tuple(c / d for c in D)
    d = max(min(d, ARM_UPPER + ARM_FORE - 0.01), abs(ARM_UPPER - ARM_FORE) + 0.01)
    cos_a = (ARM_UPPER ** 2 + d * d - ARM_FORE ** 2) / (2 * ARM_UPPER * d)
    sin_a = math.sqrt(max(0.0, 1 - cos_a * cos_a))
    raised = min(max((shoulder[1] - wrist[1]) / 80.0, 0.0), 1.0)
    if pole is None:
        pole = ((0.3 + 0.7 * raised) * side, 1.0 - 0.55 * raised, 0.45)
    else:
        pole = (pole[0] * side, pole[1], pole[2])
    k = sum(p * q for p, q in zip(pole, u))
    v = tuple(p - k * q for p, q in zip(pole, u))
    n = math.sqrt(sum(c * c for c in v))
    v = tuple(c / n for c in v)
    return tuple(S[i] + u[i] * ARM_UPPER * cos_a + v[i] * ARM_UPPER * sin_a for i in range(2))


# ---------------------------------------------------------------- motion
def lerp(a, b, t):
    if a is None or b is None:
        return a if t < 0.5 else b
    if isinstance(a, dict):
        return {k: lerp(a[k], b[k], t) for k in a}
    if isinstance(a, (tuple, list)):
        return tuple(lerp(x, y, t) for x, y in zip(a, b))
    if isinstance(a, str):
        return a
    return a + (b - a) * t


def ease(t, kind):
    if kind == 'linear':
        return t
    if kind == 'out':
        return 1 - (1 - t) ** 2
    if kind == 'in':
        return t * t
    return t * t * (3 - 2 * t)


def pose_at(keys, t, hand, mirror=False):
    for (t0, p0), (t1, p1) in zip(keys, keys[1:]):
        if t0 <= t <= t1:
            a, b = p0[hand], p1[hand]
            u = ease((t - t0) / (t1 - t0) if t1 > t0 else 1.0, b.get('ease', 'smooth'))
            pose = lerp({k: v for k, v in a.items() if k not in ('via', 'ease')},
                        {k: v for k, v in b.items() if k not in ('via', 'ease')}, u)
            start, end, via = a['at'], b['at'], b.get('via')
            if a['anchor'] != b['anchor']:
                # Different anchors: interpolate the wrist, so the hand never jumps.
                start = hand_geometry(a, mirror)['wrist']
                wrist_b = hand_geometry(b, mirror)['wrist']
                if via:
                    via = (via[0] + wrist_b[0] - end[0], via[1] + wrist_b[1] - end[1])
                end = wrist_b
                pose['anchor'] = 'wrist'
            if via and start != end:   # curved path: quadratic Bezier through `via`
                pose['at'] = tuple((1 - u) ** 2 * start[i] + 2 * (1 - u) * u * via[i] + u * u * end[i] for i in range(2))
            else:
                pose['at'] = tuple(start[i] + (end[i] - start[i]) * u for i in range(2))
            return pose
    return dict(keys[-1][1][hand])


def P(at, shape, anchor='wrist', yaw=0.0, pitch=0.0, roll=0.0, scale=1.0, depth=45.0, pole=None, **extra):
    pose = {'at': SPOT.get(at, at), 'shape': shape, 'anchor': anchor, 'yaw': yaw, 'pitch': pitch,
            'roll': roll, 'scale': scale, 'depth': depth, 'pole': pole}
    pose.update(extra)
    return pose


def mirrored(pose):
    """Same pose for the other hand, mirrored around the body's midline."""
    out = dict(pose)
    out['at'] = (2 * 200 - pose['at'][0], pose['at'][1])
    if 'via' in pose:
        out['via'] = (2 * 200 - pose['via'][0], pose['via'][1])
    return out


# ---------------------------------------------------------------- signs
# Positions follow the INES dictionary videos (used only as a reference), drawn for a
# right-handed signer: the dominant hand appears on the viewer's left.
SIGNS = {}

# ÁGUA: L hand, palm forward, thumb tip on the chin; the index bends into a hook and
# straightens, repeatedly.
up, bent = hs_L(), hs_L((10, 90, 55))   # bent: the index hooks at the middle joint, tip pointing down
# The palm turns toward the chin (yaw) and tips back a little (pitch), so the hook is seen from
# above its knuckle: an arch over the folded fingers. The hooked fingertip points down and toward
# the viewer, so the back of its last phalanx (the nail side) faces us a little: its nail shows.
water = lambda shape: P((188, 137), shape, 'thumb_tip', yaw=40, pitch=-25, roll=-8, scale=1.05, pole=(0.55, 1.0, 0.5))
SIGNS['agua'] = {
    'poster': 0.0, 'dur': 2.0, 'hands': ['right'], 'handshape': up,
    'keys': [(0.0, [water(up)]), (0.3, [water(up)]), (0.45, [water(bent)]), (0.6, [water(up)]),
             (0.75, [water(bent)]), (0.9, [water(up)]), (1.05, [water(bent)]), (1.2, [water(up)]),
             (2.0, [water(up)])],
    'marks': [(191, 140, 120)],
    'arrows': [{'d': 'M 144 66 Q 166 62 170 86', 'both': True}],
}

# CAFÉ: thumb and index in a ring on the corner of the mouth; the wrist turns inward so the
# back of the hand comes forward and the open fingers cross in front of the mouth, two times.
# The palm is turned toward the mouth, so the ring (on the palm side) sits at the mouth corner
# with its opening toward the viewer and the hand stays beside the face (eyes and nose clear);
# the three open fingers fan up beside the cheek.
ring = hs_ring()
coffee = lambda yaw, pitch, roll: P((186, 125), ring, 'pinch', yaw=yaw, pitch=pitch, roll=roll, scale=1.0, depth=40,
                                    ring=True, pole=(0.4, 1.0, 0.45))
# Turned: the back of the hand comes forward and the three open fingers cross in front of the mouth;
# the wrist turns a little past "back to the viewer" (yaw 222), so the ring stays readable at the
# mouth: the index arching up from its knuckle, the thumb tip on it, the opening shaded.
up_c, mid_c, turned_c = coffee(60, 0, -20), coffee(120, 50, 30), coffee(222, 12, 85)
SIGNS['cafe'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right'], 'handshape': ring, 'handshape_ring': True,
    # The picture turns the palm toward the viewer's right, as at the start of the sign: the ring and
    # its opening read, and the three open fingers fan out beside it (seen from the side they would
    # stack into one).
    'handshape_view': {'yaw': 50, 'roll': -10},
    # In the middle of each turn the fingers swing toward the viewer (pitch), not up across the eyes.
    'keys': [(0.0, [up_c]), (0.25, [up_c]), (0.375, [mid_c]), (0.5, [turned_c]), (0.625, [mid_c]), (0.75, [up_c]),
             (0.875, [mid_c]), (1.0, [turned_c]), (1.125, [mid_c]), (1.25, [up_c]), (2.4, [up_c])],
    'marks': [(190, 136, 160)],
    'marks_under': True,   # contact ticks on the face: the turning hand passes in front of them
    'arrows': [{'twist': 0, 'at': 0.0, 'r': (17, 6), 'drop': 4}],
}

# FAMÍLIA: both hands in F, palms forward, rings together in front of the chest; the hands
# draw a horizontal semicircle outward and forward and meet by the little fingers, palms back.
f = hs_F()
start_r = P((184, 192), f, 'index_tip', yaw=45, roll=-8, scale=1.25, depth=60)   # rings close, not touching
open_r = P((124, 184), f, 'index_tip', yaw=40, pitch=-28, roll=-10, scale=1.3, depth=85, via=(148, 200))
end_r = P((197, 176), f, 'pinky_tip', yaw=172, roll=6, scale=1.35, depth=100, via=(132, 196))
rewind_r = dict(start_r, via=(150, 275))   # back to the start low and apart, so the hands never cross
SIGNS['familia'] = {
    'poster': 0.0, 'dur': 2.8, 'hands': ['right', 'left'], 'handshape': f, 'handshape_view': {'yaw': 40},
    'keys': [(0.0, [start_r, mirrored(start_r)]), (0.3, [start_r, mirrored(start_r)]),
             (0.8, [open_r, mirrored(open_r)]), (1.3, [end_r, mirrored(end_r)]),
             (2.0, [end_r, mirrored(end_r)]), (2.8, [rewind_r, mirrored(rewind_r)])],
    'arrows': [{'trail': 0, 'from': 0.3, 'to': 1.3, 'offset': (0, 28), 'trim': 0.14},
               {'trail': 1, 'from': 0.3, 'to': 1.3, 'offset': (0, 28), 'trim': 0.14}],
    'mirror_second': True,
    'contact': ['pinky'],   # the hands meet by the little fingers: the only place they may touch
}

# OBRIGADO: flat hand, fingertips on the side of the forehead (like a salute), then the hand
# moves forward and out at forehead height, back of the hand to the viewer.
b = hs_B()
thanks_on = P((172, 78), b, 'fingertips', yaw=140, pitch=0, roll=42, scale=1.0, depth=40, pole=(0.7, 1.0, 0.45))
thanks_off = P((134, 60), b, 'fingertips', yaw=165, pitch=-15, roll=32, scale=1.1, depth=75, via=(158, 58), ease='out',
                pole=(0.7, 1.0, 0.45))
thanks_back = dict(thanks_on, ease='smooth')
SIGNS['obrigado'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right'], 'handshape': b,
    'keys': [(0.0, [thanks_on]), (0.5, [thanks_on]), (0.9, [thanks_off]), (1.95, [thanks_off]), (2.4, [thanks_back])],
    'marks': [(176, 66, -40)],
    'arrows': [{'d': 'M 170 50 Q 150 40 130 44', 'cap': True}],
}

# VOCÊ: the index points forward, at the person you are talking to. No contact with the body.
one = hs_1()
point = lambda s: P((196, 184), one, 'index_tip', yaw=-35, pitch=50, roll=-20, scale=s, depth=80)
SIGNS['voce'] = {
    'poster': 0.7, 'dur': 2.0, 'hands': ['right'], 'handshape': one,
    'keys': [(0.0, [point(0.94)]), (0.3, [point(1.14)]), (1.6, [point(1.14)]), (2.0, [point(0.94)])],
    # Ripples around the fingertip: "toward you". (Contact ticks would wrongly mean touching the body.)
    'arrows': [{'ripples': (196, 184)}],
}


# COMPUTADOR (Tecnologia): both hands with the index up, palms forward, draw mirrored vertical
# circles in front of the chest: in at the top, down the middle, out at the bottom, up the
# sides. Twice, then a short hold with the index fingers in a slight V. (INES, UFSC Signbank
# and UFV agree; INES timing.)
pc = hs_1_curved()
# Both hands are at the same depth, so they must never overlap on screen (that would be the two
# hands passing through each other): the circles sit a little apart and, near the midline, the
# hands turn back toward the viewer (smaller yaw), which keeps the index fingers apart there.
CX, CY, R = 163, 180, 26
PC_YAW_OUT, PC_YAW_IN = -35.0, -15.0
PC_PITCH = -10.0


def pc_pose(angle):
    """Right-hand pose on the circle; angle 0 = inner point (near the midline), clockwise."""
    a = math.radians(angle)
    at = (CX + R * math.cos(a), CY + R * math.sin(a))
    lean = 9 * math.cos(a)   # tips lean in near the midline, splay out on the outer side
    # Turned a little (thumb side toward the viewer), so the curled fingertip shows in profile;
    # less so at the inner point of the circle, where the two hands come closest.
    yaw = PC_YAW_OUT + (PC_YAW_IN - PC_YAW_OUT) * (1 + math.cos(a)) / 2
    # Seen a little from below (pitch), the folded fingers rise beside the index's knuckle, so the index
    # reads from its base, between them, up to its curled tip.
    return P(at, pc, 'index_tip', yaw=yaw, pitch=PC_PITCH, roll=lean, scale=1.25, depth=85, pole=(0.25, 1.0, 0.3), ease='linear')


start_angle = -135          # top-outer: the hands start up and apart
circle = [start_angle + 30 * k for k in range(25)]   # two full turns, clockwise on screen
pc_keys = [(0.0, [pc_pose(start_angle), mirrored(pc_pose(start_angle))])]
for k, ang in enumerate(circle[1:], 1):
    pose = pc_pose(ang)
    pc_keys.append((0.05 + 1.4 * k / 24, [pose, mirrored(pose)]))
hold = dict(pc_pose(start_angle), roll=-20, ease='smooth')   # INES ends with the index fingers in a V
pc_keys += [(1.6, [hold, mirrored(hold)]), (2.1, [hold, mirrored(hold)]),
            (2.3, [pc_pose(start_angle), mirrored(pc_pose(start_angle))])]


def circle_arrow(cx, cy, r, a0, a1, clockwise):
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    span = (a1 - a0) % 360 if clockwise else (a0 - a1) % 360
    large = 1 if span > 180 else 0
    return f'M {x0:.1f} {y0:.1f} A {r} {r} 0 {large} {1 if clockwise else 0} {x1:.1f} {y1:.1f}'


SIGNS['computador'] = {
    # The picture: palm forward, turned a little toward the thumb side and seen a little from below, so
    # the index rises from the knuckle row beside the folded fingers and its tip curls toward the palm.
    'poster': 1.8, 'dur': 2.3, 'hands': ['right', 'left'], 'handshape': pc, 'handshape_view': {'yaw': -30, 'pitch': -25},
    'keys': pc_keys,
    # Above the fingertips: the right hand turns clockwise (in at the top), the left mirrors it.
    # On the outer side of each circle: up the outside, then in at the top (the inner side is
    # where the fingers meet, so arrows there would cross each other).
    'arrows': [{'d': circle_arrow(CX, CY, R + 10, 100, 290, True)},
               {'d': circle_arrow(2 * 200 - CX, CY, R + 10, 80, 250, False)}],
    'mirror_second': True,
}

# Handshapes for the atlas (and future signs): name -> builder.
HANDSHAPES = {'L': hs_L, 'OK': hs_ring, 'F': hs_F, 'B': hs_B, '1': hs_1, '1 curvo': hs_1_curved,
              'S': hs_S, 'A': hs_A, 'Y': hs_Y, 'V': hs_V, '5': hs_5, 'C': hs_C, 'O': hs_O}


# ---------------------------------------------------------------- SVG
def num(v):
    s = f'{v:.1f}'
    if s.endswith('.0'):
        s = s[:-2]
    return '0' if s == '-0' else s


def poly(pts):
    return 'M' + 'L'.join(f'{num(p[0])} {num(p[1])}' for p in pts)


def stroke(color, width):
    return f' stroke="{color}" stroke-width="{num(width)}"'


# Compact path data for the animated shapes: relative commands in tenths of a pixel, so the
# per-frame SMIL values stay small. Every frame of one shape has the same commands, so the
# browser can interpolate between frames.
def _t(v):
    sign = '-' if v < 0 else ''
    a = abs(v)
    if a % 10 == 0:
        return sign + str(a // 10) if a else '0'
    return sign + (str(a // 10) if a >= 10 else '') + '.' + str(a % 10)


def _join(vals):
    out = ''
    for v in vals:
        s = _t(v)
        if out and not s.startswith('-'):
            out += ' '
        out += s
    return out


def rpath(cmds):
    """cmds: [('M', p), ('L', p), ('Q', c, p), ('C', c1, c2, p), ('Z',)], absolute points."""
    out, cur, start = [], None, None
    for c in cmds:
        letter = c[0]
        if letter == 'Z':
            out.append('z')
            cur = start
            continue
        pts = [(round(p[0] * 10), round(p[1] * 10)) for p in c[1:]]
        if letter == 'M' and cur is None:
            out.append('M' + _join(pts[0]))
        else:
            out.append(letter.lower() + _join([v for p in pts for v in (p[0] - cur[0], p[1] - cur[1])]))
        cur = pts[-1]
        if letter == 'M':
            start = cur
    return ''.join(out)


def rline(pts):
    return rpath([('M', pts[0])] + [('L', p) for p in pts[1:]])


def smooth_cmds(pts):
    """Closed curve through the midpoints of a polygon (rounded palm)."""
    mids = [((pts[i][0] + pts[(i + 1) % len(pts)][0]) / 2, (pts[i][1] + pts[(i + 1) % len(pts)][1]) / 2) for i in range(len(pts))]
    return [('M', mids[-1])] + [('Q', p, m) for p, m in zip(pts, mids)] + [('Z',)]


def smooth_closed(pts):
    return rpath(smooth_cmds(pts))


def curve_cmds(pts):
    """Open smooth curve through 3 points (start, middle, end) as one quadratic."""
    a, m, b = pts
    c = (2 * m[0] - (a[0] + b[0]) / 2, 2 * m[1] - (a[1] + b[1]) / 2)
    return [('M', a), ('Q', c, b)]


K = 0.5523                       # cubic Bezier quarter circle


def circle_cmds(c, r):
    """A circle as four cubic arcs (same commands every frame, so it can be animated)."""
    x, y = c[0], c[1]
    k = K * r
    return [('M', (x + r, y)), ('C', (x + r, y + k), (x + k, y + r), (x, y + r)), ('C', (x - k, y + r), (x - r, y + k), (x - r, y)),
            ('C', (x - r, y - k), (x - k, y - r), (x, y - r)), ('C', (x + k, y - r), (x + r, y - k), (x + r, y)), ('Z',)]


def ellipse_cmds(e):
    """An ellipse (centre x, y, half axes a, b, angle) as four cubic arcs (fixed commands)."""
    cx, cy, a, b, th = e
    c, s = math.cos(th), math.sin(th)

    def at(u, v):
        return (cx + u * c - v * s, cy + u * s + v * c)
    return [('M', at(a, 0)), ('C', at(a, K * b), at(K * a, b), at(0, b)), ('C', at(-K * a, b), at(-a, K * b), at(-a, 0)),
            ('C', at(-a, -K * b), at(-K * a, -b), at(0, -b)), ('C', at(K * a, -b), at(a, -K * b), at(a, 0)), ('Z',)]


def unit2(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    L = math.hypot(dx, dy)
    return (dx / L, dy / L, L) if L > 1e-6 else (0.0, -1.0, 0.0)




TIP_K = 0.93     # fingertip radius, relative to the distal phalanx at the DIP


def seg_radii(dg, k):
    """Radius at the start and the end of bone k: each bone tapers into the next one, so the
    outline runs on without a step at the joints."""
    r = dg['r']
    return r[k], (r[k + 1] if k < 2 else r[2] * TIP_K)


def taper_cmds(p0, r0, p1, r1, caps=(True, True)):
    """Tapered capsule from p0 (radius r0) to p1 (radius r1), as fixed commands. caps=(base, tip):
    without the base cap the outline is open there (it grows out of the palm, or into the bone
    before it); without both caps only the two sides are drawn."""
    ux, uy, L = unit2(p0, p1)
    nx, ny = -uy, ux

    def at(p, a, b):
        return (p[0] + ux * a + nx * b, p[1] + uy * a + ny * b)

    A0, A1, B1, B0 = at(p0, 0, r0), at(p1, 0, r1), at(p1, 0, -r1), at(p0, 0, -r0)
    tip = [('C', at(p1, K * r1, r1), at(p1, r1, K * r1), at(p1, r1, 0)), ('C', at(p1, r1, -K * r1), at(p1, K * r1, -r1), B1)]
    base = [('C', at(p0, -K * r0, -r0), at(p0, -r0, -K * r0), at(p0, -r0, 0)), ('C', at(p0, -r0, K * r0), at(p0, -K * r0, r0), A0)]
    if caps == (True, True):
        return [('M', A0), ('L', A1)] + tip + [('L', B0)] + base + [('Z',)]
    if caps == (False, True):
        return [('M', A0), ('L', A1)] + tip + [('L', B0)]
    return [('M', A0), ('L', A1), ('M', B1), ('L', B0)]


def seg_cmds(dg, k, start=None, caps=(True, True)):
    """Bone k of a digit as a tapered capsule; `start` moves its base along the bone axis (to
    the palm's edge, or back into the palm)."""
    p0, p1 = dg['pts'][k], dg['pts'][k + 1]
    r0, r1 = seg_radii(dg, k)
    if start is not None:
        ux, uy, L = unit2(p0, p1)
        t = ((start[0] - p0[0]) * ux + (start[1] - p0[1]) * uy) / L if L > 1e-6 else 0.0
        r0 = r0 + (r1 - r0) * min(max(t, 0.0), 1.0)
        p0 = start
    return taper_cmds(p0, r0, p1, r1, caps)


def root_open_cmds(dg):
    """The proximal phalanx of a finger in front of the palm, outline only: open at its base, each
    side line starting where _finger_roots says (the knuckle row, or the web at the palm's edge),
    round at the PIP end. Same commands as taper_cmds(..., caps=(False, True))."""
    p0, p1 = dg['pts'][0], dg['pts'][1]
    r0, r1 = seg_radii(dg, 0)
    ux, uy, L = unit2(p0, p1)
    nx, ny = -uy, ux
    sa, sb = dg.get('side_s', (None, None))
    if sa is None:
        return seg_cmds(dg, 0, dg.get('ink_base'), (False, True))

    def side(s, sg):
        r = r0 + (r1 - r0) * min(max(s / L, 0.0), 1.0) if L > 1e-6 else r0
        return (p0[0] + ux * s + nx * r * sg, p0[1] + uy * s + ny * r * sg)

    def at(p, a, b):
        return (p[0] + ux * a + nx * b, p[1] + uy * a + ny * b)
    B1 = at(p1, 0, -r1)
    tip = [('C', at(p1, K * r1, r1), at(p1, r1, K * r1), at(p1, r1, 0)), ('C', at(p1, r1, -K * r1), at(p1, K * r1, -r1), B1)]
    return [('M', side(sa, 1)), ('L', at(p1, 0, r1))] + tip + [('L', side(sb, -1))]


def f0_cmds(dg):
    """Fill of a finger's proximal phalanx in front of the palm: from its knuckle (or from just inside
    the palm's edge when the knuckle projects outside it), round at that end (the knuckle)."""
    return seg_cmds(dg, 0, dg.get('fill_base'))


def knuckle_arc_cmds(dg):
    """The round end of a finger's proximal phalanx behind its knuckle, outline only (drawn with a
    mask that keeps it outside the palm: where a side view puts the knuckle on the palm's edge, the
    knuckle's round silhouette gets its outline; over the palm nothing shows)."""
    p0, p1 = dg['pts'][0], dg['pts'][1]
    if dg.get('fill_base') and dg['trim']:
        p0 = (dg['fill_base'][0], dg['fill_base'][1], 0.0)
    r = seg_radii(dg, 0)[0]
    ux, uy, L = unit2(p0, p1)
    nx, ny = -uy, ux
    pts = [(p0[0] + r * (-ux * math.sin(math.pi * i / 6) - nx * math.cos(math.pi * i / 6)),
            p0[1] + r * (-uy * math.sin(math.pi * i / 6) - ny * math.cos(math.pi * i / 6))) for i in range(7)]
    return [('M', pts[0])] + [('L', q) for q in pts[1:]]


def root_cmds(dg, sc):
    """A finger's root zone: its proximal phalanx, a little inside its outline. The palm's outline
    is left out there, so the back of the hand runs on into the finger (no line across its base)."""
    p0, p1 = dg['pts'][0], dg['pts'][1]
    r0, r1 = seg_radii(dg, 0)
    d = ROOT_INSET * sc
    # flat at the knuckle: below it the palm's own edge goes on (a side view puts the knuckle on it)
    return taper_cmds(p0, max(r0 - d, 0.1), p1, max(r1 - d, 0.1), caps=(False, True)) + [('Z',)]


def cap_cmds(geo, name, wid):
    """Outline of a fist fingertip's round end, as two arcs (same commands every frame). The
    part of the tip that presses on the palm is not outlined: when the palm is seen edge-on, the
    contact lies on the tip's rim, and that stretch of the rim is left out."""
    dg = geo['digits'][name]
    T, D, r = dg['pts'][3], dg['pts'][2], dg['r'][2] * TIP_K + wid / 2
    ux, uy, L = unit2(D, T)
    tu = math.degrees(math.atan2(uy, ux))
    n = geo['palm_n']
    n2 = math.hypot(n[0], n[1])
    alpha = 0.0 * min(max((n2 - 0.88) / 0.12, 0.0), 1.0)
    tc = math.degrees(math.atan2(-n[1], -n[0]))
    rel = (tc - tu + 180) % 360 - 180          # contact direction relative to the tip direction
    lo, hi = -90.0, 90.0
    arcs = [(lo, hi), (hi, hi)]
    if alpha > 0 and rel + alpha > lo and rel - alpha < hi:
        arcs = [(lo, max(lo, rel - alpha)), (min(hi, rel + alpha), hi)]
    cmds = []
    for a0, a1 in arcs:
        pts = [(T[0] + r * math.cos(math.radians(tu + a0 + (a1 - a0) * i / 6)),
                T[1] + r * math.sin(math.radians(tu + a0 + (a1 - a0) * i / 6))) for i in range(7)]
        cmds += [('M', pts[0])] + [('L', q) for q in pts[1:]]
    return cmds


def capsule_cmds(p0, r0, p1, r1, fallback=(0.0, -1.0), bulge=(0.0, 0.0), s=1, open_end=None):
    """Tapered capsule from p0 (radius r0) to p1 (radius r1): straight-ish sides (bulging
    outward by `bulge`), round ends. s=-1 starts on the other side. open_end=f leaves the
    shape open: the outline stops a fraction f along the second side (for contours)."""
    ux, uy, L = unit2(p0, p1)
    if L < 1e-3:
        ux, uy = fallback
    nx, ny = -uy * s, ux * s

    def at(p, a, b):
        return (p[0] + ux * a + nx * b, p[1] + uy * a + ny * b)

    A0, A1, B0, B1 = at(p0, 0, r0), at(p1, 0, r1), at(p0, 0, -r0), at(p1, 0, -r1)
    T1, T0 = at(p1, r1, 0), at(p0, -r0, 0)
    ba, bb = bulge

    def side(P, Q, b, sign, f=1.0):
        Qf = (P[0] + (Q[0] - P[0]) * f, P[1] + (Q[1] - P[1]) * f)
        c1 = (P[0] + (Qf[0] - P[0]) / 3 + nx * b * sign, P[1] + (Qf[1] - P[1]) / 3 + ny * b * sign)
        c2 = (P[0] + (Qf[0] - P[0]) * 2 / 3 + nx * b * sign, P[1] + (Qf[1] - P[1]) * 2 / 3 + ny * b * sign)
        return ('C', c1, c2, Qf)

    cmds = [('M', A0), side(A0, A1, ba, 1),
            ('C', at(p1, K * r1, r1), at(p1, r1, K * r1), T1), ('C', at(p1, r1, -K * r1), at(p1, K * r1, -r1), B1)]
    if open_end is not None:
        return cmds + [side(B1, B0, bb, -1, open_end)]
    return cmds + [side(B1, B0, bb, -1),
                   ('C', at(p0, -K * r0, -r0), at(p0, -r0, -K * r0), T0), ('C', at(p0, -r0, K * r0), at(p0, -K * r0, r0), A0),
                   ('Z',)]


def quad_cmds(a, b, ha, hb):
    """A band from a to b, half-width ha at a and hb at b (cuffs, wrists)."""
    ux, uy, L = unit2(a, b)
    nx, ny = -uy, ux
    return [('M', (a[0] + nx * ha, a[1] + ny * ha)), ('L', (b[0] + nx * hb, b[1] + ny * hb)),
            ('L', (b[0] - nx * hb, b[1] - ny * hb)), ('L', (a[0] - nx * ha, a[1] - ny * ha)), ('Z',)]


def outer_sign(p0, p1, side):
    """Which side of a limb faces away from the body (and up): +1 or -1 for capsule_cmds."""
    ux, uy, _ = unit2(p0, p1)
    return 1 if (-uy) * side - ux * 0.6 >= 0 else -1


def arm_shapes(S, E, Wr, geo, side):
    """Sleeved arm for one frame: upper sleeve (fill + open contour), forearm sleeve, cuff and
    the bit of wrist between cuff and palm. Widths follow the hand: the wrist is as wide as
    the projected wrist of the hand model, so a turned hand gets a narrower wrist."""
    sc = geo['scale']
    ex, ey, ez = [(a[0], a[1]) for a in geo['axes']]
    dx, dy = Wr[0] - E[0], Wr[1] - E[1]
    L = math.hypot(dx, dy)
    hy = math.hypot(*ey)
    hand_dir = (-ey[0] / hy, -ey[1] / hy) if hy > 1e-3 else (0.0, -1.0)
    wgt = min(max((L - 8) / 30, 0.0), 1.0)
    fx = wgt * (dx / L if L > 1e-6 else 0.0) + (1 - wgt) * hand_dir[0]
    fy = wgt * (dy / L if L > 1e-6 else 0.0) + (1 - wgt) * hand_dir[1]
    n = math.hypot(fx, fy) or 1.0
    ux, uy = fx / n, fy / n
    nx, ny = -uy, ux
    hw = max(6.0, math.hypot(10.0 * (nx * ex[0] + ny * ex[1]), 7.0 * (nx * ez[0] + ny * ez[1])))
    f = min(max(L / ARM_FORE, 0.35), 1.0)

    def back(d):
        return (Wr[0] - ux * d, Wr[1] - uy * d)

    grow = 1 + (sc - 1) * 0.5           # nearer the viewer = a little bigger
    r_el = 14.5 * grow
    cuff_r = hw + 2.4 * sc
    sleeve_end = back(13 * f * sc)
    s = outer_sign(S, E, side)
    top = back(14 * f * sc)
    fold = lambda a, b, c, d: [('M', (top[0] - ux * a + nx * b * cuff_r, top[1] - uy * a + ny * b * cuff_r)),
                               ('L', (top[0] - ux * c + nx * d * cuff_r, top[1] - uy * c + ny * d * cuff_r))]
    folds = fold(1.5, 0.8, 8 * f, 0.28) + fold(2.2, 0.02, 10 * f, -0.5)
    parts = [('cap', S, 18.2, E, r_el + 0.6), ('cap', E, r_el, sleeve_end, cuff_r + 0.8),
             ('poly', [c[1] for c in quad_cmds(back(5 * f * sc), back(14 * f * sc), cuff_r, cuff_r + 0.4)[:4]]),
             ('poly', [c[1] for c in quad_cmds((Wr[0] + ux * 4 * sc, Wr[1] + uy * 4 * sc), back(8 * f * sc), hw, hw + 0.4)[:4]])]
    return {
        'parts': parts,
        'folds': rpath(folds),
        'up': rpath(capsule_cmds(S, 18.2, E, r_el + 0.6, bulge=(1.8, 1.0))),
        'upline': rpath(capsule_cmds(S, 18.2, E, r_el + 0.6, bulge=(1.8, 1.0), s=s, open_end=0.82)),
        'fo': rpath(capsule_cmds(E, r_el, sleeve_end, cuff_r + 0.8, fallback=(ux, uy), bulge=(1.0, 1.0))),
        'cuff': rpath(quad_cmds(back(5 * f * sc), back(14 * f * sc), cuff_r, cuff_r + 0.4)),
        'wrist': rpath(quad_cmds((Wr[0] + ux * 4 * sc, Wr[1] + uy * 4 * sc), back(8 * f * sc), hw, hw + 0.4)),
    }


def centre(pts):
    return (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))


def base_trim(pts, sc):
    """The proximal phalanx minus the part inside the palm: its outline starts at the palm's
    edge, so a finger in front of the palm grows out of it."""
    ux, uy, L = unit2(pts[0], pts[1])
    d = min(3.4 * sc, L * 0.5)
    return [(pts[0][0] + ux * d, pts[0][1] + uy * d), pts[1]]


def thenar_cmds(pts, sc, mode='fill', centre=(0.0, 0.0)):
    """The thumb's fleshy base (its metacarpal inside the palm): a tapered mound from the
    wrist end (CMC) to the thumb knuckle. mode 'outer' = its silhouette edge (away from the
    palm centre), 'inner' = the soft crease on the palm side (the life line)."""
    r0, r1 = THENAR[0] * sc, THENAR[1] * sc
    p0, p1 = pts[0], pts[1]
    if mode == 'fill':
        return capsule_cmds(p0, r0, p1, r1)
    ux, uy, L = unit2(p0, p1)
    nx, ny = -uy, ux
    mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
    g = 1 if nx * (mx - centre[0]) + ny * (my - centre[1]) > 0 else -1
    nx, ny = nx * g, ny * g
    if mode == 'outer':
        return [('M', (p0[0] + nx * r0, p0[1] + ny * r0)), ('L', (p1[0] + nx * r1, p1[1] + ny * r1))]
    a = (p1[0] - nx * r1 * 0.8, p1[1] - ny * r1 * 0.8)
    b = (p0[0] - nx * r0 * 0.55 + ux * r0 * 0.2, p0[1] - ny * r0 * 0.55 + uy * r0 * 0.2)
    c = ((a[0] + b[0]) / 2 - nx * 2.6 * sc, (a[1] + b[1]) / 2 - ny * 2.6 * sc)
    return [('M', a), ('Q', c, b)]


def arrow_paths(sign):
    """Arrows are either drawn by hand ('d') or follow a hand's path ('trail'), shifted by 'offset'."""
    out = []
    for a in sign.get('arrows', []):
        if 'd' in a:
            out.append(a)
            continue
        if 'ripples' in a:
            # Arcs around a fingertip that points at the viewer, clear of the hand below it.
            cx, cy = a['ripples']
            for r in (14, 21):
                for a0, a1 in ((-40, 35), (-165, -110)):
                    x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
                    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
                    sweep = 1 if a1 > a0 else 0
                    out.append({'d': f'M {num(x0)} {num(y0)} A {r} {r} 0 0 {sweep} {num(x1)} {num(y1)}', 'plain': True})
            continue
        if 'twist' in a:
            # A curved two-headed arrow around the wrist: the hand turns on the forearm axis.
            hand = a['twist']
            arm = sign['hands'][hand]
            pose = pose_at(sign['keys'], a['at'], hand, arm == 'left')
            geo = hand_geometry(pose, arm == 'left')
            wx, wy = geo['wrist']
            ex, ey = solve_elbow(SHOULDER[arm], geo['wrist'], pose['depth'], SIDE[arm], pose.get('pole'))
            L = math.hypot(ex - wx, ey - wy) or 1
            ux, uy = (ex - wx) / L, (ey - wy) / L
            vx, vy = -uy, ux
            rx, ry = a['r']
            cx, cy = wx + ux * a.get('drop', 0), wy + uy * a.get('drop', 0)
            pts = [(cx + vx * rx * math.cos(t) + ux * ry * math.sin(t), cy + vy * rx * math.cos(t) + uy * ry * math.sin(t))
                   for t in [math.radians(15 + 150 * i / 12) for i in range(13)]]
            out.append({'d': poly(pts), 'both': True})
            continue
        t0, t1 = a['from'], a['to']
        mirror = sign['hands'][a['trail']] == 'left'
        pts = [hand_geometry(pose_at(sign['keys'], t0 + (t1 - t0) * i / 24, a['trail'], mirror), mirror)['wrist']
               for i in range(25)]
        dx, dy = a.get('offset', (0, 0))
        pts = [(x + dx, y + dy) for x, y in pts]
        trim = a.get('trim', 0.12)
        k = max(1, round(len(pts) * trim))
        out.append({'d': poly(pts[k:len(pts) - k]), 'both': a.get('both', False)})
    return out


# ---- fragments: a digit that would show only as a small piece cut off from the hand, or only as
# slivers between nearer parts, is left out of that frame (hidden cleanly instead of floating); a
# digit that shows but also peeks out somewhere else as a sliver gets that piece masked out.
# Decided on a small label raster of the hand, painted in the same order as sign_svg draws it.
FRAG_PX = 3.6        # narrowest piece of a digit worth drawing, in screen pixels at phone scale (3 px, with a margin)
FRAG_SHOWN = 0.33    # a digit cut off from the hand is drawn only when at least this much of it shows
FRAG_OCCLUDED = 0.2  # ...or this much, when what hides the rest of it is a nearer finger
FRAG_SPECK = 2.0     # pieces smaller than this (phone px^2) are left alone: they do not read as anything
SIGN_PHONE_PX = 360.0   # a sign drawing on a phone is about this wide
PICTURE_PHONE_PX = 150.0
RASTER_K = 2.0       # raster pixels per phone pixel
LAB = {'palm': 2, 'web': 3, 'thumb': 5, 'index': 6, 'middle': 7, 'ring': 8, 'pinky': 9}


def _capsule_poly(a, ra, b, rb, n=8):
    """A tapered capsule as a convex polygon (n points per round end)."""
    ux, uy, L = unit2(a, b)
    nx, ny = -uy, ux
    out = []
    for c, r, sg in ((b, rb, 1), (a, ra, -1)):
        for i in range(n + 1):
            t = math.pi * i / n
            # half circle around the end, from the +n side to the -n side (b) or back (a)
            ca, sa = math.cos(t), math.sin(t)
            vx, vy = (nx * ca + ux * sa, ny * ca + uy * sa) if sg > 0 else (-nx * ca - ux * sa, -ny * ca - uy * sa)
            out.append((c[0] + vx * r, c[1] + vy * r))
    return out


class _Raster:
    """Labels (what is on top) and ink owners for one hand, on a coarse pixel grid."""

    def __init__(self, x0, y0, w, h, s):
        self.x0, self.y0, self.s = x0, y0, s
        self.W, self.H = max(2, int(w * s) + 1), max(2, int(h * s) + 1)
        self.lab = bytearray(self.W * self.H)
        self.own = bytearray(self.W * self.H)

    def spans(self, poly):
        """Row spans (y, x0, x1) of a polygon (even-odd), in pixel coordinates."""
        P = [((p[0] - self.x0) * self.s, (p[1] - self.y0) * self.s) for p in poly]
        ys = [p[1] for p in P]
        ya, yb = max(0, int(math.ceil(min(ys) - 0.5))), min(self.H - 1, int(math.floor(max(ys) - 0.5)))
        out = []
        for y in range(ya, yb + 1):
            yc = y + 0.5
            xs = []
            for i in range(len(P)):
                (x1, y1), (x2, y2) = P[i - 1], P[i]
                if (y1 > yc) != (y2 > yc):
                    xs.append(x1 + (yc - y1) * (x2 - x1) / (y2 - y1))
            xs.sort()
            for j in range(0, len(xs) - 1, 2):
                xa, xb = max(0, int(math.ceil(xs[j] - 0.5))), min(self.W - 1, int(math.floor(xs[j + 1] - 0.5)))
                if xb >= xa:
                    out.append((y, xa, xb))
        return out

    def paint(self, poly, code, owner=0, only=None, outside=None):
        for y, xa, xb in self.spans(poly):
            o = y * self.W
            if outside is not None:
                for i in range(o + xa, o + xb + 1):
                    if not outside[i]:
                        self.lab[i] = code
                        self.own[i] = owner
            elif only is None:
                self.lab[o + xa:o + xb + 1] = bytes([code]) * (xb - xa + 1)
                if code == 1:
                    self.own[o + xa:o + xb + 1] = bytes([owner]) * (xb - xa + 1)
            else:
                for i in range(o + xa, o + xb + 1):
                    if self.lab[i] == only[0] and self.own[i] == only[1]:
                        self.lab[i] = code

    def count(self, poly):
        return sum(xb - xa + 1 for _, xa, xb in self.spans(poly))


def _grow(poly, d):
    """A convex-ish polygon pushed out by d from its centroid (outline width)."""
    cx, cy = sum(p[0] for p in poly) / len(poly), sum(p[1] for p in poly) / len(poly)
    out = []
    for i in range(len(poly)):
        a, b, c = poly[i - 1], poly[i], poly[(i + 1) % len(poly)]
        ex, ey = c[0] - a[0], c[1] - a[1]
        L = math.hypot(ex, ey) or 1.0
        nx, ny = ey / L, -ex / L
        if nx * (b[0] - cx) + ny * (b[1] - cy) < 0:
            nx, ny = -nx, -ny
        out.append((b[0] + nx * d, b[1] + ny * d))
    return out


def _draw_parts(geo):
    """The hand's filled shapes in drawing order (as sign_svg paints them): list of (rank, label,
    [polygons]); each polygon is painted with its outline (ink) first, then its fill."""
    digs, parts = geo['digits'], []
    th = digs['thumb']
    sc = geo['scale']
    web = [(q[0], q[1]) for q in geo['web']]
    thenar = _capsule_poly(th['pts'][0], THENAR[0] * sc, th['pts'][1], THENAR[1] * sc)
    for li, layer in enumerate(('back', 'front')):
        want = layer == 'front'
        for (name, g), slot in geo['order'][layer].items():
            dg = digs[name]
            if dg.get('hidden'):
                continue
            polys = []
            if name == 'thumb' and not want and not th['front'][0] and any(dg['group'][k] == g and not dg['front'][k] for k in dg['segs']):
                polys += [('web', web), ('web', thenar)]
            for k in dg['segs']:
                if dg['front'][k] == want and dg['group'][k] == g:
                    r0, r1 = seg_radii(dg, k)
                    a = dg['pts'][k]
                    if k == 0 and want and name != 'thumb' and dg.get('fill_base') and dg['trim']:
                        a = (dg['fill_base'][0], dg['fill_base'][1], 0.0)        # f0 starts there
                        cap = _capsule_poly(a, r0, dg['pts'][k + 1], r1)
                        # its outline is open at the base, except outside the palm (knuckle_arc_cmds)
                        polys.append((name, cap, cap[:10] + cap[-1:], _grow(cap, LINE)))
                        continue
                    polys.append((name, _capsule_poly(a, r0, dg['pts'][k + 1], r1)))
            if name != 'thumb' and dg['tight'] and dg['front'][0] == want and dg['group'][0] == g:
                polys.append((name, list(dg['curl'])))
            if name != 'thumb' and dg['tight'] and dg['front'][2] == want and dg['group'][2] == g:
                # the round rim of a fist fingertip (cap_cmds): a full-width line around the tip
                T, rt = dg['pts'][3], dg['r'][2] * TIP_K + LINE
                polys.append((name, None, [(T[0] + rt * math.cos(math.pi * i / 8), T[1] + rt * math.sin(math.pi * i / 8))
                                           for i in range(16)]))
            parts.append(((li * 4, slot), polys))
    if not th['front'][0] and not th.get('hidden'):
        parts.append(((1, 0), [('web', web), ('web', thenar)]))
    parts.append(((2, 0), [('palm', [(p[0], p[1]) for p in geo['palm_curve']])]))
    if th['front'][0]:
        parts.append(((3, 0), [('web', web), ('web', thenar)]))
    return sorted(parts, key=lambda p: p[0])


def _components(lab, W, H, code):
    """4-connected pieces of the pixels labelled `code` (jumps between them with bytes.find)."""
    seen, comps = bytearray(W * H), []
    key = bytes([code])
    i = lab.find(key)
    while i >= 0:
        if not seen[i]:
            stack, comp = [i], []
            seen[i] = 1
            while stack:
                j = stack.pop()
                comp.append(j)
                x = j % W
                for k in (j - 1 if x else -1, j + 1 if x < W - 1 else -1, j - W, j + W):
                    if 0 <= k < W * H and not seen[k] and lab[k] == code:
                        seen[k] = 1
                        stack.append(k)
            comps.append(comp)
        i = lab.find(key, i + 1)
    return comps


def _touches(comp, lab, W, codes):
    n = len(lab)
    for j in comp:
        x = j % W
        for k in (j - 1 if x else -1, j + 1 if x < W - 1 else -1, j - W, j + W):
            if 0 <= k < n and lab[k] in codes:
                return True
    return False


def _solid(comp, W, k):
    """The piece holds a k x k square (it is at least k pixels wide)."""
    cs = set(comp)
    xs = [j % W for j in comp]
    ys = [j // W for j in comp]
    if max(xs) - min(xs) + 1 < k or max(ys) - min(ys) + 1 < k:
        return False
    run = {}
    for j in sorted(comp):          # horizontal runs of length >= k end here
        run[j] = run.get(j - 1, 0) + 1 if (j - 1) in cs and (j % W) else 1
    ok = {j for j, r in run.items() if r >= k}
    col = {}
    for j in sorted(ok):            # ...stacked k rows high
        col[j] = col.get(j - W, 0) + 1
        if col[j] >= k:
            return True
    return False


def digit_pieces(geo, unit_px):
    """Which parts of each digit's skin show in the drawing, as pieces (label raster in drawing
    order). Returns name -> dict(total, shown, pieces=[(n_px, joined, solid, points, by_digits)])."""
    sc = geo['scale']
    s = unit_px * RASTER_K
    pts = [(p[0], p[1]) for p in geo['palm']] + [(q[0], q[1]) for dg in geo['digits'].values() for q in dg['pts']]
    pad = 12 * sc
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    R = _Raster(min(xs) - pad, min(ys) - pad, max(xs) - min(xs) + 2 * pad, max(ys) - min(ys) + 2 * pad, s)
    grow = LINE
    parts = _draw_parts(geo)
    palm_mask = bytearray(R.W * R.H)
    for y, xa, xb in R.spans([(p[0], p[1]) for p in geo['palm_curve']]):
        palm_mask[y * R.W + xa:y * R.W + xb + 1] = b'\x01' * (xb - xa + 1)
    tight_codes = {LAB[n] for n in ('index', 'middle', 'ring', 'pinky') if geo['digits'][n]['tight']}
    run_done = set()
    for rank, polys in parts:
        is_tight = polys and all(LAB[e[0]] in tight_codes for e in polys)
        if is_tight and rank[0] not in run_done:
            # a run of fist folds: one outer outline under all of them, thin lines between them
            run_done.add(rank[0])
            for r2, p2 in parts:
                if r2[0] == rank[0] and p2 and all(LAB[e[0]] in tight_codes for e in p2):
                    for e in p2:
                        if e[1] is not None:
                            R.paint(_grow(e[2] if len(e) > 2 else e[1], grow), 1, LAB[e[0]])
        for e in polys:
            if len(e) > 3:      # the knuckle's round end: outline only outside the palm
                R.paint(e[3], 1, LAB[e[0]], outside=palm_mask)
            ink = e[2] if len(e) > 2 else e[1]
            R.paint(ink if e[1] is None else _grow(ink, THIN if is_tight else grow), 1, LAB[e[0]])
        for e in polys:
            if e[1] is not None:
                R.paint(e[1], LAB[e[0]])
        if rank == (2, 0):          # the palm's outline is left out where a finger grows out of the hand
            for name in ('index', 'middle', 'ring', 'pinky'):
                dg = geo['digits'][name]
                if dg.get('hidden') or dg['front'][0]:
                    continue
                r0, r1 = seg_radii(dg, 0)
                band = _capsule_poly(dg['pts'][0], r0 - ROOT_INSET * sc, dg['pts'][1], r1 - ROOT_INSET * sc)
                R.paint(band[:10] + band[-1:], LAB[name], only=(1, LAB['palm']))     # flat at the knuckle
            th = geo['digits']['thumb']
            if not th['front'][0] and not th.get('hidden'):
                for poly in ([(q[0], q[1]) for q in geo['web']],
                             _capsule_poly(th['pts'][0], THENAR[0] * sc, th['pts'][1], THENAR[1] * sc)):
                    R.paint(poly, LAB['web'], only=(1, LAB['palm']))
    W, H, lab, own = R.W, R.H, R.lab, R.own
    k = max(2, int(math.ceil(FRAG_PX * RASTER_K)))
    min_px = FRAG_SPECK * RASTER_K * RASTER_K
    # the web and thumb mound count as the hand where they touch the palm's skin
    web_ok = any(_touches(c, lab, W, {LAB['palm']}) for c in _components(lab, W, H, LAB['web']))
    tight = [n for n in ('index', 'middle', 'ring', 'pinky') if geo['digits'][n]['tight'] and not geo['digits'][n].get('hidden')]
    groups = [(n, [n]) for n in geo['digits'] if not geo['digits'][n].get('hidden') and (n not in tight or len(tight) < 2)]
    if len(tight) >= 2:
        groups.append(('fist', tight))
    # The opening of a thumb-index ring (OK, F, O): whatever shows through it belongs to a finger
    # behind the ring and is cut off from the rest of that finger.
    ix, th = geo['digits']['index'], geo['digits']['thumb']
    loop = None
    if math.dist(ix['pts'][3][:2], th['pts'][3][:2]) < 1.6 * (ix['r'][2] + th['r'][2]):
        loop = [(q[0], q[1]) for q in ix['pts']] + [(q[0], q[1]) for q in th['pts'][1:][::-1]]
    out = {}
    for gname, members in groups:
        codes = {LAB[n] for n in members}
        if gname == 'fist':
            # The fist is one silhouette: its folds and the thin lines between them, inside the union
            # of the folded fingers (the shared outer outline lies outside it).
            U = _Raster(R.x0, R.y0, 0, 0, s)
            U.W, U.H, U.lab, U.own = W, H, bytearray(W * H), bytearray(W * H)
            for n in members:
                dg = geo['digits'][n]
                for kk in dg['segs']:
                    r0, r1 = seg_radii(dg, kk)
                    U.paint(_capsule_poly(dg['pts'][kk], r0, dg['pts'][kk + 1], r1), 1)
                U.paint(list(dg['curl']), 1)
            G = bytes(10 if U.lab[i] and (lab[i] in codes or (lab[i] == 1 and own[i] in codes)) else 0 for i in range(W * H))
            gcode, sil = 10, U.lab.count(1)
            own_ok = codes
        else:
            G, gcode = lab, LAB[gname]
            dg = geo['digits'][gname]
            sil = 0
            for kk in dg['segs']:
                r0, r1 = seg_radii(dg, kk)
                sil += R.count(_capsule_poly(dg['pts'][kk], r0, dg['pts'][kk + 1], r1))
            own_ok = {gcode}
        allc = _components(G, W, H, gcode)
        comps = [c for c in allc if len(c) >= min_px]
        body = {LAB['palm']} | ({LAB['web']} if (gname in ('thumb', 'index', 'fist')) and web_ok else set())
        # pieces separated only by the digit's own outline belong together
        grp = bytearray(W * H)
        gid = 0
        joined_g = set()
        for c in allc:
            if grp[c[0]]:
                continue
            gid += 1
            st = [c[0]]
            grp[c[0]] = gid
            while st:
                j = st.pop()
                x = j % W
                for kk in (j - 1 if x else -1, j + 1 if x < W - 1 else -1, j - W, j + W):
                    if 0 <= kk < W * H and not grp[kk] and (G[kk] == gcode or (lab[kk] == 1 and own[kk] in own_ok)):
                        grp[kk] = gid
                        st.append(kk)
        for c in allc:
            if grp[c[0]] not in joined_g and _touches(c, lab, W, body):
                joined_g.add(grp[c[0]])
        pieces = []
        for c in comps:
            joined = grp[c[0]] in joined_g
            near = {}
            for j in c[::2]:
                x, y = j % W, j // W
                for dx in (-2, 0, 2):
                    for dy in (-2, 0, 2):
                        if 0 <= x + dx < W and 0 <= y + dy < H:
                            q = j + dx + dy * W
                            if G[q] != gcode:
                                o = own[q] if lab[q] == 1 else lab[q]
                                if o and o not in codes:
                                    near[o] = near.get(o, 0) + 1
            hand = near.get(LAB['palm'], 0) + near.get(LAB['web'], 0)
            by_digits = hand < 0.25 * max(sum(near.values()), 1)
            P = [((j % W + 0.5) / s + R.x0, (j // W + 0.5) / s + R.y0) for j in c]
            if loop and gname not in ('index', 'thumb') and sum(1 for q in P[::3] if inside(q, loop)) > 0.6 * len(P[::3]):
                joined, by_digits = False, True
            if gname == 'fist':     # the fist: its folds' skin, with a margin (its thin lines are not modelled)
                skin = [j for j in c if lab[j] in codes]
                ok = bool(skin) and _solid(skin, W, k + int(2 * RASTER_K))
            else:
                ok = _solid(c, W, k)
            pieces.append((len(c), joined, ok, P, by_digits))
        out[gname] = {'total': max(sil, 1), 'shown': G.count(bytes([gcode])), 'pieces': pieces, 'h': 1.0 / s,
                      'members': members}
    return out


def _patch(points, margin):
    """An ellipse (centre, half axes, angle) around a set of points, grown by `margin`."""
    n = len(points)
    cx, cy = sum(p[0] for p in points) / n, sum(p[1] for p in points) / n
    sxx = sum((p[0] - cx) ** 2 for p in points) / n
    syy = sum((p[1] - cy) ** 2 for p in points) / n
    sxy = sum((p[0] - cx) * (p[1] - cy) for p in points) / n
    th = 0.5 * math.atan2(2 * sxy, sxx - syy)
    c, s = math.cos(th), math.sin(th)
    us = [((p[0] - cx) * c + (p[1] - cy) * s, -(p[0] - cx) * s + (p[1] - cy) * c) for p in points]
    a = max(abs(u) for u, _ in us) + margin
    b = max(abs(v) for _, v in us) + margin
    return (cx, cy, a * 1.05, b * 1.05, th)


def _in_patch(p, e):
    cx, cy, a, b, th = e
    c, s = math.cos(th), math.sin(th)
    u, v = (p[0] - cx) * c + (p[1] - cy) * s, -(p[0] - cx) * s + (p[1] - cy) * c
    return (u / a) ** 2 + (v / b) ** 2 < 1.0


MAX_PATCHES = 2


def hide_fragments(geo, unit_px):
    """Leaves out what would show only as fragments. A digit with no piece that is wide enough
    (FRAG_PX) and either grows out of the hand or belongs to a digit that mostly shows
    (FRAG_SHOWN; FRAG_OCCLUDED when nearer fingers hide the rest) is hidden whole. A digit that does
    show, but also peeks out somewhere else as a sliver or as a small piece cut off from it, gets
    that piece masked out (an ellipse patch), so only its main part is drawn. Fingers folded into
    a fist are judged together (the fist is one silhouette with thin lines between its folds) and
    are hidden or patched together."""
    for _ in range(3):          # hiding one digit can uncover another's sliver: look again
        changed = False
        for name, info in digit_pieces(geo, unit_px).items():
            members = [geo['digits'][n] for n in info['members']]
            for dg in members:
                dg['shown_frac'] = info['shown'] / info['total']
            pcs = info['pieces']
            main = [p for p in pcs if p[2] and p[1]]
            solid = [p for p in pcs if p[2]]
            if solid and not main:
                top = max(solid, key=lambda p: p[0])
                frac = top[0] / info['total']
                if frac >= FRAG_SHOWN or (top[4] and frac >= FRAG_OCCLUDED):
                    main.append(top)
            if not main:
                if pcs or info['shown'] or name != 'fist':
                    for dg in members:
                        if not dg.get('hidden'):
                            dg['hidden'] = True
                            changed = True
                continue
            # a big piece that only a nearer finger cuts off (a finger lying across another) still reads
            frags = [p for p in pcs if not any(p is m for m in main) and not (p[4] and p[0] >= FRAG_OCCLUDED * info['total'])]
            if name == 'fist':
                # a fist that shows is drawn whole (its folds share one outline); only slivers of it
                # peeking out beside a nearer digit are masked, for all its folds at once
                frags = [p for p in frags if not p[2]]
            keep = [q for m in main for q in m[3][::2]]
            patches = []
            for fr in sorted(frags, key=lambda p: -p[0]):
                e = None
                for margin in (1.6 * LINE, 1.0 * LINE, 0.5 * LINE):
                    cand = _patch(fr[3], margin)
                    if not any(_in_patch(q, cand) for q in keep):
                        e = cand
                        break
                if e is None:
                    continue
                if len(patches) == MAX_PATCHES:
                    near = min(range(len(patches)), key=lambda i: math.dist(patches[i][:2], e[:2]))
                    pts = patches[near][5] + fr[3]
                    m = _patch(pts, 1.0 * LINE)
                    if not any(_in_patch(q, m) for q in keep):
                        patches[near] = m + (pts,)
                    continue
                patches.append(e + (fr[3],))
            for dg in members:          # the folds of a fist share their patches
                dg['patches'] = [p[:5] for p in patches]
        if not changed:
            break


def frames_for(sign):
    n = round(sign['dur'] * FPS)
    times = [sign['dur'] * i / n for i in range(n + 1)]
    frames = []
    for t in times:
        frame = {'arms': {}, 'hands': [], 'armgeo': {}}
        for i, arm in enumerate(sign['hands']):
            pose = pose_at(sign['keys'], t, i, mirror=(arm == 'left'))
            geo = hand_geometry(pose, mirror=(arm == 'left'))
            elbow = solve_elbow(SHOULDER[arm], geo['wrist'], pose['depth'], SIDE[arm], pose.get('pole'))
            frame['points'] = frame.get('points', []) + [(p[0], p[1]) for p in geo['palm']] + [
                (q[0], q[1]) for d in geo['digits'].values() for q in d['pts']]
            frame['arms'][arm] = (SHOULDER[arm], elbow, geo['wrist'])
            frame['armgeo'][arm] = arm_shapes(SHOULDER[arm], elbow, geo['wrist'], geo, SIDE[arm])
            frame['hands'].append(geo)
        frames.append(frame)
    # Digits that would show only as fragments are left out (decided at phone scale).
    if sign.get('hand_only'):
        h0 = frames[0]['hands'][0]
        pts = [(q[0], q[1]) for q in h0['palm']] + [(q[0], q[1]) for dd in h0['digits'].values() for q in dd['pts']]
        size = max(max(p[0] for p in pts) - min(p[0] for p in pts), max(p[1] for p in pts) - min(p[1] for p in pts)) + 18
        unit_px = sign.get('phone_px', PICTURE_PHONE_PX) / size
    else:
        unit_px = SIGN_PHONE_PX / float(view_box(sign, frames).split()[2])
    if sign.get('hand_only'):           # one still pose: decide once, the frames are the same
        hide_fragments(frames[0]['hands'][0], unit_px)
        for f in frames[1:]:
            for key in ('hidden', 'patches', 'shown_frac'):
                for name, dg in frames[0]['hands'][0]['digits'].items():
                    if key in dg:
                        f['hands'][0]['digits'][name][key] = dg[key]
    else:
        for f in frames:
            for geo in f['hands']:
                hide_fragments(geo, unit_px)
    # A digit shown for only one or two frames between frames where it is hidden would flicker.
    for i in range(len(sign['hands'])):
        for name in DIGITS:
            seq = [bool(f['hands'][i]['digits'][name].get('hidden')) for f in frames]
            # (only shown runs are merged: a digit hidden for a frame or two is mostly covered then anyway)
            a = 0
            while a < len(seq):
                b = a
                while b < len(seq) and seq[b] == seq[a]:
                    b += 1
                if not seq[a] and b - a <= 2 and 0 < a and b < len(seq) and all(
                        frames[k]['hands'][i]['digits'][name].get('shown_frac', 1.0) < 0.3 for k in range(a, b)):
                    for k in range(a, b):
                        seq[k] = True
                a = b
            for f, v in zip(frames, seq):
                f['hands'][i]['digits'][name]['hidden'] = v
    # Fingers whose neighbour is now hidden start their side lines again from the knuckle row.
    for f in frames:
        for geo in f['hands']:
            _finger_roots(geo)
    # Small skin lines that would show for only one or two frames read as a flicker: drop them.
    for i in range(len(sign['hands'])):
        for name in DIGITS:
            for key in ('crease_vis', 'wrinkle_vis'):
                for j in (0, 1):
                    seq = [f['hands'][i]['digits'][name][key][j] for f in frames]
                    a = 0
                    while a < len(seq):
                        b = a
                        while b < len(seq) and seq[b] == seq[a]:
                            b += 1
                        if seq[a] and b - a <= 2 and b - a < len(seq):
                            for k in range(a, b):
                                frames[k]['hands'][i]['digits'][name][key][j] = False
                        a = b
    return frames


# ---- silhouettes: what a hand or a sleeve covers in the picture (used for the earrings)
EARRINGS = {'right': (158.5, 120.5), 'left': (241.5, 120.5)}   # small gold hoops; signer's right = viewer's left
EARRING_R, EARRING_W = 4.6, 1.9
EARRING_HIDE = 0.85  # a hoop covered more than this by a hand or a sleeve is left out: the sliver beside the hand
                     # would read as a stray blob. Otherwise it is drawn (and the hand simply passes in front of it).


def hand_parts(geo):
    """The drawn silhouette of one hand: palm, web, thumb mound and every bone (screen, 2D)."""
    sc = geo['scale']
    out = [('poly', [(p[0], p[1]) for p in geo['palm_curve']]), ('poly', [(p[0], p[1]) for p in geo['web']])]
    for name, dg in geo['digits'].items():
        pts = dg['pts']
        for k in range(3):
            if name == 'thumb' and k == 0:
                out.append(('cap', pts[0], THENAR[0] * sc, pts[1], THENAR[1] * sc))
            else:
                r0, r1 = seg_radii(dg, k)
                out.append(('cap', pts[k], r0, pts[k + 1], r1))
    return out


def parts_sdf(parts, p):
    """Signed distance from p to the union of parts (negative inside)."""
    best = float('inf')
    for part in parts:
        if part[0] == 'poly':
            pl = part[1]
            dd = min(_closest(p, pl[i - 1], pl[i])[1] for i in range(len(pl)))
            v = -dd if inside(p, pl) else dd
        else:
            _, a, r0, b, r1 = part
            t, dd = _closest(p, a, b)
            v = dd - (r0 + (r1 - r0) * t)
        best = min(best, v)
    return best


def earring_cover(frame, side):
    """How much of one hoop (0..1) the hands and sleeves of this frame cover, outlines included."""
    parts = [q for geo in frame['hands'] for q in hand_parts(geo)]
    parts += [q for ag in frame['armgeo'].values() for q in ag['parts']]
    cx, cy = EARRINGS[side]
    pts = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)))
           for a in range(0, 360, 12) for r in (EARRING_R - EARRING_W / 2 + 0.2, EARRING_R, EARRING_R + EARRING_W / 2 - 0.2)]
    return sum(1 for q in pts if parts_sdf(parts, q) < LINE * 0.5) / len(pts)


def earring_states(frames):
    """Per side, per frame: is the hoop drawn? Hidden only while a hand or sleeve covers most of
    it; runs of one or two frames are merged into their neighbours, so it never flickers."""
    out = {}
    for side in EARRINGS:
        seq = [earring_cover(f, side) <= EARRING_HIDE for f in frames]
        for state in (False, True):
            a = 0
            while a < len(seq):
                b = a
                while b < len(seq) and seq[b] == seq[a]:
                    b += 1
                if seq[a] == state and b - a <= 2 and b - a < len(seq):
                    for k in range(a, b):
                        seq[k] = not state
                a = b
        out[side] = seq
    return out


def path_points(d):
    """Coordinates in an SVG path (absolute commands only); for arcs, just the end points."""
    pts = []
    for cmd, args in re.findall(r'([MLQCTSA])([^MLQCTSAZz]*)', d):
        nums = [float(v) for v in re.findall(r'-?\d+(?:\.\d+)?', args)]
        if cmd == 'A':
            pts += [(nums[i + 5], nums[i + 6]) for i in range(0, len(nums) - 6, 7)]
        else:
            pts += list(zip(nums[0::2], nums[1::2]))
    return pts


def view_box(sign, frames):
    """Smallest 4:3 window (inside the 400x300 scene) that holds the head, both hands in every
    frame, the arrows and the contact marks, with some margin."""
    xs, ys = [156, 244], [42, 148]
    for f in frames:
        for x, y in f['points']:
            xs.append(x)
            ys.append(y)
    for a in arrow_paths(sign):
        for x, y in path_points(a['d']):
            xs.append(x)
            ys.append(y)
    for x, y, _ in sign.get('marks', []):
        xs += [x - 12, x + 12]
        ys += [y - 12, y + 12]
    pad = 16
    x0, x1, y0, y1 = min(xs) - pad, max(xs) + pad, min(ys) - pad, max(ys) + pad
    w, h = max(x1 - x0, 250), y1 - y0
    w, h = max(w, h * 4 / 3), max(h, w * 3 / 4)
    w, h = min(w, W), min(h, H)
    cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2
    x0 = min(max(cx - w / 2, 0), W - w)
    y0 = min(max(cy - h / 2, 0), H - h)
    return f'{num(x0)} {num(y0)} {num(w)} {num(h)}'


def _times(k, n):
    s = f'{k / n:.4f}'.rstrip('0').rstrip('.')
    return s if s else '0'


class Anim:
    """Collects one attribute's per-frame values; emits a static value or a SMIL animation.
    Runs of identical frames are collapsed with keyTimes (same motion, much smaller file)."""

    def __init__(self, dur, frame):
        self.dur, self.frame = dur, frame

    def attr(self, name, values, discrete=False):
        if self.frame is not None:
            return f' {name}="{values[self.frame]}"', ''
        if all(v == values[0] for v in values):
            return f' {name}="{values[0]}"', ''
        n = len(values) - 1
        if discrete:
            keep = [0] + [i for i in range(1, n + 1) if values[i] != values[i - 1]]
        else:
            keep = [i for i in range(n + 1) if i in (0, n) or values[i] != values[i - 1] or values[i] != values[i + 1]]
        mode = ' calcMode="discrete"' if discrete else ''
        kt = ''
        if discrete or len(keep) < n + 1:
            kt = f' keyTimes="{";".join(_times(i, n) for i in keep)}"'
        return (f' {name}="{values[0]}"',
                f'<animate attributeName="{name}" dur="{num(self.dur)}s" repeatCount="indefinite"{mode}{kt} values="{";".join(values[i] for i in keep)}"/>')


# ---------------------------------------------------------------- the signer (static)
# Regina, drawn as a younger, fresh version of herself: long dark-brown hair falling past the
# shoulders, a big warm smile, small gold hoops, a chambray button-up shirt. The face keeps
# only the lines that build features (brows, eyes, nose, mouth): no lines under the eyes,
# no nose-to-mouth folds, no brackets at the mouth corners, no neck line. Landmarks (chin 143, mouth
# 125, forehead 70) match SPOT.
def torso_path():
    lx, rx, sy = SHOULDER['right'][0], SHOULDER['left'][0], SHOULDER['right'][1]
    sh, top = DELTOID * K, sy - DELTOID
    # Shoulders: the deltoid is an arc around the shoulder joint (the sleeve's round top sits
    # on it); below it the torso side starts at the armpit, inside the hanging arm.
    left = [('M', (lx, top)),
            ('C', (lx - sh, top), (lx - DELTOID, sy - sh), (lx - DELTOID, sy)),
            ('C', (lx - DELTOID, sy + 3.3), (lx - DELTOID + 0.9, sy + 6.6), (lx - DELTOID * 0.866, sy + 9.5)),
            ('L', (lx + 3, sy + 21)),
            ('C', (lx + 4, 246), (lx + 5, 276), (lx + 6, 306))]
    right = []          # the same side mirrored, walked backwards
    pts = [c[-1] for c in left]
    for i in range(len(left) - 1, 0, -1):
        c = left[i]
        mir = lambda q: (400 - q[0], q[1])
        start = mir(pts[i - 1])
        right.append(('C', mir(c[2]), mir(c[1]), start) if c[0] == 'C' else ('L', start))
    def fmt(cmds):
        return ''.join(c[0] + ' '.join(f'{num(q[0])} {num(q[1])}' for q in c[1:]) for c in cmds)
    torso = ('M184 157C176 166 158 172 ' + fmt(left)[1:] + f'L{num(400 - pts[-1][0])} {num(pts[-1][1])}'
             + fmt(right) + 'C242 172 224 166 216 157L200 195Z')
    return torso


def body_svg(earring_anim=None):
    """earring_anim: side -> (visibility attribute, SMIL child) for a hoop a hand covers at times."""
    ea = earring_anim or {}

    def hoop(side):
        cx, cy = EARRINGS[side]
        attr, kids = ea.get(side, ('', ''))
        el = f'<circle cx="{num(cx)}" cy="{num(cy)}" r="{num(EARRING_R)}" fill="none" stroke="{GOLD}" stroke-width="{num(EARRING_W)}"{attr}'
        return el + (f'>{kids}</circle>' if kids else '/>')
    L, B = LINE_SKIN, BODY_LINE
    sh = (DELTOID * K)
    lx, rx, sy = SHOULDER['right'][0], SHOULDER['left'][0], SHOULDER['right'][1]
    top = sy - DELTOID
    torso = torso_path()
    return f'''
  <g id="body"><g stroke-linecap="round" stroke-linejoin="round">
    <path d="M200 40C233 40 252 61 251 93C250 108 252 120 256 131C261 144 266 152 267 165C268 176 272 184 271 194C270 206 262 214 252 218C254 209 251 202 245 197L155 197C149 202 146 209 148 218C138 214 130 206 129 194C128 184 132 176 133 165C134 152 139 144 144 131C148 120 150 108 149 93C148 61 167 40 200 40Z" fill="{HAIR}"/>
    <path d="M152 112C151 132 146 152 139 170M248 112C249 132 254 152 261 170" fill="none" stroke="{HAIR_MID}" stroke-width="2.4"/>
    <path d="M178 165C180 154 189 146 200 146C211 146 220 154 222 165Z" fill="{SHIRT_DEEP}" stroke="{SHIRT_LINE}" stroke-width="{B}"/>
    <path d="M186 121C187 137 186 151 181 162C176 172 169 182 167 200L233 200C231 182 224 172 219 162C214 151 213 137 214 121Z" fill="{SKIN}" stroke="{L}" stroke-width="{B}"/>
    <path d="M185 128C190 147 210 147 215 128L215 141C210 153 190 153 185 141Z" fill="{SKIN_SHADE}"/>
    <path d="{torso}" fill="{SHIRT}" stroke="{SHIRT_LINE}" stroke-width="{B}"/>
    <path d="M{num(lx + 3)} 214C{num(lx + 4)} 246 {num(lx + 5)} 276 {num(lx + 6)} 306L{num(lx + 19)} 306C{num(lx + 16)} 274 {num(lx + 14)} 244 {num(lx + 14)} 218Z" fill="{SHIRT_SHADE}"/>
    <path d="M{num(rx - 3)} 214C{num(rx - 4)} 246 {num(rx - 5)} 276 {num(rx - 6)} 306L{num(rx - 19)} 306C{num(rx - 16)} 274 {num(rx - 14)} 244 {num(rx - 14)} 218Z" fill="{SHIRT_SHADE}"/>
    <path d="M200 195V306M203.5 198V306" fill="none" stroke="{SHIRT_LINE}" stroke-width="1.1" opacity=".7"/>
    <circle cx="201.8" cy="224" r="2.3" fill="{SHIRT_LIGHT}" stroke="{SHIRT_LINE}" stroke-width="1"/>
    <circle cx="201.8" cy="252" r="2.3" fill="{SHIRT_LIGHT}" stroke="{SHIRT_LINE}" stroke-width="1"/>
    <circle cx="201.8" cy="280" r="2.3" fill="{SHIRT_LIGHT}" stroke="{SHIRT_LINE}" stroke-width="1"/>
    <path d="M187 147C184 156 180 162 172 167L184 194L199.5 189C193 178 189.5 165 187 147Z" fill="{SHIRT_LIGHT}" stroke="{SHIRT_LINE}" stroke-width="{B}"/>
    <path d="M213 147C216 156 220 162 228 167L216 194L200.5 189C207 178 210.5 165 213 147Z" fill="{SHIRT_LIGHT}" stroke="{SHIRT_LINE}" stroke-width="{B}"/>
    <path d="M163 93C156 88 151 95 153 104C155 112 159 117 165 116Z" fill="{SKIN}" stroke="{L}" stroke-width="{B}"/>
    <path d="M237 93C244 88 249 95 247 104C245 112 241 117 235 116Z" fill="{SKIN}" stroke="{L}" stroke-width="{B}"/>
    <path d="M160 97C157 99 157 105 160 108M240 97C243 99 243 105 240 108" fill="none" stroke="{SKIN_DEEP}" stroke-width="1.2"/>
    {hoop('right')}
    {hoop('left')}
    <path d="M200 52C224 52 239 68 239 92C238.6 110 232 123 223.6 132C216 140 208 145 200 145C192 145 184 140 176.4 132C168 123 161.4 110 161 92C161 68 176 52 200 52Z" fill="{SKIN}" stroke="{L}" stroke-width="{B}"/>
    <path d="M238.6 96C238 112 232 123 223.6 132C216 140 208 145 200 145C209.5 141 217 134.5 222.5 126C228 117 232 107 233.4 96Z" fill="{SKIN_SHADE}" opacity=".4"/>
    <ellipse cx="175.5" cy="111" rx="7.5" ry="5" fill="#e17f6b" opacity=".3"/>
    <ellipse cx="224.5" cy="111" rx="7.5" ry="5" fill="#e17f6b" opacity=".3"/>
    <path d="M174.5 87.5C178 82 187 80.5 194.5 83.5C195.5 84.5 195 86 193.8 86C187 84 180 84.5 175.5 88.5ZM225.5 87.5C222 82 213 80.5 205.5 83.5C204.5 84.5 205 86 206.2 86C213 84 220 84.5 224.5 88.5Z" fill="{HAIR_MID}"/>
    <path d="M178.5 97.8C181 93.6 190 93.2 192.8 97.4C189.5 100.4 182 100.6 178.5 97.8ZM221.5 97.8C219 93.6 210 93.2 207.2 97.4C210.5 100.4 218 100.6 221.5 97.8Z" fill="#fffaf5"/>
    <ellipse cx="186" cy="97.2" rx="3.3" ry="3.4" fill="#3b2217"/>
    <ellipse cx="214" cy="97.2" rx="3.3" ry="3.4" fill="#3b2217"/>
    <circle cx="187.2" cy="95.9" r="1.1" fill="#fff"/>
    <circle cx="215.2" cy="95.9" r="1.1" fill="#fff"/>
    <path d="M181.5 91.4C184.8 90 188.6 90 191.4 91.4M218.5 91.4C215.2 90 211.4 90 208.6 91.4" fill="none" stroke="{SKIN_SHADE}" stroke-width=".9" opacity=".7"/>
    <path d="M178 98C181 93 190 92.4 193.2 97M178.6 97.2L176 95.4M222 98C219 93 210 92.4 206.8 97M221.4 97.2L224 95.4" fill="none" stroke="#3a2219" stroke-width="2"/>
    <path d="M197.4 98C196.6 103 195.8 107 194.6 110.2" fill="none" stroke="{SKIN_SHADE}" stroke-width="1.5"/>
    <path d="M194.4 112C193.2 111 193.4 109.4 194.8 108.8M205.6 112C206.8 111 206.6 109.4 205.2 108.8M195.6 112.4C197.6 114.6 202.4 114.6 204.4 112.4" fill="none" stroke="{SKIN_DEEP}" stroke-width="1.35"/>
    <path d="M184.5 120.4C193 122 207 122 215.5 120.4C212 129.4 205.6 131.8 200 131.8C194.4 131.8 188 129.4 184.5 120.4Z" fill="{MOUTH}"/>
    <path d="M185.6 121C193.4 122.7 206.6 122.7 214.4 121C213.4 124 211 125.8 208 126.3C202.8 127.1 197.2 127.1 192 126.3C189 125.8 186.6 124 185.6 121Z" fill="{TEETH}"/>
    <path d="M183.5 119.8C189.5 117.2 195.8 116.8 200 118C204.2 116.8 210.5 117.2 216.5 119.8C207.5 121.7 192.5 121.7 183.5 119.8Z" fill="{LIPS}"/>
    <path d="M187.8 125.6C191.4 130.4 195.8 131.8 200 131.8C204.2 131.8 208.6 130.4 212.2 125.6C210.8 132 205.6 134.8 200 134.8C194.4 134.8 189.2 132 187.8 125.6Z" fill="{LIPS}"/>
    <path d="M183.5 119.8C188.2 128.6 194.6 132 200 132C205.4 132 211.8 128.6 216.5 119.8" fill="none" stroke="{L}" stroke-width="1.15"/>
    <path d="M155 107C149 68 168 42 200 42C232 42 251 66 245 107C243 95 239 85 233 77C225 67 211 61 196 58C186 60 177 64 171 71C165 79 159 93 155 107Z" fill="{HAIR}"/>
    <path d="M196 58C196 52 198 47 201 43M176 62C182 54 190 50 196 50M206 50C218 51 230 58 236 70" fill="none" stroke="{HAIR_LIGHT}" stroke-width="1.6" opacity=".9"/>
    <path d="M168 66C163 76 160 88 158 100M233 70C238 80 240 90 242 100" fill="none" stroke="{HAIR_MID}" stroke-width="2"/>
  </g></g>'''


def front_hair_svg():
    """The lock of hair that falls in front of the signer's left shoulder (viewer's right),
    from below the jaw over the collar."""
    return (f'<path d="M229 139C238 141 244 150 246 162C248 175 251 188 257 199C260 205 261 211 258 217'
            f'C253 210 246 205 241 197C235 187 235 175 233 163C232 154 230 146 226 141Z" fill="{HAIR}"/>'
            f'<path d="M238 150C241 163 242 174 246 184C248 191 251 198 254 205" fill="none" stroke="{HAIR_LIGHT}"'
            f' stroke-width="1.6" stroke-linecap="round" opacity=".8"/>')


def rest_arm_svg():
    """The non-signing arm hangs by the body (signer's left = viewer's right)."""
    s, e, w = SHOULDER['left'], (272.0, 309.0), (279.0, 410.0)
    up = rpath(capsule_cmds(s, 18.2, e, 15.1, bulge=(1.8, 1.0)))
    line = rpath(capsule_cmds(s, 18.2, e, 15.1, bulge=(1.8, 1.0), s=outer_sign(s, e, 1), open_end=0.82))
    fo = rpath(capsule_cmds(e, 14.5, w, 13.0, bulge=(1.0, 1.0)))
    return (f'<path d="{fo}" fill="{SHIRT}" stroke="{SHIRT_LINE}" stroke-width="{BODY_LINE}"/>'
            f'<path d="{up}" fill="{SHIRT}"/>'
            f'<path d="{line}" fill="none" stroke="{SHIRT_LINE}" stroke-width="{BODY_LINE}"/>')


def sign_svg(sid, sign, frames, frame=None, title='', body=True):
    A = Anim(sign['dur'], frame)
    defs, draw = [], []

    paths, shown = {}, {}   # animated shapes, and in which frames some <use> shows each one

    def animated_path(pid, values):
        paths[f'{sid}-{pid}'] = values

    def use(pid, extra, vis=None):
        pid = f'{sid}-{pid}'
        on = shown.setdefault(pid, [False] * len(frames))
        for i in range(len(frames)):
            on[i] = on[i] or vis is None or vis[i] == 'visible'
        if vis is None:
            return f'<use href="#{pid}"{extra}/>'
        a, kids = A.attr('visibility', vis, discrete=True)
        return f'<use href="#{pid}"{extra}{a}>{kids}</use>' if kids else f'<use href="#{pid}"{extra}{a}/>'

    def path_defs():
        """Only the shapes something shows; while a shape is hidden it holds its last shown
        value, so runs of equal frames collapse in the SMIL values."""
        out = []
        for pid, values in paths.items():
            on = shown.get(pid)
            if not on or not any(on):
                continue
            first = next(i for i, v in enumerate(on) if v)
            held, last = [], values[first]
            for v, vis in zip(values, on):
                last = v if vis else last
                held.append(last)
            a, kids = A.attr('d', held if A.frame is None else values)
            out.append(f'<path id="{pid}"{a}>{kids}</path>' if kids else f'<path id="{pid}"{a}/>')
        return ''.join(out)

    def shadow(pid, dx, dy):
        use(pid, '')   # marks the shape as shown
        return (f'<g clip-path="url(#{sid}-torso)"><use href="#{sid}-{pid}" transform="translate({dx} {dy})"'
                f' fill="{SHIRT_DEEP}" stroke="none" opacity=".4"/></g>')
    if not sign.get('hand_only'):
        defs.append(f'<clipPath id="{sid}-torso"><path d="{torso_path()}"/></clipPath>')
    order = list(enumerate(sign['hands']))
    if sign.get('mirror_second'):
        order = order[::-1]   # draw the non-dominant hand first
    if 'left' not in sign['hands'] and not sign.get('hand_only'):
        draw.append(f'<g stroke-linecap="round" stroke-linejoin="round">{rest_arm_svg()}</g>' + front_hair_svg())

    for i, arm in order:
        if not sign.get('hand_only'):
            for part in ('up', 'upline', 'fo', 'folds', 'cuff', 'wrist'):
                animated_path(f'{arm}-{part}', [f['armgeo'][arm][part] for f in frames])
            draw.append(shadow(f'{arm}-fo', 3, 4) + '<g stroke-linecap="round" stroke-linejoin="round">'
                        + use(f'{arm}-up', f' fill="{SHIRT}"')
                        + use(f'{arm}-upline', f' fill="none"' + stroke(SHIRT_LINE, BODY_LINE))
                        + use(f'{arm}-fo', f' fill="{SHIRT}"' + stroke(SHIRT_LINE, BODY_LINE))
                        + use(f'{arm}-folds', ' fill="none"' + stroke(SHIRT_LINE, 1.2) + ' opacity=".7"')
                        + use(f'{arm}-wrist', f' fill="{SKIN}"' + stroke(INK, LINE))
                        + use(f'{arm}-cuff', f' fill="{SHIRT_LIGHT}"' + stroke(SHIRT_LINE, BODY_LINE))
                        + '</g>' + (front_hair_svg() if arm == 'left' else ''))

        hands = [f['hands'][i] for f in frames]
        hid = f'h{i}'
        visl = lambda conds: ['visible' if c else 'hidden' for c in conds]
        animated_path(f'{hid}-palm', [smooth_closed(h['palm']) for h in hands])
        animated_path(f'{hid}-lines', [rpath(curve_cmds(h['crease']) + curve_cmds(h['head_line'])) for h in hands])
        for j in range(4):
            animated_path(f'{hid}-kn{j}', [rpath(curve_cmds(h['knuckles'][j])) for h in hands])
        animated_path(f'{hid}-thenar', [rpath(thenar_cmds(h['digits']['thumb']['pts'], h['scale'])) for h in hands])
        animated_path(f'{hid}-web', [rpath([('M', h['web'][0])] + [('L', p) for p in h['web'][1:]] + [('Z',)]) for h in hands])
        animated_path(f'{hid}-thenar-inner', [rpath(thenar_cmds(h['digits']['thumb']['pts'], h['scale'], 'inner', centre(h['palm'])))
                                              for h in hands])
        for name in DIGITS:
            segs = hands[0]['digits'][name]['segs']
            for k in segs:
                animated_path(f'{hid}-{name}-s{k}', [rpath(seg_cmds(h['digits'][name], k)) for h in hands])
            if name != 'thumb' and any(h['digits'][name]['tight'] for h in hands):
                animated_path(f'{hid}-{name}-curl', [rline(h['digits'][name]['curl']) for h in hands])
                animated_path(f'{hid}-{name}-tipcover', [rline(h['digits'][name]['tipcover']) for h in hands])
                for wid, tag in ((LINE, 'cap'), (THIN, 'capthin')):
                    animated_path(f'{hid}-{name}-{tag}', [rpath(cap_cmds(h, name, wid)) for h in hands])
            # The thumb's outline starts right where the thenar ends (its MCP); a finger's
            # outline starts at the palm's edge and its fill reaches into the palm.
            if name == 'thumb':
                animated_path(f'{hid}-{name}-i1', [rpath(seg_cmds(h['digits'][name], 1, caps=(False, True))) for h in hands])
            else:
                animated_path(f'{hid}-{name}-i0', [rpath(root_open_cmds(h['digits'][name])) for h in hands])
                animated_path(f'{hid}-{name}-root', [rpath(root_cmds(h['digits'][name], h['scale'])) for h in hands])
                animated_path(f'{hid}-{name}-f0', [rpath(f0_cmds(h['digits'][name])) for h in hands])
                animated_path(f'{hid}-{name}-ka', [rpath(knuckle_arc_cmds(h['digits'][name])) for h in hands])
                if any(h['digits'][name]['tight'] for h in hands):
                    animated_path(f'{hid}-{name}-sd2', [rpath(seg_cmds(h['digits'][name], 2, caps=(False, False))) for h in hands])
            for j in (0, 1):
                animated_path(f'{hid}-{name}-c{j}', [rpath(curve_cmds(h['digits'][name]['creases'][j])) for h in hands])
                animated_path(f'{hid}-{name}-w{j}', [rpath([c for arc in h['digits'][name]['wrinkles'][j] for c in curve_cmds(arc)])
                                                     for h in hands])
            animated_path(f'{hid}-{name}-nail', [smooth_closed(h['digits'][name]['nail']) for h in hands])

        # Pieces of a digit that would peek out as slivers or small cut-off fragments are masked out
        # (ellipse patches from hide_fragments), so only the digit's main part is drawn.
        frag_mask = {}
        for name in DIGITS:
            npatch = max(len(h['digits'][name].get('patches', ())) for h in hands)
            if not npatch:
                continue
            kids = ''
            for j in range(npatch):
                vals, vis = [], []
                for h in hands:
                    dg = h['digits'][name]
                    pt = dg.get('patches', [])
                    e = pt[j] if j < len(pt) else (dg['pts'][3][0], dg['pts'][3][1], 0.1, 0.1, 0.0)
                    vals.append(rpath(ellipse_cmds(e)))
                    vis.append(j < len(pt) and not dg['hidden'])
                animated_path(f'{hid}-{name}-patch{j}', vals)
                kids += use(f'{hid}-{name}-patch{j}', ' fill="#000"', visl(vis))
            mid = f'{sid}-{hid}-{name}-frag'
            defs.append(f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="-500" y="-500" width="1500" height="1500">'
                        f'<rect x="-500" y="-500" width="1500" height="1500" fill="#fff"/>{kids}</mask>')
            frag_mask[name] = mid

        def masked(name, part):
            return f'<g mask="url(#{frag_mask[name]})">{part}</g>' if part and name in frag_mask else part

        def digit_w(name):
            return sum(h['digits'][name]['w'] for h in hands) / len(hands)

        def seg_ink(name, k, on, want, thin):
            """Outline of bone k of a digit in the frames where `on`: a full outline, or a thin
            line between fist fingers. In front of the palm the base grows out of it (no line
            across it); a fist fingertip has no cap (see tipring)."""
            if not any(on):
                return ''
            segs = hands[0]['digits'][name]['segs']
            ink = stroke(INK, 2 * (THIN if thin else LINE))
            out = ''
            butt_tip = [name != 'thumb' and k == 2 and h['digits'][name]['tight'] for h in hands]
            if k == segs[0] and want:
                tv_ = visl([o and h['digits'][name]['trim'] for o, h in zip(on, hands)])
                rv_ = visl([o and not h['digits'][name]['trim'] for o, h in zip(on, hands)])
                if any(v == 'visible' for v in tv_):
                    out += use(f'{hid}-{name}-i{k}', ink + ' stroke-linecap="butt"', tv_)
                    if name != 'thumb':
                        out += use(f'{hid}-{name}-ka', ink + f' stroke-linecap="butt" mask="url(#{sid}-{hid}-out)"', tv_)
                if any(v == 'visible' for v in rv_):
                    out += use(f'{hid}-{name}-s{k}', ink, rv_)
                return out
            bv = visl([o and b for o, b in zip(on, butt_tip)])
            rv = visl([o and not b for o, b in zip(on, butt_tip)])
            if any(v == 'visible' for v in bv):
                out += use(f'{hid}-{name}-sd2', ink + ' stroke-linecap="butt"', bv)
                out += use(f'{hid}-{name}-{"capthin" if thin else "cap"}', stroke(INK, THIN if thin else LINE), bv)
            if any(v == 'visible' for v in rv):
                out += use(f'{hid}-{name}-s{k}', ink, rv)
            return out

        def group_ink(layer, slot):
            """The outer outline of a run of fist fingers, drawn when the run starts (its farthest
            finger), under every finger of the run."""
            want = layer == 'front'
            out = ''
            for name in DIGITS[:4]:
                part = ''
                for k in (0, 1, 2):
                    on = [h['digits'][name]['tight'] and h['digits'][name]['front'][k] == want and not h['digits'][name]['hidden']
                          and h['run_start'][layer].get((name, 0)) == slot for h in hands]
                    part += seg_ink(name, k, on, want, False)
                out += masked(name, part)
            return out

        def digit(name, layer, slot):
            """The parts of one digit that sit in one depth slot of one layer (behind or in front
            of the palm): outline and fill (a digit folded over itself, or with another digit
            passing between its base and tip, is two parts), then creases, knuckle wrinkles, a
            fingertip outline and the nail, each only where it really shows."""
            segs = hands[0]['digits'][name]['segs']
            want = layer == 'front'

            def here(h, k):
                dg = h['digits'][name]
                return not dg['hidden'] and dg['front'][k] == want and h['order'][layer].get((name, dg['group'][k])) == slot

            if not any(here(h, k) for h in hands for k in segs):
                return ''
            ink, fill = '', ''
            for k in segs:
                on = [here(h, k) for h in hands]
                if not any(on):
                    continue
                # A fist finger has only a thin line here: its outer outline was drawn under the
                # whole run of fist fingers (group_ink).
                ink += seg_ink(name, k, [o and not h['digits'][name]['tight'] for o, h in zip(on, hands)], want, False)
                ink += seg_ink(name, k, [o and h['digits'][name]['tight'] for o, h in zip(on, hands)], want, True)
                if k == 0 and want and name != 'thumb':
                    tv_ = visl([o and h['digits'][name]['trim'] for o, h in zip(on, hands)])
                    rv_ = visl([o and not h['digits'][name]['trim'] for o, h in zip(on, hands)])
                    if any(v == 'visible' for v in tv_):
                        fill += use(f'{hid}-{name}-f0', f' fill="{SKIN}"', tv_)
                    if any(v == 'visible' for v in rv_):
                        fill += use(f'{hid}-{name}-s0', f' fill="{SKIN}"', rv_)
                else:
                    fill += use(f'{hid}-{name}-s{k}', f' fill="{SKIN}"', visl(on))
            if name != 'thumb':
                vis = visl([here(h, 0) and h['digits'][name]['tight'] for h in hands])
                if any(v == 'visible' for v in vis):
                    fill += use(f"{hid}-{name}-curl", f' fill="{SKIN}"', vis)
                vis = visl([here(h, 2) and h['digits'][name]['tight'] for h in hands])
                if any(v == 'visible' for v in vis):
                    fill += use(f"{hid}-{name}-tipcover", f' fill="{SKIN}"', vis)
            elif not want:
                # Behind the palm the thumb, its fleshy base and the web to the index are one
                # silhouette.
                vis = visl([here(h, 1) and not h['digits']['thumb']['front'][0] for h in hands])
                if any(v == 'visible' for v in vis):
                    ink = use(f'{hid}-web', stroke(INK, 2 * LINE), vis) + use(f'{hid}-thenar', stroke(INK, 2 * LINE), vis) + ink
                    fill = use(f'{hid}-web', f' fill="{SKIN}"', vis) + use(f'{hid}-thenar', f' fill="{SKIN}"', vis) + fill
            out = ink + fill
            for j in (1, 2):   # joint j belongs to the bone after it
                vis = visl([here(h, j) and h['digits'][name]['crease_vis'][j - 1] for h in hands])
                if any(v == 'visible' for v in vis):
                    out += use(f'{hid}-{name}-c{j - 1}', stroke(CREASE_INK, 1.3), vis)
                vis = visl([here(h, j) and h['digits'][name]['wrinkle_vis'][j - 1] for h in hands])
                if any(v == 'visible' for v in vis):
                    out += use(f'{hid}-{name}-w{j - 1}', stroke(CREASE_INK, 1.1) + ' opacity=".8"', vis)
            vis = visl([here(h, 2) and h['digits'][name]['pad_vis'] for h in hands])
            if any(v == 'visible' for v in vis):
                r = sum(h['digits'][name]['r'][2] for h in hands) / len(hands) * TIP_K
                cx, k1 = A.attr('cx', [num(h['digits'][name]['pts'][3][0]) for h in hands])
                cy, k2 = A.attr('cy', [num(h['digits'][name]['pts'][3][1]) for h in hands])
                v, kv = A.attr('visibility', vis, discrete=True)
                out += (f'<circle{cx}{cy} r="{num(r)}" fill="{SKIN}" stroke="{INK}" stroke-width="{num(LINE)}"{v}>'
                        f'{k1}{k2}{kv}</circle>')
            vis = visl([here(h, 2) and h['digits'][name]['nail_vis'] for h in hands])
            if any(v == 'visible' for v in vis):
                out += use(f'{hid}-{name}-nail', f' fill="{NAIL}" stroke="{NAIL_LINE}" stroke-width=".9"', vis)
            return out

        holes = ''
        if all('hole' in h for h in hands):
            animated_path(f'{hid}-hole', [smooth_closed(h['hole']) for h in hands])
            vis = visl([h['hole_vis'] and not h['digits']['index']['hidden'] and not h['digits']['thumb']['hidden'] for h in hands])
            if any(v == 'visible' for v in vis):
                holes = use(f'{hid}-hole', f' fill="{SKIN_DEEP}" fill-opacity=".55"', vis)
        th_front = visl([h['digits']['thumb']['front'][0] for h in hands])
        # (when the thumb itself is behind the palm too, its base is drawn with it, see digit())
        th_back = visl([not h['digits']['thumb']['front'][0] and not h['digits']['thumb']['hidden'] and
                        (h['digits']['thumb']['front'][1] or h['order']['back'].get(('thumb', h['digits']['thumb']['group'][1])) is None)
                        for h in hands])
        th_back_all = visl([not h['digits']['thumb']['front'][0] and not h['digits']['thumb']['hidden'] for h in hands])
        life = visl([h['life_vis'] for h in hands])
        # Thumb mound and web behind the palm: outlines first, then fills, so the two read as one
        # silhouette with the thumb (no line between mound and web).
        thenar_back = ((use(f'{hid}-web', stroke(INK, 2 * LINE), th_back) + use(f'{hid}-thenar', stroke(INK, 2 * LINE), th_back)
                        + use(f'{hid}-web', f' fill="{SKIN}"', th_back) + use(f'{hid}-thenar', f' fill="{SKIN}"', th_back))
                       if any(v == 'visible' for v in th_back) else '')
        thenar_ink, thenar_front, web_front = '', '', ''
        if any(v == 'visible' for v in th_front):
            # Palm, thumb mound and web are one silhouette: their outlines go under the palm, their
            # fills over it, so only the outer contour shows (the web's free edge between the
            # thumb and the index knuckle, the mound's edge when the thumb is spread).
            thenar_ink = use(f'{hid}-web', stroke(INK, 2 * LINE), th_front) + use(f'{hid}-thenar', stroke(INK, 2 * LINE), th_front)
            web_front = use(f'{hid}-web', f' fill="{SKIN}"', th_front)
            thenar_front = use(f'{hid}-thenar', f' fill="{SKIN}"', th_front)
            if any(v == 'visible' for v in life):
                thenar_front += use(f'{hid}-thenar-inner', stroke(CREASE_INK, 1.3) + ' opacity=".85"', life)
        palm_vis = visl([h['lines_vis'] for h in hands])
        knuckles = ''
        for j in range(4):
            vis = visl([h['knuckle_vis'][j] for h in hands])
            if any(v == 'visible' for v in vis):
                knuckles += use(f'{hid}-kn{j}', f' stroke="{CREASE_INK}" stroke-width="1.1" opacity=".7"', vis)
        # The palm's outline is drawn only along its free edges: where a finger, or the thumb's mound
        # and web seen from behind, grows out of the hand, the outline is left out (a mask), so
        # the digit's own outline runs on into the hand's.
        roots = ''.join(use(f'{hid}-{name}-root', ' fill="#000"', visl([not h['digits'][name]['hidden'] for h in hands]))
                        for name in DIGITS[:4])
        if any(v == 'visible' for v in th_back_all):
            roots += use(f'{hid}-web', ' fill="#000"', th_back_all) + use(f'{hid}-thenar', ' fill="#000"', th_back_all)
        defs.append(f'<mask id="{sid}-{hid}-root" maskUnits="userSpaceOnUse" x="-500" y="-500" width="1500" height="1500">'
                    f'<rect x="-500" y="-500" width="1500" height="1500" fill="#fff"/>{roots}</mask>')
        # Outside the palm only: the round end of a knuckle that a side view puts on the palm's edge.
        palm_black = use(f'{hid}-palm', ' fill="#000"')
        defs.append(f'<mask id="{sid}-{hid}-out" maskUnits="userSpaceOnUse" x="-500" y="-500" width="1500" height="1500">'
                    f'<rect x="-500" y="-500" width="1500" height="1500" fill="#fff"/>{palm_black}</mask>')
        layer_svg = lambda layer: ''.join(group_ink(layer, s) + ''.join(masked(n, digit(n, layer, s)) for n in DIGITS)
                                          for s in range(10))
        draw.append(('' if sign.get('hand_only') else shadow(f'{hid}-palm', 4, 5))
                    + '<g fill="none" stroke-linecap="round" stroke-linejoin="round">'
                    + layer_svg('back')
                    + thenar_back + thenar_ink
                    # The ring's opening is shaded under the palm, web and thumb mound: where the
                    # palm (seen edge-on) bounds the opening, the shading stops at its outline.
                    + holes
                    + use(f'{hid}-palm', f' fill="none" stroke="{INK}" stroke-width="{num(2 * LINE)}" mask="url(#{sid}-{hid}-root)"')
                    + use(f'{hid}-palm', f' fill="{SKIN}"')
                    + web_front
                    + use(f'{hid}-lines', f' stroke="{CREASE_INK}" stroke-width="1.2" opacity=".75"', palm_vis)
                    + thenar_front
                    + layer_svg('front')
                    + knuckles
                    + '</g>')

    marks = ''.join(
        f'<g transform="translate({x} {y}) rotate({a})" stroke="{ACCENT}" stroke-width="2.4" stroke-linecap="round">'
        f'<path d="M0 -6V-12M-6 -4L-10 -8M6 -4L10 -8"/></g>' for x, y, a in sign.get('marks', []))

    def arrow(a):
        heads = '' if a.get('plain') else f' marker-end="url(#{sid}-tip)"'
        if a.get('both'):
            heads += f' marker-start="url(#{sid}-tip)"'
        return f'<path d="{a["d"]}" fill="none" stroke="{ACCENT}" stroke-width="2.6" stroke-linecap="round"{heads}/>'

    arrows = ''.join(arrow(a) for a in arrow_paths(sign))
    ear_anim = {}
    if body:
        for side, seq in earring_states(frames).items():
            if not all(seq):
                ear_anim[side] = A.attr('visibility', ['visible' if v else 'hidden' for v in seq], discrete=True)

    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box(sign, frames)}" role="img" aria-label="{title}">'
            f'<title>{title}</title>'
            f'<defs><marker id="{sid}-tip" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="3.6" markerHeight="3.6" orient="auto-start-reverse">'
            f'<path d="M0 0L10 5L0 10Z" fill="{ACCENT}"/></marker>'
            + ''.join(defs) + path_defs() + '</defs>'
            + (body_svg(ear_anim) if body else '')
            + (f'<g opacity=".95">{marks}</g>' if sign.get('marks_under') else '')
            + ''.join(draw) + f'<g opacity=".95">{arrows}{"" if sign.get("marks_under") else marks}</g></svg>')


def handshape_svg(sid, shape, ring=False, title='', view=None):
    """The handshape alone, big, palm to the viewer, in the same style as the signs."""
    v = view or {}
    pose = P((0, 0), shape, 'wrist', yaw=v.get('yaw', 0), pitch=v.get('pitch', 0), roll=v.get('roll', 0), scale=1.0, ring=ring)
    sign = {'dur': 1.0, 'hands': ['right'], 'keys': [(0.0, [pose]), (1.0, [pose])], 'hand_only': True}
    frames = frames_for(sign)
    h = frames[0]['hands'][0]
    pts = [(q[0], q[1]) for q in h['palm']] + [(q[0], q[1]) for d in h['digits'].values() for q in d['pts']]
    xs, ys = [q[0] for q in pts], [q[1] for q in pts]
    pad = 9
    x0, x1, y0, y1 = min(xs) - pad, max(xs) + pad, min(ys) - pad, max(ys) + 14
    size = max(x1 - x0, y1 - y0)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    svg = sign_svg(f'{sid}-mao', sign, frames, frame=0, title=title, body=False)
    svg = re.sub(r'viewBox="[^"]*"', f'viewBox="{num(cx - size / 2)} {num(cy - size / 2)} {num(size)} {num(size)}"', svg, count=1)
    hw, bottom = 10.0, cy + size / 2 + 2
    arm = (f'<path d="M{-hw - 3} 9L{-hw - 4.5} {num(bottom)}H{hw + 4.5}L{hw + 3} 9Z" fill="{SHIRT}" stroke="{SHIRT_LINE}" stroke-width="{BODY_LINE}"/>'
           f'<path d="M{-hw} 4V-2H{hw}V4Z" fill="{SKIN}" stroke="{INK}" stroke-width="{LINE}" stroke-linejoin="round"/>'
           f'<path d="M{-hw - 2.4} 4H{hw + 2.4}L{hw + 2.8} 13H{-hw - 2.8}Z" fill="{SHIRT_LIGHT}" stroke="{SHIRT_LINE}" stroke-width="{BODY_LINE}" stroke-linejoin="round"/>')
    return svg.replace('</defs>', '</defs>' + arm, 1)


TITLES = {'agua': 'Sinal de água em Libras', 'cafe': 'Sinal de café em Libras', 'familia': 'Sinal de família em Libras',
          'obrigado': 'Sinal de obrigado em Libras', 'voce': 'Sinal de você em Libras',
          'computador': 'Sinal de computador em Libras'}


def review_sheet(sid, sign, frames, count=6, cols=3):
    """Static frames in a grid, for checking poses without a browser."""
    picks = [round(i * (len(frames) - 1) / (count - 1)) for i in range(count)]
    rows = (count + cols - 1) // cols
    cells = []
    for k, idx in enumerate(picks):
        x, y = (k % cols) * W, (k // cols) * H
        inner = sign_svg(f'{sid}-c{k}', sign, frames, frame=idx).replace('<svg ', f'<svg x="{x}" y="{y}" width="{W}" height="{H}" ', 1)
        cells.append(f'<rect x="{x + 2}" y="{y + 2}" width="{W - 4}" height="{H - 4}" fill="#eef1f8"/>' + inner
                     + f'<text x="{x + 10}" y="{y + 22}" font-family="Helvetica" font-size="16" fill="#555">'
                     f'{num(sign["dur"] * idx / (len(frames) - 1))}s</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W * cols} {H * rows}" width="{W * cols}" height="{H * rows}">'
            f'<rect width="100%" height="100%" fill="#fff"/>' + ''.join(cells) + '</svg>')


# More signs live one per file in scripts/sinais/<id>.py, so several people (or agents) can add
# signs at once without touching this file. Each file runs in this module's namespace and sets
# SIGNS['<id>'] and TITLES['<id>'] (it may define its own hs_* handshapes with the helpers above).
# Each file gets its own copy of the namespace, so its local names can't overwrite the engine's
# (SIGNS, TITLES and HANDSHAPES are shared objects, so entries added to them still count).
SIGN_DIR = Path(__file__).resolve().parent / 'sinais'
for _spec in sorted(SIGN_DIR.glob('*.py')):
    try:
        exec(compile(_spec.read_text(encoding='utf-8'), str(_spec), 'exec'), dict(globals()))
    except Exception as _err:   # one broken file must not stop the other signs
        print(f'SKIPPED {_spec.name}: {type(_err).__name__}: {_err}', file=sys.stderr)


def main(argv):
    sheet_dir = None
    if '--sheet' in argv:
        i = argv.index('--sheet')
        sheet_dir = Path(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    ids = argv or list(SIGNS)
    OUT.mkdir(parents=True, exist_ok=True)
    for sid in ids:
        sign = SIGNS[sid]
        frames = frames_for(sign)
        svg = sign_svg(sid, sign, frames, title=TITLES.get(sid, sid))
        (OUT / f'{sid}.svg').write_text(svg, encoding='utf-8')
        still = round(sign.get('poster', 0) / sign['dur'] * (len(frames) - 1))
        (OUT / f'{sid}-parado.svg').write_text(sign_svg(sid, sign, frames, frame=still, title=TITLES.get(sid, sid)), encoding='utf-8')
        print(f'{sid}: {len(frames)} frames, {len(svg) // 1024} KB')
        if 'handshape' in sign:
            (ROOT / 'media' / 'maos').mkdir(parents=True, exist_ok=True)
            (ROOT / 'media' / 'maos' / f'{sid}.svg').write_text(
                handshape_svg(sid, sign['handshape'], sign.get('handshape_ring', False),
                              f'Configuração de mão de {TITLES.get(sid, sid).replace("Sinal de ", "").replace(" em Libras", "")}',
                              sign.get('handshape_view')),
                encoding='utf-8')
        if sheet_dir:
            sheet_dir.mkdir(parents=True, exist_ok=True)
            (sheet_dir / f'{sid}-sheet.svg').write_text(review_sheet(sid, sign, frames), encoding='utf-8')


if __name__ == '__main__':
    main(sys.argv[1:])
