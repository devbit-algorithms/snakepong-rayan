from snake import Snake
from paddle import Paddle
from window import Window
from ball import Ball
import turtle 
import time 
import random 

# Atribuut 
delay = 0.1

#Pen contour 
pen = turtle.Turtle() 
pen.speed(0) 
pen.shape("square") 
pen.color("white") 
pen.penup() 
pen.hideturtle() 
pen.goto(0, 250) 

#variable voor klasse window 
window = Window()

#variable van klasse paddle 
paddle = Paddle()

#variable van klasse snake 
snake = Snake()

#variable van klasse ball
bal = Ball()

#Movements 
window.wn.listen()
window.wn.onkeypress(snake.goup, "Up") 
window.wn.onkeypress(snake.godown, "Down") 
window.wn.onkeypress(snake.goleft, "Left") 
window.wn.onkeypress(snake.goright, "Right")
window.wn.onkeypress(paddle.paddle_left_up,"z")
window.wn.onkeypress(paddle.paddle_left_down,"s")

# Waarin de game word uitgevoerd 
while True: 

    # Belangerijk om de game te runnen
    window.wn.update() 

    # Om e bal te laten bewegen 
    bal.ball.setx(bal.ball.xcor() + bal.ball_dx) # Horizontale beweging 
    bal.ball.sety(bal.ball.ycor() + bal.ball_dy) # Verticale beweging 
    

    # setting om de border van boven 
    if bal.ball.ycor() < -290:  
        bal.ball.sety(-290)     
        bal.ball_dy = bal.ball_dy * -1 #tegenovergestaande richting beweging 

    if(bal.ball.xcor()) < -390: # linkse lengte van de paddle 
        bal.ball.goto(0,0)
        bal.ball_dx = bal.ball_dx * -1

        # Segment eraan toevoegen 
        new_segment = turtle.Turtle() 
        new_segment.speed(0) 
        new_segment.shape("square") 
        new_segment.color("orange")  # tail colour 
        new_segment.penup() 
        snake.segments.append(new_segment) 
        delay -= 0.001

    # Als die tegen de paddle zit 
    if(bal.ball.xcor() < -340) and (bal.ball.xcor() > -350) and (bal.ball.ycor() < paddle.paddle_.ycor() + 40 and bal.ball.ycor() > paddle.paddle_.ycor() - 40):
        bal.ball.setx(-340)
        ball_dx = ball_dx * -1

    # De randen 
   # if(ball.ycor() > 300) or  (ball.xcor() < -400 ) or (ball.ycor() > -300): 
       # ball_dx = ball_dx * -1
    # right width paddle Border
    if bal.ball.xcor() > 390:   
        ball_dx = ball_dx * -1

    # De slang body tegen zich zelf 
    if(bal.ball.distance(snake.head) < 50):
        bal.ball_dx = bal.ball_dx * -1
        bal.ball_dy = bal.ball_dy * -1

    # Limit snake head 
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290: 
        time.sleep(1) 
        snake.head.goto(0, 0) 
        snake.head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green']) 
        shapes = random.choice(['square', 'circle']) 
        for segment in snake.segments: 
            segment.goto(1000, 1000) 
        snake.segments.clear() 
        delay = 0

    # Controlle als de head tegen de body segmenten zit 
    for index in range(len(snake.segments)-1, 0, -1): 
        x = snake.segments[index-1].xcor() 
        y = snake.segments[index-1].ycor() 
        snake.segments[index].goto(x, y) 
    if len(snake.segments) > 0: 
        x = snake.head.xcor() 
        y = snake.head.ycor() 
        snake.segments[0].goto(x, y) 
    snake.move()

    for segment in snake.segments: 
        if segment.distance(snake.head) < 20: 
            time.sleep(1) 
            snake.head.goto(0, 0) 
            snake.head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green']) 
            shapes = random.choice(['square', 'circle']) 
            for segment in snake.segments: 
                segment.goto(1000, 1000) 
            segment.clear() 
  
            delay = 0.1
    
    time.sleep(delay) 

window.wn.mainloop() 



