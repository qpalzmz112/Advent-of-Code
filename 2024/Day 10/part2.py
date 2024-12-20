import os
from collections import deque

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 10")

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split()

def in_bounds(pos):
    row, col = pos
    return row >= 0 and col >= 0 and row < len(txt) and col < len(txt[0])

def txt_get(pos):
    return txt[pos[0]][pos[1]]

def evaluate_trailhead(row, col):
    peaks = 0
    todo = deque()
    todo.append((row, col))

    while todo:
        x, y = todo.pop()
        if txt[x][y] == '9':
            peaks += 1
            continue
        
        curr_height = txt_get((x, y))
        left = (x, y - 1)
        right = (x, y + 1)
        up = (x - 1, y)
        down = (x + 1, y)

        for pos in [left, right, up, down]:
            if in_bounds(pos) and txt_get(pos) == str(int(curr_height) + 1):
                todo.append(pos)

    return peaks

def solution():
    res = 0
    for row in range(len(txt)):
        for col in range(len(txt[0])):
            if txt[row][col] == '0':
                res += evaluate_trailhead(row, col)
    return res

print(solution())
                

    
