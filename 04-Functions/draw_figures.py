###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
from figures import draw_square, draw_triangle, draw_rectangle
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)   

# Side length
side_length = 100
side_length_a = 160
side_length_b = 80

## Draw figures
draw_square(pen, side_length)
pen.penup()
pen.goto(-150,150)
pen.pendown()
draw_square(pen, side_length)
pen.penup()
pen.goto(50,50)
pen.pendown()
draw_triangle(pen, side_length)
pen.penup()
pen.goto(-150,-150)
pen.pendown()
draw_triangle(pen, side_length)
pen.penup()
pen.goto(-200,250)
pen.pendown()
draw_rectangle(pen, side_length_a, side_length_b)
pen.penup()
pen.goto(50,-150)
pen.pendown()
draw_rectangle(pen, side_length_a, side_length_b)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()