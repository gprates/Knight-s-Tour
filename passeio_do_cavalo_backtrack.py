import random
from turtle import Screen, Turtle
from datetime import datetime


GRID_SIZE = 600

tamanho_tabuleiro = 8

center = (GRID_SIZE / 8) / 2

vetor_indices = [
    None,None,None,None,None,None,None,None,
    None,None,None,None,None,None,None,None,
    None,None,None,None,None,None,None,None,
    None,None,None,None,None,None,None,None,
    None,None,None,None,None,None,None,None,
    None,None,None,None,None,None,None,None,
    None,None,None,None,None,None,None,None,
    None,None,None,None,None,None,None,None
]

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

def is_movimento_valido(x, y, tabuleiro):
    if (x >= 0 and y >= 0 and x < tamanho_tabuleiro and y < tamanho_tabuleiro and tabuleiro[x][y] == -1):
        return True
    return False


def print_tabuleiro(tamanho_tabuleiro, tabuleiro):
    for i in range(tamanho_tabuleiro):
        for j in range(tamanho_tabuleiro):
            if i <=7 and j <= 7:
                vetor_indices[tabuleiro[i][j]] = (i,j)
            print(tabuleiro[i][j], end=' ')
        print()


def resolver_passeio(tamanho_tabuleiro):
    tabuleiro = [[-1 for i in range(tamanho_tabuleiro)] for i in range(tamanho_tabuleiro)]

    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # com posição aleatória, porém pode demorar até 4 horas pra rodar dependendo da posição alocada
    # x_inicial = random.randint(0, tamanho_tabuleiro - 1)
    # y_inicial = random.randint(0, tamanho_tabuleiro - 1)
    tabuleiro[0][0] = 0

    pos = 1

    if (find_passeio_valido(tamanho_tabuleiro, tabuleiro, 0, 0, move_x, move_y, pos)):
        print_tabuleiro(tamanho_tabuleiro, tabuleiro)


def find_passeio_valido(tamanho_tabuleiro, tabuleiro, curr_x, curr_y, move_x, move_y, pos):
    if (pos == tamanho_tabuleiro**2):
        return True

    for i in range(tamanho_tabuleiro):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if (is_movimento_valido(new_x, new_y, tabuleiro)):
            tabuleiro[new_x][new_y] = pos
            if (find_passeio_valido(tamanho_tabuleiro, tabuleiro, new_x, new_y, move_x, move_y, pos + 1)):
                return True

            tabuleiro[new_x][new_y] = -1
    return False

def desenha_grid():
    cell_size = GRID_SIZE / float(tamanho_tabuleiro)

    turtle.speed(0)
    turtle.penup()
    turtle.goto(-GRID_SIZE / 2, GRID_SIZE / 2)
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


def desenha_grafico():
    i = 0
    print(vetor_indices)
    print(len(vetor_indices))

    turtle.penup()
    turtle.goto(indices_x[vetor_indices[0][0]], indices_y[vetor_indices[0][1]])
    turtle.pendown()
    turtle.speed(7)

    for x, y in vetor_indices:
        turtle.goto(indices_x[x], indices_y[y])
        turtle.write(i + 1)
        i+=1


if __name__ == "__main__":
    desenha_grid()

    inicio = datetime.now()
    resolver_passeio(tamanho_tabuleiro)
    fim =  datetime.now()
    print('Tempo: ',fim-inicio)

    desenha_grafico()

    screen.exitonclick()