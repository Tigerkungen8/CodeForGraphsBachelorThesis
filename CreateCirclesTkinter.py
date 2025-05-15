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

global nodeA
nodeA = None

global nodeB
nodeB = None

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


class Ball():
    def __init__(self, x, y, radius, colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.oval = canvas.create_oval(self.x-radius, self.y-radius, self.x+radius, self.y+radius, fill=self.colour) 

    def updateColour(self, givenColour):
        canvas.delete(self.getId())    # Delete drawn oval
        self.colour = givenColour
        self.oval = canvas.create_oval(self.x-radius, self.y-radius, self.x+radius, self.y+radius, fill=self.colour)

    def getId(self):
        return self.oval
    
    def move(self, dx, dy):
        canvas.move(self.getId(), dx, dy)




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
    elif state == "edge":
        print("HHHHHHHHH")
        createConnection(posX, posY)
        pass
    elif state == "select":
        node = checkNotInAnotherBallFindBall(posX, posY) if checkNotInAnotherBallFindBall(posX, posY) != True else None
        node.updateColour("red")
        pass
    pass

def createBall(posX, posY):
    global radius
    if checkNotInAnotherBall(posX, posY) == False:
        print("Error, already ball in there")
        return
    color = "orange"
    newBall = Ball(posX, posY, radius, color)
    balls.append(newBall)
    return 

def checkNotInAnotherBall(posX, posY):
    for i in balls:
        if ( posX >= i.x - radius and posX <= i.x+radius) and (posY >= i.y - radius and posY <= i.y+radius):
            return False
    return True

def checkNotInAnotherBallFindBall(posX, posY):
    for i in balls:
        if ( posX >= i.x - radius and posX <= i.x+radius) and (posY >= i.y - radius and posY <= i.y+radius):
            return i
    return True

def createConnection(posX, posY):
    global nodeA, nodeB
    if checkNotInAnotherBallFindBall(posX,posY) != True and nodeA == None:
        nodeA = checkNotInAnotherBallFindBall(posX,posY)
        nodeA.colour = "red"

        return "Found A, but need B"
    if checkNotInAnotherBallFindBall(posX,posY) != True and nodeA != None:
        nodeB = checkNotInAnotherBallFindBall(posX,posY)
        canvas.create_line(nodeA.x, nodeA.y, nodeB.x, nodeB.y)
        nodeA, nodeB = None, None
    return 


def addLine(event):
    global lastx, lasty
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_line((lastx, lasty, x, y), fill=color, width=5, tags='currentline')
    lastx, lasty = x, y

def doneStroke(event):
    canvas.itemconfigure('currentline', width=1)        
        
def changeState():
    global state
    if state == "select":
        palette = "red"
    elif state == "node":
        palette = "blue"
    else:
        palette = "black"
     
    canvas.dtag('all', 'paletteSelected')
    canvas.itemconfigure('palette', outline='white')
    canvas.addtag('paletteSelected', 'withtag', 'palette%s' % palette)
    canvas.itemconfigure('paletteSelected', outline='#999999')

def updateState(event):
    global state
    buttonPressed = event.keysym
    if buttonPressed == "s": # select
        restartConnection()
        restartSelection()
        state = "select"
    elif buttonPressed == "e":
        restartConnection()
        restartSelection()
        state = "edge"
    elif buttonPressed == "n":
        restartConnection()
        restartSelection()
        state = "node"
    else:
        print(f"Something not right, pressed {buttonPressed}, but that doesn't mean anything.")
        pass
    changeState()

def restartConnection():
    global nodeA, nodeB
    nodeA, nodeB = None, None
    return None

def restartSelection():
    for i in balls:
        i.updateColour("orange")

def onDrag(event):
    # calculate distance moved from last position
    posX, posY = canvas.canvasx(event.x), canvas.canvasy(event.y)
    if checkNotInAnotherBallFindBall(posX, posY) != True:
        print("AAAAA")
        dx, dy = event.x-posX, event.y-posY
        node = checkNotInAnotherBallFindBall(event.x, event.y)
        canvas.move(node.oval, dx, dy)
        root.update()
        

root.bind("<Key>", updateState)
canvas.bind("<Button-1>", xy)
canvas.bind("<Button-1>", click)
#canvas.bind("<B1-Motion>", addLine)
#canvas.bind("<B1-ButtonRelease>", doneStroke)
canvas.bind("<B1-Motion>", onDrag)



id = canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor())
id = canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
canvas.tag_bind(id, "<Button-1>", lambda x: changeState())
id = canvas.create_rectangle((10, 60, 30, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
canvas.tag_bind(id, "<Button-1>", lambda x: changeState())

setColor('black')
canvas.itemconfigure('palette', width=5)
root.mainloop()