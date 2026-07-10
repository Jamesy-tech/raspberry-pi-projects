# Made for Raspberry Pi Pico 2 W using CircutPython

import time
import usb_hid
import random
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

time.sleep(5)

CYCLE_DURATION = 10
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

initial_caps_state = keyboard.led_on(Keyboard.LED_CAPS_LOCK)

def is_kill_switch_triggered():
    return keyboard.led_on(Keyboard.LED_CAPS_LOCK) != initial_caps_state

while True:
    if is_kill_switch_triggered():
        break
        
    start_active = time.monotonic()
    while time.monotonic() - start_active < CYCLE_DURATION:
        if is_kill_switch_triggered():
            break
            
        random_char = random.choice(letters)
        layout.write(random_char)
        time.sleep(0.0000001)
        
    if is_kill_switch_triggered():
        break
        
    start_idle = time.monotonic()
    while time.monotonic() - start_idle < CYCLE_DURATION:
        if is_kill_switch_triggered():
            break
        time.sleep(0.05)
        
    if is_kill_switch_triggered():
        break
