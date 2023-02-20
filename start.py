import canopen

network = canopen.Network()

network.connect(channel='can0', bustype='socketcan', bitrate=125000)
node = network.add_node(6, 'JN2100_V2.5.4.eds')

for node_id in network:
    print(node_id)
    print(network[node_id])