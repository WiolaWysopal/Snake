import turtle #needed for screen creating
import time #need for delaying snake
import random

delay = 0.1 # global variable; delays snake about 0.1 sec
dist = 15
width = 600
height = 600


wn = turtle.Screen() #creating screen object
wn.title("Python in python")
wn.bgcolor("cyan") #setting background color
wn.setup(width, height)
wn.tracer(0) #turns off the screen updates

#The head - object of Square
head = turtle.Turtle()
head.speed(0) #animation speed of Turtle module
head.shape("square")
head.color("red")
head.penup() #it's necessary beacuse turle modue leaves a line behind by default
head.goto(0, 0) #goes to center of the screen
head.direction = "stop" #possible values: 'stop', 'up', 'down'

#Snake corpus
corpus = []


#Turtle-dot
dot = turtle.Turtle()
dot.speed(0)
dot.shape("turtle")
dot.color("green")
dot.penup()
dot.goto(0, 0) 

# function responsible for moving head around the scren
def move():
    y = head.ycor(); x = head.xcor()
    if head.direction == "up":
        head.sety(y + dist) #moving with y-axis for +20 px

    if head.direction == "down":
        head.sety(y - dist) #moving with y-axis for -20 px

    if head.direction == "right":
        head.setx(x + dist) #moving with x-axis for +20 px

    if head.direction == "left":
        head.setx(x - dist) #moving with x-axis for -20 px

#Functions responsible for snake directions
def go_up():
    head.direction = "up"

def go_down():
    head.direction = "down"

def go_left():
    head.direction = "left"

def go_right():
    head.direction = "right"

def go_stop():
    head.direction = "stop"

#Binding functions to keyboards keys
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_stop, "space") #after pressing space snake stops

#Main game loop
while True:
    wn.update() #every time in the loop updates the screen; forced by 'tracer' function which stops refreshing screen
    
    # Bouncing from the edge
    if (head.xcor() > 290 or head.xcor() < -290 or
        head.ycor() > 290 or head.ycor() < -290):
        time.sleep(delay)
        head.goto(0, 0)
        head.direction = "stop"
        # this loop is responsible for deleting vertebras from corpus;
        # we have to do it this way; in turtle module there's no way to
        # delete the segments from the memory
        for vert in corpus:
            vert.goto(2*width, 2*height)
        corpus.clear() # without it verts gonna still appear

    if head.distance(dot) < dist:
        dot.goto(random.randint(-290, 290), random.randint(-290, 290))
    
    # adding new vertebras to the corpus
        vertebra = turtle.Turtle()
        vertebra.speed(0)
        vertebra.shape("square")
        vertebra.color("magenta")
        vertebra.penup()   #makes sure, that new element doesn't show on a screen
        corpus.append(vertebra)
   
    # Moving the end vertebra first in reverse order
    for i in range(len(corpus) - 1, 0, -1):
        x = corpus[i - 1].xcor()
        y = corpus[i - 1].ycor()
        corpus[i].goto(x, y)

    # Move first vertebra after head to where the head is
    if len(corpus) > 0:
        x = head.xcor()
        y = head.ycor()
        corpus[0].goto(x, y)

        
    move() #calling function responsible for snake's moves
    time.sleep(delay) #without this snake wouldn't be able to see - it would move to fast to human eye coud see and the screen would be seem as empty



wn.mainloop() # this keep window open for all time of program running



#TODO: How to find way to unhardcoding drawing a coordinates of dot-appearing?
#TODO: Split code into lesser parts