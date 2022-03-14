from machine import Pin,PWM
from servo import Servo 
import time

servo_pin = Pin(15)
my_servo = Servo(servo_pin, 330, 500, 2500, 120)

print('15')
my_servo.write_angle(15)
time.sleep(2)
print('90')
my_servo.write_angle(90)
time.sleep(2)
print('110')
my_servo.write_angle(110)