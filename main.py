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
from pynput import keyboard

com = [[162, 160, 65], [162, 160, 66], [162, 160, 67]]
current_keys_pressed = []
pressed = False

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
        
    for i in range(len(com)):
        if current_keys_pressed == com[i] and not pressed:
            print("combinations pressed", i + 1)
            pressed = True
            break

def on_release(key):
    global current_keys_pressed
    global pressed
    
    try:
        key_press = key.vk
    except AttributeError:
        key_press = key.value.vk

    # idk if this is a bug but if you press and hold a valid key combination and proceed
    # to press another valid key again while the old one is still active, it would store
    # both valid keys, so when you release the old one, it would store the new one now,
    # and when you released the new one, it would print the combination released message
    # for the new one.
    
    # CRTL + SHIFT + A
    # CRTL + SHIFT + A + B
    # CRTL + SHIFT + B (wont output the message for A because it treat it as appended)
    # CRTL + SHIFT (this would output the message for B)
    
    # this would also work with the non valid keys, but instead it wont output anything.

      
    for i in range(len(com)):
        if current_keys_pressed == com[i]:
            print("combinations released", i + 1)
            pressed = False
            break

    if key_press in current_keys_pressed:
        current_keys_pressed.remove(key_press)
    

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()