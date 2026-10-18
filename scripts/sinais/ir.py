# IR: index hand (1); the index first points at the signer's own chest, then the arm swings out
# in an arc to the signing side at shoulder height, the index pointing away. Once.
# (UFSC Signbank IR, INES IR1.)

_ir_one = hs_1()
_ir_self = P((186, 206), _ir_one, 'index_tip', yaw=150, pitch=-10, roll=95, scale=1.15, depth=40,
             pole=(0.4, 1.0, 0.4))
_ir_out = P((70, 170), _ir_one, 'index_tip', yaw=-10, pitch=10, roll=-100, scale=1.2, depth=110,
            via=(118, 150), pole=(0.6, 1.0, 0.3))
SIGNS['ir'] = {
    'poster': 1.4, 'dur': 2.4, 'hands': ['right'], 'handshape': _ir_one,
    'keys': [(0.0, [_ir_self]), (0.4, [_ir_self]), (1.0, [_ir_out]), (1.8, [_ir_out]),
             (2.4, [dict(_ir_self, via=(140, 230))])],
    # An arc over the path of the fingertip, from the chest out to the side.
    'arrows': [{'d': 'M 170 176 Q 126 108 80 128'}],
}
TITLES['ir'] = 'Sinal de ir em Libras'
