from turtle import Screen,Turtle
import time
import snake
import food
import score_board



high_score = 0

def reset():
    
    if score_board.scorer > score_board.high_score:
        score_board.high_score = score_board.scorer
        with open (file="data.txt", mode="w") as text:
           text.write(str(score_board.high_score))
    score_board.scorer = 0


def detect_collision_wall():
   
   if snaky.getXcordinates(0) > 385 or snaky.getXcordinates(0) < -385:
      return True
   if snaky.getYcordinates(0) > 285 or snaky.getYcordinates(0) < -285:
      return True

run_again = True

while run_again:
      
   screen = Screen()
   
   screen.setup(800,600)

   screen.bgcolor("black")
   
   choice = screen.textinput(title="Enter difficulty", prompt="Type easy, medium, hard").lower()

   screen.title("Welcome to my snake game")

   screen.tracer(0)

   snaky = snake.Snake()
   apple = food.Food()
   score = score_board.Score()
   game_over = Turtle()
   game_over.hideturtle()
   game_over.color("white")

   screen.listen()

   screen.onkey(key="Up",fun=snaky.up)
   screen.onkey(key="Left", fun=snaky.left)
   screen.onkey(key="Down", fun=snaky.down)
   screen.onkey(key="Right", fun=snaky.right)

   game_on = True

   while game_on:
      screen.update()
      if choice == "easy":
         time.sleep(0.1)
      elif choice == "medium":
         time.sleep(0.070)
      elif choice == "hard":
         time.sleep(0.055)
      else:
         time.sleep(0.1)
      snaky.move()
      if (apple.distance(snaky.getPosition(0)) < 20):
         apple.hideturtle()
         apple = food.Food()
         snaky.add_square()
         score_board.scorer+=1
         score.clear()
         score = score_board.Score()
      if detect_collision_wall() or snaky.detect_colision():
         game_over.write(arg="Game over", align='center',font=('Courier' , 18, 'normal'))
         user_choice = screen.textinput(title="Continue",prompt="Would you like to keep playing, yes or no")
         if user_choice == "yes":
            snaky.clear_everything()
            game_over.clear()
            score.clear()
            reset()
            apple.clear_up()
            game_on = False  
         else:
            game_on = False
            run_again = False
      
screen.exitonclick()
