import os

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


res = 0
for update in updates:
    for i in range(len(update) - 1):
        for j in range(i + 1, len(update)):
            if update[j] in afters and update[i] in afters[update[j]]:
                break
        else:
            continue
        break
    else:
        res += update[len(update) // 2]

print(res)