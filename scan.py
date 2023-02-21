import canopen
import time

network = canopen.Network()
network.connect(channel='can0', bustype='socketcan', bitrate=125000)
# This will attempt to read an SDO from nodes 1 - 127
network.scanner.search()
# We may need to wait a short while here to allow all nodes to respond
time.sleep(0.05)
for node_id in network.scanner.nodes:
    print("Found node %d!" % node_id)

network.disconnect()
