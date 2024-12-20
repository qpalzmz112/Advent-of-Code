import os

os.chdir("C:\\Users\\seanc\\source\\repos\\Advent-of-Code\\2024\\Day 9")

txt = open("input.txt", "r")
txt = txt.read()

#txt = """2333133121414131402"""
#txt = "12345"

l = 0
r = len(txt) - 1
if len(txt) % 2 == 0:
    r -= 1

output = []
free_space = 0
right_side_counter = 0
id_l = -1
id_r = -1
while l < r:
    if l % 2 == 0:
        id_l = l // 2
        for _ in range(int(txt[l])):
            output.append(id_l)
        l += 1

    else:
        free_space = int(txt[l])

        while free_space > 0:
            if right_side_counter == 0:                
                id_r = r // 2
                right_side_counter = int(txt[r])

            while free_space > 0 and right_side_counter > 0:
                output.append(id_r)
                free_space -= 1
                right_side_counter -= 1

            if right_side_counter == 0:
                if r <= l + 2:
                    break
                r -= 2

        l += 1

while right_side_counter > 0:
    output.append(id_r)
    right_side_counter -= 1

res = 0
for i, c in enumerate(output):
    res += i * c

print(res)