# AVISAR: Y hand (thumb and little finger out, the other fingers folded). The thumb starts beside the
# mouth on the signing side, pointing up, the little finger out to the front; the hand moves out in a
# straight line, forward and to the signing side (toward the person being warned), and stops in front
# of the shoulder with the palm toward that person. Once. (UFSC Signbank AVISAR: Y, boca, sem contato,
# reto, da localização; the INES video agrees.)
_avisar_y = hs_Y()
# At the mouth: palm turned half toward the face, thumb up beside the mouth corner, the little finger
# pointing out and forward, so both open digits show.
_avisar_on = P((181, 124), _avisar_y, 'thumb_tip', yaw=0, pitch=40, roll=-90, scale=1.05, depth=40,
               pole=(0.5, 1.0, 0.45))
# Away: in front of the shoulder, palm toward the person warned (the viewer), thumb up, little finger out.
_avisar_off = P((122, 156), _avisar_y, 'thumb_tip', yaw=0, pitch=12, roll=-90, scale=1.12, depth=80, ease='out',
                pole=(0.5, 1.0, 0.45))
SIGNS['avisar'] = {
    'poster': 0.3, 'dur': 2.2, 'hands': ['right'], 'handshape': _avisar_y, 'handshape_view': {'yaw': 0},
    'keys': [(0.0, [_avisar_on]), (0.4, [_avisar_on]), (0.95, [_avisar_off]), (1.75, [_avisar_off]),
             (2.2, [dict(_avisar_on, ease='smooth')])],
    'arrows': [{'d': 'M 140 118 L 104 134'}],
}
TITLES['avisar'] = 'Sinal de avisar em Libras'
