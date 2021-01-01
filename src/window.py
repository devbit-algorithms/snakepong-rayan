
import turtle 
#Defineren van onze window 
class Window(object): 
    def __init__(self): 
        self.wn = turtle.Screen() 
        self.wn.title("Snake pong") 
        self.wn.bgcolor("blue") 
        self.wn.setup(width=800, height=600) 
        self.wn.tracer(0) 