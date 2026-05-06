import math as meth
import random
from Turtletest import *
import turtle
import pyautogui, sys
from pynput import keyboard

"""laddaturtle()"""
färger = ["#0cedda","#25458a","#de47f5","#ff0000","#fffb00","#fffb00"]
t=turtle.Turtle()
t.speed(9940)
turtle.bgcolor("#abb8cc")
turtle.screensize(600,500)

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        if key.char == "x":
            print("AAAAAAAAAAAAAAAAAAAAAA")
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press)
listener.start()

try:
    while True:
        x, y = pyautogui.position()
        t.setx(x/4-300)
        t.sety(-y/4+250)
        t.color(random.choice(färger))      
    
except KeyboardInterrupt:
    print('/n')
        

turtle.done()