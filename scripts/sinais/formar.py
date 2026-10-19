# FORMAR: both hands open, the fingers spread and pointing down, together in front of the chest,
# close into fists (S), one on top of the other; then they move apart vertically: the signing hand
# rises to face height and the support hand goes down to the waist, like opening a diploma.
# (UFSC Signbank FORMAR; INES FORMAR shows the same closing and rising.)


def hs_formar_open():
    """Open beak with the fingers spread: fingers apart and a little bent, the thumb opposite them."""
    return {'index': fing(12, 18, 18, 10), 'middle': fing(3, 18, 18, 10), 'ring': fing(-7, 18, 18, 10),
            'pinky': fing(-16, 20, 18, 10), 'thumb': (20.0, 46.0, 40.0, 10.0, 10.0)}


_form_open = hs_formar_open()
_form_s = hs_S()
# Start: fingers down, backs of the hands to the viewer, side by side in front of the chest.
_form_start = P((178, 214), _form_open, 'fingertips', yaw=170, pitch=-10, roll=176, scale=1.05, depth=62,
                pole=(0.35, 1.0, 0.45))
# Closed: the two fists one on top of the other at the midline, palms turned in, thumbs up. The
# support hand is defined as a right hand and mirrored, so its `at` is chosen on the midline.
_form_top = P((176, 204), _form_s, 'wrist', yaw=-180, pitch=60, roll=90, scale=1.05, depth=66, pole=(0.35, 1.0, 0.45))
_form_bot = P((176, 232), _form_s, 'wrist', yaw=-180, pitch=60, roll=90, scale=1.05, depth=66, pole=(0.35, 1.0, 0.45))
# Apart: the signing fist up beside the face, the support fist down by the waist.
_form_up = P((112, 140), _form_s, 'wrist', yaw=-180, pitch=60, roll=80, scale=1.05, depth=60, pole=(0.5, 1.0, 0.45),
             ease='out')
_form_down = P((186, 284), _form_s, 'wrist', yaw=-180, pitch=60, roll=90, scale=1.05, depth=56, pole=(0.35, 1.0, 0.45),
               ease='out')
_form_keys = [(0.0, [_form_start, mirrored(_form_start)]), (0.25, [_form_start, mirrored(_form_start)]),
              (0.65, [_form_top, mirrored(_form_bot)]), (0.85, [_form_top, mirrored(_form_bot)]),
              (1.35, [_form_up, mirrored(_form_down)]), (2.0, [_form_up, mirrored(_form_down)]),
              (2.4, [_form_start, mirrored(_form_start)])]
SIGNS['formar'] = {
    'poster': 0.85, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _form_s,
    'keys': _form_keys,
    # The signing fist goes up, the support fist down.
    'arrows': [{'d': 'M 162 192 Q 154 174 144 166'}, {'d': 'M 248 230 Q 256 252 252 276'}],
    'mirror_second': True,
}
TITLES['formar'] = 'Sinal de formar em Libras'
