import os
import re
from PIL import Image
import numpy as np

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 14")

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split('\n')
txt = list(map(lambda x: list(map(int, re.findall(r'[\-0-9]+', x))), txt))



def solution():
    width = 101
    height = 103

    min_safety = float('inf')
    max_safety = float('-inf')
    seconds = 15000
    for i in range(seconds):
        # initialize white canvas
        arr = np.full((width, height, 3), 255, dtype=np.uint8)
        ur, ul, br, bl = 0, 0, 0, 0

        for x, y, dx, dy in txt:
            x += dx * i
            x = x % width
            y += dy * i
            y = y % height
            arr[x][y] = [0, 0, 0]

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

        safety = ur * ul * br * bl
        if safety <= min_safety:
            min_safety = safety
            data = Image.fromarray(arr)
            data.save(f"{i}.png")
        elif safety >= max_safety:
            max_safety = safety
            data = Image.fromarray(arr)
            data.save(f"{i}.png")

solution()