import runWorld as rw
import drawWorld as dw
import pygame as pg
import time
from pygame.locals import *
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
# Class definitions
class animal:
    def __init__(self,imgname):
        self.image=dw.loadImage(imgname)

class world(animal):
    frameRate = 60
    tiffany = (66,199,249)
    def __init__(self):
#One time variable. Only to be used in the initalization method
        inst_line1 = "When the cat catches the fish, you win!"
        inst_line2 = "Every time the cat reaches one of the points, it would accelerate."
        inst_line3 = "When the cat reaches the lower and upper bounds, it will bounce back."
        inst_line4 = "When the cat touches the left and right sides, it will die and the game is over."
        inst_line5 = "Click the mouse and get start. Enjoy!"
        name = "Cat Fun. Press the mouse (but not too fast)!"
#Object variable to be used in other methods
        self.width = 500
        self.height = 500
        self.fig = 20
        self.firstdisp=True
        self.initState = (randint(100,399),0,randint(200,399),0) #initial status, x-cord, x-v, y-cord, y-v
        self.fishState = (randint(100,300),randint(50,150))
        self.acpntsState = (50,350,50,350) #accerlerating points locations (x1,x1,y1,y2)
        self.acstate=False
        self.maxstate=10
# Initialize world
################################################################
        rw.newDisplay(self.width, self.height, name)
        self.mylabel0 = dw.makeLabel("Instructions:","serif",24,dw.black)
        self.mylabel1 = dw.makeLabel(inst_line1,"serif",12,dw.black)
        self.mylabel2 = dw.makeLabel(inst_line2,"serif",12,dw.black)
        self.mylabel3 = dw.makeLabel(inst_line3,"serif",12,dw.black)
        self.mylabel4 = dw.makeLabel(inst_line4,"serif",12,dw.black)
        self.mylabel5 = dw.makeLabel(inst_line5,"serif",12,dw.black)
        self.cat=animal("cat.bmp")
        self.fish=animal("Fish.bmp")
        self.pnt=animal("circle.bmp")

# state -> image (IO)
# draw the cat halfway up the screen (height/2) and at the x
# coordinate given by the first component of the state tuple
#
# Display the state by drawing a cat at that x coordinate
    def updateDisplay(self,state):
        dw.fill(world.tiffany)
        if(self.firstdisp):
            dw.draw(self.mylabel0,(50,70))
            dw.draw(self.mylabel1,(50,100))
            dw.draw(self.mylabel2,(50,120))
            dw.draw(self.mylabel3,(50,140))
            dw.draw(self.mylabel4,(50,160))
            dw.draw(self.mylabel5,(50,180))
        #display fish, cat, and points after the first click
        else:
            dw.draw(self.cat.image, (state[0],state[2])) #x,y coordinate
            dw.draw(self.pnt.image, (self.acpntsState[0],self.acpntsState[2])) #x,y coordinate
            dw.draw(self.pnt.image, (self.acpntsState[0],self.acpntsState[3])) #x,y coordinate
            dw.draw(self.pnt.image, (self.acpntsState[1],self.acpntsState[2])) #x,y coordinate
            dw.draw(self.pnt.image, (self.acpntsState[1],self.acpntsState[3])) #x,y coordinate
            dw.draw(self.fish.image, self.fishState) #x,y coordinate





################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state
    def updateState(self,state):
    #    if(state[0]+state[1]>width-fig and state[1]>0):  #condition1
    #        state1=0-state[1]     #if condtition1  satisfied
    #    elif(state[0]+state[1]<fig and state[1]<0):    #condition2
    #        state1=0-state[1]      #condition1 is not satisfied, then see if condtion2 satisfied
    #    else:
        state1=state[1]          #neither condition1 nor condition2 satisfied
        if(state[2]+state[3]>self.height-self.fig//2 and state[3]>0):
            state3=0-state[3]
        elif(state[2]+state[3]<self.fig//2 and state[3]<0):
            state3=0-state[3]
        else:
            state3=state[3]
    ## Double state[1,3] when cat touches the four accelerating points.
        if( ((state[0]<self.acpntsState[0]+self.fig//2) and (state[0]>self.acpntsState[0]-self.fig//2)) or ((state[0]<self.acpntsState[1]+self.fig//2) and (state[0]>self.acpntsState[1]-self.fig//2)) ):
            if( ((state[2]<self.acpntsState[2]+self.fig//2) and (state[2]>self.acpntsState[2]-self.fig//2)) or ((state[2]<self.acpntsState[3]+self.fig//2) and (state[2]>self.acpntsState[3]-self.fig//2)) ):
                if(self.acstate==False): #Double speed only once in each accelerating point
                    if(state1<self.maxstate):
                        state1=2*state1
                    else:
                        state1=self.maxstate
                    if(state3<self.maxstate):
                        state3=2*state3
                    else:
                        state3=self.maxstate
                    self.acstate=True
            else:
                self.acstate=False # Set acstate to False when gets out of acclerating point
        else:
            self.acstate=False# Set acstate to False when gets out of acclerating point
        return((state[0]+state1,state1, state[2]+state3,state3))

################################################################

# Terminate the simulation when the x coord reaches the screen edge,
# that is, when pos is less then zero or greater than the screen width
# state -> bool
    def endState(self,state):
        if (state[0] > self.width or state[0] < 0 or state [2] > self.height or state[2] < 0):
            return True
        #Endstate happens when cat catches the fish
        elif((state[0]<self.fishState[0]+self.fig*2) and (state[0]>self.fishState[0]-self.fig*2) and (state[2]<self.fishState[1]+self.fig*2) and (state[2]>self.fishState[1]-self.fig*2) ):
            return True
        else:
            return False


################################################################

# We handle each event by printing (a serialized version of) it on the console
# and by then responding to the event. If the event is not a "mouse button down
# event" we ignore it by just returning the current state unchanged. Otherwise
# we return a new state, with pos the same as in the original state, but
# delta-pos reversed: if the cat was moving right, we update delta-pos so that
# it moves left, and vice versa. Each mouse down event changes the cat
# direction. The game is to keep the cat alive by not letting it run off the
# edge of the screen.
#
# state -> event -> state
#
    def handleEvent(self,state, event):
        #print("Handling event: " + str(event))
        if (event.type == pg.MOUSEBUTTONDOWN):
            self.firstdisp = False 
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
    
################################################################

# World state will be single x coordinate at left edge of world

# The cat starts at the left, moving right
# Set the inital speed to 0, so that cat starts to move only after the first click
# Run the simulation no faster than 60 frames per second

# Run the simulation!
newworld=world()
rw.runWorld(newworld.initState, newworld.updateDisplay, newworld.updateState, newworld.handleEvent,
            newworld.endState, world.frameRate)
