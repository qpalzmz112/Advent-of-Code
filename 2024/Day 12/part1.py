import os
from collections import deque

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 12")

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split()
txt = list(map(list, txt))

# when starting to evaluate a region, do bfs/dfs
# grab first plot, add 4 - <num adjacent plots of same letter> to perimeter total, add 1 to area total,
# add adjacent plots of same letter (that haven't already been counted) to stack/queue, and mark current plot as (letter, True) or something to mark that it's been counted
# if . is the value for a done plot, then it's hard to correctly identify a plot that should contribute 0 to its region's perimeter

def in_bounds(row, col):
    return row >= 0 and col >= 0 and row < len(txt) and col < len(txt[0])

# given the position of a plot, count the adjacent plots of the same plant and return (perimeter, [next plots to look at])
def get_adjacent(row, col):
    plant = txt[row][col]
    perimeter = 4

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    todo = []
    for d in dirs:
        pos = (row + d[0], col + d[1])
        if in_bounds(pos[0], pos[1]):
            if txt[pos[0]][pos[1]] == plant.upper():
                perimeter -= 1
                txt[pos[0]][pos[1]] = plant
                todo.append(pos)
            elif txt[pos[0]][pos[1]] == plant:
                perimeter -= 1
    return (perimeter, todo)

def evaluate_region(row, col):
    todo = deque()
    todo.append((row, col))
    txt[row][col] = txt[row][col].lower()
    area = 0
    perimeter = 0
    while todo:
        x, y = todo.pop()
        area += 1
        perim, plots = get_adjacent(x, y)
        perimeter += perim
        for plot in plots:
            todo.append(plot)

    return (perimeter, area)

def solution():
    res = 0
    for i in range(len(txt)):
        for j in range(len(txt[0])):
            if txt[i][j].isupper():
                perimeter, area = evaluate_region(i, j)
                res += perimeter * area
    return res

print(solution())