import LCD1602
import RPi.GPIO as GPIO          
from time import sleep

LCD1602.init(0x27,1)

in1 = 14
in2 = 15
in3 = 23
in4 = 24
enA = 18
enB = 25
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
pA=GPIO.PWM(enA,1000)
pB=GPIO.PWM(enB,1000)

def fwd():
    LCD1602.clear()
    LCD1602.write(2,0, 'Forward')
    pA.ChangeDutyCycle(50)
    pB.ChangeDutyCycle(50)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def rev():
    LCD1602.clear()
    LCD1602.write(2,0, 'Reverse')
    pA.ChangeDutyCycle(50)
    pB.ChangeDutyCycle(50)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def left_turn():
    LCD1602.clear()
    LCD1602.write(2,0, 'Left Turn')
    pA.ChangeDutyCycle(30)
    pB.ChangeDutyCycle(30)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    
def right_turn():
    LCD1602.clear()
    LCD1602.write(2,0, 'Right Turn')
    pA.ChangeDutyCycle(30)
    pB.ChangeDutyCycle(30)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    LCD1602.clear()
    LCD1602.write(4,0, 'Stop')
                
pA.start(25)
pB.start(25)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("\n")    

try:
    while(1):
        fwd()
        sleep(1)
        left_turn()
        sleep(1)
        rev()
        sleep(1)
        right_turn()
        sleep(1)
        stop()
        sleep(2)
        

except KeyboardInterrupt:
    GPIO.cleanup()
    LCD1602.clear()
    sleep(0.2)
    LCD1602.write(3,0,"Program End")
    print('Program stopped')
        