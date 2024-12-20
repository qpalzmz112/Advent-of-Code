import os

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 9")

txt = open("input.txt", "r")
txt = txt.read()

#txt = """2333133121414131402"""

def print_output(txt):
    output = ""
    for num, count in txt:
        for i in range(count):
            if num is None:
                output += '.'
            else:
                output += str(num)
    print(output)

# list where each element is (id, number of occurrences)
output = []
free_spaces = []
for i, c in enumerate(txt):
    if i % 2 == 0:
        output.append((i // 2, int(c)))
    elif i != len(txt) - 1: # don't add empty space at the end of output
        free_spaces.append(i)
        output.append((None, int(c)))

r = len(output) - 1
i = 0
while r >= 0:
    while i < len(free_spaces) and free_spaces[i] < r:
        remaining_spaces = output[free_spaces[i]][1] - output[r][1]
        if remaining_spaces >= 0:
            output[free_spaces[i]] = output[r]
            output[r] = (None, output[r][1])

            if remaining_spaces != 0:
                output.insert(free_spaces[i] + 1, (None, remaining_spaces))
                free_spaces = list(map(lambda x: x + 1 if x >= free_spaces[i] else x, free_spaces))

            else:
                free_spaces.remove(free_spaces[i])
            
            break

        else:
           i += 1
    
    
    else: # didn't break out of the while loop -> need to subtract one from r because output[r][0] is still a number (didn't move the file)
        r -= 1
    while r >= 0 and output[r][0] is None:
        r -= 1
    i = 0
    

res = 0
position = 0
for ID, count in output:
    for i in range(count):
        if ID is not None:
            res += ID * position
        position += 1

print(res)
