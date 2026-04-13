from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, x,y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(6,1)
        self.color("white")
        self.speed("fastest")
        self.goto(x,y)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def r_control(self):
        self.screen.listen()
        self.screen.onkey(self.up, "Up")
        self.screen.onkey(self.down, "Down")

    def l_control(self):
        self.screen.listen()
        self.screen.onkey(self.up, "w")
        self.screen.onkey(self.down, "s")