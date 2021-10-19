import turtle
import random

# setup the window with a background colour
wn = turtle.Screen()
wn.bgcolor("grey")

# assign a name to your turtle
snow = turtle.Turtle()
snow.speed(0)

# create a list of colours
sfcolor = ["white", "blue", "purple", "grey", "magenta","#84d821"]

# create a function to create different size snowflakes
def snowflake(size):
# move the pen into starting position
    snow.penup()
    snow.forward(10*size)
    snow.left(45)
    snow.pendown()
    snow.color(random.choice(sfcolor))
    # draw branch 8 times to make a snowflake
    for i in range(8):
        branch(size)   
        snow.left(45)
    

# create one branch of the snowflake
def branch(size):
    for i in range(3):
        for i in range(3):
            snow.forward(10.0*size/3)
            snow.backward(10.0*size/3)
            snow.right(45)
        snow.left(90)
        snow.backward(10.0*size/3)
        snow.left(45)
    snow.right(90) 
    snow.forward(10.0*size)

# loop to create 20 different sized snowflakes with different starting co-ordinates
for i in range(20):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    sf_size = random.randint(1, 4)
    snow.penup()
    snow.goto(x, y)
    snow.pendown()
    snowflake(sf_size)

# leave the window open until you click to close  
wn.exitonclick()  
