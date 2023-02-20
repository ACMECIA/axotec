import canopen

# Conectar al dispositivo CANopen
network = canopen.Network()
network.connect(bustype='socketcan', channel='can0', bitrate=125000)
node_id = 10
node = network.add_node(node_id, 'EDS_FILE.eds')

# Escribir el valor 1 en el sub-índice 0x08 del índice 0x1F80
node.sdo[0x1F80][0x08].raw = 1

# Desconectar del dispositivo CANopen
network.disconnect()