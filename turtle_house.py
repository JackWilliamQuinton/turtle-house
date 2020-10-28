import math
import turtle

t = turtle.Turtle()
t.speed(10)

# Set the turtle to the bottom left corner
t.penup()
t.setx(-300)
t.sety(-250)
t.pendown()


class House:
    def __init__(self):
        pass

    # @staticmethod
    def square(self, side_length):
        global top_left_square
        for i in range(4):
            t.forward(side_length)
            t.left(90)
            if i == 2:
                top_left_square = [t.xcor(), t.ycor()]
        return()

    # @staticmethod
    def triangle(self, side_length):
        h = side_length / 4
        t.setx(top_left_square[0])
        t.sety(top_left_square[1])

        tri_sides = math.sqrt((h ** 2) + ((side_length ** 2) / 4))
        degree = math.degrees(math.atan((2 * h) / side_length))
        t.setheading(0)
        t.forward(side_length)

        t.left(180 - degree)
        t.forward(tri_sides)
        t.left(degree * 2)
        t.forward(tri_sides)
        t.setheading(0)

    # @staticmethod
    def door(self, side_length, x, y):
        t.sety(y)
        door_start = (side_length / 5) * 2
        t.forward(door_start)
        t.setheading(90)
        t.forward(side_length / 3)
        t.setheading(0)
        t.forward(side_length / 5)
        t.setheading(270)
        t.forward(side_length / 3)
        t.setheading(180)
        t.forward(side_length / 5 + door_start)
        t.setheading(0)

    # @staticmethod
    def left_window(self, rep, side_length, x, y):
        t.penup()
        t.forward(side_length / 20)
        t.setheading(90)
        t.forward(side_length / 10 * 5)
        t.setheading(0)
        t.pendown()
        if rep > 1:
            side_length = side_length / 100 * 30
            test = t.position()[0]
            x = t.position()[0]
            y = t.position()[1]
            rep -= 1
            self.build(rep, side_length, x, y)
        else:
            self.square(side_length / 100 * 30)

    # @staticmethod
    def right_window(self, rep, side_length, x, y):
        t.penup()
        t.setx(x)
        t.sety(y)
        t.forward(side_length / 20 * 12)
        t.setheading(90)
        t.forward(side_length / 10 * 5)
        t.setheading(0)
        t.pendown()
        if rep > 1:
            side_length = side_length / 100 * 30
            x = t.position()[0]
            y = t.position()[1]
            rep -= 1
            self.build(rep, side_length, x, y)
        else:
            self.square(side_length / 100 * 30)

    def build(self, rep, side_length, x, y):
        self.square(side_length)
        self.triangle(side_length)
        self.door(side_length, x, y)
        self.left_window(rep, side_length, x, y)
        self.right_window(rep, side_length, x, y)


while __name__ == '__main__':
    house1 = House()
    repetitions = int(input("Enter repetitions 1-5 \n> "))
    house_size = int(input("Enter House size \n> "))
    house1.build(repetitions, house_size, x=-300, y=-250)
    turtle.done()


