import RPi.GPIO as GPIO
from time import sleep

rot_pin_1, rot_pin_2 = 23, 24
lastEncoded, encoderValue = 0, 0


def update_encoder(channel=0):
    global encoderValue
    global lastEncoded
    MSB = GPIO.input(rot_pin_1) == GPIO.LOW
    LSB = GPIO.input(rot_pin_2) == GPIO.LOW
    encoded = (MSB << 1) | LSB
    summed  = (lastEncoded << 2) | encoded
    if summed in (13, 4, 2, 11): encoderValue +=1
    if summed in (14, 7, 1, 8): encoderValue -=1
    lastEncoded = encoded


GPIO.setmode(GPIO.BCM)
for pin in (rot_pin_1, rot_pin_2):
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=update_encoder)

def main():
    while True:
        print(encoderValue)
        sleep(1)


if __name__ == "__main__":
    main()
