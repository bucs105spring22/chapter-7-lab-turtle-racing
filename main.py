from turtle import Turtle, Screen
from random import randrange

michelangelo = Turtle()    # 1.  Create two turtles
leonardo = Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 2.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part A -  complete part A here




# Part B - complete part B here





# The lines below keep the window open after your porgram runs until you click it so you can see what is going on.
window = Screen()
window.exitonclick()
