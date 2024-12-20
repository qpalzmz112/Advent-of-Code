import os

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 4")

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split()

#txt = ["....XXMAS.", ".SAMXMS...", "...S..A...", "..A.A.MS.X", "XMASAMX.MM", "X.....XA.A", "S.S.S.S.SS", ".A.A.A.A.A", "..M.M.M.MM", ".X.X.XMASX"]

def find_matches(row, col):
    res = 0
    dirs = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

    for d in dirs:
        r = row
        c = col
        r_add, c_add = d
        for char in ['M', 'A', 'S']:
            r += r_add
            c += c_add

            if r < 0 or r >= len(txt):
                break
            if c < 0 or c >= len(txt[0]):
                break
            if txt[r][c] != char:
                break
        else:
            res += 1
    
    #if res > 0:
        #print(f"row: {row}, col: {col}, matches: {res}")
    return res

res = 0
for row in range(len(txt)):
    for col in range(len(txt[0])):
        if txt[row][col] == 'X':
            res += find_matches(row, col)
print(res)