# check if pynput is installed
def check_package():
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

com = [162, 160, 65]
current = []
pressed = False

def on_press(key):
    global pressed
    global current

    if key == keyboard.Key.esc:
        return False
    
    # convert key to virtual key
    try:
        key_press = key.vk
    except AttributeError:
        # for special keys
        key_press = key.value.vk

    # check if key is in com and not an duplicate
    if key_press in com and key_press not in current:
        current.append(key_press)
        # if the current combination is the same as com
        if current == com:
            pressed = True

            print("combinations pressed")

def on_release(key):
    global current

    try:
        key_press = key.vk
    except AttributeError:
        key_press = key.value.vk
    
    if key_press in com:
        if current == com:
            print("combinations released")
        current.remove(key_press)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

if __name__ == "__main__":
    check_package()