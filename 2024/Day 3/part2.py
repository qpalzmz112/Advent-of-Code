import os
import re

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 3")

txt = open("input.txt", "r")
txt = txt.read()

# get all mul, do, and don't expressions
matches = re.findall(r"mul\([1-9][0-9]*,[1-9][0-9]*\)|do\(\)|don't\(\)", txt)

# join list into one string
x = ''.join(matches)

# replace each don't() and subsequent mults with empty string
matches = re.sub(r"don't\(\)[^d]*", "", x)
matches = ''.join(matches)

# grab all numbers from the resulting string
nums = re.findall(r"[0-9]+", matches)

res = 0
for i in range(0, len(nums), 2):
    res += int(nums[i]) * int(nums[i + 1])
print(res)

