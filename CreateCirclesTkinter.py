from tkinter import *
from tkinter import ttk
root = Tk()

resolutionX = 1920
resultionY = 1080

global balls
balls = []

global state 
state = "select"

global radius
radius = 20

h = ttk.Scrollbar(root, orient=HORIZONTAL)
v = ttk.Scrollbar(root, orient=VERTICAL)
canvas = Canvas(root, scrollregion=(0, 0, resolutionX, resultionY), yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview

canvas.grid(column=0, row=0, sticky=(N,W,E,S))
h.grid(column=0, row=1, sticky=(W,E))
v.grid(column=1, row=0, sticky=(N,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

lastx, lasty = 0, 0



def xy(event):
    global lastx, lasty
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)

def setColor(newcolor):
    global color
    color = newcolor
    canvas.dtag('all', 'paletteSelected')
    canvas.itemconfigure('palette', outline='white')
    canvas.addtag('paletteSelected', 'withtag', 'palette%s' % color)
    canvas.itemconfigure('paletteSelected', outline='#999999')

def click(event):
    posX, posY= canvas.canvasx(event.x), canvas.canvasy(event.y)
    if state == "node":
        createBall(posX, posY)
    elif state == "edge"

    pass

def createBall(posX, posY):
    if checkNotInAnotherBall == False:
        print("Error, already ball in there")
        return
    balls.append([posX, posY])
    color = "orange"
    canvas.create_oval(posX-radius, posY-radius, posX+radius, posY+radius, fill=color)
    return 

def checkNotInAnotherBall(posX, posY):
    for i in balls:
        if ( posX >= i[0] and posX <= i[0]+radius) or (posY >= i[1] and posY <= i[1]+radius):
            return False
    return True

def createConnection():


def addLine(event):
    global lastx, lasty
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_line((lastx, lasty, x, y), fill=color, width=5, tags='currentline')
    lastx, lasty = x, y

def doneStroke(event):
    canvas.itemconfigure('currentline', width=1)        
        


canvas.bind("")
canvas.bind("<Button-1>", xy)
canvas.bind("<Button-1>", click)
#canvas.bind("<B1-Motion>", addLine)
#canvas.bind("<B1-ButtonRelease>", doneStroke)

id = canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
id = canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
id = canvas.create_rectangle((10, 60, 30, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

setColor('black')
canvas.itemconfigure('palette', width=5)
root.mainloop()