# Draw a square
def draw_square(turtle, length):
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)

def draw_triangle(turtle, length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)

def draw_rectangle(turtle, length_a, length_b):
    for i in range(2):
        turtle.forward(length_a)
        turtle.right(90)
        turtle.forward(length_b)
        turtle.right(90)