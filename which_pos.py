from pynput import keyboard
import pyautogui

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        print(pyautogui.position())
    except AttributeError:
        print('special key {0} pressed'.format(key))
        print(pyautogui.position())
'''
def on_release(key):
    print('{0} released'.format(key))
    print(pyautogui.position())
    if key == keyboard.Key.esc:
        # Stop listener
        return False
'''
# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()