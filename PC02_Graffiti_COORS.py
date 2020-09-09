#!/usr/bin/env python3
#coding: utf-8

"""
PC02_Graffiti_Coors_McNulty.py
ATLS 1300
Author: Dr. Z
Author: Cecily Coors
September 8, 2020

Graffiti of Jeff Bezos.
"""

from turtle import * #import turtle into workspace
import math

colormode(255)

panel = Screen() #sets up the screen
w=600
h=600
panel.setup(width=w,height=h) #changing size of my panel

image="Bezos.gif"
panel.bgcolor("lightgreen")
panel.bgpic(image)

#==== Add more code=====
ht()
t=Turtle()
t=penup()
t=right(30)
t=forward(200)
t=dot(100,*[150,74,0])
t=goto([190,-65])
t=pendown()
t=pensize(2)
t=fillcolor([150,74,0])
t=pencolor([150,74,0])
t=begin_fill()
t=left(90)
t=forward(50)
t=left(120)
t=forward(70)
t=left(120)
t=forward(50)
t=left(60)
t=forward(20)
t=end_fill()
t=penup()
t=goto(192,-73)
t=pendown()
t=pencolor("lightgreen")
t=pensize(4)
t=bk(30)
t=rt(90)
t=fd(30)
t=lt(90)
t=fd(30)
t=rt(90)
t=fd(30)
t=lt(90)
t=bk(30)
t=penup()
t=goto(184,-65)
t=pendown()
t=rt(90)
t=pensize(2)
t=forward(76)
t=penup()
t=goto(170,-65)
t=pendown()
t=forward(76)
t=hideturtle()
t.home()




