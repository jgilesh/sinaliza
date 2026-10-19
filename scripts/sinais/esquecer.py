# ESQUECER: flat hand (fingers together), the fingertips on the side of the forehead, palm toward it;
# the hand leaves the forehead out to the side and a little up and closes into a fist on the way,
# ending beside the head with the palm forward. Once. (UFSC Signbank ESQUECER; the INES video keeps
# the hand flat as it slides off the forehead.)

_esquecer_b = hs_B()
_esquecer_b['thumb'] = (-22.0, 18.0, 20.0, 8.0, 6.0)   # thumb alongside the index
_esquecer_s = hs_S()
# Fingertips on the forehead (dominant side), back of the hand to the viewer, like a salute.
_esquecer_on = P((172, 64), _esquecer_b, 'fingertips', yaw=140, pitch=0, roll=62, scale=1.0, depth=40,
                 pole=(0.7, 1.0, 0.45))
# Out to the side and up, closed: a fist beside the head, palm turned forward.
_esquecer_off = P((116, 96), _esquecer_s, 'wrist', yaw=25, pitch=0, roll=-10, scale=1.08, depth=55,
                  pole=(0.7, 1.0, 0.45), via=(140, 66), ease='out')
SIGNS['esquecer'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right'], 'handshape': _esquecer_b,
    'keys': [(0.0, [_esquecer_on]), (0.35, [_esquecer_on]), (1.0, [_esquecer_off]), (1.9, [_esquecer_off]),
             (2.4, [dict(_esquecer_on, via=(140, 96), ease='smooth')])],
    'marks': [(176, 52, -20)],
    'arrows': [{'d': 'M 150 40 Q 120 30 96 44'}],
}
TITLES['esquecer'] = 'Sinal de esquecer em Libras'
