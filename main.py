# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import pygame as pg

def solve(bo):
    empty_bo = find_empty(bo)
    if empty_bo:
        row, col = empty_bo
    else:
        return True
    for i in range(1,10):
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


def valid(bo,row,col,i):
    for icol in range(np.shape(bo)[1]):
        if bo[row][icol] == i and icol != col:
            return False

    for irow in range(np.shape(bo)[0]):
        if bo[irow][col] == i and irow != row:
            return False

    box_row = int(np.floor(row/3))
    box_col = int(np.floor(col/3))
    for irow in range(box_row*3,box_row*3+2):
        for icol in range(box_col * 3, box_col * 3 + 2):
            if bo[irow][icol] == i and (irow != row or icol != col):
                return False
    return True


test = [[3, 0, 0, 8, 0, 1, 0, 0, 2],
        [2, 0, 1, 0, 3, 0, 6, 0, 4],
        [0, 0, 0, 2, 0, 4, 0, 0, 0],
        [8, 0, 9, 0, 0, 0, 1, 0, 6],
        [0, 6, 0, 0, 0, 0, 0, 5, 0],
        [7, 0, 2, 0, 0, 0, 4, 0, 9],
        [0, 0, 0, 5, 0, 9, 0, 0, 0],
        [9, 0, 4, 0, 8, 0, 7, 0, 5],
        [6, 0, 0, 1, 0, 7, 0, 0, 3]]
solve(test)
print(test)

test1 = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
solve(test1)
print(test1)