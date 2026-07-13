# Made for Raspberry Pi Pico 2 W using Circuit Python [should work with most other models]
# This script quickly opens YouTube, subscribes to the desired channel and closes it
# code.py

import time
import board
import digitalio
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

time.sleep(0)

led.value = True
time.sleep(0.15)
led.value = False

keyboard.release_all()
time.sleep(0.05)

keyboard.press(Keycode.CONTROL)
keyboard.press(Keycode.T)
time.sleep(0.05)
keyboard.release_all()

time.sleep(0.05)

layout.write("https://www.youtube.com/channel/UCBeRITLbzQs2WLP1U7vJ3SQ?sub_confirmation=1")

keyboard.send(Keycode.ENTER)
keyboard.release_all()

time.sleep(6)

keyboard.send(Keycode.TAB)
keyboard.release_all()
time.sleep(0.5)
keyboard.send(Keycode.TAB)
keyboard.release_all()
keyboard.send(Keycode.ENTER)
keyboard.release_all()

time.sleep(0.75)

keyboard.press(Keycode.CONTROL)
keyboard.press(Keycode.W)

time.sleep(0.3)

keyboard.release_all()

time.sleep(100000000)
