# Raspberry-Pi-car
Rpi car using L298n H-bridge

make with:
gcc -Wall -lwiringPi keyboard_control.c -o keyboard_control

run with:
sudo ./keyboard_control


| Name | wiringPi | BCM	  | Physical |
| ---  |:--------:| -----:| --------:| 
| in1  | 0        | 17 	  | 11       |
| in2  | 1  	  | 18 	  | 12       | 
| in3  | 2  	  | 27 	  | 13       | 
| in4  | 3  	  | 22    | 15       |
| enA  | 26 	  | 12    | 32       | 
| enB  | 23 	  | 13    | 33       | 
