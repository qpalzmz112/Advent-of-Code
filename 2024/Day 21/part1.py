import os
import pathlib
from collections import defaultdict

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

txt = open("input.txt", "r")
txt = txt.read()

codes = txt.split()

numpad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], [None, '0', 'A']]
dirpad = [[None, '^', 'A'], ['<', 'v', '>']]
def in_bounds(arr, pos):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(arr) and pos[1] < len(arr[0])

def count_switches(path):
    res = 0
    curr_key = path[0]
    for key in path[1:]:
        if key != curr_key:
            curr_key = key
            res += 1
    return res

def get_shortest_path(start, dest, keypad):
    dirs = {(-1, 0): '^', (1, 0): 'v', (0, -1): '<', (0, 1): '>'}
    todo = []
    paths = []
    for d in dirs:
        pos = (start[0] + d[0], start[1] + d[1])
        if in_bounds(keypad, pos) and pos is not None:
            todo.append((pos, dirs[d], {start}))

    while todo:
        pos, moves, seen = todo.pop()
        if pos == dest:
            paths.append(moves)
        if pos in seen:
            continue

        for d in dirs:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if in_bounds(keypad, pos) and keypad[pos[0]][pos[1]] is not None:
                new_seen = seen.copy()
                new_seen.add(pos)
                todo.append((new_pos, moves + dirs[d], new_seen))

    min_length = min(len(path) for path in paths)
    paths = [path for path in paths if len(path) == min_length]

    paths = sorted(list(map(lambda x: (x, count_switches(x)), paths)), key = lambda x: x[1])
    paths = [path for path, switches in paths if switches == paths[0][1]]
    return paths[0]

def populate_moves(keypad):
    moves = defaultdict(defaultdict)

    for row in range(len(keypad)):
        for col in range(len(keypad[0])):
            curr_key = keypad[row][col]
            if curr_key is None:
                continue

            for y in range(len(keypad)):
                for x in range(len(keypad[0])):
                    new_key = keypad[y][x]
                    if new_key == curr_key or new_key is None:
                        continue

                    moves[curr_key][new_key] = get_shortest_path((row, col), (y, x), keypad) + 'A'

    return moves

def enter_code(code, numpad_moves, dirpad_moves, depth):
    if depth == 1:
        return code
    moves = "A"
    i, j = -1, 0
    use_numpad = code[1] in numpad_moves
    while j + 1 < len(code):
        i += 1
        j += 1
        if code[j] == code[i]:
            moves += 'A'
            continue
        if use_numpad:
            moves += numpad_moves[code[i]][code[j]]
        else:
            moves += dirpad_moves[code[i]][code[j]]
        

    return enter_code(moves, numpad_moves, dirpad_moves, depth - 1)

def solution():
    numpad_moves = populate_moves(numpad)
    dirpad_moves = populate_moves(dirpad)
    
    print(numpad_moves)
    res = 0
    for c in codes:
        num = int(c[:len(c) - 1])
        length =  len(enter_code('A' + c, numpad_moves, dirpad_moves, 4)[1:])
        #print(f"{length} * {num}")
        res += length * num
    return res

print(solution())

# 180874 too high
