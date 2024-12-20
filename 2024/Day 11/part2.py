import os
from collections import deque

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

def update_stone_iter(stone, blinks, dp):
    if stone in dp and blinks in dp[stone]:
        return dp[stone][blinks]

    res = 0
    if blinks > 0:
        for s in update_stone(stone):
            res += update_stone_iter(s, blinks - 1, dp)

    if stone in dp:
        dp[stone][blinks] = res if res > 0 else 1
    else:
        dp[stone] = {blinks: res if res > 0 else 1}
    
    return res if res > 0 else 1


# need 2D dynamic programming? stone, num_blinks -> number of resulting stones
def solution():
    res = 0
    dp = {}
    blinks = 75
    #txt = ['125', '17']
    for stone in txt:
        if stone in dp and blinks not in dp[stone]:
            dp[stone][blinks] = update_stone_iter(stone, blinks, dp)
        elif stone not in dp:
            dp[stone] = {blinks: update_stone_iter(stone, blinks, dp)}
        res += update_stone_iter(stone, blinks, dp)

    #print(dp)
    return res

print(solution())
