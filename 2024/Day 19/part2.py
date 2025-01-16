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
        return 1

    return sum(check_design(design[len(pattern):]) if design.startswith(pattern) else 0 for pattern in patterns)

def solution():
    counts = {}
    for design in designs:
        counts[design] = check_design(design)
    return sum(counts[design] for design in counts)

print(solution())