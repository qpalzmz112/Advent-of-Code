import os

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 1")

txt = open("input.txt", "r")
txt = txt.read()

nums = txt.split()

col1 = [int(nums[i]) for i in range(len(nums)) if i % 2 == 0]
col2 = [int(nums[i]) for i in range(len(nums)) if i % 2 == 1]

col1.sort()
col2.sort()

res = 0
for x, y in zip(col1, col2):
    res += abs(x - y)

print(res)