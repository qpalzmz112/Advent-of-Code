import os
import pathlib
from collections import deque

path = pathlib.Path(__file__).parent.resolve()
os.chdir(path)

txt = open("input.txt", "r")
txt = txt.read()

txt = txt.split('\n')
registers = {}
program = None
for row in txt:
    if row == '':
        continue

    row = row.split()
    if row[0][0] == 'R':
        register = row[1][:len(row[1]) - 1]
        num = int(row[2])
        registers[register] = num
    else:
        program = list(map(int, row[1].split(',')))

### OPCODES
# 0: division: combo operand - reg(A) := reg(A) // 2^(operand)
# 1: bitwise XOR: literal operand - reg(B) := reg(B) ^ (operand)
# 2: combo operand - reg(B) := (operand) % 8
# 3: literal operand - if reg(A) == 0: pass; else: i_ptr := (operand)
# 4: reg(B) := reg(B) ^ reg(C)
# 5: combo operand - output += (operand) % 8
# 6: 0 but value is put in reg(B)
# 7: 0 but value is put in reg(C)

### COMBO OPERANDS
# 0-3: 0-3
# 4: reg(A)
# 5: reg(B)
# 6: reg(C)
# 7: invalid

# Program: 2,4,1,5,7,5,0,3,4,0,1,6,5,5,3,0
# reg(B) = reg(A) % 8
# reg(B) = reg(B) ^ b101
# reg(C) = A >> B
# reg(A) = reg(A) // 8
# reg(B) = reg(B) ^ reg(C)
# reg(B) = reg(B) ^ b110
# output += reg(B) % 8
# if reg(A) != 0: go to start

def combo(operand):
    if operand <= 3:
        return operand
    return registers[chr(ord('A') + operand - 4)]

def run_program(execute_full=True, A=None):
    if A is not None:
        registers['A'] = A
    output = []
    i_ptr = 0
    while i_ptr < len(program):
        operator = program[i_ptr]
        operand = program[i_ptr + 1]
        i_ptr += 2

        match operator:
            case 1:
                registers['B'] = registers['B'] ^ operand
            case 2:
                registers['B'] = combo(operand) % 8
            case 3:
                if registers['A'] == 0:
                    continue
                else:
                    i_ptr -= 2
                    i_ptr = operand
            case 4:
                registers['B'] = registers['B'] ^ registers['C']
            case 5:
                char = str(combo(operand) % 8)
                if execute_full is False:
                    return int(char)
                output.append(char)
            case _:
                match operator:
                    case 0:
                        register = 'A'
                    case 6:
                        register = 'B'
                    case 7:
                        register = 'C'
                num = registers['A']
                denom = pow(2, combo(operand))
                registers[register] = num // denom
    return ','.join(output)

def are_compatible(x, y):
    # x is the left 10 bits, y is the right 10 bits
    # return true if the overlapping 7 bits of each are the same
    mask = 2**7 - 1
    x = x & mask
    y = y & (mask << 3)
    y = y >> 3
    return x ^ y == 0

def solution():
    todo = deque()
    # get all possible 3 MSBs of A that give the last num in the program
    for i in range(1, 2**3 - 1):
        if run_program(execute_full=False, A=i) == program[15]:
            todo.append((i, 14, 6)) # A, next num in program to get, exponent

    while True:
        num, index, exp = todo.popleft()
        print((num, index, exp))
        if index == -1:
            return num

        for i in range(1, 2**exp - 1)[::-1]:
            if are_compatible(num, i) and run_program(execute_full=False, A=i) == program[index]:
                newA = num * 8 + (i & 7)
                todo.appendleft((newA, index - 1, min(exp + 3, 10)))

print(solution()) 
print(run_program(A=109019476330651))