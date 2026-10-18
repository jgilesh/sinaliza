# COM LICENÇA: both hands flat with the thumb up, palms toward the body, fingers pointing at each other;
# the fingertips of the dominant hand touch those of the other hand in front of the chest, and the
# hands, still touching, move back toward the body and a little up, once. (INES COM LICENÇA, UFSC
# Signbank COM-LICENÇA.)


def hs_licenca_B():
    """Flat hand, fingers together and straight, the thumb raised in the palm plane (like an L)."""
    shape = hs_B()
    shape['thumb'] = (48.0, 10.0, 0.0, 4.0, 2.0)
    return shape


_lic_b = hs_licenca_B()
# Back of the hand to the viewer, fingers turned toward the midline (roll), thumb up.
_lic_out = P((199, 214), _lic_b, 'fingertips', yaw=180, pitch=0, roll=88, scale=1.1, depth=75)
_lic_in = P((199, 200), _lic_b, 'fingertips', yaw=180, pitch=-10, roll=86, scale=1.02, depth=45, ease='smooth')
SIGNS['com-licenca'] = {
    'poster': 0.4, 'dur': 2.2, 'hands': ['right', 'left'], 'handshape': _lic_b,
    'handshape_view': {'yaw': 0},
    'keys': [(0.0, [_lic_out, mirrored(_lic_out)]), (0.4, [_lic_out, mirrored(_lic_out)]),
             (1.0, [_lic_in, mirrored(_lic_in)]), (1.7, [_lic_in, mirrored(_lic_in)]),
             (2.2, [_lic_out, mirrored(_lic_out)])],
    # Toward the body and up, above the fingertips (between the thumbs).
    'arrows': [{'d': 'M 200 190 V 168'}],
    # The fingertips touch each other.
    'marks': [(200, 236, 180)],
    'mirror_second': True,
}
TITLES['com-licenca'] = 'Sinal de com licença em Libras'
