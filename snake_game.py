import turtle
import time
import random

# Setup screen
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake body segments
segments = []

# Score display
score = 0
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Game speed
START_DELAY = 0.25
delay = START_DELAY

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard controls
win.listen()
win.onkey(go_up, "Up")
win.onkey(go_down, "Down")
win.onkey(go_left, "Left")
win.onkey(go_right, "Right")

# Main game loop
while True:
    win.update()

    # Border collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide and reset segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reset score and delay
        score = 0
        delay = START_DELAY
        pen.clear()
        pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

    # Food collision
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Add new body segment
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("light green")
        new_segment.penup()
        segments.append(new_segment)

        # Update score
        score += 10
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

        # Optional: increase speed slightly
        delay = max(0.05, delay - 0.005)

    # Move segments in reverse
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    # Move first segment to head
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Collision with self
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = START_DELAY
            pen.clear()
            pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)







