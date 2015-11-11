# from trepan.api import debug

# import pdb
# pdb.set_trace()

import runWorld as rw
import drawWorld as dw


# Initialize world
name = "Cat Go!"
width = 500
height = 500
rw.newDisplay(width, height, name)

# World state will be single x coordinate at left edge of world
initState = 0

# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("cat.bmp")


def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(myimage, (state, width/2))


# We'll update the state on each tick by incrementing the x stateinate
def updateState(state):
    return(state+1)

# We'll terminate when the x stateinate reaches the screen edge


def endState(state):
    if (state >= width):
        return True
    else:
        return False


# For now we'll handle events just logging them to the console
#
def handleEvent(state, event):
    return(state)

# Off we go! Start the cat at the left edge, and try for 30 FPS
frameRate = 60
initState = 0
# debug()
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
