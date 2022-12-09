#!/usr/bin/python3
import RPi.GPIO as GPIO
from time import sleep
import math
import LCD1602 as LCD

LCD.init(0x27,1)


leftsensor = 21
rightsensor = 20
leftpulse = 0
leftrotation = 0
rightpulse = 0
rightrotation = 0

def init_GPIO():# initialize GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(leftsensor,GPIO.IN,GPIO.PUD_UP)
    GPIO.setup(rightsensor,GPIO.IN,GPIO.PUD_UP)

def calculate_left(channel):              # callback function
    global leftpulse, leftrotation
    leftpulse += 1                        # increase pulse by 1 whenever interrupt occurred
    leftrotation=leftpulse/20
    
def calculate_right(channel):             # callback function
    global rightpulse,rightrotation
    rightpulse += 1                       # increase pulse by 1 whenever interrupt occurred
    rightrotation=rightpulse/20

def init_interrupt():
    GPIO.add_event_detect(leftsensor, GPIO.FALLING, callback = calculate_left, bouncetime = 20)
    GPIO.add_event_detect(rightsensor, GPIO.FALLING, callback = calculate_right, bouncetime = 20)

try:
    init_GPIO()
    init_interrupt()
    while True:
        LCD.write(0,0,'left: ')
        LCD.write(8,0, str(leftrotation))
        LCD.write(0,1,'Right:  ')
        LCD.write(8,1, str(rightrotation))
        sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print('GPIO cleaned')