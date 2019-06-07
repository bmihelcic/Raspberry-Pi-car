#!/bin/bash
sudo rfcomm watch hci0 &>/dev/null &
sleep 10
/home/pi/car_project/Bluetooth/bluetooth.py

