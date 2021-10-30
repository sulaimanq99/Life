import random
import time

def render(board):
    header = '-' * len(board[0])*3
    #print(header)
    for i in range(len(board)):
        str_board = list(map(str,(board[i])))
        str_board = [s.replace('0', '#') for s in str_board]
        print('|' + "  ".join(str_board) + "|")

def dead_state(height, width):
    board = []
    for i in range(height):
        board.append([])
        for k in range(width):
            board[i].append(0)

    return(board)

def random_state(height, width): # Creates a grid with 0's and 1's, dead or alive respectivley
    board =[]
    for i in range(height):
        board.append([])
        for k in range (width):
            state = random.randint(0,1)
            board[i].append(state)
    print (board[0])
    return(board)

def no_alive(board,a,b):
    x_end = len(board) -1
    y_end = len(board[0]) -1
    alive = 0
    for x1 in range(a-1,a+2):
        if x1 < 0: x1 = x_end
        elif x1> x_end: x1 = 0

        for y1 in range(b-1,b+2):
            if y1 == b and x1 == a:continue

            if y1<0: y1 = y_end
            elif y1 > y_end: y1 = 0

            alive+= board[x1][y1]
    return alive


def next_board_state(board):
    next_state = dead_state(len(board),len(board[0]))
    for i in range(len(board)):
        for k in range(len(board[0])):
            cells_alive = no_alive(board,i,k)
            state = board[i][k]

            if state ==1:
                if cells_alive <2 or cells_alive>3: next_state[i][k] = 0
                else: next_state[i][k] = 1
            elif state == 0 and cells_alive == 3: next_state[i][k] = 1

    return next_state

'''
000000
000000
001110
011100
000000
000000'''

if __name__ == '__main__':
    b = [
        [0,0,0,0,0,0],
        [0,1,1,0,0,0],
        [0,1,1,0,0,0],
        [0,0,0,1,1,0],
        [0,0,0,1,1,0],
        [0,0,0,0,0,0]
        ]

    render(b)
    while True:
        time.sleep(0.03)
        c = next_board_state(b)
        render(c)
        time.sleep(0.03)
        b = next_board_state(c)
        render(b)