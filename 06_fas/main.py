from tkinter import *
from tkinter import ttk
import time
import random
"""
TODO:
> Move window managment to separate class
> Make better GUI: title screen, how-to screen and core screen
"""

DELAY = 5
TOTAL_SIGNS="abcdefghijklmnoqprstuwxyz"
STOP_TIME = 0
IS_ON = False
SCORE = 0
SIGN = ""

def keyPressed(event):
    global SIGN, SCORE
    print(event)
    if event.keysym is SIGN:
        SCORE += 1
        l3.config(text = "SCORE: " + str(SCORE) )
        next_lvl()

def startGame():
    global IS_ON, SCORE
    IS_ON = True
    SCORE = 0
    l3.config(text = "SCORE: " + str(SCORE) )
    next_lvl()

def next_lvl():
    global SIGN, TOTAL_SIGNS, DELAY, STOP_TIME
    STOP_TIME = time.time() + DELAY
    SIGN = random.choice(TOTAL_SIGNS)
    l2.config(text = SIGN)

running = True
window = Tk()
window.geometry("300x400")
window.option_add("*Font", 20)
window.bind('<Key>', keyPressed)

btn_start = Button(window, text='Start', bg='green', fg='white', command = startGame)
btn_start.pack()
l1 = Label(window, text="Find:")
l1.pack()
l2 = Label(window, text="0", bg='black', fg='white', font=("Arial", 30) )
l2.pack()
#style = ttk.Style()
#style.theme_use('default')
#style.configure("grey.Horizontal.TProgressbar", background='red')
p1 = ttk.Progressbar(window, length=200,mode="determinate", orient=HORIZONTAL)
p1.pack()
l3 = Label(window, text="SCORE: 0")
l3.pack()

def on_closing():
    global running
    running = False

window.protocol("WM_DELETE_WINDOW", on_closing)

while running:
    window.update()
    if IS_ON:
        time_left = int((STOP_TIME - time.time()) * 20)
        p1['value'] = time_left
        if time_left < 0:
            IS_ON = False
            l2.config(text="GAME OVER")

window.destroy()