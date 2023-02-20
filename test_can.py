import can

# Crear una instancia de la clase Bus para la interfaz CAN
bus = can.interface.Bus(channel='can0', bustype='socketcan')

# Crear un mensaje RTR para solicitar datos del nodo con ID de arbitraje 0x10
rtr_msg = can.Message(arbitration_id=0x10, is_remote_frame=True, dlc=8)

# Enviar el mensaje RTR
bus.send(rtr_msg)

# Esperar y recibir la respuesta del nodo
response_msg = bus.recv()

# Mostrar el mensaje de respuesta
print(response_msg)