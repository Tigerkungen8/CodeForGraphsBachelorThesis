""" 
Part VA

Student: Tim Erixon
Reviewed by: Tom Smedsaas
Date reviewed: 16/05/2024
"""

import tkinter as tk
import Graphs
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure

import random
import math

# Functions called by buttons
def Initiate():
    pass
        
# For the Run-loop, so that I can start and quit it by pressing the buttons
startPressed = False

def Start(): # Making Startpressed true and then running Run
    global startPressed
    startPressed = True
    Run()

def Run():
    global startPressed
    while startPressed: # = while startPressed == True:
        window.update() # Updating/redrawing it all

def Pause(): # Making Startpressed false and then running Run
    global startPressed
    startPressed = False
    Run()


def Clean():
    Pause()
    canvas.delete("all")


def Finish():
    Pause()
    window.quit()


"""
Coordinates:
____________________
|(0,0)       (600,0)|
|                   |
|                   |
|                   |
|                   |
|(0,600)   (600,600)|
|___________________|
"""


# All the Tkinter stuff
window = tk.Tk()

mainWidth = 600
mainHeigth = 600

inputWidth = 100
inputHeigth = mainHeigth

frameMain = tk.Frame(master=window, width = mainWidth, height = mainHeigth, bg = "chocolate1")
frameMain.pack(fill=tk.BOTH, side=tk.LEFT, expand = True)

canvas = FigureCanvasTkAgg(Graphs.fig, master=frameMain)  # A tk.DrawingArea.
canvas.draw()


"""
canvas = tk.Canvas(master = frameMain, width = mainWidth, height = mainHeigth, bg = "black")
canvas.pack()
"""

frameInput = tk.Frame(master = window, width = inputWidth, height = inputHeigth)
frameInput.pack(fill=tk.BOTH, side = tk.LEFT, expand = True)

labelInputAmount = tk.Label(master = frameInput, text="Antal:")
entryInputAmount = tk.Entry(master = frameInput, width = 20)
labelInputAmount.grid(row = 0, column = 0)
entryInputAmount.grid(row = 0, column = 1)
entryInputAmount.insert(0,100)

labelInputSpeed = tk.Label(master = frameInput, text="Hastighet:")
entryInputSpeed = tk.Entry(master = frameInput, width = 20)
labelInputSpeed.grid(row = 1, column = 0)
entryInputSpeed.grid(row = 1, column = 1)
entryInputSpeed.insert(0,0.4)


buttonInputInitiate = tk.Button(master = frameInput, text="Initiera", command = Initiate)
buttonInputStart = tk.Button(master = frameInput, text="Starta", command = Start)
buttonInputPause = tk.Button(master = frameInput, text="Pausa", command = Pause)
buttonInputClean = tk.Button(master = frameInput, text="Rensa", command = Clean)
buttonInputFinish = tk.Button(master = frameInput, text="Avsluta", fg="red", command = Finish)
#buttonInputMove = tk.Button(master = frameInput, text="Flytta Tillbak", command = MoveBall)


buttonInputInitiate.grid(row = 2, column = 1)
buttonInputStart.grid(row = 3, column = 1)
buttonInputPause.grid(row = 4, column = 1)
buttonInputClean.grid(row = 5, column = 1)
buttonInputFinish.grid(row = 6, column = 1)
#buttonInputMove.grid(row = 7, column = 1)


# Running it all
window.mainloop()