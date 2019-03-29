from ezgraphics import GraphicsWindow
from time import sleep

#set width and height of graphics window
WIN_WIDTH = 640
WIN_HEIGHT = 480

#set starting point for your shape
xPos = 50
yPos = 50

#set movement distance for shape (# of pixels)
MOVE_X = 1
MOVE_Y = 1

#dimensions of the oval
OVAL_WIDTH = 10
OVAL_HEIGHT = 10

#how long to pause between animation frames
WAIT_TIME = 0.01 

#setup the graphics window and canvas
myWin = GraphicsWindow(WIN_WIDTH, WIN_HEIGHT)
myCanvas = myWin.canvas()

#default movement to right/down
moveX = MOVE_X
moveY = MOVE_Y

QUANTITY = 20

SHIFT = 20

while True:

    #if far right ball hits right side of screen "bounce" (move left)
    if (xPos + (QUANTITY * SHIFT)) >= WIN_WIDTH:
        moveX = -1 * MOVE_X

    #if far left ball hits left side of screen "bounce" (move right)
    if xPos <= 0:
        moveX = MOVE_X
        
    #if balls hit bottom of screen "bounce" (move up)
    if yPos >= WIN_HEIGHT:
        moveY = -1 * MOVE_Y

    #if balls hit top of screen "bounce" (move down)
    if yPos <= 0:
        moveY = MOVE_Y
        
    #update the position of the shapes
    xPos = xPos + moveX
    yPos = yPos + moveY
    
    quantity = QUANTITY

    shift = 0
    
    while quantity > 0:
        myCanvas.drawOval(xPos + shift, yPos, OVAL_WIDTH, OVAL_HEIGHT)
        shift = shift + SHIFT
        quantity = quantity - 1

    #wait to slow down animation
    sleep(WAIT_TIME)

    #clear the screen (what happens if we remove?)
    #myCanvas.clear()

    
