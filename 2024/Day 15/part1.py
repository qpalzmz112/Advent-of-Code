import os

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 15")

txt = open("input.txt", "r")
txt = txt.read()

warehouse, movements = txt.split('\n\n')
warehouse = list(map(list, warehouse.split()))
movements = ''.join(movements.split())


def find_robot():
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == '@':
                return (i, j)

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
            if warehouse[i][j] == 'O':
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

    
    

