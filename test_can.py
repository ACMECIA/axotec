import libcan

# Configurar la interfaz CAN
can_interface = 'can0'  # Nombre de la interfaz CAN
bus = libcan.interface.Bus(can_interface, bustype='socketcan_native')

# Leer datos del bus CAN
while True:
    message = bus.recv()  # Esperar a que llegue un mensaje
    if message is not None:
        print(message)