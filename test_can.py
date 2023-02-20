import can
import struct

can_interface = 'can0'
can_bus = can.interface.Bus(can_interface, bustype='socketcan')

# Define el ID del mensaje y la longitud de los datos
message_id = 0x10
message_length = 4

# Define la función para convertir los valores de los sensores en grados
def sensor_value_to_degrees(sensor_value):
    return sensor_value * 0.01

# Define la función para leer y procesar los datos del bus CAN
def read_can_data():
    while True:
        message = can_bus.recv()
        if message.arbitration_id == message_id and message.dlc == message_length:
            longitudinal, lateral = struct.unpack('<hh', message.data)
            longitudinal_degrees = sensor_value_to_degrees(longitudinal)
            lateral_degrees = sensor_value_to_degrees(lateral)
            print(f'Longitudinal: {longitudinal_degrees}°, Lateral: {lateral_degrees}°')

# Inicia la lectura de datos del bus CAN
read_can_data()