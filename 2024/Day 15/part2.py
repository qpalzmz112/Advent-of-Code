import os
import pathlib
import copy
from collections import deque

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

txt = open("input.txt", "r")
txt = txt.read()

def parse(s):
    res = []
    for c in s:
        match c:
            case '@':
                res.append('@')
                res.append('.')
            case 'O':
                res.append('[')
                res.append(']')
            case _:
                res.append(c)
                res.append(c)
    return res

warehouse, movements = txt.split('\n\n')
warehouse = list(map(parse, warehouse.split()))
movements = ''.join(movements.split())

def find_robot():
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == '@':
                return (i, j)

def can_move_box(x, y, dx, dy):
    # moving vertically
    y_offset = 0
    if dx != 0:
        if warehouse[x][y] == '[':
            y_offset = 1
        else:
            y_offset = -1
        return warehouse[x + dx][y] != '#' and warehouse[x + dx][y + y_offset] != '#'

    # moving horizontally
    else:
        if warehouse[x][y] == '[':
            y_offset = 2 if dy == 1 else -1
        else:
            y_offset = 1 if dy == 1 else -2
        return warehouse[x][y + y_offset] != '#'

def move_boxes(x, y, dx, dy):
    # try to move a contiguous set of boxes one space in the given direction, returning True if the move was possible
    # {'[': {set of indices where the half will move if a move is possible}, ']': {set of indices...}}
    # mark boxes' spaces as free while building the above dict - if we end up not doing the move, backtrack
    # if we stop finding more boxes to move without any being unable to, go through the dict and do the obvious thing
    indices = {'[': set(), ']': set()}
    todo = deque()
    todo.append((x, y))

    while todo:
        row, col = todo.pop()
        char = warehouse[row][col]
        if char not in indices:
            continue
        if not can_move_box(row, col, dx, dy):
            return False

        indices[char].add((row + dx, col + dy))
        warehouse[row][col] = '.'
        if char == '[':
            todo.append((row, col + 1))
        else:
            todo.append((row, col - 1))
        todo.append((row + dx, col + dy))
    
    # haven't returned False, so we can move the boxes
    for c in indices:
        for row, col in indices[c]:
            warehouse[row][col] = c
    return True    

def move(x, y, dx, dy):
    global warehouse
    # return robot's new position if it moves
    if warehouse[x + dx][y + dy] == '#':
        return
    elif warehouse[x + dx][y + dy] in {'[', ']'}:
        prev_warehouse = copy.deepcopy(warehouse)
        if move_boxes(x + dx, y + dy, dx, dy):
            warehouse[x][y] = '.'
            warehouse[x + dx][y + dy] = '@'
            return (x + dx, y + dy)
        else:
            warehouse = prev_warehouse
    else:
        warehouse[x + dx][y + dy] = '@'
        warehouse[x][y] = '.'
        return (x + dx, y + dy)

def calculate_answer():
    res = 0
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0])):
            if warehouse[i][j] == '[':
                res += 100 * i + j
    return res

def print_warehouse():
    for row in warehouse:
        print(''.join(row))
    print('\n')

def solution():
    moves = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
    x, y = find_robot()
    for m in movements:
        dx, dy = moves[m]
        tmp = move(x, y, dx, dy)
        if tmp is not None:
            x, y = tmp        
    print(calculate_answer())

solution()