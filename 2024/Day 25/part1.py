import os
import pathlib

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split('\n\n')

keys = set()
locks = set()
def process_input(s):
    lock = False
    if s[0] == '#':
        lock = True

    s = s.split()
    heights = [-1] * len(s[0])
    for col in range(len(s[0])):
        for row in range(len(s)):
            if s[row][col] == '#':
                heights[col] += 1

    if lock:
        locks.add(tuple(heights))
    else:
        keys.add(tuple(heights))
    
def parse_input():
    for block in txt:
        process_input(block)

def test(key, lock):
    return max(x + y for x, y in zip(key, lock)) <= 5

def solution():
    parse_input()
    
    res = 0
    for key in keys:
        for lock in locks:
            res += test(key, lock)
    return res

print(solution())