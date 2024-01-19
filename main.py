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

user_system = platform.system()
com = []
current_keys_pressed = []
pressed = False

if user_system == "Windows":
	com = [[162, 160, 65], [162, 160, 66], [162, 160, 67]]
elif user_system == "Linux":
	com = [[65507, 65505, 65], [65507, 65505, 66], [65507, 65505, 67]]

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
      
    for i in range(len(com)):
        if current_keys_pressed == com[i]:
            print("combinations released", i + 1)
            pressed = False
            break

    if key_press in current_keys_pressed:
        current_keys_pressed.remove(key_press)
    

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
