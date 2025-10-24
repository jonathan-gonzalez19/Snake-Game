from turtle import Turtle
import random
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(random.randint(-380,380),random.randint(-280,280))
    def clear_up(self):
        self.clear
        self.goto(1000,1000)
        
    
    