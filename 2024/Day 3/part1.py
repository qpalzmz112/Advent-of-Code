import os
import re

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 3")

txt = open("input.txt", "r")
txt = txt.read()

muls = re.findall(r"mul\([1-9][0-9]*,[1-9][0-9]*\)", txt)

res = 0
for mul in muls:
    x, y = mul.split(',')
    x = x.split('(')[1]
    y = y.split(')')[0]
    res += int(x) * int(y)
print(res)