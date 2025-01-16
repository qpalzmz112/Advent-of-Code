import os
import pathlib
from collections import deque, defaultdict

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

txt = open("input.txt", "r")
txt = txt.read()


GRID_WIDTH = 70 if len(txt) > 1024 else 7

txt = txt.split()

def parse_row(s):
    return tuple(map(int, s.split(',')[::-1]))

txt = list(map(lambda x: parse_row(x), txt))
grid = {(i, j): float('inf') for i in range(GRID_WIDTH + 1) for j in range(GRID_WIDTH + 1)}

def drop_bytes(start, end):
    for i in range(start, end):
        grid[txt[i]] = '#'

def in_bounds(tup):
    return tup[0] >= 0 and tup[0] <= GRID_WIDTH and tup[1] >= 0 and tup[1] <= GRID_WIDTH

def solution():
    drop_bytes(0, 1024 if GRID_WIDTH == 70 else 12)
    dirs = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    start = (0, 0)
    end = (GRID_WIDTH, GRID_WIDTH)
    todo = deque()

    # (position: (row, col), score: int)
    todo.append((start, 0))

    while todo: 
        pos, steps = todo.pop()

        if grid[pos] > steps:
            grid[pos] = steps
        elif grid[pos] <= steps:
            continue

        if pos == end:
            continue

        for d in dirs:
            newPos = (pos[0] + d[0], pos[1] + d[1])
            if not in_bounds(newPos):
                continue
            if grid[newPos] != '#':
                todo.append((newPos, steps + 1))

    return grid[end]

print(solution())