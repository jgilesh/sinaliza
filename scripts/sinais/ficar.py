# FICAR: both hands in Y (thumb and little finger out), little fingers pointing down, palms down and
# toward the body, the thumb tips touching in front of the chest; the hands go down together to the
# waist without the thumbs parting. Once. (UFSC Signbank FICAR; INES FICAR1 agrees.)
_ficar_y = hs_Y()
# Back of the hand to the viewer, little finger down, thumb across toward the other hand; tipped so
# the palm faces down and toward the body.
_ficar = lambda y, **kw: P((198, y), _ficar_y, 'thumb_tip', yaw=180, pitch=25, roll=180, scale=1.1, depth=60,
                           pole=(0.4, 1.0, 0.4), **kw)
_ficar_hi, _ficar_lo = _ficar(198), _ficar(246)
_ficar_k = lambda p: [p, mirrored(p)]
SIGNS['ficar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _ficar_y,
    'keys': [(0.0, _ficar_k(_ficar_hi)), (0.3, _ficar_k(_ficar_hi)), (0.9, _ficar_k(_ficar_lo)), (1.8, _ficar_k(_ficar_lo)),
             (2.4, _ficar_k(_ficar_hi))],
    'arrows': [{'d': 'M 108 196 L 108 248'}, {'d': 'M 292 196 L 292 248'}],
    'mirror_second': True,
}
TITLES['ficar'] = 'Sinal de ficar em Libras'
