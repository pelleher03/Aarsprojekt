import network
from esp import epsnow

w0 = network.WLAN(network.STA_IF)  # Or network.AP_IF
w0.active(True)

e = espnow.ESPNow()
e.init()
#Mac adressen til den siste ESP32 jeg loddet, har stygge loddinger
peer = b'L\xeb\xd6{J\xa0' # MAC address of peer's wifi interface
e.add_peer(peer)

e.send("Starting...")       # Send to all peers
for i in range(100):
    e.send(peer, str(i)*20, True)
    e.send(b'end')