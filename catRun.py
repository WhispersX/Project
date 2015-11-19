import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

################################################################

# This program is an interactive simulation/game. A cat starts
# to move across the screen. The direction of movement is reversed
# on each "mouse down" event. Based on the original CatFun game, we
# add one fish and four points on the screen.
#
# When the cat catches the fish that shows randomly at a fixed
# point at each new game, it wins.
#
import runWorld as rw
import drawWorld as dw
import pygame as pg
from random import randint

################################################################

# This program is an interactive simulation/game. A cat starts
# to move across the screen. The direction of movement is reversed
# on each "mouse down" event.
#
# The state of the cat is represented by a tuple (pos, delta-pos).
# The first element, pos, represents the x-coordinate of the cat.
# The second element, delta-pos, represents the amount that the
# position changes on each iteration of the simulation loop.
#
# For example, the tuple (7,1) would represent the cat at x-coord,
# 7, and moving to the right by 1 pixel per "clock tick."
#
# The initial state of the cat in this program is (0,1), meaning that the cat
# starts at the left of the screen and moves right one pixel per tick.
#
# Pressing a mouse button down while this simulation run updates the cat state
# by leaving pos unchanged but reversing delta-pos (changing 1 to -1 and vice
# versa). That is, pressing a mouse key reverses the direction of the
# cat.
#
# The simulation ends when the cat is allowed to reach either the left
# or the right edge of the screen.

################################################################

# Initialize world
name = "Cat Fun. Press the mouse (but not too fast)!"
width = 500
height = 500
fig = 20
rw.newDisplay(width, height, name)

################################################################

# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("cat.bmp")
myfish = dw.loadImage("Fish.bmp")
myacpnt = dw.loadImage("circle.bmp")


# state -> image (IO)
# draw the cat halfway up the screen (height/2) and at the x
# coordinate given by the first component of the state tuple
#
def updateDisplay(state):
    dw.fill(dw.tiffany)
    dw.draw(myimage, (state[0], state[2])) #x,y coordinate
    dw.draw(myacpnt, (acpntsState[0], acpntsState[2])) #x,y coordinate
    dw.draw(myacpnt, (acpntsState[0], acpntsState[3])) #x,y coordinate
    dw.draw(myacpnt, (acpntsState[1], acpntsState[2])) #x,y coordinate
    dw.draw(myacpnt, (acpntsState[1], acpntsState[3])) #x,y coordinate
    dw.draw(myfish, fishState) # x,y coordinate


################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state
def updateState(state):
    global acstate
    if(state[0]+state[1]>width-fig and state[1]>0):  #condition1
        state1=0-state[1]     #if condtition1  satisfied
    elif(state[0]+state[1]<fig and state[1]<0):    #condition2
        state1=0-state[1]      #condition1 is not satisfied, then see if condtion2 satisfied
    else:
        state1=state[1]       #neither condition1 nor condition2 satisfied
    if(state[2]+state[3]>height-fig//2 and state[3]>0):
        state3=0-state[3]
    elif(state[2]+state[3] < fig//2 and state[3]<0):
        state3=0-state[3]
    else:
        state3=state[3]
## Double state[1,3] when cat touches the four accelerating points.
    if( ((state[0]<acpntsState[0]+fig//2) and (state[0]>acpntsState[0] - fig//2)) or ((state[0] < acpntsState[1]+fig//2) and (state[0] > acpntsState[1]-fig//2)) ):
        if( ((state[2]<acpntsState[2]+fig//2) and (state[2]>acpntsState[2]-fig//2)) or ((state[2]<acpntsState[3]+fig//2) and (state[2]>acpntsState[3]-fig//2)) ):
            if(acstate==False): #Double speed only once in each accelerating point
                if(state1<maxstate):
                    state1 = 2*state1
                else:
                    state1 = maxstate
                if (state3 < maxstate):
                    state3 = 2*state1
                else:
                    state3 = maxstate
                acstate = True
        else:
            acstate = False # Set acstate to False when gets out of acclerating point
    else:
        acstate = False# Set acstate to False when gets out of acclerating point
    return((state[0]+state1,state1, state[2]+state3,state3))

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
