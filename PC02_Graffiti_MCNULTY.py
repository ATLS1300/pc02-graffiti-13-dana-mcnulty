#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Dana McNulty
September 4, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
t= Turtle() 
t.speed(10)
t.penup()
t.left(180)
t.forward(90)
t.right(90)
t.forward(200)
t.right(90)
t.pendown()
t.pensize(7)
t.pencolor("gold")
t.fillcolor("light yellow")
t.begin_fill()
t.forward(140)
t.left(60)
t.forward(70)
t.left(150)
t.forward(30)
t.right(60)
t.forward(30)
t.left(60)
t.forward(30)
t.right(60)
t.forward(30)
t.left(60)
t.forward(30)
t.right(60)
t.forward(30)
t.left(60)
t.forward(30)
t.right(60)
t.forward(30)
t.left(150)
t.forward(70)
t.end_fill()
t.penup()
t.home()
t.forward(80)
t.right(90)
t.pencolor("tan")
t.fillcolor("tan")
t.forward(70)
t.left(90)
t.pendown()
t.begin_fill()
t.pensize(3)
t.forward(50)
t.right(110)
t.forward(80)
t.right(136)
t.forward(80)
t.end_fill()
t.penup()
t.goto(100, -40)
t.pencolor("pink")
t.fillcolor("light pink")
t.dot(70)
t.penup()
t.home()
t.goto(-70,60)
t.pencolor("black")
t.pensize(2)
t.pendown()
t.forward(4)
t.right(90)
t.forward(12)
t.right(90)
t.forward(8)
t.right(90)
t.forward(12)
t.right(90)
t.forward(4)
t.penup()
t.home()

















