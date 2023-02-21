import canopen

import math

def quaternion_to_euler(w,x,y,z):
    # Convierte un cuaternión (w, x, y, z) a ángulos de Euler (pitch, roll, yaw)
    # q: tupla (w, x, y, z) que representa el cuaternión
    
    # Normaliza el cuaternión

    norm = math.sqrt(w**2 + x**2 + y**2 + z**2)
    w /= norm
    x /= norm
    y /= norm
    z /= norm
    
    # Calcula los ángulos de Euler
    roll = math.atan2(2*(w*x + y*z), 1 - 2*(x**2 + y**2))
    pitch = math.asin(2*(w*y - z*x))
    yaw = math.atan2(2*(w*z + x*y), 1 - 2*(y**2 + z**2))
    
    # Convierte de radianes a grados
    roll = math.degrees(roll)
    pitch = math.degrees(pitch)
    yaw = math.degrees(yaw)
    
    return pitch, roll, yaw

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

## QUATERNIONS
# while True:
#     w = node.sdo[0x2301][0x01].raw
#     x = node.sdo[0x2301][0x02].raw
#     y = node.sdo[0x2301][0x03].raw
#     z = node.sdo[0x2301][0x03].raw

#     pitch,roll,yaw = quaternion_to_euler(w,x,y,z)

#     print(pitch,roll,yaw)

## GRAVITY
# while True:
#     x_grav = node.sdo[0x2300][0x01].raw
#     y_grav = node.sdo[0x2300][0x02].raw
#     z_grav = node.sdo[0x2300][0x03].raw

#     print(x_grav,y_grav,z_grav)


# X Y SLOPE
while True:
    x_slope = node.sdo[0x2000].raw/(2**15)*180

    y_slope = node.sdo[0x2200].raw/(2**15)*180

    print(math.round(x_slope,2), math.round(y_slope,2))



# Cerrar conexión CAN
network.disconnect()