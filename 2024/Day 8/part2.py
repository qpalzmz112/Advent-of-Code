import os

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 8")

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split()


def in_bounds(row, col):
    return row >= 0 and col >= 0 and row < len(txt) and col < len(txt[0])

def add_antinodes(x1, y1, x2, y2, antinodes):
    rise = y2 - y1
    run = x2 - x1

    pts = [(-1, x1 - run, y1 - rise), (1, x2 + run, y2 + rise)]

    while pts:
        direction, x, y = pts.pop()

        if not in_bounds(x, y):
            continue

        antinodes.add((x, y))
        pts.append((direction, x + direction*run, y + direction*rise))

antinodes = set()
for row in range(len(txt)):
    for col in range(len(txt[0])):
        if txt[row][col] != '.':
            antinodes.add((row, col))
            for i in range(row, len(txt)):
                for j in range(len(txt[0])):
                    if i == row and j <= col:
                        continue
                    if txt[i][j] == txt[row][col]:
                        add_antinodes(row, col, i, j, antinodes)

print(len(antinodes))
