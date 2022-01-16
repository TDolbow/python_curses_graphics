#Written by Trevor Dolbow
#Last updated on: 1/16/2022
#The functions in this file were written with the purpose of creating a simple terminal graphics library for curses.
#



import curses
from curses import wrapper




#This function uses the DDA algorithm to draw a line between the two points provided. This algorithm can be referenced here: 
# https://www.tutorialspoint.com/computer_graphics/line_generation_algorithm.htm
def drawLine(stdscr,x0,y0,x1,y1): 
    dx = x0-x1
    dy = y0-y1

    steps = 0

    if(abs(dx) > abs(dy)):
        steps = int(round(abs(dx)))
    else:
        steps = int(round(abs(dy)))
    
    try:
        xIncrement = dx / float(steps)
    except:
        xIncrement = 0
    try:
        yIncrement = dy / float(steps)
    except:
        yIncrement = 0

    x = x1
    y = y1

    stdscr.addstr(int(round(y0)),int(round(x0)),"#")
    stdscr.addstr(int(round(y1)),int(round(x1)),"#")

    for i in range(0,steps):
        x = x + xIncrement
        y = y + yIncrement
        stdscr.addstr(int(round(y)),int(round(x)),"#")

#This method will return an array of tuples containing the pixel locations of the line for two points
#This function can be used to return all points as an array of tuples along a line between the two points provided. The algorithm used to findcan be referenced here: 
# https://www.tutorialspoint.com/computer_graphics/line_generation_algorithm.htm
def GetLine(stdscr,x0,y0,x1,y1):
    dx = x0-x1
    dy = y0-y1

    steps = 0

    if(abs(dx) > abs(dy)):
        steps = int(round(abs(dx)))
    else:
        steps = int(round(abs(dy)))
    
    try:
        xIncrement = dx / float(steps)
    except:
        xIncrement = 0
    try:
        yIncrement = dy / float(steps)
    except:
        yIncrement = 0

    x = x1
    y = y1

    stdscr.addstr(int(round(y0)),int(round(x0)),"#")
    stdscr.addstr(int(round(y1)),int(round(x1)),"#")

    arr = []
    for i in range(0,steps):
        x = x + xIncrement
        y = y + yIncrement
        arr.append(int(round(x)), int(round(y)))
    return arr



#The following four functions all work together. fillTri should be the only function out of the four that should be called, as it will draw any triangle passed into it. 
#By passing three verticies into fillTri, a triangle of any unique shape will be drawn in the viewing plane. 
#Resources: http://www.sunshine2k.de/coding/java/TriangleRasterization/TriangleRasterization.html



def fillTri(stdscr,V1,V2,V3):

    sorted = sortVerts(V1,V2,V3)
    V1 = sorted[0]
    V2 = sorted[1]
    V3 = sorted[2]

    if(V2[1] == V3[1]):
        fillTriBottom(stdscr,V1,V2,V3)
    elif(V1[1] == V2[1]):
        fillTriTop(stdscr,V1,V2,V3)
    else:
        V4 = [int(V1[0] + ((V2[1] - V1[1]) / (V3[1] - V1[1]) * (V3[0] - V1[0]))),V2[1]]
        fillTriBottom(stdscr,V1,V2,V4)
        fillTriTop(stdscr,V2,V4,V3)

def sortVerts(V1,V2,V3):
    l = [V1,V2,V3]
    l.sort(key=lambda x:x[1]) # Sort the verticies by the second value (The Y position)\
    return l


def fillTriBottom(stdscr,V1,V2,V3):
    slope1 = (V2[0]-V1[0])/(V2[1]-V1[1])
    slope2 = (V3[0]-V1[0])/(V3[1]-V1[1])

    curx1 = V1[0]
    curx2 = V1[0]

    for scanLineY in range(int(round(V1[1])), int(round(V2[1]))):
        drawLine(stdscr,int(curx1),scanLineY,int(curx2),scanLineY,"#")
        curx1 = curx1 + slope1
        curx2 = curx2 + slope2
    drawLine(stdscr,V1[0],V1[1],V2[0],V2[1],"#")
    drawLine(stdscr,V2[0],V2[1],V3[0],V3[1],"#")
    drawLine(stdscr,V3[0],V3[1],V1[0],V1[1],"#")

def fillTriTop(stdscr,V1,V2,V3):
    slope1 = (V3[0]-V1[0])/(V3[1]-V1[1])
    slope2 = (V3[0]-V2[0])/(V3[1]-V2[1])

    curx1 = V3[0]
    curx2 = V3[0]

    for scanLineY in range(int(round(V3[1])), int(round(V1[1])), -1):
        drawLine(stdscr,int(curx1),scanLineY,int(curx2),scanLineY,"#")
        curx1 = curx1 - slope1
        curx2 = curx2 - slope2
    drawLine(stdscr,V1[0],V1[1],V2[0],V2[1],"#")
    drawLine(stdscr,V2[0],V2[1],V3[0],V3[1],"#")
    drawLine(stdscr,V3[0],V3[1],V1[0],V1[1],"#")


