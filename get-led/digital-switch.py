import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
button = 13
state = 0

GPIO.setup(button, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

while True:
    if(GPIO.input(button)):
        state = not state
        GPIO.output(led, state)
        time.sleep(0.2)