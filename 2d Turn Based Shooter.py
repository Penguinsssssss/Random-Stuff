#2d Turn Based Shooter

from turtle import *
import time
import keyboard
import math
import pyautogui

level = 0
levelSizeX = None
levelSizeY = None
levelBlocksX = []
levelBlocksY = []
gridSpacing = 50
playerX = None
playerY = None
playerSize = 10

def initialize():
    global t
    global s
    t = Turtle()
    s = Screen()
    s.tracer(0, 0)
    t.penup()
    t.speed("fastest")
    t.hideturtle()
    t.pensize(2)
    screen = Screen()
    screen.setup(1180, 620)

def resetPen():
    t.hideturtle()
    t.pensize(2)
    t.penup()
    t.speed("fastest")

def createLevels(level):
    global levelSizeX
    global levelSizeY
    global levelBlocksX
    global levelBlocksY
    global playerX
    global playerY
    if level == 0:
        levelSizeX = 8
        levelSizeY = 5
        playerX = 0
        playerY = 0
        levelBlocksX = []
        levelBlocksY = []
        block(3, 3)
        block(3, 4)
        block(4, 3)

def block(x, y):
    levelBlocksX.append(x)
    levelBlocksY.append(y)
    
def renderMap():
    t.penup()
    t.goto(0, 0)
    t.setheading(180)
    t.forward(levelSizeX / 2 * gridSpacing)
    t.setheading(90)
    t.forward(levelSizeY / 2 * gridSpacing)
    for i in range(levelSizeY + 1):
        t.pendown()
        t.setheading(0)
        t.forward(gridSpacing * levelSizeX)
        t.penup()
        t.setheading(180)
        t.forward(gridSpacing * levelSizeX)
        t.setheading(270)
        t.forward(gridSpacing)
    t.setheading(90)
    t.forward(gridSpacing)
    for i in range(levelSizeX + 1):
        t.pendown()
        t.setheading(90)
        t.forward(gridSpacing * levelSizeY)
        t.penup()
        t.setheading(270)
        t.forward(gridSpacing * levelSizeY)
        t.setheading(0)
        t.forward(gridSpacing)

def renderBlocks():
    for i in range(len(levelBlocksX)):
        t.penup()
        t.goto(0, 0)
        t.setheading(180)
        t.forward(levelSizeX / 2 * gridSpacing)
        t.setheading(90)
        t.forward(levelSizeY / 2 * gridSpacing)
        t.setheading(0)
        t.forward(gridSpacing * levelBlocksX[i])
        t.setheading(270)
        t.forward(gridSpacing * levelBlocksY[i])
        t.pendown()
        t.setheading(315)
        t.forward(math.sqrt(gridSpacing * gridSpacing * 2))
        t.penup()
        t.setheading(90)
        t.forward(gridSpacing)
        t.setheading(225)
        t.pendown()
        t.forward(math.sqrt(gridSpacing * gridSpacing * 2))
        t.setheading(0)
        t.pensize(5)
        for i in range(4):
            t.forward(gridSpacing)
            t.rt(-90)
        resetPen()

def renderPlayer():
    t.penup()
    t.goto(0, 0)
    t.setheading(180)
    t.forward(levelSizeX / 2 * gridSpacing)
    t.setheading(90)
    t.forward(levelSizeY / 2 * gridSpacing)
    t.setheading(0)
    t.forward(gridSpacing * playerX)
    t.setheading(270)
    t.forward(gridSpacing * playerY)
    t.setheading(270)
    t.forward(gridSpacing)
    t.setheading(0)
    t.forward(gridSpacing / 2)
    t.pendown()
    t.circle(gridSpacing / 2)
    
def movement():
    global playerX
    global playerY
    if keyboard.is_pressed("d"):
        playerX += 1
    if keyboard.is_pressed("a"):
        playerX -= 1
    if keyboard.is_pressed("w"):
        playerY += 1
    if keyboard.is_pressed("s"):
        playerY -= 1

initialize()
createLevels(0)
renderMap()
renderBlocks()
renderPlayer()
for i in range(300):
    movement()
    s.update()
    time.sleep(0.01)