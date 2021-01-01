import turtle 

class Paddle(object): 
        def __init__(self): 
           
            # Creating left paddle for the game
            self.paddle_ = turtle.Turtle()
            self.paddle_.speed(0)
            self.paddle_.shape('square')
            self.paddle_.color('red')
            self.paddle_.shapesize(stretch_wid=5,stretch_len=1)
            self.paddle_.penup()
            self.paddle_.goto(-350,0)
        
        # De paddle naar boven laten bewegen 
        def paddle_left_up(self):
            y = self.paddle_.ycor()
            y = y + 15
            self.paddle_.sety(y)
        
        # De paddle naar beneden laten bewegen 
        def paddle_left_down(self):
            y = self.paddle_.ycor()
            y = y - 15
            self.paddle_.sety(y)