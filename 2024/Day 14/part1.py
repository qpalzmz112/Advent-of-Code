import os
import re

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 14")

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split('\n')
txt = list(map(lambda x: list(map(int, re.findall(r'[\-0-9]+', x))), txt))



def solution():
    width = 101
    height = 103
    seconds = 100

    ur, ul, br, bl = 0, 0, 0, 0
    for x, y, dx, dy in txt:
        x += dx * seconds
        x = x % width
        y += dy * seconds
        y = y % height

        if x < width // 2:
            if y < height // 2:
                ul += 1
            elif y > height // 2:
                bl += 1
        elif x > width // 2:
            if y < height // 2:
                ur += 1
            elif y > height // 2:
                br += 1

    print(ur * ul * br * bl)

solution()