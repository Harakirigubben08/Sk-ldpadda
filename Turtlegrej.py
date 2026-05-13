import math as meth
import random
from Turtletest import *
import turtle
import pyautogui, sys
from pynput import keyboard
import os
import ctypes 

ctypes.windll.user32.MessageBoxW(0, "Tryck Escape för att stänga ner och X för att rensa ritytan (Enbart fantasin sätter gränserna i denna underbara värld, på så sätt är det lite som LEGO. Viste du att LEGO står för lek go eller något och enligt vad jag har förstått står det för lek kul eller något, så lek kul här🤩)", "Sköldpadda ", 1)

färger = ["#0cedda","#25458a","#de47f5","#ff0000","#fffb00","#fffb00"]
t = turtle.Turtle()
t.speed(9940)
t.color("green")
turtle.bgcolor("#abb8cc")
turtle.screensize(600, 500)

rensa_canvas = False

print("Tryck Escape för att stänga av")

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
        
        gamx = t.xcor()
        gamy = t.ycor()

        x, y = pyautogui.position()
        t.setx(x / 4 - 300)
        t.sety(-y / 4 + 250)
        t.color(random.choice(färger))
        
        print("----")
        print(gamx, gamy)
        print("----")
        print(t.xcor(), t.ycor())

        deltx = t.xcor() - gamx
        delty = t.ycor() - gamy

        try:
            vinkel = meth.atan(delty/deltx)
        except ValueError:
            print("NEJ!")
        t.left(vinkel)

except KeyboardInterrupt:
    print('\n')

turtle.done()