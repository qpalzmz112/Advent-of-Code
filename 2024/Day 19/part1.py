import os
import pathlib
from collections import deque
from functools import cache

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split('\n')

patterns = txt[0]
patterns = patterns.split(', ')
designs = txt[2:]

@cache
def check_design(design):
    if not design:
        return True

    for pattern in patterns:
        if design.startswith(pattern):
            if check_design(design[len(pattern):]):
                return True
    return False

def solution():
    res = 0
    for design in designs:
        if check_design(design):
            res += 1
    return res

print(solution())