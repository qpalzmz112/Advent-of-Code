import os
from collections import defaultdict

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 1")

txt = open("input.txt", "r")
txt = txt.read()

nums = txt.split()

col1 = [int(nums[i]) for i in range(len(nums)) if i % 2 == 0]
col2 = [int(nums[i]) for i in range(len(nums)) if i % 2 == 1]

col2dict = defaultdict(int)
for num in col2:
    col2dict[num] += 1

res = 0
for num in col1:
    res += num * col2dict[num]
print(res)