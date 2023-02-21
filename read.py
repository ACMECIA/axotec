import canopen

# Cargar archivo de configuración de dispositivo CANopen
network = canopen.Network()
network.connect(bustype='socketcan', channel='can1')
node_id = 0x20

node = network.add_node(node_id, 'G2_canopen.eds')
for obj in node.object_dictionary.values():
    print('0x%X: %s' % (obj.index, obj.name))
    if isinstance(obj, canopen.objectdictionary.Record):
        for subobj in obj.values():
            print('  %d: %s' % (subobj.subindex, subobj.name))

# Leer valor de un índice y subíndice específicos
index = 0x1000
subindex = 1


# device type: 0x1000
# quaternion: 0x2301

while True:
    x_grav = node.sdo[0x2300][0x01]
    y_grav = node.sdo[0x2300][0x02]
    z_grav = node.sdo[0x2300][0x03]

    print(x_grav.raw,y_grav.raw,z_grav.raw)


# Cerrar conexión CAN
network.disconnect()