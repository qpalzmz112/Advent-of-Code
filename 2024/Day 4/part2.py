import os

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 4")

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split()

def check_match(row, col):
    x = txt[row + 1][col + 1], txt[row - 1][col - 1]
    y = txt[row + 1][col - 1], txt[row - 1][col + 1]

    return 'M' in x and 'S' in x and 'M' in y and 'S' in y

res = 0
for row in range(1, len(txt) - 1):
    for col in range(1, len(txt[0]) - 1):
        if txt[row][col] == 'A':
            if check_match(row, col):
                res += 1
print(res)