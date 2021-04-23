from pynput import keyboard
import pyautogui
from PIL import ImageGrab, ImageOps
import time

time.sleep(1)
screen = ImageGrab.grab()
obj = screen.load()

print(obj[812, 840])
for i in range(1506, 1507):
    j = 879
    print("if obj[",i,",",j,"] == ", obj[i,j], "and ", end=' ')
for i in range(939, 940):
    j = 920
    print("if obj[",i,",",j,"] == ", obj[i,j], "and ", end=' ')
for i in range(1002, 1003):
    j = 921
    print("if obj[",i,",",j,"] == ", obj[i,j], "and ", end=' ')
for i in range(1065, 1066):
    j = 918
    print("if obj[", i, ",", j, "] == ", obj[i, j], "and ", end=' ')
"""(1713, 326)
special key Key.caps_lock pressed
(1555, 517)
special key Key.caps_lock pressed
(1713, 545)"""