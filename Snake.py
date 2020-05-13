import turtle
import time
import random
speed = 0.08
score = 0
highscore = 0
#Screen name
display = turtle.Screen()
#Screen title
display.title("Snake game")
#Background color
display.bgcolor("grey")
#Screen resolution
display.setup(width = 500, height = 500)
#No screen animation
display.tracer(0)
#Snake head
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("cyan")
snake_head.penup()
snake_head.goto(0,0)
snake_head.direction = "stop"
#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.shapesize(0.7, 0.7)
food.penup()
food.goto(0,100)
body = []

#Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("darkgrey")
pen.shape("square")
pen.penup()
pen.hideturtle()
pen.goto(-160, 195)
pen.write("Score: 0 \nHighscore: 0", align="center", font=("Comicsans", 20, "bold"))

#Move function
def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)
def move_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"

def move_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"
def move_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"
def move_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"
display.listen()
display.onkeypress(move_up, "w")
display.onkeypress(move_left, "a")
display.onkeypress(move_down, "s")
display.onkeypress(move_right, "d")
#Game loop
while True:
    display.update()
    #Collision with border
    if snake_head.xcor()>240 or snake_head.xcor()<-240 or snake_head.ycor()>240 or snake_head.ycor()<-240:
        time.sleep(1)
        snake_head.goto(0, 0)
        snake_head.direction = "stop"
        for body_part in body:
            body_part.goto(1000, 1000)
        #Remove food and move food to random coord
        food.goto(1000, 1000)
        x = random.randrange(-220, 220, 20)
        y = random.randrange(-220, 220, 20)
        food.goto(x, y)
        #Clear body list
        body.clear()
        #Reset score
        score = 0
        pen.clear()
        pen.write("Score: {} \nHighscore: {}".format(score, highscore), align="center", font=("Comicsans", 20, "bold"))
        speed = 0.08
    #Collision with food
    if snake_head.distance(food) < 20:
        #Move food to random coord
        x = random.randrange(-220, 220, 20)
        y = random.randrange(-220, 220, 20)
        food.goto(x, y)
        #Creating bodypart
        body_part = turtle.Turtle()
        body_part.speed(0)
        body_part.shape("square")
        body_part.color("lightblue")
        body_part.penup()
        body.append(body_part)
        #Increase speed
        speed -= 0.001
        #Score increase
        score += 1
        if score > highscore:
            highscore = score
        pen.clear()
        pen.write("Score: {} \nHighscore: {}".format(score, highscore), align="center", font=("Comicsans", 20, "bold"))
    #Move bodypart in reverse order from back
    for index in range(len(body)-1,0,-1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x, y)
    #Move first body to head
    if len(body) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        body[0].goto(x, y)
    move()
    #Body collision
    for body_part in body:
        if body_part.distance(snake_head) <20:
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_head.direction = "stop"
            for body_part in body:
                body_part.goto(1000, 1000)
            body.clear()
            #Remove food and move food to random coord
            food.goto(1000, 1000)
            x = random.randrange(-220, 220, 20)
            y = random.randrange(-220, 220, 20)
            food.goto(x, y)
            #Reset score
            score = 0
            pen.clear()
            pen.write("Score: {} \nHighscore: {}".format(score, highscore), align="center", font=("Comicsans", 20, "bold"))
            speed = 0.08
    time.sleep(speed)
#Keep screen on
display.mainloop()
