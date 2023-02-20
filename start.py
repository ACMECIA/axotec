import canopen
import time

network = canopen.Network()

network.connect(channel='can0', bustype='socketcan', bitrate=125000)

node = network.add_node(6, 'JN2100_V2.5.4.eds')     # El JN2100

for node_id in network:
    print(node_id)
    print(network[node_id])

# Watch the index and subindex
for obj in node.object_dictionary.values():
    print('0x%X: %s' % (obj.index, obj.name))
    if isinstance(obj, canopen.objectdictionary.Record):
        for subobj in obj.values():
            print('  %d: %s' % (subobj.subindex, subobj.name))


# This will attempt to read an SDO from nodes 1 - 127
# network.scanner.search()
# # We may need to wait a short while here to allow all nodes to respond
# time.sleep(0.05)
# for node_id in network.scanner.nodes:
#     print("Found node %d!" % node_id)