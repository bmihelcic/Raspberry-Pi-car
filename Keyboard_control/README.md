# Raspberry-Pi-car
Rpi car using L298n H-bridge over ssh connection.

compile with:
gcc -Wall -lwiringPi keyboard_control.c -o keyboard_control

run with:
sudo ./keyboard_control

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

