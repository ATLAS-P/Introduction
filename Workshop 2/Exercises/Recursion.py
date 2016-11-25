


import turtle
import random

def tree(drawer, length, angle, branches):
    rint = random.random() * branches

    if ((rint > 2 or branches == 2) or length > 299) and length > 50 and branches > 1:
        drawer.color((length / 76) % 1, (length / 27) % 1, (length / 41) % 1)
        drawer.forward(length)

        drawer.left(angle)
        tree(drawer, length / 1.31, angle / 1.25, branches - 1)

        for i in range(branches):
            drawer.right((angle * 2) / branches)
            tree(drawer, length / 1.31, angle / 1.25, branches - 1)

        drawer.left(angle)

        drawer.up()
        drawer.backward(length)
        drawer.down()

drawer = turtle.Turtle()
screen = turtle.Screen()

screen.tracer(0, 0)
screen.setup(3840, 2160)

drawer.speed(0)
drawer.left(90)
drawer.up()
drawer.backward(500)
drawer.down()

tree(drawer, 300, 60, 8)
screen.update()

screen.exitonclick()