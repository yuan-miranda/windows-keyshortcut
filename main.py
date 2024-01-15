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

com = [[162, 160, 65], [162, 160, 66], [162, 160, 67]]
current = []

def is_combination_pressed(key_press, combination):
    global current

    if key_press in combination and key_press not in current:
        current.append(key_press)
        # if the current combination is the same as com
        if current == combination:
            return True
    return False

def is_combination_released(key_press, combination):
    global current
    if key_press in current:
        current.remove(key_press)
        return False
    elif current == combination:
        return True

    # if key_press in combination:
    #     if current == combination:
    #         return True
    #     if key_press in current:
    #         current.remove(key_press)
    return False

def on_press(key):
    if key == keyboard.Key.esc:
        return False
    
    # convert key to virtual key
    try:
        key_press = key.vk
    except AttributeError:
        # for special keys
        key_press = key.value.vk

    # check if key is in com and not an duplicate
    # if key_press in com[0] and key_press not in current:
    #     current.append(key_press)
    #     # if the current combination is the same as com
    #     if current == com[0]:
    #         print("combinations pressed 1")
    # elif key_press in com[1] and key_press not in current:
    #     current.append(key_press)
    #     if current == com[1]:
    #         print("combinations pressed 2")

    for i in range(len(com)):
        print(current)
        if is_combination_pressed(key_press, com[i]):
            print("combinations pressed", i + 1)
            break

def on_release(key):
    try:
        key_press = key.vk
    except AttributeError:
        key_press = key.value.vk

    for i in range(len(com)):
        if is_combination_released(key_press, com[i]):
            print("combinations released", i + 1)
            break

    # if key_press in com[0]:
    #     if current == com[0]:
    #         print("combinations released 1")
    #     current.remove(key_press)

    # elif key_press in com[1]:
    #     if current == com[1]:
    #         print("combinations released 2")
    #     current.remove(key_press)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

if __name__ == "__main__":
    check_package()