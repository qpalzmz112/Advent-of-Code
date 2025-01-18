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

def get_cheats(pos, debug=False):
    res = []

    row_width = 1
    for i in range(pos[1] - 20, pos[1] + 21):
        dx = row_width // 2
        if debug:
            padding = 41 - row_width // 2
            row = " " * padding

        for j in range(pos[0] - dx, pos[0] + dx + 1):
            cheatEnd = (i, j)
            if in_bounds(cheatEnd) and txt[cheatEnd] in ('.', 'E'):
                res.append((cheatEnd, abs(pos[0] - i) + abs(pos[1] - j)))
            if debug:
                row += '.'

        if debug:
            print(row + " " * padding)
        row_width += 2 * (1 if i < pos[1] else -1)

    return res

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
            return cheats
        txt[pos] = 'O'        

        for d in dirs:
            newPos = (pos[0] + d[0], pos[1] + d[1])
            if txt[newPos] in ('.', 'E'):
                todo.append((newPos, picoseconds + 1))
                break

        for cheatEnd, length in get_cheats(pos, False):
            cheats[cheatEnd].append(picoseconds + length)

def solution(debug=False):
    cheats = solve()
    if debug:
        times = [time for cheat in cheats for time in cheats[cheat]]
        counts = defaultdict(int)
        for time in times:
            counts[time] += 1
        print(sorted(counts.items(), key=lambda x: x[0]))
    return sum(1 if num >= 100 else 0 for val in cheats.values() for num in val)

print(solution())
# consider all possible values for cheatEnd at each pos - a cheatEnd can be at most 20 manhattan distance (dx + dy) away from pos
# 1601605 too high
# 1600328 too high