import os
from functools import cmp_to_key
os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 5")

txt = open("input.txt", "r")
txt = txt.read()

rules, updates = txt.split('\n\n')

afters = {}

def update_dict(d, key, val):
    if key not in d:
        d[key] = {val}
    else:
        d[key].add(val)

for rule in rules.split():
    before, after = map(int, rule.split('|'))
    update_dict(afters, before, after) # add 'after' to the set of pages that must come after 'before'

#updates is a string where each update is separated by a newline
# this makes it into a list where each element is "num1,...,numi"
updates = updates.split()

# now, make each element "num1",...,"numi"
updates = map(lambda x: x.split(','), updates)

# and, finally, num1,...,numi
updates = map(lambda x: list(map(int, x)), updates)


fixed_updates = []

def cmp(x, y):
    if y in afters and x in afters[y]:
        return 1
    return -1

res = 0
for update in updates:
    tmp = sorted(update, key=cmp_to_key(cmp))
    if update != tmp:
       res += tmp[len(tmp) // 2] 
        
print(res)