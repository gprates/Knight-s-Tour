import random
from turtle import Screen, Turtle
from datetime import datetime


class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y


GRID_SIZE = 600

tamanho_tabuleiro = 8

center = (GRID_SIZE / 8) / 2

cx = [1, 1, 2, 2, -1, -1, -2, -2]
cy = [2, -2, 1, -1, 2, -2, 1, -1]

indices_x = {
    0: -300 + center,
    1: -225 + center,
    2: -150 + center,
    3: -75 + center,
    4: 0 + center,
    5: 75 + center,
    6: 150 + center,
    7: 225 + center
}

indices_y = {
    0: 225 + center,
    1: 150 + center,
    2: 75 + center,
    3: 0 + center,
    4: -75 + center,
    5: -150 + center,
    6: -225 + center,
    7: -300 + center,
}

screen = Screen()
turtle = Turtle()

def desenha_grid():
    cell_size = GRID_SIZE / float(tamanho_tabuleiro)

    turtle.speed(0)
    turtle.penup()
    turtle.goto(-GRID_SIZE/2, GRID_SIZE/2)
    turtle.pendown()

    angle = 90

    for _ in range(4):
        turtle.forward(GRID_SIZE)
        turtle.right(angle)

    for _ in range(2):
        for _ in range(1, tamanho_tabuleiro):
            turtle.forward(cell_size)
            turtle.right(angle)
            turtle.forward(GRID_SIZE)
            turtle.left(angle)

            angle = -angle

        turtle.forward(cell_size)
        turtle.right(angle)

def desenha_cavalo():
    i = 0


    for x, y in zip(cx,cy):
        turtle.penup()
        turtle.goto(indices_x[4], indices_y[4])
        turtle.pendown()
        turtle.speed(2)
        if abs(x) > abs(y):
            turtle.goto(indices_x[4+x], indices_y[4])
            turtle.goto(indices_x[4+x], indices_y[4+y])
        else:
            turtle.goto(indices_x[4], indices_y[4+y])
            turtle.goto(indices_x[4+x], indices_y[4+y])

        turtle.write(i + 1)
        i += 1

if __name__ == '__main__':
    desenha_grid()

    desenha_cavalo()
    
    screen.exitonclick()