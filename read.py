import canopen

# Cargar archivo de configuración de dispositivo CANopen
network = canopen.Network()
network.connect(bustype='socketcan', channel='can1')
node_id = 0x20
network.add_node(node_id, 'G2_canopen.eds')

# Leer valor de un índice y subíndice específicos
index = 0x1000
subindex = 1
value = network[node_id].sdo[index][subindex].raw

# Cerrar conexión CAN
network.disconnect()