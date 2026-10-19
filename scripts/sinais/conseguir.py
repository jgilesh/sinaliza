# CONSEGUIR: L hand beside the head, the index pointing at the temple (back of the hand to the
# viewer, thumb up). The wrist turns so the index points up and the palm faces forward, and the hand
# comes down in an arc, out to the side and down to the front of the chest. Once, with a satisfied
# smile. (UFSC Signbank CONSEGUIR; INES CONSEGUIR.)
_con_l = hs_L()
_con_temple = P((150, 94), _con_l, 'index_tip', yaw=180, pitch=0, roll=84, scale=1.0, depth=60, pole=(0.05, 1.0, 0.9))
_con_up = P((122, 146), _con_l, 'wrist', yaw=10, pitch=0, roll=-6, scale=1.05, depth=55, pole=(0.3, 1.0, 0.6),
            ease='smooth')
_con_low = P((106, 220), _con_l, 'wrist', yaw=10, pitch=-5, roll=-2, scale=1.08, depth=60, pole=(0.5, 1.0, 0.45),
             via=(96, 180), ease='smooth')
_con_back = dict(_con_temple, via=(90, 150))
SIGNS['conseguir'] = {
    'poster': 0.0, 'dur': 2.6, 'hands': ['right'], 'handshape': _con_l,
    'keys': [(0.0, [_con_temple]), (0.35, [_con_temple]), (0.75, [_con_up]), (1.25, [_con_low]), (2.0, [_con_low]),
             (2.6, [_con_back])],
    'arrows': [{'twist': 0, 'at': 0.0, 'r': (16, 6), 'drop': 6},
               {'d': 'M 154 138 Q 168 162 158 188'}],
}
TITLES['conseguir'] = 'Sinal de conseguir em Libras'
