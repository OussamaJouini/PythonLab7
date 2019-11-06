from gfxhat import lcd 
from gfxhat import backlight
import time
import random 

# function to display object
def displayObject(obj,x,y):
    objLength=0
    while objLength <= len(obj) -1:
        tupleLength=0
        while tupleLength <= len(obj[objLength]) -1 :
            displ = obj[objLength] [tupleLength]
            lcd.set_pixel(x,y,displ)
            x +=1
            tupleLength +=1
        y +=1
        objLength +=1
    lcd.show()

# function to erase object
def eraseObject(obj,x,y):
    objLength=0
    while objLength <= len(obj) -1:
        tupleLength=0
        while tupleLength <= len(obj[objLength]) -1 :
            lcd.set_pixel(x,y,0)
            x +=1
            tupleLength = tupleLength + 1
        y +=1
        objLength = objLength + 1
    lcd.show()

# function to 'move' object
def moveObject(obj,x,y,vx,vy):
    x = x + vx
    y = y + vy
    return x,y
    
# function to check edge of the screen for 'collision' 
def checkCollision(obj,x,y,vx,vy,Sx,Sy):
    if y < 0 or y+vy > Sy or x+vx > Sx or x < 0:
        if y < 0:
          y = 0
        if x < 0:
          x = 0
        if y+vy > Sy:
          y = Sy-vy
        if x+vx > Sx:
          x = Sx-vx  
    return x,y

# main function       
def bounceObj(x,y,vx,vy):  
    run = True
    while run == True:
        displayObject(obj,x,y)
        time.sleep(t)
        eraseObject(obj,x,y)
        x,y = moveObject(obj,x,y,vx,vy)
        x,y = checkCollision(obj,x,y,vx,vy,Sx,Sy)

# program that creates a bouncing ball 
ball =  [
[0,0,0,1,1,0,0,0],
[0,0,1,1,1,1,0,0],
[0,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[0,0,1,1,1,1,0,0],
[0,0,0,1,1,0,0,0]
]

obj = ball
x = 10
y = 10
vx = 3
vy = 3
Sx = 128 - len(obj[0]) - vx
Sy = 64 - len(obj) - vy
t = 0.4

bounceObj(x,y,vx,vy)