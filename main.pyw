# this script runs in the background and listens for keyboard inputs.

import os
import pynput

# add your keyboard shortcut here
commands = {
    # uncomment the line to enable the example command.
    # CTRL + SHIFT + T = open cmd
    # (pynput.keyboard.Key.ctrl_l, pynput.keyboard.Key.shift_l, '\x14'): "cmd"
}
key_pressed = []

def on_press(key):
    global key_pressed
    current_key = key if isinstance(key, pynput.keyboard.Key) else key.char
    if current_key == pynput.keyboard.Key.esc:
        return False
    if current_key in key_pressed:
        return
    
    key_pressed.append(current_key)
    if tuple(key_pressed) in commands:
        os.system(commands[tuple(key_pressed)])

def on_release(key):
    global key_pressed
    current_key = key if isinstance(key, pynput.keyboard.Key) else key.char
    if current_key not in key_pressed:
        return
    
    key_pressed.remove(current_key)

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()