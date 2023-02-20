import can

can_interface = 'can0'  # nombre de la interfaz CAN
bus = can.interface.Bus(can_interface, bustype='socketcan', bitrate=125000)  # inicialización del bus CAN

message = can.Message(arbitration_id=0xA, data=[0x01, 0x1F, 0x80, 0x08, 0x01, 0x00, 0x00, 0x00], is_extended_id=False)  # creación del mensaje para ejecutar Autostart a 1
bus.send(message)  # envío del mensaje al bus CAN