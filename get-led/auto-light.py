import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = 26
light = 6

GPIO.setup(light, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

while True:
    GPIO.output(led, not GPIO.input(light))