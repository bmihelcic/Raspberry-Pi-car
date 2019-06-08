# Raspberry-Pi-car
Rpi car using L298n H-bridge and controlling with "Bluetooth RC Controller app".

Steps:
1. Firstly download "Arduino Bluetooth RC Car" app by Andi.Co on your smartphone.
2. Turn on Bluetooth on Raspberry and pair it with your phone (You need to pair mac addresses using "sudo bluetoothctl" command).
3. type "sudo rfcomm watch hci0" in terminal
4. In app on your phone, connect to Raspberry
5. Open another terminal and run script with "./bluetooth.py"
6. Drive :)

If you want raspberry to automatically run these commands after reboot, edit cron jobs using "sudo crontab -e" command and at the end of the file add: "@reboot /home/pi/Raspberry-Pi-car/Bluetooth_control/Pi_blt_startup.sh"
You also have to install 2 modules:

sudo apt install rpi.gpio<br>
sudo pip3 install pyserial<br>
