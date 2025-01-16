import os
import pathlib
from collections import deque, defaultdict

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split()
orig_txt = txt
txt = {}
for i, row in enumerate(orig_txt):
    for j, char in enumerate(row):
        txt[(i, j)] = char

def find_char(c):
    for i in range(len(orig_txt)):
        for j in range(len(orig_txt[0])):
            if txt[(i, j)] == c:
                return (i, j)

def solution():
    # N, E, S, W
    dirs = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    start = find_char('S')
    end = find_char('E')
    todo = deque()
    txt[start] = 0
    txt[end] = float('inf')
    # (position: (row, col), direction: (dRow, dCol), score: int)
    todo.append((start, (0, 1), 0))

    while todo:
        pos, direction, score = todo.pop()

        if txt[pos] ==  '.' or (isinstance(txt[pos], int) and txt[pos] > score):
            txt[pos] = score
        elif txt[pos] == float('inf'):
            txt[pos] = score
        elif txt[pos] < score:
            continue

        if pos == end:
            continue

        for d in dirs:
            if d != (direction[0] * -1, direction[1] * -1):
                newPos = (pos[0] + d[0], pos[1] + d[1])
                if txt[newPos] != '#':
                    if d == direction:                        
                        todo.append((newPos, d, score + 1))
                    else:
                        todo.append((newPos, d, score + 1001))

    todo.append((end, (1, 0), txt[end]))
    todo.append((end, (0, -1), txt[end]))
    tiles = set()
    while todo:
        pos, direction, score = todo.pop()
        if txt[pos] > score:
            continue

        tiles.add(pos)
        for d in dirs:
            if d != (direction[0] * -1, direction[1] * -1):
                newPos = (pos[0] + d[0], pos[1] + d[1])
                if txt[newPos] == '#':
                    continue
                if d == direction:
                    todo.append((newPos, d, score - 1))
                else:
                    todo.append((newPos, d, score - 1001))
    return len(tiles)


print(solution())

# Reversing to find all tiles on min-cost paths:
# Start with score = min cost of reaching the end from part 1
# Obviously, any tile we see whose cost is > score should be ignored, as it is not part of a min-cost path
# But we also need to decrement score as we go backwards in the same way that we incremented it in part 1

###############
#.......#....O#
#.#.###.#.###O#
#.....#.#...#O#
#.###.#####.#O#
#.#.#.......#O#
#.#.#####.###O#
#..OOXOOOOOO#O#
###O#O#####O#O#
#OOO#O....#O#O#
#O#O#O###.#O#O#
#OOOOO#...#O#O#
#O###.#.#.#O#O#
#O..#.....#OOO#
###############

# Main confusion point: the junction marked 'X' above
# The tile to the left is part of a min cost path to the end, but not to 'X'
# While reversing, when we get to X, our score is 4010 (even though the min cost to get to X is 3010)
# Then, since we can 'spend' one point to move one tile left, our score is 4009 and the min cost to get to that tile from the start is 4009. 
# Thus, we can reach the start from there while remaining on a min cost path.

# At the same time, we can spend 1001 points to go down a tile from X, giving us a score of 3009, which matches the min cost of reaching that tile.
# Since that tile's min cost matches our score, we keep going. Consider if the maze had a new wall causing this tile's score to exceed 3009. Then, we would not go down this path in reverse.