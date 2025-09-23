import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
light_time = 0.2
num = 0
up = 9
down = 10
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
while True:
    if GPIO.input(up):
        num = num + 1
    elif GPIO.input(down):
        num = num - 1
    if GPIO.input(up) and GPIO.input(down):
        num = 255
        time.sleep(light_time)
    dec = dec2bin(num)
    for i in range(8):
        if dec[i] == 1:
            GPIO.output(leds[i], 1)
        else:
            GPIO.output(leds[i], 0)
    time.sleep(light_time)