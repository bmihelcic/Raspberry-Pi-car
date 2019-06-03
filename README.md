# Raspberry-Pi-car
Rpi car using L298n H-bridge over ssh connection.
In this case battery pack was made from 3 Li-ion cells (18650 batteries) connected in series, outputing around 12V together. 12V were directly attached to Vin pin of the L298 module, and also buck-converter was used to provide stable 5V (5.08 to be precise) to the Raspberry. It's worth to mention that buck converter's output should be calibrated to around 5.05 - 5.1 V otherwise Rpi reboots constantly because of inproper voltage. Also, Raspberry was running Raspbian OS.

Control over ssh using keyboard.<br>
w - forward<br>
a - turn left<br>
d - turn right<br>
s - stop<br>
r - reverse<br>
1 - speed 1<br>
2 - speed 2<br>
3 - speed 3<br>
0 - speed 0 (stop)<br>

compile with:
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
