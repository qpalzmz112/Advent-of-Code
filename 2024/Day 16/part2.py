import os
import pathlib
from collections import deque

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split()
txt = list(map(list, txt))

def find_start():
    for i in range(len(txt)):
        for j in range(len(txt[0])):
            if txt[i][j] == 'S':
                return (i, j)

def solution():
    # N, E, S, W
    dirs = {(-1, 0), (0, 1), (1, 0), (0, -1)}
    min_score = float('inf')
    best_path_tiles = set()
    pos = find_start()
    todo = deque()

    # (position: (row, col), direction: (dRow, dCol), score: int)
    todo.append((pos, (0, 1), 0, set()))

    while todo:
        # use BFS so we can mark current position as a wall to avoid loops
        pos, direction, score, tiles = todo.popleft()
        txt[pos[0]][pos[1]] = '#'
        if score > min_score:
            continue

        for d in dirs:
            # ignore the direction directly behind us
            # in general, this shouldn't be done at the first move but it works for the input given
            if d != (direction[0] * -1, direction[1] * -1):
                tiles.add(pos)
                newPos = (pos[0] + d[0], pos[1] + d[1])
                if txt[newPos[0]][newPos[1]] == '.':
                    # free space is in the direction we are facing
                    if d == direction:
                        # this is hacky, but append left when the next space doesn't require a turn to greedily prioritize cheaper paths -
                        # only works under the assumption that the maze isn't large enough for saving 1000 cost now to backfire in the long run
                        todo.appendleft((newPos, d, score + 1, tiles))
                    else:
                        todo.append((newPos, d, score + 1001, tiles))
                elif txt[newPos[0]][newPos[1]] == 'E':
                    if d == direction:
                        if score + 1 < min_score:
                            best_path_tiles = tiles
                            min_score = min(min_score, score + 1)
                        elif score + 1 == min_score:
                            best_path_tiles = best_path_tiles.union(tiles)
                            min_score = min(min_score, score + 1)                        
                    else:
                        if score + 1001 < min_score:
                            best_path_tiles = tiles
                            min_score = min(min_score, score + 1001)
                        elif score + 1001 == min_score:
                            best_path_tiles = best_path_tiles.union(tiles)
                            min_score = min(min_score, score + 1001)   
    return min_score

print(solution())