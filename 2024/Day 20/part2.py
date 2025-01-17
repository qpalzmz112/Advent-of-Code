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

def solve():
    dirs = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    cheats = defaultdict(list)
    start = find_char('S')

    todo = deque()
    todo.append((start, 0))
    while todo:
        pos, picoseconds = todo.pop()
        if pos in cheats:
            cheats[pos] = list(map(lambda x: picoseconds - x, cheats[pos]))

        if txt[pos] == 'E':
            return picoseconds, cheats
        txt[pos] = 'O'
        

        for d in dirs:
            newPos = (pos[0] + d[0], pos[1] + d[1])
            if txt[newPos] in ('.', 'E'):
                todo.append((newPos, picoseconds + 1))

            cheatEnd = (newPos[0] + d[0], newPos[1] + d[1])
            if txt[newPos] == '#' and in_bounds(cheatEnd) and txt[cheatEnd] in ('.', 'E'):
                cheats[cheatEnd].append(picoseconds + 2)
                # cheat is on tiles newPos, cheatEnd

def solution():
    orig_time, cheats = solve()
    return sum(1 if num >= 100 else 0 for val in cheats.values() for num in val)
    
print(solution())

# consider all possible values for cheatEnd at each pos - a cheatEnd can be at most 20 manhattan distance (dx + dy) away from pos