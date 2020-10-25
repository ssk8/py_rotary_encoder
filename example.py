from encoder import Encoder
from time import sleep

enc_pin_1 = 24
enc_pin_2 = 23
enc_button_pin = 17

encoder = Encoder(enc_pin_1, enc_pin_2, enc_button_pin)

while True:
    sleep(.5)
    print(encoder.value, encoder.enc_button_press)
    if encoder.enc_button_press:
        encoder.enc_button_press = False
