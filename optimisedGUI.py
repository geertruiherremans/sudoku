import numpy as np
import pygame
import copy
import time
from pygame.locals import *

# Functionalities
plot = True

# initialise the pygame font
pygame.font.init()

# Total window
screen = pygame.display.set_mode((500, 500))

# Title and Icon
pygame.display.set_caption("Sudoku solver")

x = 0
y = 0
dif = 500 / 9
BLACK = 0, 0, 0
WHITE = 255, 255, 255
BLUE = 225, 246, 255
BLUE2 = 0, 0, 200
RED = 255, 0, 0

board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]

board = [[3, 0, 0, 8, 0, 1, 0, 0, 2],
        [2, 0, 1, 0, 3, 0, 6, 0, 4],
        [0, 0, 0, 2, 0, 4, 0, 0, 0],
        [8, 0, 9, 0, 0, 0, 1, 0, 6],
        [0, 6, 0, 0, 0, 0, 0, 5, 0],
        [7, 0, 2, 0, 0, 0, 4, 0, 9],
        [0, 0, 0, 5, 0, 9, 0, 0, 0],
        [9, 0, 4, 0, 8, 0, 7, 0, 5],
        [6, 0, 0, 1, 0, 7, 0, 0, 3]]


def draw(bo):
    for i in range(11):
        if i % 3 == 0:
            pygame.draw.line(screen, BLACK, (dif * i, 0), (dif * i, 500), width=3)
        else:
            pygame.draw.line(screen, BLACK, (dif * i, 0), (dif * i, 500))
    for j in range(11):
        if j % 3 == 0:
            pygame.draw.line(screen, BLACK, (0, dif * j), (500, dif * j), width=3)
        else:
            pygame.draw.line(screen, BLACK, (0, dif * j), (500, dif * j))
    for i in range(9):
        for j in range(9):
            if original[j][i] != 0:
                font2 = pygame.font.SysFont(str(bo[j][i]), 60)
                img2 = font2.render(str(bo[j][i]), True, BLACK)
                screen.blit(img2, (i * dif + 15, j * dif + 10))
            elif bo[j][i] != 0:
                font2 = pygame.font.SysFont(str(bo[j][i]), 60)
                img2 = font2.render(str(bo[j][i]), True, BLUE2)
                screen.blit(img2, (i * dif + 15, j * dif + 10))


num_dict = {K_1: 1, K_2: 2, K_3: 3, K_4: 4, K_5: 5, K_6: 6, K_7: 7, K_8: 8, K_9: 9}
key_dict = {K_LEFT: (-1, 0), K_RIGHT: (1, 0), K_UP: (0, -1), K_DOWN: (0, 1)}
run = True


def highlight_box(i, j):
    pygame.draw.rect(screen, BLUE, (dif * i, dif * j, dif, dif))


def valid(bo, row, col, i):
    for icol in range(np.shape(bo)[1]):
        if bo[row][icol] == i and icol != col:
            return False

    for irow in range(np.shape(bo)[0]):
        if bo[irow][col] == i and irow != row:
            return False

    box_row = int(np.floor(row / 3))
    box_col = int(np.floor(col / 3))
    for irow in range(box_row * 3, box_row * 3 + 2):
        for icol in range(box_col * 3, box_col * 3 + 2):
            if bo[irow][icol] == i and (irow != row or icol != col):
                return False
    return True


def optimised_solve(bo):
    quick_solve(bo)
    solve(bo)


def quick_solve(bo):
    updated = True
    while updated:
        updated = False
        all_empty = np.argwhere(np.array(bo) == 0)
        for index in all_empty:
            if unique_solution(bo,index[0],index[1]):
                bo[index[0]][index[1]] = unique_solution(bo,index[0],index[1])
                updated = True


def unique_solution(bo,i,j):
    solution = 0
    for value in range(1,10):
        if valid(bo,i,j,value):
            if solution:
                return False
            else:
                solution = value
    return solution


def solve(bo):
    if plot:
        screen.fill(WHITE)
        draw(bo)
        pygame.display.update()
    empty_bo = find_empty(bo)
    if empty_bo:
        row, col = empty_bo
    else:
        return True
    for i in range(1, 10):
        if valid(bo, row, col, i):
            bo[row][col] = i
            if solve(bo):
                return True
        bo[row][col] = 0
    return False


def find_empty(bo):
    for i in range(np.shape(bo)[0]):
        if not np.all(bo[i]):
            return i, bo[i].index(0)
    return False


font1 = pygame.font.SysFont('', 60)
img1 = font1.render('', True, BLACK)
original = copy.deepcopy(board)
solve_board = copy.deepcopy(board)
wrong = 0
to_solve = True
while run:
    while to_solve:
        screen.fill(WHITE)
        highlight_box(x, y)
        draw(board)
        if wrong == 1:
            screen.blit(img1, (x * dif + 15, y * dif + 10))
        pygame.display.update()
        # pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in key_dict:
                    x = max(min(x + key_dict[event.key][0], 8), 0)
                    y = max(min(y + key_dict[event.key][1], 8), 0)
                    wrong = 0
                if event.key == K_BACKSPACE:
                    if original[y][x] == 0:
                        board[y][x] = 0
                if event.key in num_dict:
                    if original[y][x] == 0:
                        if valid(board, y, x, num_dict[event.key]):
                            board[y][x] = num_dict[event.key]
                            wrong = 0
                        else:
                            font1 = pygame.font.SysFont('x', 60)
                            img1 = font1.render('x', True, RED)
                            wrong = 1
                if event.key == K_SPACE:
                    pygame.display.set_caption("Let's solve this puzzle!")
                    draw(original)
                    pygame.display.update()
                    tic = time.perf_counter()
                    optimised_solve(solve_board)
                    toc = time.perf_counter()
                    pygame.display.set_caption(f"Solved puzzle in {toc - tic:0.4f} seconds")
                    screen.fill(WHITE)
                    draw(solve_board)
                    pygame.display.update()
                    to_solve = False
            if event.type == pygame.QUIT:
                run = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()