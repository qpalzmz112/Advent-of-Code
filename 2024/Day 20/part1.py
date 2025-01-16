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

def in_bounds(pos):
    return pos[0] >= 0 and pos[0] < len(orig_txt) and pos[1] >= 0 and pos[1] < len(orig_txt[0])

def solve(start, curr_dir, picoseconds, canCheat):
    dirs = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    cheats = {}
    
    todo = deque()
    todo.append((start, curr_dir, picoseconds, canCheat))

    while todo:
        pos, curr_dir, picoseconds, canCheat = todo.pop()

        if txt[pos] == 'E':
            if canCheat:
                return picoseconds, cheats
            else:
                return picoseconds

        for d in dirs:
            if d == (curr_dir[0] * -1, curr_dir[1] * -1):
                continue

            newPos = (pos[0] + d[0], pos[1] + d[1])
            if txt[newPos] != '#':
                todo.append((newPos, d, picoseconds + 1, canCheat))

            elif canCheat:
               cheatStart = (newPos[0] + d[0], newPos[1] + d[1])
               if in_bounds(cheatStart) and txt[cheatStart] != '#':
                   cheats[(newPos, cheatStart)] = solve(cheatStart, d, picoseconds + 2, False)

def solution():
    orig_time, cheats = solve(find_char('S'), (-1, 0), 0, True)
    return sum(1 if orig_time - cheats[key] >= 100 else 0 for key in cheats)
    

print(solution())

# change solution to go through maze once, making a note of each position we can cheat to (position: score at time of adding)
# then, for each position we are at, if it's a key in the above dictionary, update its value to (current score - score at time of adding + 2), i.e.,
# the number of steps the cheat saves