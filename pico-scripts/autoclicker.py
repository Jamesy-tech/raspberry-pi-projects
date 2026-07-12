# Made for Raspberry Pi Pico 2 W using CircuitPython [should work with most other models]
# Starts an infinite auto clicker that can be stopped by unplugging the Pi
# code.py

import time
import usb_hid
from adafruit_hid.mouse import Mouse

time.sleep(1.5)

mouse = Mouse(usb_hid.devices)

LEFT_HANDED = False # < Change if needed

BUTTON = Mouse.RIGHT_BUTTON if LEFT_HANDED else Mouse.LEFT_BUTTON

while True:
    mouse.press(BUTTON)
    time.sleep(0.02)
    mouse.release(BUTTON)
    time.sleep(0.1)
