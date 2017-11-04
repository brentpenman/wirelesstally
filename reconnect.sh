#! /bin/bash
while true ; do
	if ifconfig wlan0 | grep -qsw "inet" ; then
		sleep 5
	else
		echo "Network Disconnect, Reconnecting"
		ifconfig wlan0 down		
		ifconfig wlan0 up
		/bin/bash -c "/etc/init.d/dhcpcd restart"		
		sleep 10
	fi
done
