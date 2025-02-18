from turtle import Turtle
STARTING_POSITIONS=[(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN =270
LEFT =180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments =[]
        self.create_snake()
        self.snake_head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
           self.add_segment(position)
    def add_segment(self,position):
        self.segment = Turtle("square")
        self.segment.color("white")
        self.segment.penup()
        self.segment.goto(position)
        self.segments.append(self.segment)
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)
    def up(self):
        if self.snake_head.heading()!=DOWN:
           self.snake_head.setheading(UP)
    def down(self):
        if self.snake_head.heading() !=UP:
           self.snake_head.setheading(DOWN)
    def left(self):
        if self.snake_head.heading() !=RIGHT:
           self.snake_head.setheading(LEFT)
    def right(self):
        if self.snake_head.heading() !=LEFT:
           self.snake_head.setheading(RIGHT)