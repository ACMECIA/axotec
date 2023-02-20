import can

# Configura el bus CAN
can_interface = 'can0'
bus = can.interface.Bus(can_interface, bustype='socketcan')

# Define el mensaje CAN
msg = can.Message(arbitration_id=0xA, data=[0x1F, 0x80, 0x1F, 0x08, 0x01, 0x00, 0x00, 0x00], extended_id=False)

# Envía el mensaje CAN
bus.send(msg)

# Cierra el bus CAN
bus.shutdown()