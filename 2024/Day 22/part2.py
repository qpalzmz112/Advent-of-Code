import os
import pathlib
from collections import deque, defaultdict

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

def nth_secret_num(num, n, sequences):
    orig_num = num
    d = {}
    sequence = deque(maxlen=4)

    for i in range(n):
        newNum = f(num)
        sequence.append((newNum % 10) - (num % 10))
        if len(sequence) == 4:
            tup = tuple(sequence)
            if tup not in d:
                d[tup] = newNum % 10
        num = newNum

    sequences[orig_num] = d
    return num

def solution():
    sequences = {}
    for num in txt:
        nth_secret_num(num, 2000, sequences)

    sequence_totals = defaultdict(int)
    for num in txt:
        for sequence in sequences[num]:
            sequence_totals[sequence] += sequences[num][sequence]

    return max(sequence_totals.values())

print(solution())

# for each input number, get preceding sequence for each secret number from 4 to 2000
# put the sequences as tuples into sequences[input num] = {sequence: price} to avoid counting a sequence after we've seen it for an input number
# then, after that's done for each input number, start a new dict mapping sequences to sums and go through sequences[input num] for each input num and for each sequence
# in that sub-dict, add its price to the sequence's sum in the new dict