# EXCLUIR: the support hand lies open in front of the waist, palm up. The signing hand, open and flat
# (B), palm down, comes onto it, slides across the support palm scraping it and goes off to the dominant
# side, as if taking something out of there. Once. (UFSC Signbank EXCLUIR; the INES EXCLUIR1 video shows
# another variant: one open hand sweeping out to the side, no support hand.)


def hs_excluir_flat():
    """B lying palm up (support): flat hand, fingers together, the thumb along the side of the index (an
    open thumb would point at the viewer and show only as its tip)."""
    return {'index': fing(2, 0, 0, 0), 'middle': fing(0, 0, 0, 0), 'ring': fing(-2, 0, 0, 0),
            'pinky': fing(-4, 0, 0, 0), 'thumb': (-8.0, 6.0, 10.0, 6.0, 4.0)}


_excluir_b, _excluir_sup = hs_B(), hs_excluir_flat()
_excluir_pole = (0.4, 1.0, 0.45)
# Support hand (defined as a right hand, then mirrored): palm up, tipped a little toward the viewer, the
# fingers pointing across toward the midline.
_excluir_base = mirrored(P((144, 266), _excluir_sup, 'wrist', yaw=-50, pitch=15, roll=94, scale=1.1, depth=70))


def _excluir_top(at, **kw):
    # Palm down, the fingers pointing across toward the support hand, the back of the hand turned a little
    # toward the viewer.
    return P(at, _excluir_b, 'fingertips', yaw=125, pitch=0, roll=92, scale=1.1, depth=kw.pop('depth', 76),
             pole=_excluir_pole, **kw)


_excluir_above = _excluir_top((262, 220))
_excluir_on = _excluir_top((262, 252), ease='in')
_excluir_out = _excluir_top((150, 246), depth=70, ease='out')
SIGNS['excluir'] = {
    'poster': 0.7, 'dur': 2.6, 'hands': ['right', 'left'], 'handshape': _excluir_b,
    'keys': [(t, [p, _excluir_base]) for t, p in [(0.0, _excluir_above), (0.3, _excluir_above),
                                                 (0.6, _excluir_on), (0.75, _excluir_on), (1.35, _excluir_out),
                                                 (2.0, _excluir_out),
                                                 (2.6, dict(_excluir_above, via=(200, 200), ease='smooth'))]],
    'marks': [(246, 246, 20)],
    # Above the hands: across the support palm and out to the dominant side.
    'arrows': [{'d': 'M 236 198 L 120 198'}],
    'mirror_second': True,
}
TITLES['excluir'] = 'Sinal de excluir em Libras'
