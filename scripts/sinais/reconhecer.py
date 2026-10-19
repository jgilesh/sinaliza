# RECONHECER: V hand (index and middle up and apart), fingers up beside the eye, palm forward; it comes
# down in an arc, the wrist turning, until the V lies flat in front of the chest, palm down, fingers
# pointing to the other side, and stops there. Once. (UFSC Signbank RECONHECER: V, neutral space;
# INES RECONHECER agrees.)


def hs_reconhecer_v():
    """V: index and middle straight and apart, ring and little finger folded under the thumb."""
    shape = fist({'index': fing(12, 0, 0, 0), 'middle': fing(-8, 0, 0, 0)})
    shape['thumb'] = thumb_over(shape, ['ring'])
    return shape


_reconhecer_v = hs_reconhecer_v()
# Up: beside the eye, outside the face, palm forward and turned a little toward the face.
_reconhecer_up = P((138, 142), _reconhecer_v, 'wrist', yaw=15, pitch=-8, roll=-4, scale=1.05, depth=58,
                   pole=(0.2, 1.0, 1.2))
# Down: in front of the chest, the V lying flat with the fingers pointing across to the other side,
# palm down; the back of the hand tipped up toward the viewer so the two spread fingers read.
_reconhecer_down = P((158, 226), _reconhecer_v, 'wrist', yaw=140, pitch=0, roll=88, scale=1.12, depth=75,
                     pole=(0.45, 1.0, 0.4), via=(118, 200))
SIGNS['reconhecer'] = {
    'poster': 1.0, 'dur': 2.4, 'hands': ['right'], 'handshape': _reconhecer_v,
    'keys': [(0.0, [_reconhecer_up]), (0.35, [_reconhecer_up]), (1.0, [_reconhecer_down]), (1.8, [_reconhecer_down]),
             (2.4, [dict(_reconhecer_up, via=(110, 200))])],
    # Down in an arc from beside the eye to the front of the chest.
    'arrows': [{'d': 'M 104 130 Q 98 206 138 222'}],
}
TITLES['reconhecer'] = 'Sinal de reconhecer em Libras'
