from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

paddle = Turtle("square")
paddle.color("white")
paddle.penup()
paddle.goto(350, 0)

ball = Turtle("circle")
ball.color("white")
ball.penup()

screen.exitonclick()
