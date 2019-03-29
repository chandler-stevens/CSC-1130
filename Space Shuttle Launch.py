from ezgraphics import GraphicsWindow
from time import sleep

#set width and height of graphics window
WIN_WIDTH = 512
WIN_HEIGHT = 1024

#starting points for Shuttle
H1X = 256
H1Y = 945
H2X = 250
H2Y = 953
H3X = 250
H3Y = 975
H4X = 240
H4Y = 1000
H5X = 272
H5Y = 1000
H6X = 262
H6Y = 975
H7X = 262
H7Y = 953
H8X = 250
H8Y = 1000
H9X = 256
H9Y = 1020
H10X = 262
H10Y = 1000

#starting points for SRB Left
L1X = 246
L1Y = 950
L2X = 242
L2Y = 955
L3X = 242
L3Y = 995
L4X = 238
L4Y = 1000
L5X = 254
L5Y = 1000
L6X = 250
L6Y = 995
L7X = 250
L7Y = 955
L8X = 242
L8Y = 1000
L9X = 246
L9Y = 1030
L10X = 250
L10Y = 1000

#starting points for SRB Right
R1X = 266
R1Y = 950
R2X = 262
R2Y = 955
R3X = 262
R3Y = 995
R4X = 258
R4Y = 1000
R5X = 274
R5Y = 1000
R6X = 270
R6Y = 995
R7X = 270
R7Y = 955
R8X = 262
R8Y = 1000
R9X = 266
R9Y = 1030
R10X = 270
R10Y = 1000

#starting points for Fuel Tank
F1X = 256
F1Y = 940
F2X = 250
F2Y = 950
F3X = 250
F3Y = 1010
F4X = 262
F4Y = 1010
F5X = 262
F5Y = 950

#set movement distance for shape (# of pixels)
moveY = 1
moveLX = 2
moveLY = 1
moveRX = 2
moveRY = 1
moveFX = 1
moveFY = 1
detachL = False
detachR = False
detachF = False

#how long to pause between animation frames
WAIT_TIME = 0.1

#setup the graphics window and canvas
myWin = GraphicsWindow(WIN_WIDTH, WIN_HEIGHT)
myCanvas = myWin.canvas()

while F1Y < 1024:
    if L1Y > 512 and not detachL:
        #move SRB Left up
        L1Y -= moveY
        L2Y -= moveY
        L3Y -= moveY
        L4Y -= moveY
        L5Y -= moveY
        L6Y -= moveY
        L7Y -= moveY
        L8Y -= moveY
        L9Y -= moveY
        L10Y -= moveY
        myCanvas.drawPolygon(L1X,L1Y,L2X,L2Y,L3X,L3Y,L4X,L4Y,L5X,L5Y,L6X,L6Y,L7X,L7Y)
    elif L1Y <= 1024:
        #detach SRB Left
        detachL = True
        L1X -= moveLX
        L1Y += moveLY
        L2X -= moveLX
        L2Y += moveLY
        L3X -= moveLX
        L3Y += moveLY
        L4X -= moveLX
        L4Y += moveLY
        L5X -= moveLX
        L5Y += moveLY
        L6X -= moveLX
        L6Y += moveLY
        L7X -= moveLX
        L7Y += moveLY
        myCanvas.drawPolygon(L1X,L1Y,L2X,L2Y,L3X,L3Y,L4X,L4Y,L5X,L5Y,L6X,L6Y,L7X,L7Y)
        moveLY += 1
    
    if R1Y > 512  and not detachR:
        #move SRB Right up
        R1Y -= moveY
        R2Y -= moveY
        R3Y -= moveY
        R4Y -= moveY
        R5Y -= moveY
        R6Y -= moveY
        R7Y -= moveY
        R8Y -= moveY
        R9Y -= moveY
        R10Y -= moveY
        myCanvas.drawPolygon(R1X,R1Y,R2X,R2Y,R3X,R3Y,R4X,R4Y,R5X,R5Y,R6X,R6Y,R7X,R7Y)
    elif R1Y <= 1024:
        #detach SRB Right
        detachR = True
        R1X += moveRX
        R1Y += moveRY
        R2X += moveRX
        R2Y += moveRY
        R3X += moveRX
        R3Y += moveRY
        R4X += moveRX
        R4Y += moveRY
        R5X += moveRX
        R5Y += moveRY
        R6X += moveRX
        R6Y += moveRY
        R7X += moveRX
        R7Y += moveRY
        myCanvas.drawPolygon(R1X,R1Y,R2X,R2Y,R3X,R3Y,R4X,R4Y,R5X,R5Y,R6X,R6Y,R7X,R7Y)
        moveRY += 1

    #move Fuel Tank
    if F1Y > 256  and not detachF:
        #move Fuel Tank up
        F1Y -= moveY
        F2Y -= moveY
        F3Y -= moveY
        F4Y -= moveY
        F5Y -= moveY
        myCanvas.drawPolygon(F1X,F1Y,F2X,F2Y,F3X,F3Y,F4X,F4Y,F5X,F5Y)
    elif F1Y <= 1024:
        #detach Fuel Tank
        detachF = True
        F1X -= moveFX
        F1Y += moveFY
        F2X -= moveFX
        F2Y += moveFY
        F3X -= moveFX
        F3Y += moveFY
        F4X -= moveFX
        F4Y += moveFY
        F5X -= moveFX
        F5Y += moveFY
        myCanvas.drawPolygon(F1X,F1Y,F2X,F2Y,F3X,F3Y,F4X,F4Y,F5X,F5Y)
        moveFY += 1

    #move Shuttle up
    H1Y -= moveY
    H2Y -= moveY
    H3Y -= moveY
    H4Y -= moveY
    H5Y -= moveY
    H6Y -= moveY
    H7Y -= moveY
    H8Y -= moveY
    H9Y -= moveY
    H10Y -= moveY
    myCanvas.drawPolygon(H1X,H1Y,H2X,H2Y,H3X,H3Y,H4X,H4Y,H5X,H5Y,H6X,H6Y,H7X,H7Y)
    myCanvas.setFill("orange")
    myCanvas.setOutline("orange")
    myCanvas.drawPolygon(H8X,H8Y,H9X,H9Y,H10X,H10Y)

    if not detachL:
        myCanvas.drawPolygon(L8X,L8Y,L9X,L9Y,L10X,L10Y)
        myCanvas.drawPolygon(R8X,R8Y,R9X,R9Y,R10X,R10Y)
    
    myCanvas.setFill()
    myCanvas.setOutline("black")
    moveY += 1
    
    #wait to slow down animation
    sleep(WAIT_TIME)

    #clear the screen (what happens if we remove?)
    myCanvas.clear()
    
