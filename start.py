import canopen

network = canopen.Network()

network.connect(channel='can0', bustype='socketcan', bitrate=125000)

for node_id in network:
    print(network[node_id])