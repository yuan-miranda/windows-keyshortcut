# check if pynput is installed
try:
    from pynput import keyboard
except:
    user_input = input('package pynput not found, do you want to install it? (Y/n)').lower()
        
    if user_input == "y" or len(user_input) == 0:
        import setup
    else:
        print("operation canceled")
        exit()

import platform
import os
from pynput import keyboard

user_system = platform.system()
com = []
current_keys_pressed = []
pressed = False

if user_system == "Windows":
    com = {
        (162, 164, 84): "cmd",
        (162, 164, 78): "notepad"
    }
elif user_system == "Linux":    # Kali VM
    com = {
        # still not updated, my vm is acting weird
        (65507, 65513, 116): "konsole"
    }

def on_press(key):
    global current_keys_pressed
    global pressed

    if key == keyboard.Key.esc:
        return False
    
    # convert key to virtual key
    try:
        key_press = key.vk
    except AttributeError:
        # for special keys
        key_press = key.value.vk

    if key_press not in current_keys_pressed:
        current_keys_pressed.append(key_press)

    for key, value in com.items():
        if tuple(current_keys_pressed) == key and not pressed:

            # executes the command
            os.system(value)

            pressed = True
            break
        
    # if key_press not in current_keys_pressed:
    #     current_keys_pressed.append(key_press)
        
    # for i in range(len(com)):
    #     if current_keys_pressed == com[i] and not pressed:
    #         print("combinations pressed", i + 1)
    #         pressed = True
    #         break

def on_release(key):
    global current_keys_pressed
    global pressed
    
    try:
        key_press = key.vk
    except AttributeError:
        key_press = key.value.vk
    

    for key, value in com.items():
        if tuple(current_keys_pressed) == key:

            # do something when the combination is released

            pressed = False
            break
    
    if key_press in current_keys_pressed:
        current_keys_pressed.remove(key_press)

    # for i in range(len(com)):
    #     if current_keys_pressed == com[i]:
    #         print("combinations released", i + 1)
    #         pressed = False
    #         break

    # if key_press in current_keys_pressed:
    #     current_keys_pressed.remove(key_press)
    

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
