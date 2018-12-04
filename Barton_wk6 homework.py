# Starter code for homework 6


CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800


from Gui import *

def main():
    # remove this line and add your own code
    #canvas.text([0,0], text = "hello")
    '''locationX = int(input("Enter a location X: "))
    locationY = int(input("Enter a location Y: "))
    height = int(input("How Tall: "))
    lines = int(input("How many lines: "))
    color = input("color: ")'''
    

    #line_curve(locationX, locationY, height, lines, color)
    line_curve(-450, 350, 200, 20, 'blue')
    line_curve(0, 150, 128, 16, 'red')
    line_curve(400, 0, 180, 20, 'brown')

def line_curve(x, y, height, lines, color):
    x_one = x #20
    x_two = x #20
    y_one = y  - height#20
    y_two = y #200
    scale = height/lines

    while lines > 0:
        canvas.line([[x_one, y_one],[x_two,y_two]], fill=color, width = .5)
        lines = lines - 1
        y_two = y_two - scale
        x_one = x_one + scale

def row_line_curve(x, y, height
        
    

###################################################################
# Feel free to read what's here, but do not change

g = Gui()
g.title('HW6 Line Curves')

# canvas is the drawing area
canvas = g.ca(width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
main()
g.mainloop()
