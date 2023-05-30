# Información importante
Debian 9/Stretch based Raspbian system


# Ethernet connection

IP del ethernet del Axotec: 192.168.100.200

Poner una IP similar en wired connection en la computadora local como 192.168.100.1 yluego

ssh root@192.168.100.20

password: axotec

# Install accelerometer

scp -r bma280-accelerometer-5.4.65-install pi@192.168.100.200:/home/pi/Del

in the folder run

sudo ./setup.py

# Conexión a wifi

sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

Insertar 
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=PE

network={
	ssid="ACME0"
	psk="Electronic2016!"
	key_mgmt=WPA-PSK
}
```
Despues

sudo nano /etc/dhcpcd.conf 

comentar las últimas 2 líneas

static routers=192.168.100.1
static domain_name_servers=192.168.100.1 8.8.8.8

Tambien para cambiar la IP estática del eth0, cambiamos el 
192.168.100.200 
por
192.168.82.200
por convención de ACME

Para poner una IP estática de wifi agregamos


interface wlan0
static ip_address=192.168.82.xxx/24
static routers=192.168.82.1
static domain_name_servers=192.168.82.1

se recomiendo priemro conectar al wifi y que la ip se asigne solo, luego poner esa ip en la linea anterior

# Corriendo comandos AT

apt install minicom

correr para configurar, seleccionar la interfaz que se quiera manejar
ttyUSB2 para el chip
 


minicom -b 115200 -D /dev/ttyUSB2


ahora podremos correr los comandos AT
por ejemplo si ejecutamos AT, veremos OK como retorno


Ahora, podemos utilizar atcom de python que tambien funciona como terminal,
pip3 install atcom

y en la terminal podemos correr para reiniciar la interfaz, esto no sirve cuando se pierde la comunicación con el chip
atcom --port /dev/ttyUSB2 AT+CRESET

# Conexion a datos móviles


NUEVA FORMA DE HACERLO 

Sigue la guia de axotec de ifm pero sin username y password, todo se mantiene igual, lo unico que cambia es el APN: claro.pe o movistar.pe en `/etc/ppp/chat-script`

Adicionalmente:
nano /etc/ppp/peers/provider

cambiar por lo siguiente 

```
# example configuration for a dialup connection authenticated with PAP or CHAP
#
# This is the default configuration used by pon(1) and poff(1).
# See the manual page pppd(8) for information on all the options.

# MUST CHANGE: replace myusername@realm with the PPP login name given to
# your by your provider.
# There should be a matching entry with the password in /etc/ppp/pap-secrets
# and/or /etc/ppp/chap-secrets.

#user "myusername@realm"
user ""

# MUST CHANGE: replace ******** with the phone number of your provider.
# The /etc/chatscripts/pap chat script may be modified to change the
# modem initialization string.

#connect "/usr/sbin/chat -v -f /etc/chatscripts/pap -T ********"
connect "/usr/sbin/chat -v -f /etc/chatscripts/pap -T "

# Serial device to which the modem is connected.
/dev/modem

# Speed of the serial line.

#115200
9600

# Assumes that your IP address is allocated dynamically by the ISP.
noipdefault
# Try to get the name server addresses from the ISP.
usepeerdns
# Use this connection as the default route.
defaultroute

# Makes pppd "dial again" when the connection is lost.
persist

# Do not ask the remote to authenticate.
noauth

```

# Cambio de zona horaria

ejecutar 

raspi-config

y cambiar la zona horaria a la de Lima



# Instalando docker

// Metodo principal
https://docs.docker.com/engine/install/debian/




docker build -t axotec_image .

docker run --name axotec_container --network host -it axotec_image 

docker run --name vpn_container --network host -it vpn_image

docker run -it -p 1880:1880 --name mynodered --restart always nodered/node-red


# VPN 
ref
https://github.com/hwdsl2/setup-ipsec-vpn/blob/master/docs/clients.md#configure-linux-vpn-clients-using-the-command-line

sudo apt-get update
password: axotec

apt-get update
apt-get upgrade



```
apt-get install strongswan xl2tpd net-tools

VPN_SERVER_IP='137.184.105.94'	
VPN_IPSEC_PSK='Mikrotik123*'

VPN_USER='ACMCel'
VPN_PASSWORD='121383Loco!'

```



ip route

192.168.88.1


sudo ipsec up myvpn
sudo echo "c myvpn" > /var/run/xl2tpd/l2tp-control
ip route

192.168.88.1

route add 137.184.105.94 gw 192.168.88.1

route add 137.184.105.94 gw 192.168.253.169
route add default dev ppp0
wget -qO- http://ipv4.icanhazip.com; echo

revisar el IP con ifconfig que puede variar por la red
ssh pi@192.168.88.125


para acceder del axotec a mi localhost, revisar con ifconfig el ip de ppp0

ssh del@10.0.0.99


## Axotec de horno KOMATSU 

### OpenVPN
en la carpeta `/home/del/Del/ACME/AXOTEC/komatsu_vpn` ejecutar

openvpn3 session-start --config userKomatsuLE200_01_User.ovpn


### Para desconectarse de la VPN
openvpn3 sessions-list
openvpn3 session-manage --session-path /net/openvpn/v3/sessions/6927bc78saa3ds415bsb07es5170bbce2e69 --disconnect


 
ssh root@10.20.0.31

### VPN ACME

Configurar el usuario PROYECTOS4 y su IP estática es 10.0.0.2

```
apt-get install strongswan xl2tpd net-tools

VPN_SERVER_IP='137.184.105.94'
VPN_IPSEC_PSK='Mikrotik123*'
VPN_USER='PROYECTOS4'
VPN_PASSWORD='121383Loco!'

```
```
VPN_SERVER_IP='137.184.105.94'
VPN_IPSEC_PSK='Mikrotik123*'
VPN_USER='PROYECTOS5'
VPN_PASSWORD='121383Loco!'
```
systemctl status 




### Ver la IP pública 

wget -qO- http://ipv4.icanhazip.com; echo

### Servicios linux

Para ver en tiempo real 
journalctl -u mobile_data.service -f


### Acelerómetro

se cambió en el archivo /sys/bus/iio/devices/iio\:device0/power/control 

de `auto` a `on` para que no sea manejado por el sistema de power management


# GPS

Activando el GPS

Por defecto el GPS está desactivado, así que luego de instalar el ATCOM en python, corremos

```
atcom --port /dev/ttyUSB2 AT+CGPS=1,1
```
Para ponerlo en automático cuando encienda

```
atcom --port /dev/ttyUSB2 AT+CGPS=0,1    # se detiene el gps
atcom --port /dev/ttyUSB2 AT+CGPSAUTO=1  # se activa el modo auto
atcom --port /dev/ttyUSB2 AT+CGPS=1,1    # se activa de nuevo
```

Para habilitar correctamente la obtencion de velocidad y posicionamiento

```
atcom --port /dev/ttyUSB2 AT+CGPS=0,1          # se detiene el gps
atcom --port /dev/ttyUSB2 AT+CGPSNMEA=198143   # se configura
atcom --port /dev/ttyUSB2 AT+CGPS=1,1          # se activa de nuevo
```

Para verificar que hemos editado el nmea correctamente, corremos 

```
atcom --port /dev/ttyUSB2 AT+CGPSNMEA? 
```
y deberíamos de obtener  `+CGPSNMEA: 198143` como respuesta, en caso no sea, mirar la documentación de los comandos AT para GPS y ver si los bits que se requieren están activados.

Para ver la posición del GPS

```
atcom --port /dev/ttyUSB2 AT+CGPSINFO
```

Podemos visualizar toda la data que se envía por el puerto serial (ttyUSB1) de la siguiente forma:

```
cat /dev/ttyUSB1
```

Si no se obtiene data, esperar unos minutos, sino hacer un cold start y esperar nuevamente unos minutos.

```
atcom --port /dev/ttyUSB2 AT+CGPSCOLD
```

# Bluetooth
quitarle los permisos de escritura al archivo ```btuart```


### CAN Bus

ip link set down can1
ip link set can1 up type can bitrate 250000 listen-only on
ip link set can1 up type can bitrate 250000 listen-only off


##JD2120
ip link set down can1
ip link set can1 up type can bitrate 125000

ip link set down can0
ip link set can0 up type can bitrate 125000
# para ver el can 
candump can1

# Instalando nodered localmente

```
sudo apt-get update && sudo apt-get upgrade

sudo apt-get install nodejs
sudo apt-get install npm

```

```
sudo npm install -g --unsafe-perm node-red

```


ejecutar `node-red`


Ahora creamos un servicio 

sudo nano /etc/systemd/system/node-red.service

y pegamos lo siguiente 

```
[Unit]
Description=Node-RED
After=network.target

[Service]
ExecStart=/usr/bin/env node-red-pi --max-old-space-size=256 -v
Restart=on-failure
KillSignal=SIGINT

[Install]
WantedBy=multi-user.target
```

ejecutamos `sudo systemctl daemon-reload` y `sudo systemctl enable node-red.service`

y si funciona, cuando hagamos reboot, el nodered debería estar en el localhost:1880

# Configurar el AXOTEC como wireless Access Point




Primero habilitar el servidor dhcp
https://thepi.io/how-to-use-your-raspberry-pi-as-a-wireless-access-point/
seguir ese link pero solo para el dhcp

Primero instalamos el dnsmasq, que será el servidor DHCP y DNS

```
sudo apt-get install dnsmasq

```

Como lo vamos a modificar, entonces detenemos el servicio

```
sudo systemctl stop hostapd

```

Primero configuramos un IP estatico para la interfaz wlan0, para modificar el archivo, ejecutamos 

```
sudo nano /etc/dhcpcd.conf
```

Al final del archivo agregamos lo siguiente

```
interface wlan0
static ip_address=192.168.0.10/24
```

De quere hacer lo mismo con el ethernet es lo mismo, solo utilizar la interfaz `eth0`, pero esto ya se hace normalmente con la IP `192.168.82.200`

Ahora configuramos el archivo de configración del servidor DCHP, para lo cuál primero se recomienda guardar la configuración predeterminada

```
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig
```

Y luego editamos un nuveo archivo

```
sudo nano /etc/dnsmasq.conf

```
donde agregaremos las siguientes líneas 

```
interface=wlan0
  dhcp-range=192.168.0.11,192.168.0.30,255.255.255.0,24h
```

Esto significa que el servidor proveerá direcciones IP entre `192.168.0.11` hasta `192.168.0.30` en la interfaz `wlan0`.


Luego habilitamos la conexion por wifi al axotec 
https://raspberrypi.stackexchange.com/questions/88214/setting-up-a-raspberry-pi-as-an-access-point-the-easy-way/88234#88234

revisar el link si se desea otras configuraciones


Primero realizamos la configuración básica para crear el access point con lo siguiente

```
cat > /etc/wpa_supplicant/wpa_supplicant-wlan0.conf <<EOF
country=PE
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="Axotec"
    mode=2
    frequency=2437
    #key_mgmt=NONE   # uncomment this for an open hotspot
    # delete next 3 lines if key_mgmt=NONE
    key_mgmt=WPA-PSK
    proto=RSN WPA
    psk="password"
}
EOF

chmod 600 /etc/wpa_supplicant/wpa_supplicant-wlan0.conf
systemctl disable wpa_supplicant.service
systemctl enable wpa_supplicant@wlan0.service
rfkill unblock wlan
```
En estas líneas principalmente importa la definición del `SSID`, que es el nombre de la red y el `PSK`, que es la contraseña de esta 


## Access ponit simple por wifi
Esta configuración permite el conectarse a la red del axotec por wifi
```
cat > /etc/systemd/network/08-wlan0.network <<EOF
[Match]
Name=wlan0
[Network]
Address=192.168.0.10/24
MulticastDNS=yes
DHCPServer=yes
EOF
```

Tener en cuenta la `IP` del Axotec, que hemos configurado previamente de forma estática

Con esto ya estaría el access point con el Axotec, el procedimiento es similar si se desea que se utilice la interfaz `eth0`, solo que sinla configuración access point.

`configurar IP estática -> configurar servidor DHCP para eth0`
