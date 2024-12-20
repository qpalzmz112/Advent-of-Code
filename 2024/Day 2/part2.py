import os

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 2")

txt = open("input.txt", "r")
txt = txt.read()

rows = [list(map(int, row.split(' '))) for row in txt.split('\n')]

def check_with_removal(row):
    for i in range(len(row)):
        new_row = [row[j] for j in range(len(row)) if j != i]
        if check_row(new_row):
            return True
    return False

def check_row(row):
    removed_one = False
    increasing = row[0] < row[1]
    min_diff = 1 if increasing else -3
    max_diff = 3 if increasing else -1

    for i in range(len(row) - 1):
        diff = row[i + 1] - row[i]
        if diff < min_diff or diff > max_diff:
            return False
    return True
  
           
res = 0
for row in rows:
    if check_with_removal(row):
        res += 1
print(res)