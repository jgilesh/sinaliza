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
INK = '#3b2b24'
SKIN = '#ebb894'
SKIN_DARK = '#cf9670'
HAIR = '#3a2920'
HAIR_LIGHT = '#5b4032'
SHIRT = '#2f6aa0'        # a plain top, as interpreters wear, so the hands stand out
SHIRT_DARK = '#255683'
LIPS = '#b9605a'
GOLD = '#c9a24a'
ACCENT = '#f26b2d'
NAIL = '#f7e0d0'
LINE = 1.7          # visible outline width
ARM_UPPER, ARM_FORE = 118.0, 104.0
SHOULDER = {'right': (146.0, 192.0), 'left': (254.0, 192.0)}   # signer's right = viewer's left
SIDE = {'right': -1, 'left': 1}                                 # direction "outward" on screen

# Body landmarks (viewer coordinates) used by the sign specs.
SPOT = {
    'chin': (200, 143), 'chin_r': (192, 141),
    'mouth': (200, 125), 'mouth_r': (189, 124), 'cheek_r': (178, 114),
    'forehead': (200, 70), 'forehead_r': (187, 72),
    'chest': (200, 214),
}

# ---------------------------------------------------------------- hand model
# Right hand, palm facing the viewer (+z toward the viewer), fingers up (-y),
# thumb on the viewer's right (+x). Units are picture pixels at scale 1.
FINGERS = {
    'pinky':  ((-12.0, -33.0), (12.5, 8.5, 7.5), 7.4),
    'ring':   ((-4.2, -36.2), (16.5, 11.0, 8.5), 8.4),
    'middle': ((4.0, -37.2), (18.0, 11.5, 9.0), 8.8),
    'index':  ((12.0, -35.2), (16.0, 10.5, 8.5), 8.6),
}
THUMB = ((11.0, -9.0), (13.0, 11.0, 9.5), 9.8)
PALM = [(-12.5, -1), (12.5, -1), (16.5, -9), (17.5, -24), (16, -33.5), (12.5, -38), (4, -40),
        (-4.5, -39), (-12, -36), (-16, -31), (-16.5, -14), (-14.5, -5)]
CREASE = [(-7, -30), (1, -23), (5, -14), (5, -6)]
PALM_HALF_THICKNESS = 4.5
DIGITS = ['pinky', 'ring', 'middle', 'index', 'thumb']


def chain(base, lens, spread, flexes, twist=0.0):
    """Joint points of one finger. spread: degrees toward +x; flexes: degrees of bend;
    twist: 0 bends toward the palm side (+z), 90 bends sideways toward the thumb (+x)."""
    s, tw = math.radians(spread), math.radians(twist)
    d = (math.sin(s), -math.cos(s), 0.0)                                       # straight finger
    b = (math.cos(s) * math.sin(tw), math.sin(s) * math.sin(tw), math.cos(tw))  # bend direction
    pts = [(base[0], base[1], 0.0)]
    theta = 0.0
    for length, flex in zip(lens, flexes):
        theta += math.radians(flex)
        c, n = math.cos(theta), math.sin(theta)
        x, y, z = pts[-1]
        pts.append(tuple(q + length * (d[i] * c + b[i] * n) for i, q in enumerate((x, y, z))))
    return pts


def distal_dorsal(shape, name):
    """Direction the back of the fingertip (the nail side) faces, in hand coordinates."""
    spread, flexes, *twist = shape[name]
    s, tw = math.radians(spread), math.radians(twist[0] if twist else 0.0)
    d = (math.sin(s), -math.cos(s), 0.0)
    b = (math.cos(s) * math.sin(tw), math.sin(s) * math.sin(tw), math.cos(tw))
    theta = math.radians(sum(flexes))
    return tuple(d[i] * math.sin(theta) - b[i] * math.cos(theta) for i in range(3))


def digit_points(shape, name):
    spread, flexes, *twist = shape[name]
    base, lens, _ = THUMB if name == 'thumb' else FINGERS[name]
    return chain(base, lens, spread, flexes, *twist)


def solve_thumb(shape, target, start=(40, 40, 20, 10)):
    """Thumb pose whose tip reaches `target` (3D), by a small pattern search."""
    def err(p):
        tip = chain(THUMB[0], THUMB[1], p[0], p[1:])[-1]
        return sum((a - b) ** 2 for a, b in zip(tip, target))
    best, step = list(start), 16.0
    limits = [(-40, 100), (0, 95), (0, 95), (0, 85)]
    while step > 0.05:
        improved = False
        for i in range(4):
            for d in (step, -step):
                cand = best[:]
                cand[i] = min(max(cand[i] + d, limits[i][0]), limits[i][1])
                if err(cand) < err(best):
                    best, improved = cand, True
        if not improved:
            step /= 2
    return (best[0], tuple(best[1:]))


CURL = (0.0, (88.0, 100.0, 60.0))


def hs_1_curved():
    """Index up with the tip slightly curled forward, others closed, thumb over the middle
    finger (INES 15)."""
    shape = {'index': (2, (0, 14, 26)), 'middle': CURL, 'ring': CURL, 'pinky': CURL}
    shape['thumb'] = solve_thumb(shape, (3.0, -27.0, 20.0), start=(-10, 50, 30, 10))
    return shape


def hs_B():
    """Flat hand, fingers together, thumb open (INES 63)."""
    return {'index': (1, (0, 0, 0)), 'middle': (0, (0, 0, 0)), 'ring': (-1, (0, 0, 0)),
            'pinky': (-2, (0, 0, 0)), 'thumb': (52, (8, 6, 0))}


def hs_L(index_flex=(0, 0, 0)):
    """Index up, thumb sideways, other fingers closed (INES 8)."""
    return {'index': (2, index_flex), 'middle': (CURL[0] - 2, CURL[1]), 'ring': (CURL[0], CURL[1]),
            'pinky': (CURL[0] + 2, CURL[1]), 'thumb': (86, (4, 6, 0))}


def hs_1():
    """Index straight, others closed, thumb over the middle finger (INES 14)."""
    shape = {'index': (2, (0, 0, 0)), 'middle': CURL, 'ring': CURL, 'pinky': CURL}
    shape['thumb'] = solve_thumb(shape, (3.0, -27.0, 20.0), start=(-10, 50, 30, 10))
    return shape


def hs_F():
    """Index bent sideways at the knuckle, lying across toward the thumb, whose tip touches it;
    other three fingers open (INES 54)."""
    shape = {'index': (6, (80, 18, 6), 70), 'middle': (5, (0, 0, 0)), 'ring': (-3, (0, 0, 0)), 'pinky': (-12, (0, 0, 0))}
    tip = chain(FINGERS['index'][0], FINGERS['index'][1], *shape['index'])[-1]
    shape['thumb'] = solve_thumb(shape, (tip[0] + 0.5, tip[1] + 4.5, tip[2]))
    return shape


def hs_F_round():
    """Index and thumb tips together in a ring, other three fingers open (INES 55)."""
    # The index curls sideways toward the thumb, so the ring lies in the palm plane and its
    # hole shows when the palm faces the viewer (like an "OK" sign).
    shape = {'index': (14, (10, 70, 70), 85), 'middle': (-4, (0, 0, 0)), 'ring': (-11, (0, 0, 0)), 'pinky': (-19, (0, 0, 0))}
    tip = chain(FINGERS['index'][0], FINGERS['index'][1], *shape['index'])[-1]
    shape['thumb'] = solve_thumb(shape, (tip[0] + 1.0, tip[1] + 3.0, tip[2]), start=(40, 10, 10, 10))
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


def hand_geometry(pose, mirror):
    """Projects one hand. Returns screen paths plus depth flags for layering."""
    shape, yaw, pitch, roll, scale = pose['shape'], pose['yaw'], pose['pitch'], pose['roll'], pose['scale']
    if mirror:   # left hand = mirror image of the right hand
        yaw, roll = -yaw, -roll

    def tf(p):
        x, y, z = p
        if mirror:
            x = -x
        x, y, z = rot((x, y, z), yaw, pitch, roll)
        return (x * scale, y * scale, z * scale)

    ax, ay, _ = tf(anchor_point(shape, pose['anchor']))
    wx, wy = pose['at'][0] - ax, pose['at'][1] - ay

    def scr(p):
        x, y, z = tf(p)
        return (wx + x, wy + y, z)

    palm = [scr((x, y, 0.0)) for x, y in PALM]
    palm_z = sum(p[2] for p in palm) / len(palm)
    # Give the palm some thickness, so a hand seen from the side is a slab, not a line:
    # each outline point moves half the thickness toward the side it faces.
    nx, ny, _ = tf((0.0, 0.0, PALM_HALF_THICKNESS))
    cx, cy = sum(p[0] for p in palm) / len(palm), sum(p[1] for p in palm) / len(palm)
    palm = [(x + nx, y + ny, z) if (x - cx) * nx + (y - cy) * ny >= 0 else (x - nx, y - ny, z) for x, y, z in palm]
    normal_z = rot((0, 0, -1 if mirror else 1), yaw, pitch, roll)[2] * (-1 if mirror else 1)
    geo = {'wrist': (wx, wy), 'palm': palm, 'crease': [scr((x, y, 0.0)) for x, y in CREASE],
           'palm_facing': normal_z, 'digits': {}}
    for name in DIGITS:
        pts = [scr(p) for p in digit_points(shape, name)]
        depth = (pts[2][2] + pts[3][2]) / 2 - palm_z
        w = (THUMB if name == 'thumb' else FINGERS[name])[2] * scale
        (x2, y2, z2), (x3, y3, z3) = pts[2], pts[3]
        seg = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2 + (z3 - z2) ** 2) or 1
        toward = (z3 - z2) / seg
        dx, dy, dz = distal_dorsal(shape, name)
        if mirror:
            dx = -dx
        nail_z = rot((dx, dy, dz), yaw, pitch, roll)[2]
        geo['digits'][name] = {'pts': pts, 'front': depth > 3.5 or name == 'thumb' and depth > -2, 'w': w,
                               'pad': (x3, y3, w * 0.78) if toward > 0.8 and name != 'thumb' else None,
                               'creases': [crease(pts, j, w) for j in (1, 2)],
                               'nail': nail(pts, w) if nail_z > 0.2 else None}
    if pose.get('ring'):
        # The opening of a thumb-index ring, shaded so it reads as a hole even over the face.
        ix, th = geo['digits']['index']['pts'], geo['digits']['thumb']['pts']
        geo['hole'] = [(q[0], q[1]) for q in ix[1:] + th[1:][::-1]]
    return geo


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
up, bent = hs_L(), hs_L((55, 80, 30))
water = lambda shape: P((188, 137), shape, 'thumb_tip', yaw=15, roll=-8, scale=1.05, pole=(0.55, 1.0, 0.5))
SIGNS['agua'] = {
    'poster': 0.0, 'dur': 2.0, 'hands': ['right'], 'handshape': up,
    'keys': [(0.0, [water(up)]), (0.3, [water(up)]), (0.45, [water(bent)]), (0.6, [water(up)]),
             (0.75, [water(bent)]), (0.9, [water(up)]), (1.05, [water(bent)]), (1.2, [water(up)]),
             (2.0, [water(up)])],
    'marks': [(191, 140, 120)],
    'arrows': [{'d': 'M 144 66 Q 166 62 170 86', 'both': True}],
}

# CAFÉ: thumb and index in a ring on the corner of the mouth; the wrist twists so the open
# fingers swing from pointing up to pointing across the lips, two or three times.
ring = hs_F_round()
coffee = lambda yaw, roll: P('mouth_r', ring, 'pinch', yaw=yaw, roll=roll, scale=1.0, depth=40, ring=True)
up_c, turned_c = coffee(12, -14), coffee(150, 84)
SIGNS['cafe'] = {
    'poster': 0.0, 'dur': 2.4, 'hands': ['right'], 'handshape': ring, 'handshape_ring': True,
    'keys': [(0.0, [up_c]), (0.25, [up_c]), (0.5, [turned_c]), (0.75, [up_c]), (1.0, [turned_c]),
             (1.25, [up_c]), (2.4, [up_c])],
    'marks': [(194, 127, 70)],
    'arrows': [{'twist': 0, 'at': 0.0, 'r': (17, 6), 'drop': 4}],
}

# FAMÍLIA: both hands in F, palms forward, rings together in front of the chest; the hands
# draw a horizontal semicircle outward and forward and meet by the little fingers, palms back.
f = hs_F()
start_r = P((191, 192), f, 'index_tip', yaw=10, roll=-8, scale=1.0, depth=60)
open_r = P((128, 184), f, 'index_tip', yaw=40, pitch=-28, roll=-10, scale=1.05, depth=85, via=(150, 200))
end_r = P((197, 176), f, 'pinky_tip', yaw=172, roll=6, scale=1.1, depth=100, via=(136, 196))
rewind_r = dict(start_r, via=(150, 275))   # back to the start low and apart, so the hands never cross
SIGNS['familia'] = {
    'poster': 0.0, 'dur': 2.8, 'hands': ['right', 'left'], 'handshape': f,
    'keys': [(0.0, [start_r, mirrored(start_r)]), (0.3, [start_r, mirrored(start_r)]),
             (0.8, [open_r, mirrored(open_r)]), (1.3, [end_r, mirrored(end_r)]),
             (2.0, [end_r, mirrored(end_r)]), (2.8, [rewind_r, mirrored(rewind_r)])],
    'arrows': [{'trail': 0, 'from': 0.3, 'to': 1.3, 'offset': (0, 28), 'trim': 0.14},
               {'trail': 1, 'from': 0.3, 'to': 1.3, 'offset': (0, 28), 'trim': 0.14}],
    'mirror_second': True,
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
point = lambda s: P((196, 184), one, 'index_tip', yaw=-10, pitch=72, roll=0, scale=s, depth=80)
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
CX, CY, R = 166, 182, 22


def pc_pose(angle):
    """Right-hand pose on the circle; angle 0 = inner point (near the midline), clockwise."""
    a = math.radians(angle)
    at = (CX + R * math.cos(a), CY + R * math.sin(a))
    lean = 9 * math.cos(a)   # tips lean in near the midline, splay out on the outer side
    return P(at, pc, 'index_tip', yaw=4, roll=lean, scale=1.0, depth=85, pole=(0.25, 1.0, 0.3), ease='linear')


start_angle = -135          # top-outer: the hands start up and apart
circle = [start_angle + 30 * k for k in range(25)]   # two full turns, clockwise on screen
pc_keys = [(0.0, [dict(pc_pose(start_angle), ease='smooth')] * 2)]
for k, ang in enumerate(circle[1:], 1):
    pose = pc_pose(ang)
    pc_keys.append((0.05 + 1.4 * k / 24, [pose, mirrored(pose)]))
pc_keys[0] = (0.0, [pc_pose(start_angle), mirrored(pc_pose(start_angle))])
pc_keys.append((2.3, [pc_pose(start_angle), mirrored(pc_pose(start_angle))]))


def circle_arrow(cx, cy, r, a0, a1, clockwise):
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return f'M {x0:.1f} {y0:.1f} A {r} {r} 0 {large} {1 if clockwise else 0} {x1:.1f} {y1:.1f}'


SIGNS['computador'] = {
    'poster': 1.8, 'dur': 2.3, 'hands': ['right', 'left'], 'handshape': pc,
    'keys': pc_keys,
    # Above the fingertips: the right hand turns clockwise (in at the top), the left mirrors it.
    'arrows': [{'d': circle_arrow(CX, CY, R + 13, 165, 330, True)},
               {'d': circle_arrow(2 * 200 - CX, CY, R + 13, 15, 210, False)}],
    'mirror_second': True,
}


# ---------------------------------------------------------------- SVG
def num(v):
    s = f'{v:.1f}'
    return s[:-2] if s.endswith('.0') else s


def poly(pts):
    return 'M' + 'L'.join(f'{num(p[0])} {num(p[1])}' for p in pts)


def stroke(color, width):
    return f' stroke="{color}" stroke-width="{num(width)}"'


def smooth_closed(pts):
    """Closed curve through the midpoints of a polygon (rounded palm)."""
    mids = [((pts[i][0] + pts[(i + 1) % len(pts)][0]) / 2, (pts[i][1] + pts[(i + 1) % len(pts)][1]) / 2) for i in range(len(pts))]
    d = f'M{num(mids[-1][0])} {num(mids[-1][1])}'
    for p, m in zip(pts, mids):
        d += f'Q{num(p[0])} {num(p[1])} {num(m[0])} {num(m[1])}'
    return d + 'Z'


TAPER = (1.0, 0.93, 0.85)   # finger width at each phalanx, base to tip


def unit2(a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    L = math.hypot(dx, dy)
    return (dx / L, dy / L, L) if L > 1e-6 else (0.0, -1.0, 0.0)


def crease(pts, j, w):
    """Short line across the finger at joint j (a knuckle crease), so each joint reads."""
    ux, uy, L = unit2(pts[j - 1], pts[j + 1])
    if L < 3:   # finger seen end-on: no crease
        return poly([pts[j], pts[j]])
    half = w * TAPER[j] * 0.3
    x, y = pts[j][0], pts[j][1]
    return poly([(x - uy * half, y + ux * half), (x + uy * half, y - ux * half)])


def nail(pts, w):
    """The fingernail, drawn when the back of the fingertip faces the viewer. On a folded
    finger the tip points into the palm, so the nail shows as a small cap at the end."""
    ux, uy, L = unit2(pts[2], pts[3])
    x, y = pts[3][0], pts[3][1]
    if L >= 4:
        a = min(L * 0.62, w * 0.85)
        return poly([(x - ux * a, y - uy * a), (x - ux * 1.2, y - uy * 1.2)])
    vx, vy, _ = unit2(pts[1], pts[2])
    half = w * 0.2
    return poly([(x - vy * half, y + vx * half), (x + vy * half, y - vx * half)])


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


def frames_for(sign):
    n = round(sign['dur'] * FPS)
    times = [sign['dur'] * i / n for i in range(n + 1)]
    frames = []
    for t in times:
        frame = {'arms': {}, 'hands': []}
        for i, arm in enumerate(sign['hands']):
            pose = pose_at(sign['keys'], t, i, mirror=(arm == 'left'))
            geo = hand_geometry(pose, mirror=(arm == 'left'))
            elbow = solve_elbow(SHOULDER[arm], geo['wrist'], pose['depth'], SIDE[arm], pose.get('pole'))
            frame['points'] = frame.get('points', []) + [(p[0], p[1]) for p in geo['palm']] + [
                (q[0], q[1]) for d in geo['digits'].values() for q in d['pts']]
            frame['arms'][arm] = (SHOULDER[arm], elbow, geo['wrist'])
            frame['hands'].append(geo)
        frames.append(frame)
    return frames


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


class Anim:
    """Collects one attribute's per-frame values; emits a static value or a SMIL animation."""

    def __init__(self, dur, frame):
        self.dur, self.frame = dur, frame

    def attr(self, name, values, discrete=False):
        if self.frame is not None:
            return f' {name}="{values[self.frame]}"', ''
        if all(v == values[0] for v in values):
            return f' {name}="{values[0]}"', ''
        mode = ' calcMode="discrete"' if discrete else ''
        return (f' {name}="{values[0]}"',
                f'<animate attributeName="{name}" dur="{num(self.dur)}s" repeatCount="indefinite"{mode} values="{";".join(values)}"/>')


def limb_paths(frames, arm):
    upper = [poly([f['arms'][arm][0], f['arms'][arm][1]]) for f in frames]
    fore = [poly([f['arms'][arm][1], f['arms'][arm][2]]) for f in frames]
    sleeve = []
    for f in frames:
        (sx, sy), (ex, ey), _ = f['arms'][arm]
        sleeve.append(poly([(sx, sy), (sx + (ex - sx) * 0.42, sy + (ey - sy) * 0.42)]))
    return upper, fore, sleeve


def body_svg():
    """The signer: a woman in her fifties with dark hair pulled back, small hoop earrings
    and a warm smile. Landmarks (chin, mouth, forehead) match SPOT."""
    return f'''
  <g id="body">
    <path d="M153 94C148 60 168 37 200 37C232 37 252 60 247 94C249 110 243 120 236 124L164 124C157 120 151 110 153 94Z" fill="{HAIR}"/>
    <ellipse cx="163" cy="101" rx="7" ry="10.5" fill="{SKIN}" stroke="{INK}" stroke-width="{LINE}"/>
    <ellipse cx="237" cy="101" rx="7" ry="10.5" fill="{SKIN}" stroke="{INK}" stroke-width="{LINE}"/>
    <circle cx="162" cy="115" r="4.2" fill="none" stroke="{GOLD}" stroke-width="1.8"/>
    <circle cx="238" cy="115" r="4.2" fill="none" stroke="{GOLD}" stroke-width="1.8"/>
    <path d="M188 128V176H212V128Z" fill="{SKIN_DARK}" stroke="{INK}" stroke-width="{LINE}"/>
    <path d="M112 302L116 218C118 194 132 184 152 177L180 167C188 184 212 184 220 167L248 177C268 184 282 194 284 218L288 302Z" fill="{SHIRT}" stroke="{INK}" stroke-width="{LINE}" stroke-linejoin="round"/>
    <path d="M180 167C188 184 212 184 220 167" fill="none" stroke="{SHIRT_DARK}" stroke-width="5"/>
    <ellipse cx="200" cy="98" rx="37" ry="46" fill="{SKIN}" stroke="{INK}" stroke-width="{LINE}"/>
    <path d="M162 98C157 62 176 45 202 45C228 45 246 61 239 98C237 84 232 74 224 68C210 60 190 58 178 66C170 72 165 84 162 98Z" fill="{HAIR}"/>
    <path d="M176 52C192 55 214 58 232 70C222 58 206 50 188 49C183 49 179 50 176 52Z" fill="{HAIR_LIGHT}"/>
    <circle cx="178" cy="114" r="6" fill="#e58f7c" opacity=".28"/>
    <circle cx="222" cy="114" r="6" fill="#e58f7c" opacity=".28"/>
    <path d="M179 87Q186 82 194 86M206 86Q214 82 221 87" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>
    <ellipse cx="186" cy="98" rx="3.1" ry="3.8" fill="{INK}"/>
    <ellipse cx="214" cy="98" rx="3.1" ry="3.8" fill="{INK}"/>
    <path d="M180.5 95.5Q186 91 191.5 95M208.5 95Q214 91 219.5 95.5" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>
    <path d="M200 104Q196 113 201 115" fill="none" stroke="{INK}" stroke-width="1.8" stroke-linecap="round" opacity=".55"/>
    <path d="M185 116Q182.5 121 186 126M215 116Q217.5 121 214 126" fill="none" stroke="{SKIN_DARK}" stroke-width="1.4" stroke-linecap="round"/>
    <path d="M189 123Q200 133 211 123Q200 127 189 123Z" fill="{LIPS}" stroke="{INK}" stroke-width="1.5" stroke-linejoin="round"/>
  </g>'''


def rest_arm_svg():
    """The non-signing arm hangs by the body (signer's left = viewer's right)."""
    s, e, w = SHOULDER['left'], (266, 308), (270, 410)
    return (f'<path d="{poly([s, e])}" stroke="{INK}" stroke-width="{24 + 2 * LINE}"/>'
            f'<path d="{poly([e, w])}" stroke="{INK}" stroke-width="{20 + 2 * LINE}"/>'
            f'<path d="{poly([s, e])}" stroke="{SKIN}" stroke-width="24"/>'
            f'<path d="{poly([e, w])}" stroke="{SKIN}" stroke-width="20"/>'
            f'<path d="{poly([s, (s[0] + (e[0] - s[0]) * .42, s[1] + (e[1] - s[1]) * .42)])}" stroke="{INK}" stroke-width="{29 + 2 * LINE}"/>'
            f'<path d="{poly([s, (s[0] + (e[0] - s[0]) * .42, s[1] + (e[1] - s[1]) * .42)])}" stroke="{SHIRT}" stroke-width="29"/>')


def sign_svg(sid, sign, frames, frame=None, title=''):
    A = Anim(sign['dur'], frame)
    defs, draw = [], []

    def animated_path(pid, values):
        pid = f'{sid}-{pid}'
        a, kids = A.attr('d', values)
        defs.append(f'<path id="{pid}"{a}>{kids}</path>' if kids else f'<path id="{pid}"{a}/>')

    def use(pid, extra, vis=None):
        pid = f'{sid}-{pid}'
        if vis is None:
            return f'<use href="#{pid}"{extra}/>'
        a, kids = A.attr('visibility', vis, discrete=True)
        return f'<use href="#{pid}"{extra}{a}>{kids}</use>' if kids else f'<use href="#{pid}"{extra}{a}/>'

    order = list(enumerate(sign['hands']))
    if sign.get('mirror_second'):
        order = order[::-1]   # draw the non-dominant hand first
    if 'left' not in sign['hands'] and not sign.get('hand_only'):
        draw.append(f'<g fill="none" stroke-linecap="round">{rest_arm_svg()}</g>')

    for i, arm in order:
        if not sign.get('hand_only'):
            upper, fore, sleeve = limb_paths(frames, arm)
            animated_path(f'{arm}-up', upper)
            animated_path(f'{arm}-fo', fore)
            animated_path(f'{arm}-sl', sleeve)
            draw.append('<g fill="none" stroke-linecap="round" stroke-linejoin="round">'
                        + use(f'{arm}-up', stroke(INK, 24 + 2 * LINE)) + use(f'{arm}-up', stroke(SKIN, 24))
                        + use(f'{arm}-sl', stroke(INK, 29 + 2 * LINE)) + use(f'{arm}-sl', stroke(SHIRT, 29))
                        + use(f'{arm}-fo', stroke(INK, 19 + 2 * LINE)) + use(f'{arm}-fo', stroke(SKIN, 19))
                        + '</g>')

        hands = [f['hands'][i] for f in frames]
        hid = f'h{i}'
        animated_path(f'{hid}-palm', [smooth_closed(h['palm']) for h in hands])
        animated_path(f'{hid}-crease', [poly(h['crease']) for h in hands])
        for name in DIGITS:
            for k in range(3):
                animated_path(f'{hid}-{name}-s{k}', [poly(h['digits'][name]['pts'][k:k + 2]) for h in hands])
            for j in range(2):
                animated_path(f'{hid}-{name}-c{j}', [h['digits'][name]['creases'][j] for h in hands])
            nails = [h['digits'][name]['nail'] for h in hands]
            if any(nails):
                last = next(n for n in nails if n)
                animated_path(f'{hid}-{name}-nail', [n or last for n in nails])

        def digit(name, layer):
            vis = ['visible' if hand['digits'][name]['front'] == (layer == 'front') else 'hidden' for hand in hands]
            if all(v == 'hidden' for v in vis):
                return ''
            w = sum(h['digits'][name]['w'] for h in hands) / len(hands)
            out = ''.join(use(f'{hid}-{name}-s{k}', stroke(INK, w * TAPER[k] + 2 * LINE), vis) for k in range(3))
            out += ''.join(use(f'{hid}-{name}-s{k}', stroke(SKIN, w * TAPER[k]), vis) for k in range(3))
            out += ''.join(use(f'{hid}-{name}-c{j}', stroke(SKIN_DARK, 1.2), vis) for j in range(2))
            nail_vis = ['visible' if v == 'visible' and h['digits'][name]['nail'] else 'hidden' for v, h in zip(vis, hands)]
            if any(v == 'visible' for v in nail_vis):
                nw = w * 0.5
                out += (use(f'{hid}-{name}-nail', stroke(SKIN_DARK, nw + 1.6), nail_vis)
                        + use(f'{hid}-{name}-nail', stroke(NAIL, nw), nail_vis))
            return out

        def pad(name):
            pads = [h['digits'][name]['pad'] for h in hands]
            if all(p is None for p in pads):
                return ''
            last = next(p for p in pads if p is not None)
            pads = [p or last for p in pads]
            vis = ['visible' if h['digits'][name]['pad'] else 'hidden' for h in hands]
            i = 0
            while i < len(vis):   # drop runs of 1-2 frames: they read as a flicker
                j = i
                while j < len(vis) and vis[j] == vis[i]:
                    j += 1
                if vis[i] == 'visible' and j - i < 3 and j - i < len(vis):
                    vis[i:j] = ['hidden'] * (j - i)
                i = j
            if all(v == 'hidden' for v in vis):
                return ''
            cx, k1 = A.attr('cx', [num(p[0]) for p in pads])
            cy, k2 = A.attr('cy', [num(p[1]) for p in pads])
            r, k3 = A.attr('r', [num(p[2] + LINE) for p in pads])
            r2, k4 = A.attr('r', [num(p[2]) for p in pads])
            ny, k5 = A.attr('cy', [num(p[1] - p[2] * 0.38) for p in pads])
            rn, k6 = A.attr('r', [num(p[2] * 0.42) for p in pads])
            v, kv = A.attr('visibility', vis, discrete=True)
            return (f'<g{v}>{kv}<circle{cx}{cy}{r} fill="{INK}">{k1}{k2}{k3}</circle>'
                    f'<circle{cx}{cy}{r2} fill="{SKIN}">{k1}{k2}{k4}</circle>'
                    f'<circle{cx}{ny}{rn} fill="{NAIL}">{k1}{k5}{k6}</circle></g>')

        holes = ''
        if all('hole' in h for h in hands):
            animated_path(f'{hid}-hole', [smooth_closed(h['hole']) for h in hands])
            holes = use(f'{hid}-hole', f' fill="{INK}" fill-opacity=".22"')
        crease_vis = ['visible' if h['palm_facing'] > 0.35 else 'hidden' for h in hands]
        draw.append('<g fill="none" stroke-linecap="round" stroke-linejoin="round">'
                    + ''.join(digit(n, 'back') for n in DIGITS)
                    + use(f'{hid}-palm', f' fill="{SKIN}" stroke="{INK}" stroke-width="{num(2 * LINE)}" paint-order="stroke"')
                    + use(f'{hid}-palm', f' fill="{SKIN}"')
                    + use(f'{hid}-crease', f' stroke="{SKIN_DARK}" stroke-width="1.6"', crease_vis)
                    + holes
                    + ''.join(digit(n, 'front') for n in DIGITS)
                    + ''.join(pad(n) for n in DIGITS)
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

    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box(sign, frames)}" role="img" aria-label="{title}">'
            f'<title>{title}</title>'
            f'<defs><marker id="{sid}-tip" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="3.6" markerHeight="3.6" orient="auto-start-reverse">'
            f'<path d="M0 0L10 5L0 10Z" fill="{ACCENT}"/></marker>'
            + ''.join(defs) + '</defs>'
            + body_svg() + ''.join(draw) + f'<g opacity=".95">{arrows}{marks}</g></svg>')


def handshape_svg(sid, shape, ring=False, title=''):
    """The handshape alone, big, palm to the viewer, in the same style as the signs."""
    pose = P((0, 0), shape, 'wrist', yaw=0, pitch=0, roll=0, scale=1.0, ring=ring)
    sign = {'dur': 1.0, 'hands': ['right'], 'keys': [(0.0, [pose]), (1.0, [pose])], 'hand_only': True}
    frames = frames_for(sign)
    h = frames[0]['hands'][0]
    pts = [(q[0], q[1]) for q in h['palm']] + [(q[0], q[1]) for d in h['digits'].values() for q in d['pts']]
    xs, ys = [q[0] for q in pts], [q[1] for q in pts]
    pad = 9
    x0, x1, y0, y1 = min(xs) - pad, max(xs) + pad, min(ys) - pad, max(ys) + 14
    size = max(x1 - x0, y1 - y0)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    svg = sign_svg(f'{sid}-mao', sign, frames, frame=0, title=title)
    # Only the hand and a short wrist: drop the body.
    svg = re.sub(r'<g id="body">.*?</g>', '', svg, count=1, flags=re.S)
    svg = re.sub(r'viewBox="[^"]*"', f'viewBox="{num(cx - size / 2)} {num(cy - size / 2)} {num(size)} {num(size)}"', svg, count=1)
    wrist = (f'<path d="M0 -2V{num(size)}" stroke="{INK}" stroke-width="{num(22 + 2 * LINE)}" stroke-linecap="round"/>'
             f'<path d="M0 -2V{num(size)}" stroke="{SKIN}" stroke-width="22" stroke-linecap="round"/>')
    return svg.replace('</defs>', '</defs>' + wrist, 1)


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
                              f'Configuração de mão de {TITLES.get(sid, sid).replace("Sinal de ", "").replace(" em Libras", "")}'),
                encoding='utf-8')
        if sheet_dir:
            sheet_dir.mkdir(parents=True, exist_ok=True)
            (sheet_dir / f'{sid}-sheet.svg').write_text(review_sheet(sid, sign, frames), encoding='utf-8')


if __name__ == '__main__':
    main(sys.argv[1:])
