#!/usr/bin/python3
import serial
import RPi.GPIO as GPIO

ENABLE_PRINT=1

class Bluetooth(object):
   def __init__(self):
      self.ser=serial.Serial()
      self.ser.baudrate=115200
      self.ser.port='/dev/rfcomm0'
      print('Connecting to '+self.ser.name+'...')
      self.ser.open()
      print(self.ser.name+' is open.')
   
   def Close(self):
      self.ser.close()
           
class Car(object):
   in1 = 17
   in2 = 18
   in3 = 27
   in4 = 22
   enA = 12
   enB = 13
   lowPwm=10
   highPwm=80
   brzina=0
   def __init__(self):
      GPIO.setwarnings(False)
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.in1, GPIO.OUT)
      GPIO.setup(self.in2, GPIO.OUT)
      GPIO.setup(self.in3, GPIO.OUT)
      GPIO.setup(self.in4, GPIO.OUT)
      GPIO.setup(self.enA,GPIO.OUT)
      GPIO.setup(self.enB,GPIO.OUT)
      self.pwmLeft=GPIO.PWM(self.enA,50)
      self.pwmRight=GPIO.PWM(self.enB,50)
      self.pwmLeft.start(0)
      self.pwmRight.start(0)
   def destroy(self):
      if ENABLE_PRINT == 1:
         print("destroy")
      GPIO.output(self.in1,GPIO.LOW)
      GPIO.output(self.in2,GPIO.LOW)
      GPIO.output(self.in3,GPIO.LOW)
      GPIO.output(self.in4,GPIO.LOW)
      GPIO.output(self.enA,GPIO.LOW)
      GPIO.output(self.enB,GPIO.LOW)
      GPIO.cleanup()
   def forward(self):
      if ENABLE_PRINT == 1:
         print("forward")
      self.pwmLeft.ChangeDutyCycle(self.brzina)
      self.pwmRight.ChangeDutyCycle(self.brzina)
      GPIO.output(self.in1,GPIO.LOW)
      GPIO.output(self.in2,GPIO.HIGH)
      GPIO.output(self.in3,GPIO.LOW)
      GPIO.output(self.in4,GPIO.HIGH)
   def reverse(self):
      if ENABLE_PRINT == 1:
         print("reverse")
      self.pwmLeft.ChangeDutyCycle(self.brzina)
      self.pwmRight.ChangeDutyCycle(self.brzina)
      GPIO.output(self.in1,GPIO.HIGH)
      GPIO.output(self.in2,GPIO.LOW)
      GPIO.output(self.in3,GPIO.HIGH)
      GPIO.output(self.in4,GPIO.LOW)
   def turn_left(self):
      if ENABLE_PRINT == 1:
         print("turn_left")
      self.pwmLeft.ChangeDutyCycle(self.brzina)
      self.pwmRight.ChangeDutyCycle(0)
      GPIO.output(self.in1,GPIO.LOW)
      GPIO.output(self.in2,GPIO.HIGH)
      GPIO.output(self.in3,GPIO.LOW)
      GPIO.output(self.in4,GPIO.LOW)
   def turn_right(self):
      if ENABLE_PRINT == 1:
         print("turn_right")
      self.pwmLeft.ChangeDutyCycle(0)
      self.pwmRight.ChangeDutyCycle(self.brzina)
      GPIO.output(self.in1,GPIO.LOW)
      GPIO.output(self.in2,GPIO.LOW)
      GPIO.output(self.in3,GPIO.LOW)
      GPIO.output(self.in4,GPIO.HIGH)
   def stop(self):
      if ENABLE_PRINT == 1:
         print("stop")
      GPIO.output(self.in1,GPIO.LOW)
      GPIO.output(self.in2,GPIO.LOW)
      GPIO.output(self.in3,GPIO.LOW)
      GPIO.output(self.in4,GPIO.LOW)
   def forward_left(self):
      if ENABLE_PRINT == 1:
         print("forward_left")
      GPIO.output(self.in1,GPIO.LOW)
      GPIO.output(self.in2,GPIO.HIGH)
      GPIO.output(self.in3,GPIO.LOW)
      GPIO.output(self.in4,GPIO.HIGH)
      self.pwmLeft.ChangeDutyCycle(self.highPwm)
      self.pwmRight.ChangeDutyCycle(self.lowPwm)
   def forward_right(self):
      if ENABLE_PRINT == 1:
         print("forward_right")
      GPIO.output(self.in1,GPIO.LOW)
      GPIO.output(self.in2,GPIO.HIGH)
      GPIO.output(self.in3,GPIO.LOW)
      GPIO.output(self.in4,GPIO.HIGH)
      self.pwmLeft.ChangeDutyCycle(self.lowPwm)
      self.pwmRight.ChangeDutyCycle(self.highPwm)
   def backward_left(self):
      if ENABLE_PRINT == 1:
         print("backward_left")
      GPIO.output(self.in1,GPIO.HIGH)
      GPIO.output(self.in2,GPIO.LOW)
      GPIO.output(self.in3,GPIO.HIGH)
      GPIO.output(self.in4,GPIO.LOW)
      self.pwmLeft.ChangeDutyCycle(self.highPwm)
      self.pwmRight.ChangeDutyCycle(self.lowPwm)
   def backward_right(self):
      if ENABLE_PRINT == 1:
         print("backward_right")
      GPIO.output(self.in1,GPIO.HIGH)
      GPIO.output(self.in2,GPIO.LOW)
      GPIO.output(self.in3,GPIO.HIGH)
      GPIO.output(self.in4,GPIO.LOW)
      self.pwmLeft.ChangeDutyCycle(self.lowPwm)
      self.pwmRight.ChangeDutyCycle(self.highPwm)
   def speed_zero(self):
      if ENABLE_PRINT == 1:
         print("speed_zero")
      self.brzina=0
   def speed_one(self):
      if ENABLE_PRINT == 1:
         print("speed_one")
      self.brzina=10
   def speed_two(self):
      if ENABLE_PRINT == 1:
         print("speed_two")
      self.brzina=20
   def speed_three(self):
      if ENABLE_PRINT == 1:
         print("speed_three")
      self.brzina=30
   def speed_four(self):
      if ENABLE_PRINT == 1:
         print("speed_four")
      self.brzina=40
   def speed_five(self):
      if ENABLE_PRINT == 1:
         print("speed_five")
      self.brzina=50
   def speed_six(self):
      if ENABLE_PRINT == 1:
         print("speed_six")
      self.brzina=60
   def speed_seven(self):
      if ENABLE_PRINT == 1:
         print("speed_seven")
      self.brzina=70
   def speed_eight(self):
      if ENABLE_PRINT == 1:
         print("speed_eight")
      self.brzina=80
   def speed_nine(self):
      if ENABLE_PRINT == 1:
         print("speed_nine")
      self.brzina=90
   def speed_ten(self):
      if ENABLE_PRINT == 1:
         print("speed_ten")
      self.brzina=100
       
def loop():
   while True:
      rx=Bluetooth.ser.read(1)
      options[rx](Raspberry_car)

options={
    b'F':Car.forward,
    b'B':Car.reverse,
    b'L':Car.turn_left,
    b'R':Car.turn_right,
    b'G':Car.forward_left,
    b'I':Car.forward_right,
    b'H':Car.backward_left,
    b'J':Car.backward_right,
    b'S':Car.stop,
    b'0':Car.speed_zero,
    b'1':Car.speed_one,
    b'2':Car.speed_two,
    b'3':Car.speed_three,
    b'4':Car.speed_four,
    b'5':Car.speed_five,
    b'6':Car.speed_six,
    b'7':Car.speed_seven,
    b'8':Car.speed_eight,
    b'9':Car.speed_nine,
    b'q':Car.speed_ten
}

if __name__ == '__main__':
   Raspberry_car=Car()
   Bluetooth=Bluetooth()

   try:
      loop()
   except KeyboardInterrupt:
      Car.destroy(Raspberry_car)
      Bluetooth.Close()
