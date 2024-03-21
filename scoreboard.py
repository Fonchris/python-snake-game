from turtle import Turtle
FONT = ("courier",20,"normal")
SCORE_POSITION = (0,270)
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score =0
        with open("data.txt")as data:
           self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(SCORE_POSITION)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"score:{self.score} high_score :{self.high_score}",font =FONT,align="center")
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_scoreboard()
    # def game_over(self):
        #self.goto(0,0)
        #self.write(f"GAME_OVER", font=FONT, align="center")