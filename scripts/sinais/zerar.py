# ZERAR: the flat hand, palm forward, beside the head on the signing side, sweeps across in front of
# the chin to the other side, palm turning down (as if wiping), and comes back to beside the head,
# closing into O seen from the side. Once. (UFSC Signbank ZERAR: B + O, arc contralateral and back;
# INES ZERAR.)

_zerar_b, _zerar_o = hs_B(), hs_O()
# Beside the head, palm forward, fingers up.
_zerar_start = P((118, 150), _zerar_b, 'wrist', yaw=0, pitch=0, roll=-4, scale=1.05, depth=50, pole=(0.6, 1.0, 0.45))
# Across in front of the chin: palm down, fingers pointing to the other side.
_zerar_across = P((196, 160), _zerar_b, 'wrist', yaw=135, pitch=0, roll=86, scale=1.05, depth=70,
                  pole=(0.4, 1.0, 0.45))
# On the way across: low, below the chin, the palm already turning down (keeps the face clear).
_zerar_mid = P((150, 186), _zerar_b, 'wrist', yaw=80, pitch=0, roll=62, scale=1.05, depth=62, pole=(0.45, 1.0, 0.45),
               ease='linear')
# Back beside the head in O, seen from the thumb side so the round opening reads.
_zerar_end = P((126, 146), _zerar_o, 'wrist', yaw=-100, pitch=15, roll=0, scale=1.15, depth=55,
               pole=(0.5, 1.0, 0.4), via=(160, 150), ease='out')
SIGNS['zerar'] = {
    'poster': 1.5, 'dur': 2.6, 'hands': ['right'], 'handshape': _zerar_o, 'handshape_view': {'yaw': -100, 'pitch': 15},
    'keys': [(0.0, [_zerar_start]), (0.35, [_zerar_start]), (0.6, [_zerar_mid]), (0.85, [_zerar_across]), (1.3, [_zerar_end]),
             (2.1, [_zerar_end]), (2.6, [dict(_zerar_start, ease='smooth')])],
    # Across (upper arrow), then back to the signing side (lower arrow).
    'arrows': [{'d': 'M 122 186 Q 172 200 234 180'}, {'d': 'M 232 204 Q 172 226 122 202'}],
}
TITLES['zerar'] = 'Sinal de zerar em Libras'
