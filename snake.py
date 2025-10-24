from turtle import Turtle
class Snake:
    snakes = []
    def __init__(self):
        pos = 0
        for i in range(3):
            square = Turtle("square")
            square.color("white")
            square.penup()
            square.setposition(pos,0)
            pos-=20
            self.snakes.append(square)
    def move(self):
        for i in range (len(self.snakes)-1, 0, -1):
            xcor = self.snakes[i-1].xcor()
            ycor = self.snakes[i-1].ycor()
            self.snakes[i].goto(xcor,ycor)
        self.snakes[0].forward(20)
    def up(self):
        if self.snakes[0].heading() != 270  :
            self.snakes[0].setheading(90)
        
    def down(self):
        if self.snakes[0].heading() != 90:
            self.snakes[0].setheading(270)
            
    def left(self):
        if self.snakes[0].heading() != 0:
            self.snakes[0].setheading(180)
    def right(self):
        if self.snakes[0].heading() != 180:
            self.snakes[0].setheading(0)
    def getPosition(self,index):
        
        for i in range (len(self.snakes)):
            if i == index:
                return self.snakes[i].position()
    def getXcordinates(self,index):
        for i in range (len(self.snakes)):
            if i == index:
                return self.snakes[i].xcor()
    def getYcordinates(self,index):
        for i in range (len(self.snakes)):
            if i == index:
                return self.snakes[i].ycor()
    def add_square(self):
        square = Turtle("square")
        square.goto(self.snakes[-1].position())
        square.penup()
        self.snakes.append(square)
        square.hideturtle()
        square.color("black")
        square.showturtle()
        square.color("white")
    def detect_colision(self):
        
        head = self.snakes[0]
        
        for i in self.snakes[1:]:
            
            if head.distance(i) < 10:
                return True
    def clear_everything(self):
        
        for i in self.snakes:
            i.goto(1000,1000)
        self.snakes.clear()
        pos = 0
        for i in range(3):
            square = Turtle("square")
            square.color("white")
            square.penup()
            square.setposition(pos,0)
            pos-=20
            self.snakes.append(square)
        self.snakes[0] = self.snakes[0]
        
        
        
                
        
           
            
            
            
        
        

