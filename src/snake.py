
import turtle 

class Snake(object): 
    def __init__(self):
        # defineert head of snake 
        self.head = turtle.Turtle()
        self.head.shape("square") 
        self.head.color("white") 
        self.head.penup() 
        self.head.goto(0, 0) 
        self.head.direction = "Stop"

        #Segments 
        self.segments = []

    def goup(self): 
        if self.head.direction != "down": 
            self.head.direction = "up"
            
    def godown(self): 
        if self.head.direction != "up": 
            self.head.direction = "down"

    def goleft(self): 
        if self.head.direction != "right": 
            self.head.direction = "left"

    def goright(self): 
        if self.head.direction != "left": 
            self.head.direction = "right"

    def move(self): 
        if self.head.direction == "up": 
            y = self.head.ycor() 
            self.head.sety(y+20) 
        if self.head.direction == "down": 
            y = self.head.ycor() 
            self.head.sety(y-20) 
        if self.head.direction == "left": 
            x = self.head.xcor() 
            self.head.setx(x-20) 
        if self.head.direction == "right": 
            x = self.head.xcor() 
            self.head.setx(x+20) 
    


