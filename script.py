from turtle import Turtle, Screen
import time

screen = Screen()
screen.bgcolor("navy")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

paddle = Turtle("square")
paddle.color("cyan")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

paddle2 = Turtle("square")
paddle2.color("lime")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(-350, 0)

ball = Turtle("circle")
ball.color("yellow")
ball.penup()

score = Turtle()
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)

ballx = 10
bally = 10
player1_score = 0
player2_score = 0
sleep_time = 0.1

def go_up():
    paddle.goto(paddle.xcor(), paddle.ycor() + 20)

def go_down():
    paddle.goto(paddle.xcor(), paddle.ycor() - 20)

def go_up2():
    paddle2.goto(paddle2.xcor(), paddle2.ycor() + 20)

def go_down2():
    paddle2.goto(paddle2.xcor(), paddle2.ycor() - 20)

def bounce():
    global bally
    bally *= -1

def collide():
    global ballx
    ballx *= -1

def restart_game():
    ball.goto(0, 0)
    global ballx, bally, sleep_time
    total_score = player1_score + player2_score
    sleep_time = max(0.02, 0.1 - (total_score // 5) * 0.01)
    ballx = 10
    bally = 10

def update_score():
    score.clear()
    score.write(f"Player 1: {player1_score}  Player 2: {player2_score}", align="center", font=("Arial", 16, "normal"))


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_up2, "w")
screen.onkey(go_down2, "s")

update_score()

game_is_on = True
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    ball.goto(ball.xcor()+ballx, ball.ycor()+bally)

    if ball.ycor() > 280 or ball.ycor() < -280:
        bounce()
    
    if (ball.distance(paddle2) < 50 and ball.xcor() < -340) or (ball.distance(paddle) < 50 and ball.xcor() > 340):
        collide()
    
    if ball.xcor() > 400:
        player2_score += 1
        update_score()
        restart_game()
    
    if ball.xcor() < -400:
        player1_score += 1
        update_score()
        restart_game()

screen.exitonclick()
