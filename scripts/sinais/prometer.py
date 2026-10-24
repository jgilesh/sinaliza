# PROMETER: both hands flat (B). The signing hand goes up beside the shoulder, palm forward and
# fingers up, as in an oath; the other hand lies flat on the chest, palm toward the body. They reach
# that position and hold it. (UFSC Signbank PROMETER: B+B, chest; the INES PROMETER video shows only the
# raised hand.)



def hs_prometer_flat():
    """B with the thumb a little closer to the index than the atlas B (raised beside the head, the
    atlas thumb would reach the earring)."""
    shape = hs_B()
    shape['thumb'] = (12.0, 14.0, 8.0, 6.0, 4.0)
    return shape


_prometer_b = hs_prometer_flat()
# Raised hand: palm to the viewer, fingers up, beside the head and clear of the face.
_prometer_up = P((108, 160), _prometer_b, 'wrist', yaw=0, pitch=0, roll=-12, scale=1.1, depth=70, pole=(0.05, 1.0, 0.1))
_prometer_low = P((128, 238), _prometer_b, 'wrist', yaw=0, pitch=40, roll=-14, scale=1.05, depth=60, pole=(0.3, 1.0, 0.4))
# Hand on the chest, defined as a right hand (back to the viewer, fingers toward the viewer's right)
# and mirrored: the left hand's fingers point across the body toward the signer's right.
_prometer_chest = mirrored(P((166, 222), _prometer_b, 'wrist', yaw=180, pitch=6, roll=80, scale=1.12, depth=22,
                             pole=(0.6, 1.0, 0.2)))
_prometer_chest_off = mirrored(P((152, 246), _prometer_b, 'wrist', yaw=180, pitch=30, roll=70, scale=1.08, depth=50,
                                 pole=(0.6, 1.0, 0.3)))
SIGNS['prometer'] = {
    'poster': 0.9, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _prometer_b,
    'keys': [(0.0, [_prometer_low, _prometer_chest_off]), (0.25, [_prometer_low, _prometer_chest_off]),
             (0.8, [dict(_prometer_up, ease='out'), dict(_prometer_chest, ease='out')]),
             (2.0, [_prometer_up, _prometer_chest]),
             (2.6, [_prometer_low, _prometer_chest_off])],
    'marks': [(256, 210, 60)],
    # Up beside the shoulder, on the outer side of the raised hand.
    'arrows': [{'d': 'M 80 226 Q 74 196 80 168'}],
    'mirror_second': True,
}
TITLES['prometer'] = 'Sinal de prometer em Libras'
