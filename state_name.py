from turtle import Turtle

FONT = ("Arial", 16, "normal")

class StateName(Turtle):
    def __init__(self, name, x_cor, y_cor):
        super().__init__()
        self.name = name
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.create_state_name()

    def create_state_name(self):
        self.hideturtle()
        self.penup()
        self.goto(self.x_cor, self.y_cor)
        self.write(self.name, align="center", font=FONT)