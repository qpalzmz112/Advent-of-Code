import os

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 6")

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split()

# want txt[i] to be a list of chars so that they can be reassigned to 'X's as needed
txt = list(map(list, txt))

# find the guard
row = None
col = None
for i, row in enumerate(txt):
    for j in range(len(row)):
        if row[j] == '^':
            row, col = i, j
            break
    # if the above for loop wasn't broken out of, continue (to avoid the break below...)
    else:
        continue
    # if we get here, the above for loop was broken out of, i.e., we found the guard - we can break out of the for loop and move on
    break


# matrix to rotate 90 degrees clockwise: 
        # [0 1]
        # [-1 0]
def rotate_right(direction):
    return (direction[1], -direction[0])

def in_bounds(pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(txt) and pos[1] < len(txt[0])

res = 0
direction = (-1, 0) # row, col; not x, y. So, -1 means move 'up' a row
while in_bounds((row, col)):
    ahead = (row + direction[0], col + direction[1])
        # consider #
                    #, in which case two rotations in a row are necessary                 
    while in_bounds(ahead) and txt[ahead[0]][ahead[1]] == '#':
        direction = rotate_right(direction)
        ahead = (row + direction[0], col + direction[1])

    if txt[row][col] != 'X':
        txt[row][col] = 'X'
        res += 1

    row += direction[0]
    col += direction[1]

print(res)