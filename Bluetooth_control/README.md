# Raspberry-Pi-car
Rpi car using L298n H-bridge and controlling with "Bluetooth RC Controller app".

Steps:
1. Firstly download "Arduino Bluetooth RC Car" app by Andi.Co on your smartphone.
2. Open file "sudo nano /etc/systemd/system/dbus-org.bluez.service" on Raspberry and edit two lines, it should look like:<br>
 	ExecStart=/usr/lib/bluetooth/bluetoothd -C<br>
	ExecStartPost=/usr/bin/sdptool add SP
3. Turn on Bluetooth on Raspberry and pair it with your phone (You need to pair mac addresses using "sudo bluetoothctl" command).
4. type "sudo rfcomm watch hci0" in terminal
5. In app on your phone, connect to Raspberry
6. Open another terminal and run script with "./bluetooth.py"
7. Drive :)

If you want raspberry to automatically (on reboot) listen for bluetooth connection and run the programm so you can drive right away, edit cron jobs using "sudo crontab -e" command and at the end of the file add: "@reboot /home/pi/Raspberry-Pi-car/Bluetooth_control/pi_blt_startup.sh".

You also have to install 2 modules:

sudo apt install rpi.gpio<br>
sudo pip3 install pyserial<br>
