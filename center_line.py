from turtle import Turtle


class DottedLine(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=3, stretch_len=2)
        self.up()
        self.goto(0, -300)
        self.left(90)

    def draw_line(self):
        for i in range(0, 32):
            self.down()
            self.forward(20)
            self.up()
            self.forward(20)
