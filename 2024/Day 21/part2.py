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

def get_paths(keypad):
    res = defaultdict(defaultdict)
    for row in range(len(keypad)):
        for col in range(len(keypad[0])):
            start = keypad[row][col]
            if start is None:
                continue
            for y in range(len(keypad)):
                for x in range(len(keypad[0])):
                    end = keypad[y][x]
                    if end is None or end == start:
                        continue

                    horiz = abs(col - x) * ('<' if col > x else '>')
                    vert = abs(row - y) * ('^' if row > y else 'v')

                    # would be nice to understand this...
                    if x > col and keypad[y][col] is not None:
                        res[start][end] = vert + horiz + 'A'
                    elif keypad[row][x] is not None:
                        res[start][end] = horiz + vert + 'A'
                    else:
                        res[start][end] = vert + horiz + 'A'

    return res

numpad_moves = get_paths(numpad)
dirpad_moves = get_paths(dirpad)

def enter_code(code):
    moves = ""
    i, j = -1, 0
    use_numpad = code[1] in numpad_moves
    while j + 1 < len(code):
        i += 1
        j += 1
        if code[j] == code[i]:
            moves += 'A'
        elif use_numpad:
            moves += numpad_moves[code[i]][code[j]]
        else:
            moves += dirpad_moves[code[i]][code[j]]
    return moves

def solution():  
    res = 0
    for c in codes:
        print(c)
        num = int(c[:len(c) - 1])   
        
        for i in range(26):
            print(i)
            j = 0
            new_c = ""
            while j < len(c):
                if c[j] == 'A':
                    new_c += enter_code('A' + c[:j + 1])
                    c = c[j + 1:]
                    j = 0
                else:
                   j += 1
            c = new_c
        length =  len(c)
        res += length * num
    return res

print(solution())
