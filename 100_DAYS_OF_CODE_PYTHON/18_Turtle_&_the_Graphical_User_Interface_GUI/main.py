# from turtle import Turtle, Screen / one way to import module


# import Turtle 
# tim = turtle.Turtle()
# #  another way to import module

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("blue", "purple")

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)
# my_screen = Screen()
# my_screen.exitonclick()


# from turtle import * 
# """Import evertthing at once"""

# alias name 
import turtle  as Ashish
import random
tim =  Ashish.Turtle()
Ashish.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color
# for _ in range(0, 15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range (num_sides):
#         tim.forward(100) 
#         tim.right(angle)
        
# for shape_side_n in range(3, 8):
#     tim.color(random.choice(color))
#     draw_shape(shape_side_n)
tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(3)
screen = Ashish.Screen()
screen.exitonclick()