from turtle import Turtle


high_score=0
with open(file="data.txt", mode="r") as text:
    content = text.read()
    high_score = int(content)
    
ALIGMENT = 'center'
FONT = ('Courier' , 18, 'normal')

scorer =0 




    
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 255)
        scorestr = "Score = " + str(scorer)
        self.write(arg=scorestr  + " Highest Score " + str(high_score), align=ALIGMENT , font=FONT )
        self.hideturtle()
    

        
     
    
    