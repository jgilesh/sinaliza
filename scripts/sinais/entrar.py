# ENTRAR: both hands flat (B). The support hand lies across in front of the chest, palm down, fingers
# toward the signing side. The dominant hand stands upright behind it, palm toward the midline, then
# moves forward in an arc over the back of the support hand and down past its fingers, tipping forward.
# Once. (UFSC Signbank ENTRAR: B+B, mão fraca dorso, para a frente, arco, contato final. The INES
# ENTRAR1 video shows another variant: the dominant hand passes under the support hand.)
_entrar_b = hs_B()
# Support (defined as a right hand, then mirrored to the left): palm down, fingers toward the signing
# side, the back tilted up a little toward the viewer.
_entrar_sup = mirrored(P((154, 218), _entrar_b, 'wrist', yaw=145, pitch=0, roll=92, scale=1.1, depth=80,
                         pole=(0.3, 1.0, 0.3)))
# Dominant: upright over the back of the support hand, near the body, palm toward the midline and a
# little toward the viewer.
_entrar_up = P((208, 224), _entrar_b, 'wrist', yaw=55, pitch=0, roll=6, scale=1.0, depth=50,
               pole=(0.45, 1.0, 0.4))
# Over and down, past the support fingertips: the hand has tipped forward and hangs, fingers down and
# toward the viewer, the back of the hand seen.
_entrar_in = P((130, 236), _entrar_b, 'wrist', yaw=50, pitch=130, roll=-10, scale=1.2, depth=100,
               pole=(0.45, 1.0, 0.4), via=(196, 166))
SIGNS['entrar'] = {
    'poster': 0.3, 'dur': 2.4, 'hands': ['right', 'left'], 'handshape': _entrar_b,
    'keys': [(0.0, [_entrar_up, _entrar_sup]), (0.35, [_entrar_up, _entrar_sup]),
             (1.0, [_entrar_in, _entrar_sup]), (1.7, [_entrar_in, _entrar_sup]),
             (2.4, [dict(_entrar_up, via=(150, 260)), _entrar_sup])],
    'arrows': [{'d': 'M 234 166 Q 160 126 112 196'}],
    # No mirror_second: the support hand is drawn in front, so the dominant hand starts behind it.
}
TITLES['entrar'] = 'Sinal de entrar em Libras'
