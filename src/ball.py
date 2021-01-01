

# Ping-Pong game with turtle module.
# Done by Sri Manikanta Palakollu.
# Version - 3.7.0

import turtle 

class Ball(object):
    def __init__ (self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape('circle')
        self.ball.color('yellow')
        self.ball.penup()
        self.ball.goto(0,60)
        self.ball_dx = 3   
        self.ball_dy = 3
    



    