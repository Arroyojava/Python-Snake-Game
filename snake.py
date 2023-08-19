from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-5, 0), (-10, 0), (-15, 0), (-20, 0), (-25, 0), (-30, 0), (-35, 0)]
MOVE_DISTANCE = 5
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turtle_segments = []
        self.create_snake()
        self.head = self.turtle_segments[0]
        self.final_speed = 0.01

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        turtle_segment = Turtle(shape="circle")
        turtle_segment.color("light green")
        turtle_segment.penup()
        turtle_segment.setposition(position)
        self.turtle_segments.append(turtle_segment)

    def extend(self):
        for i in range(3):
            self.add_segment(self.turtle_segments[-1].position())

    def move(self):
        for segment in range(len(self.turtle_segments) - 1, 0, -1):
            new_x = self.turtle_segments[segment - 1].xcor()
            new_y = self.turtle_segments[segment - 1].ycor()
            self.turtle_segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def increase_speed(self, current_speed):
        speed = current_speed - 0.0008
        if speed < 0:
            return self.final_speed
        else:
            print(speed)
            return speed

    def reset(self):
        for seg in self.turtle_segments:
            seg.goto(1000, 1000)
        self.turtle_segments.clear()
        self.create_snake()
        self.head = self.turtle_segments[0]
