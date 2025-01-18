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

def get_cheats(pos, threshold):
    res = 0

    row_width = 1
    for i in range(pos[0] - 20, pos[0] + 21):
        dx = row_width // 2

        for j in range(pos[1] - dx, pos[1] + dx + 1):
            cheatEnd = (i, j)
            if in_bounds(cheatEnd) and txt[cheatEnd] != '#':
                diff_x = abs(pos[0] - i)
                diff_y = abs(pos[1] - j)
                if diff_x + diff_y > 20:
                        print(diff_x, diff_y)
                        continue
                if txt[pos] - txt[cheatEnd] - diff_x - diff_y >= threshold:
                    #print(f"start: {pos}, txt[start]: {txt[pos]}, end: {cheatEnd}, txt[end]: {txt[cheatEnd]}, manhattan distance: {diff_x + diff_y}")
                    res += 1
                    

        row_width += 2 * (1 if i < pos[1] else -1)

    return res

def preprocess(dirs):
    end = find_char('E')
    todo = deque()
    todo.append((end, 0))

    while todo:
        pos, picoseconds = todo.pop()
        txt[pos] = picoseconds      

        for d in dirs:
            newPos = (pos[0] + d[0], pos[1] + d[1])
            if txt[newPos] in('.', 'S'):
                todo.append((newPos, picoseconds + 1))
                break

def solve(start, dirs, threshold):
    res = 0

    todo = deque()
    todo.append(start)
    while todo:
        pos = todo.pop()
        res += get_cheats(pos, threshold)

        if txt[pos] == 0:
            return res     

        for d in dirs:
            newPos = (pos[0] + d[0], pos[1] + d[1])
            if isinstance(txt[newPos], int) and txt[newPos] < txt[pos]:
                todo.append(newPos)
                break

def solution():
    start = find_char('S')
    dirs = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    preprocess(dirs)
    return solve(start, dirs, 100)
    
print(solution())
# consider all possible values for cheatEnd at each pos - a cheatEnd can be at most 20 manhattan distance (dx + dy) away from pos
# 1601605 too high
# 1600328 too high