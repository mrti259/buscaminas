#!/usr/bin/python3
from random import randint
from os import system

def clean_screen():
    system('clear')
    system('cls')

def check_input(text, conditions):
    answer = input(text)
    while True:
        for condition in conditions:
            if answer == str(condition):
                return answer
        answer = input(text)

def generate_board(rows_number, columns_number, mines_number):
    board = []
    # Generating rows and columns
    for i in range(rows_number +2): #2 extras
        board_row = []
        for j in range(columns_number +2): #2 extras
            board_row.append(0)
        board.append(board_row)
    # Placing mines
    while mines_number > 0: 
        row = randint(1, rows_number)
        column = randint(1, columns_number)
        if board[row][column] < 9:
            board[row][column] = 69
            # Placing hints
            for m in range(-1, 2):
                for n in range(-1, 2):
                    board[row+m][column+n] += 1
            mines_number -= 1
    # Changing no-hint values
    row = 0
    for rows in board:
        column = 0
        for i in rows:
            if i == 0:
                board[row][column] = '  '
            elif i > 9:
                board[row][column] = 'X '
            else:
                board[row][column] = str(board[row][column]) + ' '
            column += 1
        row += 1
    return board

def count(what, where):
    count = 0
    for row in where:
        for i in row:
            if i == what:
                count += 1
    return count

def print_board(board):
    print('\n '+'\\', end=' ')
    for c in range(1, len(board[0])-1):
        if c < 10:
            print(' %s'%c, end=' ')
        else:
            print('%s'%c, end=' ')
    print('/ ')
    r = 1
    for row in board[1:len(board)-1]:
        if r < 10:
            print(' %s|'%r, end='')
        else:
            print('%s'%r, end='|')
        for i in row[1:len(row)-1]:
            print(i, end='|')
        if r < 10:
            print(' %s'%r)
        else:
            print('%s'%r)
        r += 1
    print(' /',end=' ')
    for c in range(1, len(board[0])-1):
        if c < 10:
            print(' %s'%c, end=' ')
        else:
            print('%s'%c, end=' ')
    print('\\'+' ')


def updating_board(board1, board2, row, column):
    if board1[row][column] == '  ':
        board2[row][column] = '__'
        blanks.append([row, column])
    else:
        board2[row][column] = board1[row][column]

def blank(board1, board2, row, column):
    if row > 0 and row <= rows and column > 0 and column <= columns:
        for m in range(-1, 2):
            for n in range(-1, 2):
                if not [row+m, column+n] in blanks:
                    updating_board(board1, board2, row+m, column+n)


# User choose how to play
rows = int(check_input('Elija una cantidad de filas (de 8 a 20): ', range(8, 21)))
columns = int(check_input('Elija una cantidad de columnas (de 8 a 20): ', range(8,21)))

gameboard = generate_board(rows, columns, int(0.1*rows*columns))
#print_board(gameboard)
userboard = generate_board(rows, columns, 0)

while True:
    clean_screen()
    print_board(userboard)
    print('Hay', count('X ', gameboard), 'minas ocultas.')
    print('Hay', count('F ', userboard), 'banderas ubicadas.\n')

    column = int(check_input('Elija una columna: ', range(1, columns+1)))
    row = int(check_input('Elija una fila: ', range(1, rows+1)))
    flag = input('Ingrese \'F\' si quiere colocar una bandera: ').upper()

    if len(flag) > 0 and flag[0] == 'F':
        userboard[row][column] = 'F '
    else:
        if gameboard[row][column] == '  ':
            blanks = [[row, column]]
            for d in blanks:
                r = d[0]
                c = d[1]
                blank(gameboard, userboard, r, c)
        updating_board(gameboard, userboard, row, column)

    if count('X ', userboard) > 0:
        clean_screen()
        print_board(userboard)
        print('¡MINA! Perdiste.')
        break
    elif count('F ', userboard) == count('X ', gameboard):
        check_board = []
        for i in userboard[1:rows]:
            row = []
            for j in i[1:columns]:
                row.append(j)
            check_board.append(row)
        if count('  ', check_board) == 0:
            clean_screen()
            print_board(userboard)
            print('¡Ganaste!')
            break
