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

# given the position of a plot, count the adjacent plots of the same plant and return (sides, [next plots to look at])
def get_adjacent(row, col):
    plant = txt[row][col]

    todo = []
    sides = 0
    up = (-1, 0)
    down = (1, 0)
    left = (0, -1)
    right = (0, 1)
    dirs = [up, right, down, left]
    def helper(d):
        if in_bounds(row + d[0], col + d[1]):
            return txt[row + d[0]][col + d[1]]

    chars = {plant, plant.upper()}
    for i, d in enumerate(dirs):
        next_dir = dirs[(i + 1) % 4]
       
        #  P x
        #  x
        # will get one side counted; 
        # P x will get two sides counted
        if helper(d) not in chars and helper(next_dir) not in chars:
            sides += 1

        # p x
        # P p
        # x p
        # above will count one side for P, this will count one more
        elif helper(d) in chars and helper(next_dir) in chars and helper((d[0] + next_dir[0], d[1] + next_dir[1])) not in chars:
            sides += 1

        if helper(d) == plant.upper():
            todo.append((row + d[0], col + d[1]))
            txt[row + d[0]][col + d[1]] = plant
    
    print(row, col, sides)
    return (sides, todo)

def evaluate_region(row, col):
    todo = deque()
    todo.append((row, col))
    txt[row][col] = txt[row][col].lower()
    area = 0
    sides = 0
    while todo:
        x, y = todo.pop()
        area += 1
        perim, plots = get_adjacent(x, y)
        sides += perim
        for plot in plots:
            todo.append(plot)

    print(f"Plant: {txt[row][col]}, sides: {sides}")
    return (sides, area)

def solution():
    res = 0
    for i in range(len(txt)):
        for j in range(len(txt[0])):
            if txt[i][j].isupper():
                perimeter, area = evaluate_region(i, j)
                res += perimeter * area
    return res

print(solution())