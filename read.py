import can

# Configurar la interfaz CAN
bus = can.interface.Bus(channel='can1', bustype='socketcan')

# Leer los mensajes CAN
while True:
    message = bus.recv()
    if message.arbitration_id == 0x2301:
        print(message.data)
    #print(f"can{message.channel}  {message.arbitration_id:x}   [{message.dlc}]  {' '.join(f'{b:02x}' for b in message.data)}")