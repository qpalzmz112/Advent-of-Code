import os

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 8")

txt = open("input.txt", "r")
txt = txt.read()



txt = txt.split()


# given a pair of antennae on the same frequency, look at the slope of the line connecting them. 
# e.g., x...y -> look at the point <slope> to the left of x and <slope> to the right of y.
# if either of these points is in bounds, it is a valid antinode position -> add it to a set of antinode positions

# can an antinode go between antennae?
# x
# .
# . #
# .
# .
# .
# . . . y
# an antinode 2 below x and one to the right would be valid, as well as 4 below x and 2 to the right
# observe that for any pair of antennae, there are only four possible antinode positions 
# this problem only seems to consider the first two possible positions listed

# there can be more than two antennae on the same freq, so iterate through all pairs and do the above check

def in_bounds(row, col):
    return row >= 0 and col >= 0 and row < len(txt) and col < len(txt[0])

def add_antinodes(x1, y1, x2, y2, antinodes):
    rise = y2 - y1
    run = x2 - x1

    pts = [(x1 - run, y1 - rise), (x2 + run, y2 + rise)]

    for pt in pts:
        if in_bounds(pt[0], pt[1]):
            antinodes.add(pt)

antinodes = set()
for row in range(len(txt)):
    for col in range(len(txt[0])):
        if txt[row][col] != '.':
            for i in range(row, len(txt)):
                for j in range(len(txt[0])):
                    if i == row and j <= col:
                        continue
                    if txt[i][j] == txt[row][col]:
                        add_antinodes(row, col, i, j, antinodes)

print(len(antinodes))
