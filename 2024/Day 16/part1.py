import os
import pathlib
from collections import deque, defaultdict

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split()
orig_txt = txt
txt = {}
for i, row in enumerate(orig_txt):
    for j, char in enumerate(row):
        txt[(i, j)] = char

def find_char(c):
    for i in range(len(orig_txt)):
        for j in range(len(orig_txt[0])):
            if txt[(i, j)] == c:
                return (i, j)

def solution():
    # N, E, S, W
    dirs = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    start = find_char('S')
    end = find_char('E')
    todo = deque()
    txt[start] = 0
    txt[end] = float('inf')
    # (position: (row, col), direction: (dRow, dCol), score: int)
    todo.append((start, (0, 1), 0))

    while todo:
        pos, direction, score = todo.pop()

        if txt[pos] ==  '.' or (isinstance(txt[pos], int) and txt[pos] > score):
            txt[pos] = score
        elif txt[pos] == float('inf'):
            txt[pos] = score
        elif txt[pos] < score:
            continue

        if pos == end:
            continue

        for d in dirs:
            if d != (direction[0] * -1, direction[1] * -1):
                newPos = (pos[0] + d[0], pos[1] + d[1])
                if txt[newPos] != '#':
                    if d == direction:                        
                        todo.append((newPos, d, score + 1))
                    else:
                        todo.append((newPos, d, score + 1001))

    return txt[end]

print(solution())