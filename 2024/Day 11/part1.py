import os

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 11")

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split()

def update_stone(stone):
    if stone == '0':
        return ['1']
    elif len(stone) % 2 == 0:
        # omit leading 0s, e.g., 1000 -> 10, 0
        mid = len(stone) // 2
        first_half = stone[:mid]
        second_half = stone[mid:]
        while len(second_half) > 1 and second_half[0] == '0':
            second_half = second_half[1:]
        return [first_half, second_half]
    else:
        return [str(int(stone) * 2024)]

def update_stone_iter(stone, blinks):
    curr_stones = [stone]
    for _ in range(blinks):
        new_stones = []
        for s in curr_stones:
            new_stones += update_stone(s)
        curr_stones = new_stones
    return curr_stones


def solution():
    res = 0
    for stone in txt:
        res += len(update_stone_iter(stone, 25))
    return res

print(solution())
