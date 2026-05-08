import math as meth
import random
from Turtletest import *
import turtle
import pyautogui, sys
from pynput import keyboard
import os

"""laddaturtle()"""

färger = ["#0cedda","#25458a","#de47f5","#ff0000","#fffb00","#fffb00"]
t = turtle.Turtle()
t.speed(9940)
turtle.bgcolor("#abb8cc")
turtle.screensize(600, 500)

rensa_canvas = False

def on_press(key):
    global rensa_canvas
    try:
        if key.char == "x" or key.char == "X":
            rensa_canvas = True
    except AttributeError:
        if key == keyboard.Key.esc:
            os._exit(0)

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    while True:
        if rensa_canvas:
            rensa_canvas = False
            turtle.clearscreen()
            turtle.bgcolor("#abb8cc")
            t = turtle.Turtle()
            t.speed(9940)

        x, y = pyautogui.position()
        t.setx(x / 4 - 300)
        t.sety(-y / 4 + 250)
        t.color(random.choice(färger))

except KeyboardInterrupt:
    print('\n')

turtle.done()