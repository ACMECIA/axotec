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

Sigue la guia de axotec de ifm pero sin username y password, todo se mantiene igual, lo unico que cambia es el APN: claro.pe o movistar.pe en chat-script

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


// Primer método (preferible)
sudo apt update
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker

// Otro metodo

sudo apt-get update --allow-releaseinfo-change

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker pi

sudo reboot

docker version 

<!-- docker pull debian:buster-slim -->

<!-- docker run --name debian_container -it debian:buster-slim -->
clonar el dockerfile y en la carpeta correr el buil o crear la imagen con

```
FROM balenalib/raspberry-pi-debian:stretch-build
RUN useradd --create-home --shell /bin/bash axotec_user && echo "axotec_user:axotec" | chpasswd && adduser axotec_user sudo
WORKDIR /home/axotec_user

USER axotec_user

RUN apt-get update
RUN apt-get install strongswan xl2tpd net-tools



CMD ["bash"]

```

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



### Importante bluetooth 
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

# Instalando nodered en el AXOTEC

clonar el siguiente respositorio y seguir su README

```
git clone https://github.com/dpflores/node-red-installation
```

# USO DE GPS

Instalamos el atcom para ejecutar comandos AT
```
sudo apt install python3-pip
pip3 install atcom
```


### Activando el GPS

Por defecto el GPS está desactivado, así que luego de instalar el ATCOM en python, corremos
```
atcom --port /dev/ttyUSB2 AT+CGPS=1,1
```
Para ponerlo en automático cuando encienda
```
atcom --port /dev/ttyUSB2 AT+CGPSAUTO=1
```
Para ver la data raw del GPS
```
atcom --port /dev/ttyUSB2 AT+CGPSINFO
```

Habilitar el registro de velocidad 
