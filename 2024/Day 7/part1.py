import os

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 7")

txt = open("input.txt", "r")
txt = txt.read()

rows = txt.split("\n")

def test_row(target, numbers):
    todo = [(0, numbers)]

    while todo:
        total, nums = todo.pop()
        if len(nums) == 0:
            if total == target:
                return True
        else:
            todo.append((total + nums[0], nums[1:]))
            todo.append((total * nums[0], nums[1:]))

    return False


res = 0
for row in rows:
    target, nums = row.split(': ')
    target = int(target)
    nums = list(map(int, nums.split(' ')))

    if test_row(target, nums):
        res += target

print(res)
    


