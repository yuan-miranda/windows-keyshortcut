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



from pynput import keyboard

# gets the virtual key of a key
def on_press(key):
    try:
        key_press = key.vk
    except AttributeError:
        key_press = key.value.vk

    print(key_press)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()