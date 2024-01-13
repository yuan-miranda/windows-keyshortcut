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