from turtle import *

class ScoreBoard(Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.score = 0
        self.goto(x,y)
        self.color("white")
        self.hideturtle()
        self.write(f"Score : {self.score}", False, "center", ("Arial", 20, "bold"))

    def l_update_score(self):
        self.clear()
        self.score +=1
        self.write(f"Score : {self.score}",False,"center",("Arial",20,"bold"))

    def r_update_score(self):
        self.clear()
        self.score +=1
        self.write(f"Score : {self.score}",False,"center",("Arial",20,"bold"))
