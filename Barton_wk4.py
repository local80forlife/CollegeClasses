# Andrew Barton: CSC 110 Week 4 homework - 10/23/18
# GUI program draws a basic car, grassy field, and a road with side walk

import random
from Gui import *

CANVAS_WIDTH = 900
CANVAS_HEIGHT = 600

#main function to run the code
#function parameters are as follows
#road(left side X axis, right side X axis, Y axis)
#grass(left side X axis, right side X axis, Y axis
#car(X axis, Y axis, size)
def main():
    road(-450, 450, -160)
    road(-450, 450, -10)
    road(-450, 450, 140)
    grass(-450, 450, -250)
    grass(-450, 450, -100)
    grass(-450, 450, 50)
    car(10, -100, 100)
    car(-80, 50, 100)
    car(-300, 200, 100)
    ball(-100, 100, 5)
    ball(200, -100, 10)
    ball(200, 100, 5)

#Draw the grass field with blades of grass randomly in the field
def grass(leftX, rightX, y_axis):
    canvas.line([[leftX, y_axis],[rightX, y_axis]], fill = 'green', width = 100)
    
    for i in range(200):
        x_pos = random.randint(leftX, rightX)
        y_pos = random.randint(y_axis-50, y_axis+50)
        canvas.line([[x_pos, y_pos], [x_pos, y_pos + 3]], fill='black', width=1)

#Create the road and a side walk    
def road(leftX, rightX, y_axis):
    #creating the width of the sidewalk slabs into even parts across the width
    #of the sidewalk drawing
    slabWidth = (abs(leftX)+abs(rightX))/10
    slabPos = leftX
    
    #Drawing the sidewalk and the road
    canvas.line([[leftX, y_axis],[rightX, y_axis]], fill = 'black', width = 20)
    canvas.line([[leftX, y_axis-20],[rightX, y_axis-20]], fill='grey', width=40)
    
    #create the lines in the sidewalk making slabs
    for line in range(10):
        canvas.line([[slabPos, y_axis],[slabPos, y_axis-40]], fill='black',
                    width=2)
        slabPos += slabWidth
        
#Drawing a car, pos_x is the cars position on x axis. pos_y is the position on
#y axis
def car(pos_x, pos_y, scale):

    carFront = scale + pos_x
    carBack = carFront - scale
    carTop =  pos_y
    carBottom = carTop-(scale/3)

    canvas.oval([[carBack, carTop+(scale/8)],[carFront, carTop-(scale/8)]],
                fill = 'blue')
    canvas.rectangle([[carBack, carBottom], [carFront, carTop]], fill='blue' )
    canvas.circle([carBack+(scale/8), carBottom-10], scale/8, outline='white',
                  fill='black', width=1)
    canvas.circle([carFront-(scale/8), carBottom-10], scale/8, outline='white',
                  fill='black', width=1)

#drawing a ball
def ball(x_axis, y_axis, size):
    canvas.circle([x_axis, y_axis], size, outline='black', fill='white',
                  width=1)

#text for the title bar
g = Gui()
g.title('Barton Homework: week 4')

# canvas is the drawing area
canvas = g.ca(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
main()
g.mainloop()


#I started with the Tree example and kept changing things to figure out how to
#use the GUI. I got stuck with the scaling of object, Kinda got it to work
#with more time I could get it

#I tested by drawing one piece at a time, I might have fallen short on the
#functions, I was counting main() as a function

#I learned that drawing by pixels is very time consuming, and takes a lot of
#practice
