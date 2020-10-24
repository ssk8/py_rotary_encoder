import RPi.GPIO as GPIO
from time import sleep

A, B = 23, 24
lastEncoded = 0
encoderValue = 0

def update_encoder(channel=0):
    global lastEncoded
    global encoderValue

    MSB = GPIO.input(A) == GPIO.LOW
    LSB = GPIO.input(B) == GPIO.LOW

    encoded = (MSB << 1) |LSB
    sum  = (lastEncoded << 2) | encoded

    if(sum == 0b1101 or sum == 0b0100 or sum == 0b0010 or sum == 0b1011): encoderValue +=1
    if(sum == 0b1110 or sum == 0b0111 or sum == 0b0001 or sum == 0b1000): encoderValue -=1

    lastEncoded = encoded



GPIO.setmode(GPIO.BCM)
for pin in (A, B):
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=update_encoder)

def buttonA():
    return GPIO.input(A) == GPIO.LOW


def buttonB():
    return GPIO.input(B) == GPIO.LOW

while True:
    print(encoderValue)
    sleep(1)
