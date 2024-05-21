from turtle import *

tim = Turtle()
screen = Screen()

# Challenge 1
# Turtle to move in square
# for _ in range (4):
#     tim.forward(100)
#     tim.right(90)
# screen.exitonclick()

# Challenge 2
# Draw a dashed line for 10 spaces until it does 5)
# for _ in range (4):
#     for _ in range (15):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pendown()
#     tim.right(90)

# screen.exitonclick()

# # Challenge 3
# # Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon
# def draw_shape(corners):
#     corners_degree = 360/corners
#     for _ in range (corners):
#         for _ in range (15):
#             tim.forward(10)
#             tim.penup()
#             tim.forward(10)
#             tim.pendown()
#         tim.right(corners_degree)
#
# shapes = [3,4,5,6,7,8,9,10] # triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon
# color_list = ["red", "orange", "IndianRed", "green", "blue", "indigo", "violet"]
# color_index = 0 # Counter for color list
#
#
# # Draw different shapes
# for i, corners in enumerate(shapes):
#     tim.goto(0, 0)  # Move back to the origin (or any desired starting point)
#     draw_shape(corners)
#     tim.pencolor(color_list[color_index])
#     color_index = (color_index + 1) % len(color_list)
#     tim.penup()
#     tim.forward(20)
#     tim.pendown()

# screen.exitonclick()

# # Challenge 4
# # Generate a Random Walk
# import random
# import turtle as t
#
# t.colormode(255)
#
# def random_color():
#   """Generates a random RGB color tuple."""
#   r = random.randint(0, 255)
#   g = random.randint(0, 255)
#   b = random.randint(0, 255)
#   return (r, g, b)  # Return the RGB tuple
#
# directions = [0, 90, 180, 270]
# tim.pensize(5)
# tim.hideturtle()
# tim.speed("fastest")
#
# for _ in range(200):  # Fixed: 200 iterations for the walk
#     tim.color(random_color())
#     tim.forward(10)
#     tim.setheading(random.choice(directions))  # Corrected function call
#
# """
# A Python Tuples
#
# my_tuple = (1, 3, 8)
# each item were separated by a comma, similar to a list
# my_tuple = [1]
#
# You cannot change the value like a list, it's fixed
# Tuple object does not support item assignment
#
# if you want to change it, you can convert it into a list
# list(my_tuple) = [1, 3, 8]
# """
# screen.exitonclick()


# Challenge 5 Draw a spirograph

import random
import turtle as t

t.colormode(255)

def random_color():
  """Generates a random RGB color tuple."""
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return (r, g, b)  # Return the RGB tuple

def draw_spiragraph(size_of_gap):
    for _ in range (int(360/ size_of_gap)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

draw_spiragraph(5)

screen = t.Screen()
screen.exitonclick()