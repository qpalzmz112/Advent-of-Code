import os
import pathlib

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

txt = open("input.txt", "r")
txt = txt.read()

txt = list(map(int, txt.split()))

def prune(num):
    return num % 16777216

def mix(x, y):
    return x ^ y

def f(num):
    num = prune(mix(num, num * 64))
    num = prune(mix(num, num // 32))
    return prune(mix(num, num * 2048))

def nth_secret_num(num, n):
    for _ in range(n):
        num = f(num)
    return num

def solution():
    return sum(nth_secret_num(num, 2000) for num in txt)

print(solution())
