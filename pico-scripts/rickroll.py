# Made for Raspberry Pi Pico 2 W using CircutPython [should work with most other models]
# Opens a new tab, types the YouTube URL link for the official "Never Gonna Give You Up" music video and presses enter
# Works on ChromeOS, Windows
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
time.sleep(0.1)

keyboard.press(Keycode.CONTROL)
keyboard.press(Keycode.T)
time.sleep(0.05)
keyboard.release_all()

time.sleep(0.5)

layout.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

time.sleep(0.1)

keyboard.send(Keycode.ENTER)
