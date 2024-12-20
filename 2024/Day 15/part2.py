import os

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 15")

txt = open("input.txt", "r")
txt = txt.read()

txt = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

def parse(s):
    res = []
    for c in s:
        match c:
            case '@':
                res.append('@')
                res.append('.')
            case 'O':
                res.append('[')
                res.append(']')
            case _:
                res.append(c)
                res.append(c)
    return res

warehouse, movements = txt.split('\n\n')
warehouse = list(map(parse, warehouse.split()))
movements = ''.join(movements.split())

def find_robot():
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == '@':
                return (i, j)

def can_move_box(x, y, dx, dy):
    # moving vertically
    y_offset = 0
    if dx != 0:
        if warehouse[x][y] == '[':
            y_offset = 1
        else:
            y_offset = -1
        return warehouse[x + dx][y + dy] != '#' and warehouse[x + dx][y + dy + y_offset] != '#'

    # moving horizontally
    else:
        return warehouse[x][y + 2 * dy] != '#'

def bfs_boxes(x, y, dx, dy):
    # return a list of indices where there is a half of a box
    # {'[': {set of indices where the half will move if a move is possible}, ']': {set of indices...}}
    # mark boxes' spaces as free while building the above dict - if we end up not doing the move, backtrack
    # if we stop finding more boxes to move without any being unable to, go through the dict and do the obvious thing

def move(x, y, dx, dy):
    if warehouse[x + dx][y + dy] == '#':
        return
    elif warehouse[x + dx][y + dy] == 'O':
        tmpx = x + dx
        tmpy = y + dy
        while warehouse[tmpx][tmpy] != '#':
            if warehouse[tmpx][tmpy] == '.':
                warehouse[tmpx][tmpy] = 'O'
                warehouse[x + dx][y + dy] = '@'
                warehouse[x][y] = '.'
                return (x + dx, y + dy)                
            tmpx += dx
            tmpy += dy
    else:
        warehouse[x + dx][y + dy] = '@'
        warehouse[x][y] = '.'
        return (x + dx, y + dy)

def calculate_answer():
    res = 0
    for i in range(len(warehouse)):
        for j in range(len(warehouse[0])):
            if warehouse[i][j] == '[':
                res += 100 * i + j
    return res

def print_warehouse():
    for row in warehouse:
        print(''.join(row))
    print('\n')

def solution():
    moves = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
    x, y = find_robot()
    for m in movements:
        dx, dy = moves[m]
        tmp = move(x, y, dx, dy)
        if tmp is not None:
            x, y = tmp
        
    print(calculate_answer())

solution()