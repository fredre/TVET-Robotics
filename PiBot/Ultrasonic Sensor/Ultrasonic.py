import RPi.GPIO as GPIO
import LCD1602 as LCD
import time

LCD.init(0x27,1)

TRIG = 8
ECHO = 7

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

def distance():
    GPIO.output(TRIG, 0)
    time.sleep(0.000002)

    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(ECHO) == 0:
        a = 0
        time1 = time.time()
    while GPIO.input(ECHO) == 1:
        a = 1
        time2 = time.time()
        during = time2 - time1
    return during * 340 / 2 * 100

def loop():
    while True:
        dis = distance()
        LCD.write(0,0,'Distance: %.2f' % dis)
        time.sleep(0.3)

def destroy():
    GPIO.cleanup()
    LCD.clear()
    LCD.write(5,0,'...')

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()