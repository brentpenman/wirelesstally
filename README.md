# wirelesstally
A wireless camera tally system built with Raspberry Pis


## Server Configuration:
Install screen, dnsmasq, hostapd

### dnsmasq setup:

#### /etc/dnsmasq.conf:
	dhcp-range=10.2.1.2,10.2.1.100,255.255.255.0,24h

### hostapd setup:
#### /etc/hostapd/hostapd.conf:
	interface=wlan0
	ssid=Tally
	hw_mode=g
	channel=7
	wmm_enabled=0
	macaddr_acl=0
	auth_algs=1
	ignore_broadcast_ssid=0
	wpa=2
	wpa_passphrase=tallytally
	wpa_key_mgmt=WPA-PSK
	wpa_pairwise=TKIP
	rsn_pairwise=CCMP

#### /etc/default/hostapd:
	DAEMON_CONF="/etc/hostapd/hostapd.conf"

### /etc/network/interfaces:
	source-directory /etc/network/interfaces.d

	allow-hotplug wlan0
	iface wlan0 inet static
	 address 10.2.1.1
	 netmask 255.255.255.0
	 network 10.2.1.0

### /etc/rc.local
	screen -dmS tally /bin/bash -c "/usr/bin/python /home/pi/server.py"

### /etc/wpa_supplicant/wpa_supplicant.conf
	#COMMENT OUT ALL LINES

## Client Setup

install screen

### /etc/wpa_supplicant/wpa_supplicant.conf:
	ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
	update_config=1

	network={
		ssid="Tally"
		psk="tallytally"
		key_mgmt=WPA-PSK
	}	


### /etc/rc.local:

	screen -dmS tally /bin/bash -c "/usr/bin/python /home/pi/client.py"
	screen -dmS reconnect /home/pi/reconnect.sh

