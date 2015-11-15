import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint


name = "Cat Fun. Press the mouse (but not too fast)!"
width = 500
height = 500
rw.newDisplay(width, height, name)

myimage = dw.loadImage("cat.bmp")

def updateDisplay(state):
    dw.fill(dw.black)
    dw.draw(myimage, (state[0],state[2])) #x,y coordinate

def updateState(state):
    return((state[0]+state[1],state[1], state[2]+state[3],state[3]))

def endState(state):
    if (state[0] > width or state[0] < 0 or state [2] > height or state[2] < 0):
        return True
    else:
        return False

def handleEvent(state, event):
    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
        if state[1] > 0:
            newState1 = 0-randint(1,3)
        else:
            newState1 = randint(1,3)
        if state[3] > 0:
            newState3 = 0-randint(1,3)
        else:
            newState3 = randint(1,3)
        #print(newState1,newState3)
        #print('success')
        return((state[0],newState1,state[2],newState3))
    else:
        #print('unsuccess')
        return(state)

initState = (randint(100,399),randint(1,3),randint(100,399),randint(1,3)) #initial status, x-cord, x-v, y-cord, y-v

frameRate = 60

rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
