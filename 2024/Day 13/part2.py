import os
import pathlib
import re

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split("\n\n")

def parse_round(text):
    # given three lines of input, return A, B, X (since A and B are 2d vectors, I'll just call the third one X)
    def get_nums(line):
        return list(map(int, re.findall(r"[0-9]+", line)))

    lines = text.split('\n')
    return {c: get_nums(lines[i]) for i, c in enumerate(['A', 'B', 'X'])}    

def scale(vec, c):
    return (vec[0] * c, vec[1] * c)

def solution():
    cost = 0
    for r in txt:
        pts = parse_round(r)
        a1, a2 = pts['A']
        b1, b2 = pts['B']
        x, y = pts['X']
        x += 10000000000000
        y += 10000000000000

        numerator = b1 * y - b2 * x
        denominator = b1 * a2 - a1 * b2
        
        # floating point error makes this tough..
        if numerator % denominator != 0:
            continue
        c1 = numerator // denominator
   
        c2 = (x - (c1 * a1)) / b1
        cost += 3 * c1 + c2

    print(cost)


solution()