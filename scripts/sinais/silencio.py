# SILÊNCIO: index finger up (1), placed upright on the lips, palm turned toward the other side (half
# toward the viewer, so the folded fingers and the thumb read); the hand rises to the mouth and holds.
# (INES and UFSC Signbank agree.)
_sil_1 = hs_1()
_sil_on = P((199, 108), _sil_1, 'index_tip', yaw=48, pitch=0, roll=2, scale=1.1, depth=40, pole=(0.4, 1.0, 0.45))
_sil_low = P((190, 190), _sil_1, 'index_tip', yaw=40, pitch=0, roll=8, scale=1.1, depth=50, pole=(0.4, 1.0, 0.45))
SIGNS['silencio'] = {
    'poster': 1.2, 'dur': 2.4, 'hands': ['right'], 'handshape': _sil_1,
    'keys': [(0.0, [_sil_low]), (0.2, [_sil_low]), (0.7, [_sil_on]), (1.9, [_sil_on]), (2.4, [_sil_low])],
    'marks': [(214, 124, 80)],
}
TITLES['silencio'] = 'Sinal de silêncio em Libras'
