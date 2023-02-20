import can

# Configura la interfaz CAN
can_interface = 'can0'
bus = can.interface.Bus(can_interface, bustype='socketcan')

# Lee los mensajes del bus CAN
while True:
    message = bus.recv()
    if message is not None:
        print(f"ID: {message.arbitration_id}  Data: {message.data}")